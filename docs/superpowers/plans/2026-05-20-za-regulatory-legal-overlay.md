# ZA Regulatory-Legal Overlay Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build the South African jurisdiction overlay for the regulatory-legal plugin — statute YAML files, topic overlays, skill router, practice profile template, cold-start interview fork, validators, and eval cases.

**Architecture:** Additive overlay in `jurisdictions/za/regulatory-legal/` following the employment-legal reference implementation pattern (ADR-001). Router-based skill wiring: the ZA practice profile template instructs skills to read the router, which maps each skill to its topic overlays and statute files. No upstream SKILL.md modifications except the cold-start interview ZA fork.

**Tech Stack:** YAML (statutes, eval cases), Markdown (topics, router, templates), Python (validators)

**Spec:** `docs/superpowers/specs/2026-05-20-za-regulatory-legal-expansion.md`

---

## File Map

### New files to create

```
jurisdictions/za/regulatory-legal/
├── practice-profile-template.md
├── router.md
└── topics/
    ├── regulatory-process.md
    ├── feed-sources.md
    ├── rule-status-verification.md
    └── regulators.md

jurisdictions/za/statutes/
├── paja.yaml          (NEW)
├── fsr.yaml           (NEW)
├── fica.yaml          (NEW)
├── nema.yaml          (NEW)
├── ohsa.yaml          (NEW)
├── nca.yaml           (NEW)
└── precca.yaml        (NEW)

jurisdictions/za/evals/regulatory-legal/
├── reg-feed-watcher/
│   ├── case-01-fsca-conduct-standard.yaml
│   ├── case-02-popia-code-comment-period.yaml
│   ├── case-03-sarb-speech-fyi.yaml
│   └── case-04-fica-scope-expansion.yaml
├── policy-diff/
│   ├── case-01-popia-breach-notification.yaml
│   ├── case-02-unverified-paja-challenge.yaml
│   ├── case-03-competition-threshold-new-policy.yaml
│   └── case-04-bbbee-eme-below-threshold.yaml
├── comments/
│   ├── case-01-fsca-draft-conduct-standard.yaml
│   ├── case-02-busa-companies-act-coordination.yaml
│   └── case-03-non-lawyer-consequential-gate.yaml
├── gap-surfacer/
│   ├── case-01-overdue-popia-gap.yaml
│   ├── case-02-unverified-rule-no-overdue.yaml
│   └── case-03-watch-to-active-promotion.yaml
├── policy-redraft/
│   ├── case-01-popia-breach-redraft.yaml
│   ├── case-02-new-competition-policy.yaml
│   └── case-03-unverified-rule-redraft.yaml
└── cold-start-interview/
    ├── case-01-inhouse-financial-services.yaml
    ├── case-02-nonlawyer-manufacturing.yaml
    └── case-03-multi-sector-conglomerate.yaml
```

### Existing files to modify

```
jurisdictions/za/statutes/popia.yaml       (extend: add s60-65, s73-77)
jurisdictions/za/statutes/cpa.yaml         (extend: add s60, s71-73, s82)
jurisdictions/za/statutes/competition.yaml (extend: add s11-13, s49A-49D)
jurisdictions/za/statutes/ecta.yaml        (extend: add s29-30)
jurisdictions/za/statutes/cybercrimes.yaml (extend: add CSIRT s54)
jurisdictions/za/statutes/bbbee.yaml       (extend: add s13F-13J)
jurisdictions/za/statutes/paia.yaml        (extend: add s74-77)

scripts/validate-za-router.py             (add regulatory-legal to PRACTICE_AREAS)
scripts/validate-za-templates.py           (add regulatory-legal to TEMPLATE_CONFIG)

regulatory-legal/skills/cold-start-interview/SKILL.md  (add ZA fork after Part 0)
```

---

## Task 1: Create new statute YAML files (7 files)

**Files:**
- Create: `jurisdictions/za/statutes/paja.yaml`
- Create: `jurisdictions/za/statutes/fsr.yaml`
- Create: `jurisdictions/za/statutes/fica.yaml`
- Create: `jurisdictions/za/statutes/nema.yaml`
- Create: `jurisdictions/za/statutes/ohsa.yaml`
- Create: `jurisdictions/za/statutes/nca.yaml`
- Create: `jurisdictions/za/statutes/precca.yaml`

Each statute file must pass `scripts/validate-za-statutes.py`. Schema requires: `statute`, `authority`, `last_confirmed`, `source_url`, `sections` at top level. Each section requires: `ref`, `value`, `effective_from`, `effective_until`, `effect`. Optional: `currency` (must be "ZAR"), `unit`, `gazette_date`, `note`.

- [ ] **Step 1: Create `paja.yaml`**

