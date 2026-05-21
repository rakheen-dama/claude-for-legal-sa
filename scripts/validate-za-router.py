#!/usr/bin/env python3
"""Validate the ZA skill router's cross-references.

Usage: validate-za-router.py
Reads each practice area's router.md, extracts the embedded YAML block, and
verifies that every skill directory, topic file, and statute file referenced
in the router actually exists.

Also warns about orphaned topic files (present on disk but not referenced by
any skill in the router).

Exits 0 if all references resolve, 1 if any are missing or the router cannot
be parsed.
"""
import re
import sys
from pathlib import Path

import yaml


REPO_ROOT = Path(__file__).resolve().parent.parent
STATUTES_DIR = REPO_ROOT / "jurisdictions" / "za" / "statutes"

YAML_FENCE = re.compile(r"```yaml\s*\n(.*?)```", re.DOTALL)

PRACTICE_AREAS = [
    {
        "name": "employment-legal",
        "router": REPO_ROOT / "jurisdictions" / "za" / "employment-legal" / "router.md",
        "skills_dir": REPO_ROOT / "employment-legal" / "skills",
        "topics_dir": REPO_ROOT / "jurisdictions" / "za" / "employment-legal" / "topics",
    },
    {
        "name": "commercial-legal",
        "router": REPO_ROOT / "jurisdictions" / "za" / "commercial-legal" / "router.md",
        "skills_dir": REPO_ROOT / "commercial-legal" / "skills",
        "topics_dir": REPO_ROOT / "jurisdictions" / "za" / "commercial-legal" / "topics",
    },
    {
        "name": "privacy-legal",
        "router": REPO_ROOT / "jurisdictions" / "za" / "privacy-legal" / "router.md",
        "skills_dir": REPO_ROOT / "privacy-legal" / "skills",
        "topics_dir": REPO_ROOT / "jurisdictions" / "za" / "privacy-legal" / "topics",
    },
    {
        "name": "litigation-legal",
        "router": REPO_ROOT / "jurisdictions" / "za" / "litigation-legal" / "router.md",
        "skills_dir": REPO_ROOT / "litigation-legal" / "skills",
        "topics_dir": REPO_ROOT / "jurisdictions" / "za" / "litigation-legal" / "topics",
    },
    {
        "name": "ip-legal",
        "router": REPO_ROOT / "jurisdictions" / "za" / "ip-legal" / "router.md",
        "skills_dir": REPO_ROOT / "ip-legal" / "skills",
        "topics_dir": REPO_ROOT / "jurisdictions" / "za" / "ip-legal" / "topics",
    },  # Phase 5
    {
        "name": "regulatory-legal",
        "router": REPO_ROOT / "jurisdictions" / "za" / "regulatory-legal" / "router.md",
        "skills_dir": REPO_ROOT / "regulatory-legal" / "skills",
        "topics_dir": REPO_ROOT / "jurisdictions" / "za" / "regulatory-legal" / "topics",
    },
    {
        "name": "legal-clinic",
        "router": REPO_ROOT / "jurisdictions" / "za" / "legal-clinic" / "router.md",
        "skills_dir": REPO_ROOT / "legal-clinic" / "skills",
        "topics_dir": REPO_ROOT / "jurisdictions" / "za" / "legal-clinic" / "topics",
    },
    {
        "name": "corporate-legal",
        "router": REPO_ROOT / "jurisdictions" / "za" / "corporate-legal" / "router.md",
        "skills_dir": REPO_ROOT / "corporate-legal" / "skills",
        "topics_dir": REPO_ROOT / "jurisdictions" / "za" / "corporate-legal" / "topics",
    },
]


def extract_yaml(text: str) -> str | None:
    """Return the first fenced YAML block from markdown text."""
    m = YAML_FENCE.search(text)
    return m.group(1) if m else None


def validate_practice_area(area: dict) -> int:
    """Validate a single practice area's router. Returns 0 on success, 1 on failure."""
    name = area["name"]
    router_path = area["router"]
    skills_dir = area["skills_dir"]
    topics_dir = area["topics_dir"]

    if not router_path.exists():
        print(f"FAIL: [{name}] router file not found: {router_path}", file=sys.stderr)
        return 1

    raw = router_path.read_text()
    yaml_text = extract_yaml(raw)
    if yaml_text is None:
        print(f"FAIL: [{name}] no ```yaml``` block found in router.md", file=sys.stderr)
        return 1

    try:
        router = yaml.safe_load(yaml_text)
    except yaml.YAMLError as e:
        print(f"FAIL: [{name}] YAML parse error in router.md: {e}", file=sys.stderr)
        return 1

    if not isinstance(router, dict) or len(router) == 0:
        print(f"FAIL: [{name}] router YAML must be a non-empty mapping", file=sys.stderr)
        return 1

    errors: list[str] = []
    all_referenced_topics: set[str] = set()

    for skill, refs in router.items():
        # Skill directory
        skill_dir = skills_dir / skill
        if not skill_dir.is_dir():
            errors.append(f"{skill}: skill directory not found: {skill_dir.relative_to(REPO_ROOT)}")

        if not isinstance(refs, dict):
            errors.append(f"{skill}: expected a mapping with 'topics' and 'statutes'")
            continue

        # Topic files
        for topic in refs.get("topics", []):
            all_referenced_topics.add(topic)
            topic_file = topics_dir / f"{topic}.md"
            if not topic_file.exists():
                errors.append(f"{skill}: topic file not found: {topic_file.relative_to(REPO_ROOT)}")

        # Statute files
        for statute in refs.get("statutes", []):
            statute_file = STATUTES_DIR / f"{statute}.yaml"
            if not statute_file.exists():
                errors.append(f"{skill}: statute file not found: {statute_file.relative_to(REPO_ROOT)}")

    if errors:
        print(f"FAIL: [{name}] router cross-reference errors", file=sys.stderr)
        for err in errors:
            print(f"  [{name}] {err}", file=sys.stderr)
        return 1

    # Warn about orphaned topic files
    if topics_dir.is_dir():
        existing_topics = {p.stem for p in topics_dir.glob("*.md")}
        orphaned = sorted(existing_topics - all_referenced_topics)
        for orphan in orphaned:
            print(f"WARN: [{name}] orphaned topic file not referenced by any skill: topics/{orphan}.md")

    skill_count = len(router)
    print(f"OK: [{name}] {skill_count} skills, all references resolve")
    return 0


def main() -> int:
    rc = 0
    for area in PRACTICE_AREAS:
        if validate_practice_area(area) != 0:
            rc = 1
    return rc


if __name__ == "__main__":
    sys.exit(main())
