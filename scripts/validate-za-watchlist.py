#!/usr/bin/env python3
"""Validate the ZA pending-legislation watchlist.

Usage: validate-za-watchlist.py
Reads jurisdictions/za/watchlist.yaml and validates each item against
the required schema.

Required fields per item:
  item, type, status, expected_effect, affected_statutes (list),
  affected_topics (list), source_url, last_checked (YYYY-MM-DD)

type must be one of: bill | regulation | case | commencement | consultation

affected_statutes entries must resolve to files in jurisdictions/za/statutes/.

Exits 0 if valid, 1 on any error.
"""
import re
import sys
from pathlib import Path

import yaml


REPO_ROOT = Path(__file__).resolve().parent.parent
WATCHLIST_PATH = REPO_ROOT / "jurisdictions" / "za" / "watchlist.yaml"
STATUTES_DIR = REPO_ROOT / "jurisdictions" / "za" / "statutes"

REQUIRED_ITEM_FIELDS = [
    "item",
    "type",
    "status",
    "expected_effect",
    "affected_statutes",
    "affected_topics",
    "source_url",
    "last_checked",
]

TYPE_ENUM = {"bill", "regulation", "case", "commencement", "consultation"}

DATE_PATTERN = re.compile(r"^\d{4}-\d{2}-\d{2}$")


def validate_item(idx: int, item: dict, statute_names: set[str]) -> list[str]:
    """Return a list of error strings for a single watchlist item."""
    errors = []
    label = f"items[{idx}]"

    if not isinstance(item, dict):
        return [f"{label}: must be a mapping, got {type(item).__name__}"]

    for field in REQUIRED_ITEM_FIELDS:
        if field not in item:
            errors.append(f"{label}: missing required field: '{field}'")

    # item — non-empty string
    if "item" in item and (not isinstance(item["item"], str) or not item["item"].strip()):
        errors.append(f"{label}: 'item' must be a non-empty string")

    # type — enum
    if "type" in item:
        if item["type"] not in TYPE_ENUM:
            errors.append(
                f"{label}: 'type' must be one of {sorted(TYPE_ENUM)}, got: {item['type']!r}"
            )

    # status — non-empty string
    if "status" in item and (not isinstance(item["status"], str) or not item["status"].strip()):
        errors.append(f"{label}: 'status' must be a non-empty string")

    # expected_effect — non-empty string
    if "expected_effect" in item and (
        not isinstance(item["expected_effect"], str) or not item["expected_effect"].strip()
    ):
        errors.append(f"{label}: 'expected_effect' must be a non-empty string")

    # affected_statutes — list of known statute base names
    if "affected_statutes" in item:
        if not isinstance(item["affected_statutes"], list):
            errors.append(f"{label}: 'affected_statutes' must be a list")
        else:
            for statute in item["affected_statutes"]:
                if not isinstance(statute, str):
                    errors.append(f"{label}: 'affected_statutes' entries must be strings")
                elif statute not in statute_names:
                    errors.append(
                        f"{label}: 'affected_statutes' references unknown statute: {statute!r} "
                        f"(no matching jurisdictions/za/statutes/{statute}.yaml)"
                    )

    # affected_topics — list
    if "affected_topics" in item and not isinstance(item["affected_topics"], list):
        errors.append(f"{label}: 'affected_topics' must be a list")

    # source_url — starts with http:// or https://
    if "source_url" in item:
        if not isinstance(item["source_url"], str) or not item["source_url"].startswith(
            ("http://", "https://")
        ):
            errors.append(
                f"{label}: 'source_url' must start with http:// or https://, "
                f"got: {item.get('source_url')!r}"
            )

    # last_checked — YYYY-MM-DD
    if "last_checked" in item:
        val = item["last_checked"]
        if not isinstance(val, str) or not DATE_PATTERN.match(val):
            errors.append(
                f"{label}: 'last_checked' must match YYYY-MM-DD, got: {val!r}"
            )

    return errors


def main() -> int:
    if not WATCHLIST_PATH.exists():
        print(f"FAIL: watchlist file not found: {WATCHLIST_PATH}", file=sys.stderr)
        return 1

    try:
        data = yaml.safe_load(WATCHLIST_PATH.read_text())
    except yaml.YAMLError as e:
        print(f"FAIL: YAML parse error in {WATCHLIST_PATH.name}: {e}", file=sys.stderr)
        return 1

    if not isinstance(data, dict) or "items" not in data:
        print(
            f"FAIL: watchlist.yaml must be a mapping with an 'items' key",
            file=sys.stderr,
        )
        return 1

    items = data["items"]
    if not isinstance(items, list):
        print(f"FAIL: 'items' must be a list", file=sys.stderr)
        return 1

    # Build known statute base names
    statute_names = {p.stem for p in STATUTES_DIR.glob("*.yaml")}

    all_errors: list[str] = []
    for idx, item in enumerate(items):
        errors = validate_item(idx, item, statute_names)
        all_errors.extend(errors)

    rel = WATCHLIST_PATH.relative_to(REPO_ROOT)
    if all_errors:
        print(f"FAIL: {rel}", file=sys.stderr)
        for err in all_errors:
            print(f"  {err}", file=sys.stderr)
        return 1

    print(f"OK: {rel} ({len(items)} items)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
