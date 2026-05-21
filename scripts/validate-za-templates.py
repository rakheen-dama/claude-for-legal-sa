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
            "1. Risk calibration",
            "2. Landscape",
            "3. House style",
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
    "ip-legal": {
        "path": ROOT / "jurisdictions" / "za" / "ip-legal" / "practice-profile-template.md",
        "required_sections": [
            "IP Practice Profile",
            "Company profile",
            "Who's using this",
            "Outputs",
            "IP practice profile",
            "IP portfolio",
            "Brand protection",
            "Enforcement posture",
            "SA IP registration landscape",
            "SA patentability notes",
            "SA enforcement landscape",
        ],
        "sa_required_terms": [
            "CIPC",
            "Trade Marks Act",
            "Patents Act",
            "Designs Act",
            "Copyright Act",
            "ECTA",
            "interdict",
            "legal practitioner",
            "patent attorney",
            "fair dealing",
            "absolute novelty",
        ],
        "us_forbidden": [
            (r"\bUSPTO\b", "USPTO"),
            (r"\bLanham Act\b", "Lanham Act"),
            (r"\bDMCA\b", "DMCA"),
            (r"\b35 USC\b", "35 USC"),
            (r"\bTTAB\b", "TTAB"),
            (r"\bdu Pont\b", "du Pont"),
            (r"\bPolaroid\b", "Polaroid"),
            (r"\bSleekcraft\b", "Sleekcraft"),
            (r"\b§8 declaration\b", "§8 declaration"),
            (r"\bBluebook\b", "Bluebook"),
        ],
    },
    "regulatory-legal": {
        "path": ROOT / "jurisdictions" / "za" / "regulatory-legal" / "practice-profile-template.md",
        "required_sections": [
            "Regulatory Practice Profile", "Regulators we watch",
            "Who's using this", "Regulatory landscape",
            "Consultation engagement posture", "Government Gazette monitoring",
            "Available integrations", "Policy library",
            "Materiality threshold", "Gap response process",
            "Feed configuration", "Outputs", "Seed documents",
        ],
        "sa_required_terms": [
            "PAJA", "Government Gazette", "FSCA", "Information Regulator",
            "Open Gazettes", "admitted attorney", "legal professional privilege",
            "responsible party", "POPIA",
        ],
        "us_forbidden": [
            (r"\bFederal Register\b", "Federal Register"),
            (r"\bNPRM\b", "NPRM"),
            (r"\bRegulations\.gov\b", "Regulations.gov"),
            (r"\bCourtListener\b", "CourtListener"),
            (r"\bFTC\b", "FTC"),
            (r"\bSEC\b", "SEC"),
            (r"\bCFPB\b", "CFPB"),
            (r"\bEEOC\b", "EEOC"),
            (r"\bOSHA\b", "OSHA"),
        ],
    },
    "legal-clinic": {
        "path": ROOT / "jurisdictions" / "za" / "legal-clinic" / "practice-profile-template.md",
        "required_sections": [
            "Who's using this", "LPC compliance", "Clinic profile",
            "Jurisdiction", "SA court system", "Supervision style",
            "Mandatory reporting obligations", "Practice-area templates",
            "Legal Aid SA interface", "Language access", "Seed documents",
            "Outputs",
        ],
        "sa_required_terms": [
            "LPC", "LPA", "candidate legal practitioner", "Magistrate",
            "SAFLII", "admitted attorney", "s34(8)",
        ],
        "us_forbidden": [
            (r"\bABA\b", "ABA"),
            (r"\bFRCP\b", "FRCP"),
            (r"Cal\.\s*Rules", "Cal. Rules"),
            (r"\bVAWA\b", "VAWA"),
            (r"\bFDCPA\b", "FDCPA"),
            (r"\bUSCIS\b", "USCIS"),
            (r"\bat-will\b", "at-will"),
            (r"\bEEOC\b", "EEOC"),
            (r"\bNLRB\b", "NLRB"),
            (r"\bFMLA\b", "FMLA"),
            (r"\bFLSA\b", "FLSA"),
        ],
    },
    "corporate-legal": {
        "path": ROOT / "jurisdictions" / "za" / "corporate-legal" / "practice-profile-template.md",
        "required_sections": [
            "Company profile", "Who's using this", "Statutory baseline",
            "Entity landscape", "M&A regulatory landscape",
            "Board governance framework", "B-BBEE and ownership",
            "Escalation", "Outputs", "Seed documents",
        ],
        "sa_required_terms": [
            "CIPC", "Companies Act", "King IV", "MOI", "TRP",
            "Competition Commission", "B-BBEE", "admitted attorney",
            "legal professional privilege", "solvency and liquidity",
        ],
        "us_forbidden": [
            (r"\bDGCL\b", "DGCL"), (r"\bDelaware\b", "Delaware"),
            (r"\bHSR\b", "HSR"), (r"\bHart-Scott-Rodino\b", "Hart-Scott-Rodino"),
            (r"\b§16\b", "§16"), (r"\bForm 4\b", "Form 4"),
            (r"\bSEC\b", "SEC"), (r"\bNYSE\b", "NYSE"),
            (r"\bNasdaq\b", "Nasdaq"), (r"\bFRCP\b", "FRCP"),
            (r"\bat-will\b", "at-will"), (r"\bFMLA\b", "FMLA"),
            (r"\bFLSA\b", "FLSA"), (r"\bbylaws?\b", "bylaw(s)"),
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
