#!/usr/bin/env python3
"""Validate ZA statute YAML files against the shared schema.

Usage: validate-za-statutes.py [--strict-staleness]
Discovers all .yaml files under jurisdictions/za/statutes/, validates each
against the expected schema structure, checks temporal integrity, checks for
staleness, and detects duplicate-open entries.

Exits 0 if all valid, 1 if any invalid or no files found.

Flags:
  --strict-staleness   Stale files are treated as errors (non-zero exit).
                       By default, stale files emit WARN: lines and exit 0.
"""
import re
import sys
from datetime import date, timedelta
from pathlib import Path

import yaml


REPO_ROOT = Path(__file__).resolve().parent.parent
STATUTES_DIR = REPO_ROOT / "jurisdictions" / "za" / "statutes"

REQUIRED_TOP_LEVEL = ["statute", "authority", "last_confirmed", "source_url", "sections"]
REQUIRED_SECTION_FIELDS = ["ref", "value", "effective_from", "effective_until", "effect"]
DATE_PATTERN = re.compile(r"^\d{4}-\d{2}-\d{2}$")

VOLATILITY_ENUM = {"annual", "statutory", "stable"}

# Staleness windows by volatility level (in days)
STALENESS_WINDOWS = {
    "annual": 366,      # 12 months
    "statutory": 548,   # 18 months
    "stable": 1096,     # 36 months
}
DEFAULT_STALENESS_WINDOW = STALENESS_WINDOWS["stable"]

# Heuristic: strip trailing _<4-digit-year>, _<4-digit-year>_<2-digit-month>,
# or _v<digits> to get the base name.
# Examples: prescribed_rate_2026_03 → prescribed_rate; earnings_threshold_2024 → earnings_threshold
_BASE_NAME_RE = re.compile(r"_(\d{4}(_\d{2})?|v\d+)$")


def _section_base_name(key: str) -> str:
    """Return the base name for a section key, stripping year/version suffix."""
    return _BASE_NAME_RE.sub("", key)


def _check_duplicate_open_entries(sections: dict, errors: list[str]) -> None:
    """Hard-fail if two sections share a base name and are both open (effective_until null).

    Two open entries with the same base name mean two current values are in force for the
    same provision — that is almost always a data error (an old entry was not closed when a
    new one was added). The check applies to all value types: a stale string-valued open
    entry is just as problematic as a stale numeric one.
    """
    # Group all open sections by base name (regardless of value type)
    open_by_base: dict[str, list[str]] = {}
    for key, section in sections.items():
        if not isinstance(section, dict):
            continue
        if section.get("effective_until") is not None:
            continue
        base = _section_base_name(key)
        open_by_base.setdefault(base, []).append(key)

    for base, keys in open_by_base.items():
        if len(keys) > 1:
            errors.append(
                f"duplicate open entries sharing base name '{base}': "
                + ", ".join(sorted(keys))
                + " — only one section with a given base name may have effective_until: null"
            )