```yaml
statute: "Promotion of Administrative Justice Act 3 of 2000"
authority: "Department of Justice and Constitutional Development"
last_confirmed: "2026-05-20"
source_url: "https://www.gov.za/documents/promotion-administrative-justice-act"

sections:
  procedural_fairness_individual:
    ref: "PAJA s3"
    value: "adequate notice, reasonable opportunity to make representations, clear statement of action"
    effective_from: "2000-11-30"
    effective_until: null
    effect: "Administrator taking action affecting rights of any person must give procedurally fair process including notice, opportunity to be heard, and clear communication of the action"

  public_participation:
    ref: "PAJA s4"
    value: "notice-and-comment, public inquiry, advisory committee, or combination"
    effective_from: "2000-11-30"
    effective_until: null
    effect: "Administrative action materially and adversely affecting rights of the public requires public participation via one or more of: publication of notice with reasonable comment period, public inquiry, notice-and-comment procedure, advisory committee, or combination"

  written_reasons:
    ref: "PAJA s5"
    value: "90 days to request, 90 days to furnish"
    effective_from: "2000-11-30"
    effective_until: null
    effect: "Any person whose rights have been materially and adversely affected may request written reasons within 90 days; administrator must furnish within 90 days of request"

  judicial_review_grounds:
    ref: "PAJA s6(2)"
    value: "administrator not authorised, material error of law, procedurally unfair, error of fact, not rationally connected, unconstitutional, unreasonable"
    effective_from: "2000-11-30"
    effective_until: null
    effect: "Court may judicially review administrative action on grounds including: administrator not authorised (s6(2)(a)), material error of law (s6(2)(b)), procedurally unfair (s6(2)(c)), materially influenced by error of fact (s6(2)(d)), not rationally connected to purpose (s6(2)(e)), unconstitutional (s6(2)(f)), unreasonable (s6(2)(h))"

  internal_remedies:
    ref: "PAJA s7(2)"
    value: true
    effective_from: "2000-11-30"
    effective_until: null
    effect: "Must exhaust internal remedies before approaching court for judicial review unless court exempts in interests of justice"

  judicial_review_time_limit:
    ref: "PAJA s7(1)"
    value: 180
    unit: "days"
    effective_from: "2000-11-30"
    effective_until: null
    effect: "Judicial review proceedings must be instituted without unreasonable delay and not later than 180 days after internal remedies exhausted or after person was informed of the action and reasons"
    note: "Court may extend on application if interests of justice require"
```

- [ ] **Step 2: Create `fsr.yaml`**

```yaml
statute: "Financial Sector Regulation Act 9 of 2017"
authority: "National Treasury"
last_confirmed: "2026-05-20"
source_url: "https://www.treasury.gov.za/legislation/acts/2017/FSR%20Act%209%20of%202017.pdf"

sections:
  pa_standards_making:
    ref: "FSR Act s98-106"
    value: "prudential standards binding on financial institutions supervised by PA"
    effective_from: "2018-04-01"
    effective_until: null
    effect: "Prudential Authority may make prudential standards that are binding on financial institutions it supervises, covering capital, solvency, governance, risk management"

  fsca_conduct_standards:
    ref: "FSR Act s107-115"
    value: "conduct standards binding on financial institutions supervised by FSCA"
    effective_from: "2018-04-01"
    effective_until: null
    effect: "Financial Sector Conduct Authority may make conduct standards governing market conduct, treating customers fairly, product governance, disclosure"

  joint_standards:
    ref: "FSR Act s126"
    value: "joint standards by PA and FSCA"
    effective_from: "2018-04-01"
    effective_until: null
    effect: "PA and FSCA may jointly make standards on matters of common interest including financial conglomerates, systemically important financial institutions"

  consultation_procedure:
    ref: "FSR Act s131-136"
    value: "publish draft, invite comment, consider representations"
    effective_from: "2018-04-01"
    effective_until: null
    effect: "Before making standards, regulator must publish draft in Government Gazette and on website, invite written comment (typically 30-60 days), consider representations, and publish response to material comments"
    note: "Comment period not fixed by statute — typically 30-60 business days in practice"

  regulatory_strategy:
    ref: "FSR Act s144"
    value: "regulatory strategy published annually"
    effective_from: "2018-04-01"
    effective_until: null
    effect: "Each financial sector regulator must annually publish a regulatory strategy describing planned standards, priorities, and supervisory focus areas"
```

- [ ] **Step 3: Create `fica.yaml`**

```yaml
statute: "Financial Intelligence Centre Act 38 of 2001"
authority: "Financial Intelligence Centre"
last_confirmed: "2026-05-20"
source_url: "https://www.fic.gov.za/resources/pages/legislation.aspx"

sections:
  rmcp_requirement:
    ref: "FICA s42"
    value: "risk management and compliance programme required for all accountable institutions"
    effective_from: "2017-10-02"
    effective_until: null
    effect: "Every accountable institution must develop, document, maintain, and implement a Risk Management and Compliance Programme addressing ML/TF risks"
    note: "s42 replaced earlier s21 RMCP requirements via 2017 amendment"

  beneficial_ownership:
    ref: "FICA s21B"
    value: "establish and verify beneficial ownership of clients"
    effective_from: "2022-12-19"
    effective_until: null
    effect: "Accountable institutions must establish and verify the beneficial ownership of all clients, maintaining records of beneficial owners and their ownership/control structure"

  suspicious_transaction_reporting:
    ref: "FICA s29"
    value: "report to FIC within prescribed period"
    effective_from: "2003-02-01"
    effective_until: null
    effect: "Any person who carries on a business, manages or is employed by a business must report suspicious or unusual transactions to the FIC"

  cash_threshold_reporting:
    ref: "FICA s28"
    value: 24999.99
    currency: "ZAR"
    effective_from: "2010-12-01"
    effective_until: null
    effect: "Cash transactions at or above R25,000 (or prescribed threshold) must be reported to the FIC"
    note: "Threshold set by regulation — verify current amount"

  accountable_institutions:
    ref: "FICA Schedule 1"
    value: "banks, long-term insurers, FSPs, attorneys, estate agents, motor vehicle dealers, crypto-asset service providers, others"
    effective_from: "2003-02-01"
    effective_until: null
    effect: "Schedule 1 lists all categories of accountable institutions subject to FICA compliance obligations including CDD, record-keeping, and reporting"
    note: "Schedule expanded multiple times — crypto-asset service providers added 2022"

  administrative_sanctions:
    ref: "FICA s45C"
    value: "administrative sanctions up to R50 million"
    currency: "ZAR"
    effective_from: "2017-10-02"
    effective_until: null
    effect: "FIC may impose administrative sanctions for non-compliance including financial penalties up to R50 million, restriction or suspension of activities, and remedial action directives"
```

- [ ] **Step 4: Create `nema.yaml`**

