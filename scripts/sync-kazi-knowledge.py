#!/usr/bin/env python3
"""sync-kazi-knowledge — bundle the jurisdictions/za statute files cited by the
kazi-legal-za skills into the plugin's data/ directory, so they ship on install.

Repo-root directories (jurisdictions/za) are NOT delivered inside an installed
plugin. The kazi-legal-za skills need their SA statute knowledge to be present at
runtime, so every statute referenced in kazi-legal-za/knowledge-map.yaml is copied
into kazi-legal-za/data/za/statutes/. The source of truth stays jurisdictions/za;
this bundle is a generated mirror.

Usage:
  python3 scripts/sync-kazi-knowledge.py            # copy cited files into the bundle
  python3 scripts/sync-kazi-knowledge.py --check     # CI: exit 1 if the bundle is stale/missing

Exit: 0 = bundle in sync (or written); 1 = --check found drift; 2 = config error.
"""

import argparse
import sys
from pathlib import Path

import yaml

REPO_ROOT = Path(__file__).resolve().parent.parent
PLUGIN = REPO_ROOT / "kazi-legal-za"
KNOWLEDGE_MAP = PLUGIN / "knowledge-map.yaml"
SRC_STATUTES = REPO_ROOT / "jurisdictions" / "za" / "statutes"
BUNDLE_STATUTES = PLUGIN / "data" / "za" / "statutes"


def cited_statute_files() -> set[str]:
    """The set of `*.yaml` filenames referenced by any skill's za_knowledge."""
    try:
        data = yaml.safe_load(KNOWLEDGE_MAP.read_text(encoding="utf-8"))
    except (OSError, yaml.YAMLError) as e:
        print(f"sync-kazi-knowledge: cannot read {KNOWLEDGE_MAP}: {e}", file=sys.stderr)
        sys.exit(2)
    files: set[str] = set()
    for skill, spec in (data.get("skills") or {}).items():
        for ref in (spec or {}).get("za_knowledge") or []:
            files.add(ref.split("#", 1)[0])
    return files


def main() -> None:
    ap = argparse.ArgumentParser(description="Bundle cited ZA statutes into kazi-legal-za/data/.")
    ap.add_argument("--check", action="store_true", help="verify the bundle matches source; do not write")
    args = ap.parse_args()

    cited = cited_statute_files()
    if not cited:
        print("sync-kazi-knowledge: no za_knowledge cited in knowledge-map.yaml; nothing to bundle.")
        # An empty bundle is valid, but a stray leftover file would be drift — check for it.
        cited = set()

    missing_src, drift, wrote = [], [], []
    BUNDLE_STATUTES.mkdir(parents=True, exist_ok=True)

    for name in sorted(cited):
        src = SRC_STATUTES / name
        dst = BUNDLE_STATUTES / name
        if not src.is_file():
            missing_src.append(name)
            continue
        src_bytes = src.read_bytes()
        if not dst.is_file() or dst.read_bytes() != src_bytes:
            if args.check:
                drift.append(name)
            else:
                dst.write_bytes(src_bytes)
                wrote.append(name)

    # Any bundled file no longer cited is stale and must go.
    stale = []
    if BUNDLE_STATUTES.is_dir():
        for f in BUNDLE_STATUTES.glob("*.yaml"):
            if f.name not in cited:
                stale.append(f.name)
                if not args.check:
                    f.unlink()

    if missing_src:
        print(f"sync-kazi-knowledge: cited statute(s) not found in {SRC_STATUTES}:", file=sys.stderr)
        for n in missing_src:
            print(f"  - {n}", file=sys.stderr)
        sys.exit(2)

    if args.check:
        if drift or stale:
            print("sync-kazi-knowledge: bundle is OUT OF SYNC with source.", file=sys.stderr)
            for n in drift:
                print(f"  drift:  {n} (run sync-kazi-knowledge.py)", file=sys.stderr)
            for n in stale:
                print(f"  stale:  {n} (no longer cited; run sync-kazi-knowledge.py)", file=sys.stderr)
            sys.exit(1)
        print(f"sync-kazi-knowledge: bundle in sync ({len(cited)} statute(s)).")
        sys.exit(0)

    summary = f"sync-kazi-knowledge: bundle written ({len(cited)} statute(s) cited)."
    if wrote:
        summary += " updated: " + ", ".join(wrote)
    if stale:
        summary += " removed: " + ", ".join(stale)
    print(summary)
    sys.exit(0)


if __name__ == "__main__":
    main()
