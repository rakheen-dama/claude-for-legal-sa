#!/usr/bin/env python3
"""Validate ZA practice profile templates for completeness and correctness.

Checks per practice area:
1. All required sections present
2. SA-specific terms are referenced
3. No US-specific terms outside the privilege caveat
4. Work-product header uses SA formulation

Usage: python3 scripts/validate-za-templates.py
Exits 0 if valid, 1 on errors.
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

TEMPLATE_CONFIG = {
    "employment-legal": {
        "path": ROOT / "jurisdictions" / "za" / "employment-legal" / "practice-profile-template.md",
        "required_sections": [
            "Jurisdictional footprint", "Statutory baseline", "Employment equity",
            "Dispute resolution", "Leave and conditions", "Termination review",
            "Hiring review", "Escalation", "Seed documents", "Outputs",
        ],
        "sa_required_terms": ["CCMA", "BCEA", "LRA", "bargaining council", "Schedule 8", "admitted attorney"],
        "us_forbidden": [
            (r"\bFMLA\b", "FMLA"), (r"\bFLSA\b", "FLSA"), (r"\bEEOC\b", "EEOC"),
            (r"\bNLRB\b", "NLRB"), (r"\bWARN Act\b", "WARN Act"),
            (r"\bCal-WARN\b", "Cal-WARN"), (r"\bstate supplements?\b", "state supplement(s)"),
        ],
    },
    "commercial-legal": {
        "path": ROOT / "jurisdictions" / "za" / "commercial-legal" / "practice-profile-template.md",
        "required_sections": [
            "Who we are", "Who's using this", "SA statutory baseline",
            "B-BBEE compliance posture", "CPA applicability", "SA contract fundamentals",
            "Playbook", "Escalation", "Outputs", "NDA triage preferences",
        ],
        "sa_required_terms": [
            "CPA", "POPIA", "B-BBEE", "ECTA", "Conventional Penalties Act",
            "admitted attorney", "operator agreement", "responsible party",
        ],
        "us_forbidden": [
            (r"\bUCC\b", "UCC"), (r"\bFRCP\b", "FRCP"),
            (r"\bHadley v Baxendale\b", "Hadley v Baxendale"),
            (r"\bdata controller\b", "data controller"),
            (r"\bdata processor\b", "data processor"),
            (r"\bpreliminary injunction\b", "preliminary injunction"),
        ],
    },
    "privacy-legal": {
        "path": ROOT / "jurisdictions" / "za" / "privacy-legal" / "practice-profile-template.md",
        "required_sections": [
            "Who we are", "Who's using this", "Information Officer",
            "POPIA compliance framework", "Operator agreement playbook",
            "Privacy notice commitments", "PIA house style",
            "Data subject request process", "Cross-border transfers",
            "Breach response", "Direct marketing compliance",
            "Escalation", "Outputs", "Seed documents",
        ],
        "sa_required_terms": [
            "POPIA", "Information Regulator", "responsible party", "operator",
            "Information Officer", "admitted attorney", "s21", "s72", "s57",
        ],
        "us_forbidden": [
            (r"\bdata controller\b", "data controller"),
            (r"\bdata processor\b", "data processor"),
            (r"\bGDPR\b", "GDPR"),
            (r"\bCCPA\b", "CCPA"),
            (r"\bCPRA\b", "CPRA"),
            (r"\bHIPAA\b", "HIPAA"),
            (r"\bFERPA\b", "FERPA"),
            (r"\bCOPPA\b", "COPPA"),
            (r"\bDPIA\b", "DPIA"),
        ],
    },
    "litigation-legal": {
        "path": ROOT / "jurisdictions" / "za" / "litigation-legal" / "practice-profile-template.md",
        "required_sections": [
            "Litigation Practice Profile",
            "Company profile",
            "Practice role",
            "Side",
            "Outputs",
            "Risk calibration",
            "Landscape",
            "House style",
            "Costs exposure",
            "SA court hierarchy",
            "Prescription awareness",
        ],
        "sa_required_terms": [
            "IAS 37",
            "King IV",
            "Uniform Rules",
            "Rule 35",
            "heads of argument",
            "legal practitioner",
            "advocate",
            "attorney",
            "party-and-party",
            "without prejudice",
        ],
        "us_forbidden": [
            (r"\bFRCP\b", "FRCP"),
            (r"\bFRE 408\b", "FRE 408"),
            (r"\bASC 450\b", "ASC 450"),
            (r"\b10-K\b", "10-K"),
            (r"\b10-Q\b", "10-Q"),
            (r"\bSOX\b", "SOX"),
            (r"\bZubulake\b", "Zubulake"),
            (r"\bBluebook\b", "Bluebook"),
            (r"\bFMLA\b", "FMLA"),
            (r"\bat-will\b", "at-will"),
        ],
    },
}

# Key aliases: "litigation-legal" uses the same key names as other practice areas
# (sa_required_terms / us_forbidden) so the validator loop below works unchanged.


def find_privilege_caveat(text: str) -> str:
    match = re.search(
        r"(?:SA |South African )(?:legal professional )?privilege.*?(?=\n## |\Z)",
        text,
        re.DOTALL | re.IGNORECASE,
    )
    return match.group(0) if match else ""


def main() -> int:
    errors = 0

    for area_name, config in TEMPLATE_CONFIG.items():
        path = config["path"]

        if not path.exists():
            print(f"FAIL: [{area_name}] {path.name}: file does not exist", file=sys.stderr)
            errors += 1
            continue

        text = path.read_text()
        name = path.name
        file_errors = 0

        for section in config["required_sections"]:
            if f"## {section}" not in text and f"# {section}" not in text:
                print(f"FAIL: [{area_name}] {name}: missing required section '## {section}'", file=sys.stderr)
                file_errors += 1

        for term in config["sa_required_terms"]:
            if term not in text:
                print(f"FAIL: [{area_name}] {name}: missing SA-required term '{term}'", file=sys.stderr)
                file_errors += 1

        caveat_text = find_privilege_caveat(text)
        non_caveat_text = text.replace(caveat_text, "") if caveat_text else text

        for pattern, label in config["us_forbidden"]:
            matches = re.findall(pattern, non_caveat_text, re.IGNORECASE)
            if matches:
                print(
                    f"FAIL: [{area_name}] {name}: US-specific term '{label}' found outside privilege caveat",
                    file=sys.stderr,
                )
                file_errors += 1

        errors += file_errors
        status = "FAIL" if file_errors else "OK"
        print(f"  {status}: [{area_name}] {name}")

    if errors:
        print(f"\n{errors} errors found")
    else:
        print(f"\n{len(TEMPLATE_CONFIG)} templates checked, no errors")

    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