```yaml
statute: "National Environmental Management Act 107 of 1998"
authority: "Department of Forestry, Fisheries and the Environment"
last_confirmed: "2026-05-20"
source_url: "https://www.dffe.gov.za/legislation/acts/nema"

sections:
  eia_requirement:
    ref: "NEMA s24"
    value: "environmental impact assessment required for listed activities"
    effective_from: "1999-01-29"
    effective_until: null
    effect: "Activities that may significantly affect the environment require environmental authorisation via EIA process before they may commence — listed in Listing Notices 1-3"

  duty_of_care:
    ref: "NEMA s28"
    value: "reasonable measures to prevent, minimise, and rectify environmental degradation"
    effective_from: "1999-01-29"
    effective_until: null
    effect: "Every person who causes, has caused, or may cause significant environmental degradation must take reasonable measures to prevent, minimise, and rectify such degradation"

  compliance_notice:
    ref: "NEMA s31L"
    value: "compliance notice issued by environmental management inspector"
    effective_from: "2014-06-02"
    effective_until: null
    effect: "Environmental management inspector may issue compliance notice requiring person to cease activity, take remedial steps, or achieve compliance within specified timeframe"

  eia_comment_period:
    ref: "EIA Regulations GN R326 reg 41"
    value: 30
    unit: "days minimum"
    effective_from: "2017-04-07"
    effective_until: null
    effect: "Public participation process for EIA must allow interested and affected parties at least 30 days to submit comments on basic assessment or scoping reports"
    gazette_date: "2017-04-07"

  administrative_fines:
    ref: "NEMA s24G"
    value: "administrative fine for commencing listed activity without authorisation"
    effective_from: "2014-06-02"
    effective_until: null
    effect: "Person who commenced a listed activity without environmental authorisation may apply for rectification and must pay an administrative fine — does not exempt from criminal prosecution"
```

- [ ] **Step 5: Create `ohsa.yaml`**

```yaml
statute: "Occupational Health and Safety Act 85 of 1993"
authority: "Department of Employment and Labour"
last_confirmed: "2026-05-20"
source_url: "https://www.labour.gov.za/legislation/acts/occupational-health-and-safety/occupational-health-and-safety-act"

sections:
  general_duties_employer:
    ref: "OHSA s8"
    value: "provide and maintain safe working environment"
    effective_from: "1994-01-01"
    effective_until: null
    effect: "Every employer must provide and maintain a working environment that is safe and without risk to the health of employees, including safe systems of work, information, training, and supervision"

  ceo_duty:
    ref: "OHSA s16(1)"
    value: "chief executive officer personally liable"
    effective_from: "1994-01-01"
    effective_until: null
    effect: "CEO of an employer is personally responsible for ensuring compliance with the Act unless duties have been validly assigned to another person in writing (s16(2))"

  incident_reporting:
    ref: "OHSA s24"
    value: "report to inspector and investigate"
    effective_from: "1994-01-01"
    effective_until: null
    effect: "Employer must report workplace incidents (death, injury, illness, dangerous occurrence) to an inspector as soon as practicable and investigate the incident"
    note: "Written report within 7 days of incident per General Administrative Regulations"

  incident_report_deadline:
    ref: "OHSA General Administrative Regulations reg 9"
    value: 7
    unit: "days"
    effective_from: "1994-01-01"
    effective_until: null
    effect: "Written incident report (Annexure 1 form) must be submitted to the provincial director within 7 days of the incident"

  prohibition_notice:
    ref: "OHSA s30"
    value: "inspector may prohibit use of plant, machinery, or process"
    effective_from: "1994-01-01"
    effective_until: null
    effect: "Inspector who believes use of plant, machinery, or process threatens health or safety of persons may issue a prohibition notice requiring immediate cessation — non-compliance is a criminal offence"
```

- [ ] **Step 6: Create `nca.yaml`**

```yaml
statute: "National Credit Act 34 of 2005"
authority: "Department of Trade, Industry and Competition"
last_confirmed: "2026-05-20"
source_url: "https://www.thedtic.gov.za/financial-and-consumer-services/consumer-and-corporate-regulation/national-credit-act/"

sections:
  credit_provider_registration:
    ref: "NCA s40"
    value: "must register with NCR before providing credit"
    effective_from: "2007-06-01"
    effective_until: null
    effect: "No person may carry on business as a credit provider unless registered with the National Credit Regulator — registration conditions apply"

  reckless_credit:
    ref: "NCA s80-81"
    value: "credit agreement reckless if granted without proper assessment"
    effective_from: "2007-06-01"
    effective_until: null
    effect: "Credit agreement is reckless if credit provider failed to conduct a proper affordability assessment (s81(2)(a)(i)) or if the consumer did not understand the risks (s81(2)(a)(ii)) or if entering the agreement would make the consumer over-indebted (s81(2)(b))"

  ncr_enforcement:
    ref: "NCA s150-151"
    value: "NCR may issue compliance notices"
    effective_from: "2007-06-01"
    effective_until: null
    effect: "NCR may issue compliance notices to credit providers requiring them to take steps to remedy non-compliance, cease prohibited conduct, or submit to audit"

  administrative_fines:
    ref: "NCA s151"
    value: "administrative fine up to R1 million or 10 percent of annual turnover"
    effective_from: "2007-06-01"
    effective_until: null
    effect: "National Consumer Tribunal may impose administrative fine up to R1 million or 10 percent of annual turnover for contravention of the Act"

  interest_rate_caps:
    ref: "NCA s105, Regulations Table A"
    value: "maximum prescribed rates vary by credit type"
    effective_from: "2016-05-06"
    effective_until: null
    effect: "Maximum interest rates are prescribed per credit type: mortgage agreements (RR+12%), credit facilities (RR+14%), unsecured credit (RR+21%), short-term transactions (5% per month), incidental credit (2% per month)"
    note: "RR = repo rate; rates effective per 2016 regulations — verify current amounts"
```