def validate_statute(data: dict, filename: str) -> list[str]:
    errors = []

    for field in REQUIRED_TOP_LEVEL:
        if field not in data:
            errors.append(f"missing required top-level field: {field}")

    if "statute" in data and (not isinstance(data["statute"], str) or len(data["statute"]) < 5):
        errors.append("'statute' must be a string of at least 5 characters")

    if "last_confirmed" in data and isinstance(data["last_confirmed"], str):
        if not DATE_PATTERN.match(data["last_confirmed"]):
            errors.append(f"'last_confirmed' must match YYYY-MM-DD, got: {data['last_confirmed']}")

    if "volatility" in data:
        if data["volatility"] not in VOLATILITY_ENUM:
            errors.append(
                f"'volatility' must be one of {sorted(VOLATILITY_ENUM)}, "
                f"got: {data['volatility']!r}"
            )

    if "source_url" in data and isinstance(data["source_url"], str):
        if not data["source_url"].startswith(("http://", "https://")):
            errors.append(f"'source_url' must start with http:// or https://, got: {data['source_url']}")

    sections = data.get("sections", {})
    if not isinstance(sections, dict) or len(sections) == 0:
        errors.append("'sections' must be a non-empty mapping")
        return errors

    for key, section in sections.items():
        if not isinstance(section, dict):
            errors.append(f"sections/{key}: must be a mapping")
            continue

        for field in REQUIRED_SECTION_FIELDS:
            if field not in section:
                errors.append(f"sections/{key}: missing required field: {field}")

        if "effect" in section and (not isinstance(section["effect"], str) or len(section["effect"]) < 5):
            errors.append(f"sections/{key}: 'effect' must be a string of at least 5 characters")

        if "currency" in section and section["currency"] != "ZAR":
            errors.append(f"sections/{key}: 'currency' must be 'ZAR', got: {section['currency']}")

        for date_field in ("effective_from", "effective_until", "gazette_date"):
            val = section.get(date_field)
            if val is not None and isinstance(val, str) and not DATE_PATTERN.match(val):
                errors.append(f"sections/{key}: '{date_field}' must be null or YYYY-MM-DD, got: {val}")

        eff_from = section.get("effective_from")
        eff_until = section.get("effective_until")
        if eff_from is not None and eff_until is not None:
            if eff_until < eff_from:
                errors.append(
                    f"sections/{key}: effective_until ({eff_until}) is before "
                    f"effective_from ({eff_from})"
                )

    # Duplicate-open-entry check (hard fail)
    _check_duplicate_open_entries(sections, errors)

    return errors


def check_staleness(data: dict, filename: str) -> list[str]:
    """Return WARN lines for stale last_confirmed dates. Does not cause hard errors."""
    warnings = []

    last_confirmed_raw = data.get("last_confirmed")
    if not isinstance(last_confirmed_raw, str) or not DATE_PATTERN.match(last_confirmed_raw):
        return warnings  # malformed date already caught by validate_statute

    try:
        last_confirmed = date.fromisoformat(last_confirmed_raw)
    except ValueError:
        return warnings

    volatility = data.get("volatility")
    window_days = STALENESS_WINDOWS.get(volatility, DEFAULT_STALENESS_WINDOW)
    cutoff = date.today() - timedelta(days=window_days)

    if last_confirmed < cutoff:
        volatility_label = volatility if volatility else "absent→stable"
        age_days = (date.today() - last_confirmed).days
        warnings.append(
            f"WARN: {filename}: last_confirmed {last_confirmed_raw} is {age_days} days old "
            f"(volatility={volatility_label}, window={window_days}d)"
        )

    return warnings


def main() -> int:
    strict_staleness = "--strict-staleness" in sys.argv

    files = sorted(STATUTES_DIR.glob("*.yaml"))

    if not files:
        print(f"FAIL: no .yaml files found in {STATUTES_DIR}", file=sys.stderr)
        return 1

    all_ok = True
    stale_found = False

    for path in files:
        rel = path.relative_to(REPO_ROOT)
        try:
            data = yaml.safe_load(path.read_text())
        except yaml.YAMLError as e:
            print(f"FAIL: {rel} — YAML parse error: {e}", file=sys.stderr)
            all_ok = False
            continue

        errors = validate_statute(data, path.name)
        if errors:
            print(f"FAIL: {rel}", file=sys.stderr)
            for err in errors:
                print(f"  {err}", file=sys.stderr)
            all_ok = False
        else:
            section_count = len(data.get("sections", {}))
            print(f"OK: {rel} ({section_count} sections)")

        # Staleness check (independent of schema errors)
        warnings = check_staleness(data, str(rel))
        for warn in warnings:
            print(warn)
            stale_found = True

    if stale_found and strict_staleness:
        print(
            "FAIL: stale files detected and --strict-staleness is set",
            file=sys.stderr,
        )
        all_ok = False

    return 0 if all_ok else 1


if __name__ == "__main__":
    sys.exit(main())
