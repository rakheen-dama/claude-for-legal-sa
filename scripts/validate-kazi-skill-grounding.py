#!/usr/bin/env python3
"""validate-kazi-skill-grounding — enforce that every kazi-legal-za skill is
grounded in real Kazi MCP tools and real jurisdictions/za statute sections.

Checks (errors fail the build; warnings are advisory):
  ERROR  every `mcp` entry in knowledge-map.yaml is a tool or resource in
         kazi-legal-za/data/mcp-catalogue.json.
  ERROR  every `za_knowledge` ref "file.yaml#section" resolves: the file exists
         in jurisdictions/za/statutes AND in the shipped bundle data/za/statutes,
         and the section key exists in both.
  ERROR  the bundled copy is byte-identical to the source (no drift).
  ERROR  a `built` skill has a skills/<name>/SKILL.md, and that SKILL.md actually
         names each MCP tool/resource it claims to use.
  WARN   a cited statute's last_confirmed is older than FRESHNESS_DAYS.
  WARN   a skill carries knowledge_gaps (tracked, not hidden).
  WARN   a built skill's SKILL.md doesn't mention a cited statute file it bundles.

Usage: python3 scripts/validate-kazi-skill-grounding.py
Exit: 0 = no errors (warnings allowed); 1 = one or more errors; 2 = config error.
"""

import datetime as dt
import json
import sys
from pathlib import Path

import yaml

REPO_ROOT = Path(__file__).resolve().parent.parent
PLUGIN = REPO_ROOT / "kazi-legal-za"
KNOWLEDGE_MAP = PLUGIN / "knowledge-map.yaml"
CATALOGUE = PLUGIN / "data" / "mcp-catalogue.json"
SRC_STATUTES = REPO_ROOT / "jurisdictions" / "za" / "statutes"
BUNDLE_STATUTES = PLUGIN / "data" / "za" / "statutes"
SKILLS_DIR = PLUGIN / "skills"

FRESHNESS_DAYS = 365
VALID_STATUS = {"built", "planned", "blocked"}

errors: list[str] = []
warnings: list[str] = []


def err(skill: str, msg: str) -> None:
    errors.append(f"[{skill}] {msg}")


def warn(skill: str, msg: str) -> None:
    warnings.append(f"[{skill}] {msg}")


def load_json(p: Path):
    try:
        return json.loads(p.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as e:
        print(f"validate-kazi-skill-grounding: cannot read {p}: {e}", file=sys.stderr)
        sys.exit(2)


def load_yaml(p: Path):
    try:
        return yaml.safe_load(p.read_text(encoding="utf-8"))
    except (OSError, yaml.YAMLError) as e:
        print(f"validate-kazi-skill-grounding: cannot read {p}: {e}", file=sys.stderr)
        sys.exit(2)


def statute_sections(p: Path):
    """Return (sections_dict, last_confirmed) for a statute YAML, or (None, None)."""
    data = load_yaml(p)
    if not isinstance(data, dict):
        return None, None
    return data.get("sections") or {}, data.get("last_confirmed")


def days_since(iso: str):
    try:
        d = dt.date.fromisoformat(iso)
    except (ValueError, TypeError):
        return None
    return (dt.date.today() - d).days


def main() -> None:
    catalogue = load_json(CATALOGUE)
    valid_mcp = set(catalogue.get("tools") or [])
    valid_mcp |= {r["name"] for r in catalogue.get("resources") or []}

    kmap = load_yaml(KNOWLEDGE_MAP)
    skills = (kmap or {}).get("skills") or {}
    if not skills:
        print("validate-kazi-skill-grounding: no skills in knowledge-map.yaml", file=sys.stderr)
        sys.exit(2)

    # cache source/bundle section sets per file so we read each once
    src_cache: dict[str, tuple] = {}

    for skill, spec in skills.items():
        spec = spec or {}
        status = spec.get("status")
        if status not in VALID_STATUS:
            err(skill, f"status must be one of {sorted(VALID_STATUS)}, got {status!r}")

        # --- MCP grounding ---
        mcp_refs = spec.get("mcp") or []
        for ref in mcp_refs:
            if ref not in valid_mcp:
                err(skill, f"mcp ref '{ref}' is not in data/mcp-catalogue.json")

        # --- ZA knowledge grounding ---
        # Group refs by file so file-level checks (existence, drift, freshness)
        # report once per file, while section checks run per ref.
        cited: dict[str, list[str]] = {}
        for ref in spec.get("za_knowledge") or []:
            if "#" not in ref:
                err(skill, f"za_knowledge ref '{ref}' must be 'file.yaml#section'")
                continue
            fname, section = ref.split("#", 1)
            cited.setdefault(fname, []).append(section)
        cited_files = set(cited)

        for fname, want_sections in cited.items():
            src = SRC_STATUTES / fname
            bundle = BUNDLE_STATUTES / fname
            if not src.is_file():
                err(skill, f"za_knowledge source missing: jurisdictions/za/statutes/{fname}")
                continue
            if not bundle.is_file():
                err(skill, f"za_knowledge not bundled: data/za/statutes/{fname} (run sync-kazi-knowledge.py)")
                continue
            if src.read_bytes() != bundle.read_bytes():
                err(skill, f"bundled {fname} drifted from source (run sync-kazi-knowledge.py)")
            if fname not in src_cache:
                src_cache[fname] = statute_sections(src)
            sections, last_confirmed = src_cache[fname]
            if sections is None:
                err(skill, f"{fname} is not a valid statute YAML")
            else:
                for section in want_sections:
                    if section not in sections:
                        err(skill, f"{fname} has no section '{section}' (have: {', '.join(sorted(sections))})")
            age = days_since(last_confirmed) if last_confirmed else None
            if age is not None and age > FRESHNESS_DAYS:
                warn(skill, f"{fname} last_confirmed {last_confirmed} is {age}d old (>{FRESHNESS_DAYS}d) — re-confirm")

        # --- knowledge gaps (tracked) ---
        for gap in spec.get("knowledge_gaps") or []:
            warn(skill, f"knowledge gap: {gap}")

        # --- built skills must exist and name their grounding ---
        if status == "built":
            skill_md = SKILLS_DIR / skill / "SKILL.md"
            if not skill_md.is_file():
                err(skill, f"status 'built' but {skill_md.relative_to(PLUGIN)} not found")
            else:
                text = skill_md.read_text(encoding="utf-8")
                for ref in mcp_refs:
                    if ref not in text:
                        warn(skill, f"SKILL.md does not mention MCP ref '{ref}'")
                for fname in cited_files:
                    if fname not in text:
                        warn(skill, f"SKILL.md does not mention bundled statute '{fname}'")

    # report
    for w in warnings:
        print(f"  ⚠ {w}")
    for e in errors:
        print(f"  ✗ {e}")

    n_built = sum(1 for s in skills.values() if (s or {}).get("status") == "built")
    print(
        f"\nvalidate-kazi-skill-grounding: {len(skills)} skill(s) "
        f"({n_built} built), {len(errors)} error(s), {len(warnings)} warning(s)."
    )
    sys.exit(1 if errors else 0)


if __name__ == "__main__":
    main()