- [ ] **Step 7: Create `precca.yaml`**

```yaml
statute: "Prevention and Combating of Corrupt Activities Act 12 of 2004"
authority: "Department of Justice and Constitutional Development"
last_confirmed: "2026-05-20"
source_url: "https://www.justice.gov.za/legislation/acts/2004-012.pdf"

sections:
  general_offence:
    ref: "PRECCA s3"
    value: "giving or receiving gratification corruptly is an offence"
    effective_from: "2004-07-27"
    effective_until: null
    effect: "Any person who directly or indirectly gives or receives a gratification in order to act in a manner that amounts to abuse of authority, breach of trust, violation of duty, or misuse of position is guilty of the offence of corruption"

  reporting_duty:
    ref: "PRECCA s34(1)"
    value: "persons in position of authority must report to SAPS"
    effective_from: "2004-07-27"
    effective_until: null
    effect: "Any person who holds a position of authority and knows or ought reasonably to have known that another person has committed a corruption offence involving R100,000 or more must report to any police official"

  reporting_threshold:
    ref: "PRECCA s34(1)"
    value: 100000
    currency: "ZAR"
    effective_from: "2004-07-27"
    effective_until: null
    effect: "Duty to report corruption applies when the amount involved is R100,000 or more"
    note: "Threshold has not been adjusted since commencement"

  penalties:
    ref: "PRECCA s26"
    value: "imprisonment and unlimited fine"
    effective_from: "2004-07-27"
    effective_until: null
    effect: "Conviction for corruption: imprisonment up to life (for s3-16 offences) or unlimited fine, or both; failure to report (s34): imprisonment up to 10 years or fine or both"

  positions_of_authority:
    ref: "PRECCA s34(4)"
    value: "director, partner, chief executive, manager, or person with management authority"
    effective_from: "2004-07-27"
    effective_until: null
    effect: "Reporting duty under s34 applies to: directors of companies, partners, chief executive officers, and any person who has management authority within the entity"
```

- [ ] **Step 8: Run statute validation**

Run: `python3 scripts/validate-za-statutes.py`

Expected: All 7 new files show `OK` with section counts. No FAIL lines for the new files. Existing files continue to pass.

- [ ] **Step 9: Commit**

```bash
git add jurisdictions/za/statutes/paja.yaml jurisdictions/za/statutes/fsr.yaml jurisdictions/za/statutes/fica.yaml jurisdictions/za/statutes/nema.yaml jurisdictions/za/statutes/ohsa.yaml jurisdictions/za/statutes/nca.yaml jurisdictions/za/statutes/precca.yaml
git commit -m "feat(za): add 7 new statute YAML files for regulatory-legal overlay

PAJA, FSR Act, FICA, NEMA, OHSA, NCA, PRECCA — covering administrative
justice, financial sector regulation, AML/CFT, environmental management,
occupational health and safety, national credit, and anti-corruption."
```

---

## Task 2: Extend existing statute YAML files

**Files:**
- Modify: `jurisdictions/za/statutes/popia.yaml`
- Modify: `jurisdictions/za/statutes/cpa.yaml`
- Modify: `jurisdictions/za/statutes/competition.yaml`
- Modify: `jurisdictions/za/statutes/ecta.yaml`
- Modify: `jurisdictions/za/statutes/cybercrimes.yaml`
- Modify: `jurisdictions/za/statutes/bbbee.yaml`
- Modify: `jurisdictions/za/statutes/paia.yaml`

Add new section entries to each existing statute file. New sections follow the same YAML schema. Read each file first, then append new sections under the existing `sections:` key.

- [ ] **Step 1: Extend `popia.yaml` — add Information Regulator enforcement powers and code of conduct process**

Append these sections after the existing sections:

```yaml
  enforcement_powers_assessment:
    ref: "POPIA s73"
    value: "Regulator may conduct assessment of compliance by responsible party"
    effective_from: "2021-07-01"
    effective_until: null
    effect: "Information Regulator may conduct an assessment of processing of personal information by a responsible party to determine compliance with conditions for lawful processing"

  enforcement_notice:
    ref: "POPIA s74"
    value: "enforcement notice requiring responsible party to take or cease steps"
    effective_from: "2021-07-01"
    effective_until: null
    effect: "Information Regulator may serve enforcement notice on a responsible party requiring it to take specified steps or cease specified processing within a specified period"

  code_of_conduct_submission:
    ref: "POPIA s60"
    value: "responsible party or industry body may submit code of conduct to Regulator"
    effective_from: "2021-07-01"
    effective_until: null
    effect: "Any responsible party or body representing a category of responsible parties may submit a code of conduct to the Information Regulator for approval — code must apply the conditions for lawful processing to the specific sector"

  code_of_conduct_approval:
    ref: "POPIA s65"
    value: "Regulator may issue or approve code of conduct"
    effective_from: "2021-07-01"
    effective_until: null
    effect: "Information Regulator may approve a submitted code of conduct after public comment process, or may itself issue a code of conduct for a sector if no adequate code has been submitted"
```

- [ ] **Step 2: Extend `cpa.yaml` — add NCC complaints, product safety recalls, industry codes**

```yaml
  ncc_complaint_procedure:
    ref: "CPA s71"
    value: "consumer may file complaint with NCC"
    effective_from: "2011-04-01"
    effective_until: null
    effect: "Consumer may file complaint with National Consumer Commission alleging contravention of CPA; NCC must investigate and may issue compliance notice or refer to National Consumer Tribunal"

  product_safety_recall:
    ref: "CPA s60"
    value: "Minister or NCC may order product recall"
    effective_from: "2011-04-01"
    effective_until: null
    effect: "If goods are unsafe, the NCC may require supplier to recall, repair, replace, or refund; supplier must notify consumers and implement recall within prescribed timeframes"

  industry_codes:
    ref: "CPA s82"
    value: "industry body may apply to NCC for approval of industry code"
    effective_from: "2011-04-01"
    effective_until: null
    effect: "Industry body may apply to NCC for approval of an industry code of conduct; approved codes supplement CPA and industry ombud schemes may be established to resolve complaints"
```

- [ ] **Step 3: Extend `competition.yaml` — add merger thresholds, investigation powers, leniency**

```yaml
  intermediate_merger_threshold:
    ref: "Competition Act s11(1), GN 216 GG 44453"
    value: "combined turnover/assets R600m+ and target turnover/assets R100m+"
    effective_from: "2021-04-01"
    effective_until: null
    effect: "Intermediate merger: parties must notify Competition Commission and may not implement until approved — combined turnover or asset value at or above R600 million and target at or above R100 million"
    note: "Thresholds set by regulation — verify current amounts"

  large_merger_threshold:
    ref: "Competition Act s13(1), GN 216 GG 44453"
    value: "combined turnover/assets R6.6bn+ and target turnover/assets R190m+"
    effective_from: "2021-04-01"
    effective_until: null
    effect: "Large merger: parties must notify Competition Commission and Competition Tribunal must approve — combined turnover or asset value at or above R6.6 billion and target at or above R190 million"
    note: "Thresholds set by regulation — verify current amounts"

  investigation_powers:
    ref: "Competition Act s49A-49D"
    value: "Commission may summon, search, and seize"
    effective_from: "2009-08-28"
    effective_until: null
    effect: "Competition Commission may summon persons to appear and produce documents (s49A), enter and search premises with warrant (s49B), and seize documents or electronic records (s49C)"

  leniency_policy:
    ref: "Competition Act s49B(2A), Corporate Leniency Policy"
    value: "immunity or reduced penalty for first cartel member to disclose"
    effective_from: "2008-02-01"
    effective_until: null
    effect: "First member of a cartel to approach the Commission and make full disclosure may receive immunity from prosecution or a recommendation for no or reduced administrative penalty"
```

- [ ] **Step 4: Extend `ecta.yaml` — add cryptography registration**

```yaml
  cryptography_provider_registration:
    ref: "ECTA s29-30"
    value: "cryptography service providers must register"
    effective_from: "2002-08-30"
    effective_until: null
    effect: "Cryptography service providers must register with the Department of Communications before providing cryptography products or services in South Africa"
    note: "Registration requirements largely dormant but section remains in force"
```

- [ ] **Step 5: Extend `cybercrimes.yaml` — add CSIRT reporting**

```yaml
  csirt_reporting_obligation:
    ref: "Cybercrimes Act s54"
    value: "electronic communications service providers and financial institutions must report cyber offences to CSIRT"
    effective_from: null
    effective_until: null
    effect: "ESPs and financial institutions must report certain cyber security incidents to national CSIRT within prescribed timeframe once section is brought into force"
    note: "Section 54 NOT YET IN FORCE — awaiting proclamation. Monitor Government Gazette for commencement date"
```

- [ ] **Step 6: Extend `bbbee.yaml` — add Commission investigation powers**

```yaml
  commission_investigation:
    ref: "B-BBEE Act s13F"
    value: "B-BBEE Commission may investigate fronting practices"
    effective_from: "2014-10-24"
    effective_until: null
    effect: "B-BBEE Commission may investigate any person suspected of a fronting practice on own initiative or on receipt of a complaint — may summon persons and require production of documents"

  fronting_offence:
    ref: "B-BBEE Act s13O(1)"
    value: "fronting practice is a criminal offence"
    effective_from: "2014-10-24"
    effective_until: null
    effect: "Person found to have knowingly engaged in a fronting practice is guilty of an offence and liable on conviction to a fine or imprisonment not exceeding 10 years or both"

  sector_code_process:
    ref: "B-BBEE Act s9(1)"
    value: "sector code gazetted by Minister after consultation"
    effective_from: "2014-10-24"
    effective_until: null
    effect: "Minister may publish sector-specific codes of good practice in the Government Gazette after consultation with the relevant sector charter council and the B-BBEE Advisory Council"
```

- [ ] **Step 7: Extend `paia.yaml` — add appeal timelines and complaint process**

```yaml
  internal_appeal_timeline:
    ref: "PAIA s74(1)"
    value: 60
    unit: "days"
    effective_from: "2001-03-09"
    effective_until: null
    effect: "Third party or requester who is aggrieved by a decision of the information officer of a public body may lodge an internal appeal within 60 days of notification of the decision"

  information_regulator_complaint:
    ref: "PAIA s77A"
    value: "complaint to Information Regulator within 180 days"
    effective_from: "2021-06-30"
    effective_until: null
    effect: "A requester or third party may submit a complaint to the Information Regulator within 180 days of the decision, if dissatisfied with the information officer's decision or outcome of internal appeal"
    note: "Information Regulator took over complaint jurisdiction from SAHRC"

  deemed_refusal:
    ref: "PAIA s27"
    value: "failure to respond within 30 days is deemed refusal"
    effective_from: "2001-03-09"
    effective_until: null
    effect: "If information officer of a public body fails to give notice of decision within 30 days (or extended period), the request is deemed refused"
```

- [ ] **Step 8: Run statute validation**

Run: `python3 scripts/validate-za-statutes.py`

Expected: All 7 extended files show `OK` with increased section counts. All other files continue to pass.

- [ ] **Step 9: Commit**

```bash
git add jurisdictions/za/statutes/popia.yaml jurisdictions/za/statutes/cpa.yaml jurisdictions/za/statutes/competition.yaml jurisdictions/za/statutes/ecta.yaml jurisdictions/za/statutes/cybercrimes.yaml jurisdictions/za/statutes/bbbee.yaml jurisdictions/za/statutes/paia.yaml
git commit -m "feat(za): extend 7 existing statute files for regulatory-legal overlay

Add regulatory enforcement, investigation, and consultation sections to
POPIA, CPA, Competition, ECTA, Cybercrimes, B-BBEE, and PAIA statutes."
```

---

## Task 3: Create topic overlay files (4 files)

**Files:**
- Create: `jurisdictions/za/regulatory-legal/topics/regulatory-process.md`
- Create: `jurisdictions/za/regulatory-legal/topics/feed-sources.md`
- Create: `jurisdictions/za/regulatory-legal/topics/rule-status-verification.md`
- Create: `jurisdictions/za/regulatory-legal/topics/regulators.md`

Topic overlays are authoritative markdown reference documents loaded by skills when jurisdiction = ZA. They follow the pattern in `jurisdictions/za/employment-legal/topics/dismissal.md`: H1 title with SA designation, scope statement, `---` dividers, nested headers, no placeholder markers.

Content for each topic file is detailed in the spec at `docs/superpowers/specs/2026-05-20-za-regulatory-legal-expansion.md` sections 3.1-3.4. The subagent implementing this task must read those spec sections and produce the full topic content.

- [ ] **Step 1: Create directory structure**

```bash
mkdir -p jurisdictions/za/regulatory-legal/topics
```

- [ ] **Step 2: Create `regulatory-process.md`**

Write the full topic overlay for SA rulemaking process. Content from spec section 3.1:
- Government Gazette publication process
- PAJA s3 and s4 public participation requirements
- Typical comment periods (30 days standard, 45-60 complex, 14-21 urgent, up to 90 major)
- Multi-step rulemaking (discussion paper → draft → final)
- Comment submission mechanics (email/post — no Regulations.gov)
- NEDLAC process for major socio-economic legislation
- Gazette commencement rules (publication date / future date / proclamation)

Skills served: reg-feed-watcher, comments, cold-start-interview

- [ ] **Step 3: Create `feed-sources.md`**

Write the full topic overlay for SA regulatory feed sources. Content from spec section 3.2:
- Tier 1 free feeds: Open Gazettes (Atom + JSON), direct regulator RSS/email, gov.za
- Tier 2 structured/paid: Laws.Africa Content API, Sabinet
- Regulator-to-feed mapping table for core 12 regulators
- Feed check workflow (pull → filter → classify → digest)
- What doesn't exist: no Federal Register API equivalent, no Regulations.gov, no CourtListener

Skills served: reg-feed-watcher, cold-start-interview

- [ ] **Step 4: Create `rule-status-verification.md`**

Write the full topic overlay for SA rule-status verification. Content from spec section 3.3:
- How SA regulations come into force (publication / future date / proclamation)
- How they can be invalidated (PAJA s6 judicial review, Constitutional Court, regulator withdrawal)
- PAJA s6(2) grounds for judicial review
- PAJA s7 internal remedies and 180-day time limit
- Red flags (SA version) for regulations not in force
- Verification steps (Laws.Africa → Open Gazettes → web search → regulator website)
- `⚠️ RULE STATUS UNVERIFIED` banner with SA-specific framing

Skills served: policy-diff, policy-redraft, gap-surfacer

- [ ] **Step 5: Create `regulators.md`**

Write the full topic overlay for SA regulators. Content from spec section 3.4:
- Core 12 regulators table (SARS, CIPC, DEL, FSCA, PA/SARB, National Treasury, NCR, B-BBEE Commission, SAHPRA, NCC, Competition Commission, Information Regulator)
- For each: enabling statute, instruments issued, consultation process, comment period norms, website URL
- Sector-specific regulators table (NERSA, ICASA, CMS, DMRE, DFFE, FIC)
- Industry bodies for joint regulatory comment submissions (BUSA, BASA, ASISA, Minerals Council, CGCSA, ISPA, SAICA, NSBC)

Skills served: reg-feed-watcher, comments, cold-start-interview, gap-surfacer

- [ ] **Step 6: Commit**

```bash
git add jurisdictions/za/regulatory-legal/topics/
git commit -m "feat(za): add 4 topic overlay files for regulatory-legal

regulatory-process.md, feed-sources.md, rule-status-verification.md,
regulators.md — covering SA rulemaking, feed architecture, rule-status
checks, and core 12 regulators."
```

---

## Task 4: Create skill router

**Files:**
- Create: `jurisdictions/za/regulatory-legal/router.md`

The router maps each in-scope skill to its relevant topic and statute files. Format must match `jurisdictions/za/employment-legal/router.md` exactly: markdown with header, resolution notes, and a single fenced YAML block.

- [ ] **Step 1: Create `router.md`**

```markdown
# Skill Router — South African Regulatory Law Overlay

When jurisdiction = ZA, skills load the topic overlays and statute files listed below.

Topic files resolve to: `jurisdictions/za/regulatory-legal/topics/{name}.md`
Statute files resolve to: `jurisdictions/za/statutes/{name}.yaml`

```yaml
reg-feed-watcher:
  topics: [regulatory-process, feed-sources, regulators]
  statutes: [paja, fsr]

policy-diff:
  topics: [rule-status-verification, regulators]
  statutes: [paja]

comments:
  topics: [regulatory-process, regulators]
  statutes: [paja, fsr]

gap-surfacer:
  topics: [rule-status-verification, regulators]
  statutes: [paja]

policy-redraft:
  topics: [rule-status-verification]
  statutes: [paja]

cold-start-interview:
  topics: [regulatory-process, feed-sources, regulators]
  statutes: [paja, fsr, fica, nema, ohsa, nca, precca, popia, cpa, competition, ecta, cybercrimes, bbbee, paia]
```
```

Note: The cold-start-interview loads all statute files because it needs to know the full regulatory landscape for the watchlist configuration. Other skills load only the statutes they directly reference.

- [ ] **Step 2: Commit**

```bash
git add jurisdictions/za/regulatory-legal/router.md
git commit -m "feat(za): add regulatory-legal ZA skill router

Maps 6 in-scope skills to their topic overlays and statute files."
```

---

## Task 5: Create practice profile template

**Files:**
- Create: `jurisdictions/za/regulatory-legal/practice-profile-template.md`

The template follows the pattern of `jurisdictions/za/employment-legal/practice-profile-template.md`. It contains the configuration location comment (with JURISDICTION OVERLAY instruction), SA title, SA-specific sections replacing US sections, SA privilege framework, and the shared guardrails inherited from the US template.

Content design is detailed in the spec section 4 (Practice Profile Template Design). The subagent implementing this task must:

1. Read the US template at `regulatory-legal/CLAUDE.md` for the guardrails, outputs, and infrastructure sections to carry forward
2. Read the ZA employment-legal template at `jurisdictions/za/employment-legal/practice-profile-template.md` for the SA privilege framework and SA-specific patterns
3. Replace US-specific sections per the spec's section replacement table
4. Add the 3 new SA-specific sections (Regulatory landscape, Consultation engagement posture, Government Gazette monitoring)
5. Add the SA privilege caveat for regulatory compliance documents
6. Use `[PLACEHOLDER]` markers for user-configurable fields

- [ ] **Step 1: Create `practice-profile-template.md`**

The template must include these sections (required by `validate-za-templates.py`):
- `# Regulatory Practice Profile — South Africa`
- `## Regulators we watch` (SA regulator table)
- `## Who's using this` (SA role options)
- `## Regulatory landscape` (NEW — SA regulatory domains)
- `## Consultation engagement posture` (NEW — engagement approach + industry bodies)
- `## Government Gazette monitoring` (NEW — cadence, filter, Gazette types)
- `## Available integrations` (Open Gazettes, Laws.Africa, SA regulator RSS)
- `## Policy library`
- `## Materiality threshold` (SA examples)
- `## Gap response process`
- `## Feed configuration` (Open Gazettes, Laws.Africa, SA regulator feeds)
- `## Outputs` (SA privilege header + regulatory compliance privilege caveat)
- `## Seed documents`

SA-required terms that must appear in the template: `PAJA`, `Government Gazette`, `FSCA`, `Information Regulator`, `Open Gazettes`, `admitted attorney`, `legal professional privilege`, `responsible party`, `POPIA`

US-forbidden terms (outside privilege caveat): `Federal Register`, `NPRM`, `OSHA` (US), `EEOC`, `FTC`, `SEC`, `CFPB`, `Regulations.gov`, `CourtListener`

- [ ] **Step 2: Commit**

```bash
git add jurisdictions/za/regulatory-legal/practice-profile-template.md
git commit -m "feat(za): add regulatory-legal ZA practice profile template

SA-specific sections for regulatory landscape, consultation engagement,
Gazette monitoring. SA privilege framework with regulatory compliance
caveat. Replaces US integrations with Open Gazettes and Laws.Africa."
```

---

## Task 6: Add ZA fork to cold-start interview

**Files:**
- Modify: `regulatory-legal/skills/cold-start-interview/SKILL.md`

Add a jurisdiction check section after Part 0, following the exact pattern from `employment-legal/skills/cold-start-interview/SKILL.md` lines 182-260. The fork detects jurisdiction = ZA from the company profile and branches into SA-specific questions.

- [ ] **Step 1: Read the existing SKILL.md and locate the insertion point**

The fork goes after the Part 0 sections are written and before the US-specific interview continues. Find the section boundary after Part 0 (role, integrations, practice setting) and before the watchlist/regulator questions begin.

- [ ] **Step 2: Insert the ZA fork**

Add `### Jurisdiction check — South African overlay` section containing:

1. Check company profile for jurisdiction = ZA
2. Fork instruction: "The rest of this interview uses SA-specific questions. The output writes to the ZA practice profile template."
3. SA Part 1: Regulatory domains (Q1) and regulator watchlist confirmation (Q2) — 6 must-have questions
4. SA Part 2: Consultation and Gazette configuration (Q3, Q4, Q5, Q6)
5. SA Part 3: Nice-to-have questions (Q7-Q10, full setup only)
6. SA Part 4: Seed documents

Question content is specified in the spec section 5 (Cold-Start Interview Questions).

- [ ] **Step 3: Commit**

```bash
git add regulatory-legal/skills/cold-start-interview/SKILL.md
git commit -m "feat(za): add ZA fork to regulatory-legal cold-start interview

Jurisdiction check after Part 0 branches into SA-specific questions
covering regulatory domains, regulator watchlist, Gazette monitoring,
consultation engagement, and industry body memberships."
```

---

## Task 7: Extend validation scripts

**Files:**
- Modify: `scripts/validate-za-router.py` (line 27-58: add regulatory-legal to PRACTICE_AREAS)
- Modify: `scripts/validate-za-templates.py` (line 19-159: add regulatory-legal to TEMPLATE_CONFIG)

- [ ] **Step 1: Add regulatory-legal to `validate-za-router.py`**

Add a new entry to the `PRACTICE_AREAS` list after the ip-legal entry:

```python
    {
        "name": "regulatory-legal",
        "router": REPO_ROOT / "jurisdictions" / "za" / "regulatory-legal" / "router.md",
        "skills_dir": REPO_ROOT / "regulatory-legal" / "skills",
        "topics_dir": REPO_ROOT / "jurisdictions" / "za" / "regulatory-legal" / "topics",
    },
```

- [ ] **Step 2: Add regulatory-legal to `validate-za-templates.py`**

Add a new entry to the `TEMPLATE_CONFIG` dict:

```python
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
```

- [ ] **Step 3: Run validators**

```bash
python3 scripts/validate-za-router.py
python3 scripts/validate-za-templates.py
```

Expected: `OK: [regulatory-legal]` from both validators.

- [ ] **Step 4: Commit**

```bash
git add scripts/validate-za-router.py scripts/validate-za-templates.py
git commit -m "feat(za): extend validators for regulatory-legal overlay

Add regulatory-legal to router cross-reference validator and template
completeness validator with SA-required terms and US-forbidden terms."
```

---

## Task 8: Create scenario eval cases (20 cases)

**Files:**
- Create: 20 YAML files under `jurisdictions/za/evals/regulatory-legal/`

Each eval case follows the schema from existing cases (e.g., `jurisdictions/za/evals/privacy-legal/policy-monitor/case-01-undisclosed-subprocessor.yaml`): `name`, `skill`, `input`, `expected_flags`, `expected_statutes`, `must_not_contain`, `notes`.

Case content is fully specified in the spec section 7 (Eval Case Outlines). The subagent implementing this task must create all 20 cases with the exact content from the spec.

- [ ] **Step 1: Create directory structure**

```bash
mkdir -p jurisdictions/za/evals/regulatory-legal/{reg-feed-watcher,policy-diff,comments,gap-surfacer,policy-redraft,cold-start-interview}
```

- [ ] **Step 2: Create reg-feed-watcher cases (4)**

Create `case-01-fsca-conduct-standard.yaml`, `case-02-popia-code-comment-period.yaml`, `case-03-sarb-speech-fyi.yaml`, `case-04-fica-scope-expansion.yaml` per spec section 7.1.

- [ ] **Step 3: Create policy-diff cases (4)**

Create `case-01-popia-breach-notification.yaml`, `case-02-unverified-paja-challenge.yaml`, `case-03-competition-threshold-new-policy.yaml`, `case-04-bbbee-eme-below-threshold.yaml` per spec section 7.2.

- [ ] **Step 4: Create comments cases (3)**

Create `case-01-fsca-draft-conduct-standard.yaml`, `case-02-busa-companies-act-coordination.yaml`, `case-03-non-lawyer-consequential-gate.yaml` per spec section 7.3.

- [ ] **Step 5: Create gap-surfacer cases (3)**

Create `case-01-overdue-popia-gap.yaml`, `case-02-unverified-rule-no-overdue.yaml`, `case-03-watch-to-active-promotion.yaml` per spec section 7.4.

- [ ] **Step 6: Create policy-redraft cases (3)**

Create `case-01-popia-breach-redraft.yaml`, `case-02-new-competition-policy.yaml`, `case-03-unverified-rule-redraft.yaml` per spec section 7.5.

- [ ] **Step 7: Create cold-start-interview cases (3)**

Create `case-01-inhouse-financial-services.yaml`, `case-02-nonlawyer-manufacturing.yaml`, `case-03-multi-sector-conglomerate.yaml` per spec section 7.6.

- [ ] **Step 8: Commit**

```bash
git add jurisdictions/za/evals/regulatory-legal/
git commit -m "feat(za): add 20 regulatory-legal eval cases

4 reg-feed-watcher, 4 policy-diff, 3 comments, 3 gap-surfacer,
3 policy-redraft, 3 cold-start-interview — covering SA regulatory
process, Gazette monitoring, rule-status verification, and comment
period tracking."
```

---

## Task 9: Final validation run

**Files:** None created — validation only.

- [ ] **Step 1: Run all three validators**

```bash
python3 scripts/validate-za-statutes.py
python3 scripts/validate-za-router.py
python3 scripts/validate-za-templates.py
```

Expected output:
- Statutes: all files `OK` (26 existing + 7 new = 33 total)
- Router: `OK: [regulatory-legal] 6 skills, all references resolve`
- Templates: `OK: [regulatory-legal] practice-profile-template.md`

- [ ] **Step 2: Run existing upstream validation**

```bash
python3 -c "import json,glob; [json.load(open(f)) for f in glob.glob('**/*.json', recursive=True)]"
```

Expected: No errors (JSON sanity check).

- [ ] **Step 3: Verify directory structure**

```bash
find jurisdictions/za/regulatory-legal -type f | sort
```

Expected:
```
jurisdictions/za/regulatory-legal/practice-profile-template.md
jurisdictions/za/regulatory-legal/router.md
jurisdictions/za/regulatory-legal/topics/feed-sources.md
jurisdictions/za/regulatory-legal/topics/regulators.md
jurisdictions/za/regulatory-legal/topics/regulatory-process.md
jurisdictions/za/regulatory-legal/topics/rule-status-verification.md
```

- [ ] **Step 4: Verify eval case count**

```bash
find jurisdictions/za/evals/regulatory-legal -name "*.yaml" | wc -l
```

Expected: `20`

- [ ] **Step 5: Spot-check a statute for schema compliance**

```bash
python3 -c "
import yaml
data = yaml.safe_load(open('jurisdictions/za/statutes/paja.yaml'))
print(f'Statute: {data[\"statute\"]}')
print(f'Sections: {len(data[\"sections\"])}')
for k, v in data['sections'].items():
    print(f'  {k}: {v[\"ref\"]}')
"
```

Expected: 6 sections with correct refs.

- [ ] **Step 6: Spot-check router cross-references**

```bash
python3 -c "
import yaml, re
from pathlib import Path
text = Path('jurisdictions/za/regulatory-legal/router.md').read_text()
m = re.search(r'\`\`\`yaml\s*\n(.*?)\`\`\`', text, re.DOTALL)
router = yaml.safe_load(m.group(1))
print(f'Skills: {len(router)}')
for skill, refs in router.items():
    topics = refs.get('topics', [])
    statutes = refs.get('statutes', [])
    print(f'  {skill}: {len(topics)} topics, {len(statutes)} statutes')
"
```

Expected: 6 skills with correct topic/statute counts.
