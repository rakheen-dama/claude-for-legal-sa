# ZA Legal-Clinic Overlay Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Adapt the legal-clinic plugin for South African university law clinics by creating statute YAML files, topic overlays, a skill router, a practice profile template, cold-start interview fork, eval cases, and validator updates — all following the employment-legal reference implementation pattern.

**Architecture:** Additive overlays in `jurisdictions/za/legal-clinic/` (per ADR-001). Skills load SA content via a router file referenced from the ZA practice profile template. Shared statute YAML files in `jurisdictions/za/statutes/`. No upstream skill files modified except `cold-start-interview/SKILL.md` (jurisdiction fork after Part 0).

**Tech Stack:** YAML (statute data), Markdown (topic overlays, templates, router), Python (validators)

**Spec:** `docs/superpowers/specs/2026-05-20-za-legal-clinic-expansion.md`

**Reference implementation:** `jurisdictions/za/employment-legal/` — match all patterns exactly.

---

## File Map

### Create (new files)

**Statute YAML files** (8 new in `jurisdictions/za/statutes/`):
- `lpa.yaml` — Legal Practice Act 28 of 2014
- `lpc-rules.yaml` — LPC Rules (GG 41781) + Code of Conduct (GG 42127)
- `legal-aid-sa.yaml` — Legal Aid South Africa Act 39 of 2014
- `dva.yaml` — Domestic Violence Act 116 of 1998
- `maintenance.yaml` — Maintenance Act 99 of 1998
- `childrens-act.yaml` — Children's Act 38 of 2005
- `small-claims.yaml` — Small Claims Courts Act 61 of 1984
- `criminal-procedure.yaml` — Criminal Procedure Act 51 of 1977

**Topic overlay files** (7 new in `jurisdictions/za/legal-clinic/topics/`):
- `clinic-regulatory-framework.md`
- `supervision-and-ethics.md`
- `sa-court-system.md`
- `sa-procedural-rules.md`
- `sa-legal-research.md`
- `clinic-practice-areas.md`
- `clinic-client-access.md`

**Overlay infrastructure** (3 new in `jurisdictions/za/legal-clinic/`):
- `router.md`
- `practice-profile-template.md`

**Eval cases** (16 new in `jurisdictions/za/evals/legal-clinic/`):
- `cold-start-interview/case-01-accredited-wits-clinic.yaml`
- `cold-start-interview/case-02-non-accredited-new-university.yaml`
- `ramp/case-01-first-semester-candidate-gauteng.yaml`
- `build-guide/case-01-housing-eviction-unit.yaml`
- `client-intake/case-01-dva-minor-children.yaml`
- `client-intake/case-02-consumer-debt-nca.yaml`
- `draft/case-01-dva-protection-order.yaml`
- `draft/case-02-demand-letter-saps-assault.yaml`
- `memo/case-01-maintenance-unmarried-mother.yaml`
- `status/case-01-eviction-jhb-magistrate.yaml`
- `research-start/case-01-eviction-pie-act.yaml`
- `research-start/case-02-refugee-asylum-appeal.yaml`
- `deadlines/case-01-prescription-municipality-assault.yaml`
- `deadlines/case-02-dva-return-date.yaml`
- `supervisor-review-queue/case-01-dva-letter-children.yaml`
- `supervisor-review-queue/case-02-queue-overload-ratio.yaml`

### Modify (existing files)

- `jurisdictions/za/statutes/state-liability.yaml` — add Act 40 of 2002 s3 (6-month notice)
- `legal-clinic/skills/cold-start-interview/SKILL.md` — add ZA jurisdiction fork after Part 0
- `scripts/validate-za-router.py` — add legal-clinic to PRACTICE_AREAS
- `scripts/validate-za-templates.py` — add legal-clinic to TEMPLATE_CONFIG
- `scripts/validate-za-statutes.py` — add new statute files to validation list (if hardcoded)

---

## Task 1: Create statute YAML files — clinic regulatory (LPA, LPC Rules, Legal Aid SA)

**Files:**
- Create: `jurisdictions/za/statutes/lpa.yaml`
- Create: `jurisdictions/za/statutes/lpc-rules.yaml`
- Create: `jurisdictions/za/statutes/legal-aid-sa.yaml`

- [ ] **Step 1: Create `lpa.yaml`**

```yaml
statute: "Legal Practice Act 28 of 2014"
authority: "Department of Justice and Constitutional Development"
last_confirmed: "2026-05-20"
source_url: "https://www.saflii.org/za/legis/consol_act/lpa2014120.pdf"

sections:
  law_clinic_definition:
    ref: "LPA s34(8)"
    value: "A law clinic attached to a university faculty of law that renders legal services under supervision of attorneys, accessible to the public, free of charge except disbursements"
    effective_from: null
    effective_until: null
    effect: "Law clinics must be attached to a university, render services under attorney supervision, be publicly accessible, and provide services free of charge (may recover disbursements only)."

  law_clinic_supervision:
    ref: "LPA s34(8)(b)(i)"
    value: "Services rendered by or under the supervision of attorneys"
    effective_from: null
    effective_until: null
    effect: "All legal services rendered by a law clinic must be rendered by or under the direct supervision of admitted attorneys."

  community_service_practitioners:
    ref: "LPA s29, Regulation 4B"
    value: 40
    unit: "hours per calendar year"
    effective_from: "2024-01-01"
    effective_until: null
    effect: "Practising legal practitioners must complete 40 hours of community service or pro bono legal services per calendar year to maintain good standing with the LPC."
    gazette_date: "2023-08-11"

  community_service_candidates:
    ref: "LPA s29, Regulation 4A"
    value: 8
    unit: "hours per calendar year"
    effective_from: "2024-01-01"
    effective_until: null
    effect: "Candidate legal practitioners must complete 8 hours of community service per calendar year as a component of practical vocational training. Must be supervised by principal."
    gazette_date: "2023-08-11"

  admission_requirements:
    ref: "LPA s26(1)"
    value: "LLB degree or recognised equivalent, practical vocational training, competency-based examination"
    effective_from: null
    effective_until: null
    effect: "A person must hold an LLB (or recognised equivalent), complete practical vocational training as a candidate legal practitioner, and pass the LPC competency examination before admission."

  practical_vocational_training_attorney:
    ref: "LPA s26(1)(c), Regulation 6(1)"
    value: 24
    unit: "months (or 12 months with 400hr coursework)"
    effective_from: null
    effective_until: null
    effect: "Candidate attorneys must serve under a PVTC for 24 uninterrupted months (with 150hr coursework during or within 12 months after), or 12 months if 400hr coursework completed beforehand."
```

- [ ] **Step 2: Create `lpc-rules.yaml`**

```yaml
statute: "South African Legal Practice Council Rules (GG 41781, 20 July 2018) and Code of Conduct (GG 42127, 14 December 2018)"
authority: "South African Legal Practice Council"
last_confirmed: "2026-05-20"
source_url: "https://www.lssa.org.za/wp-content/uploads/2020/01/LPC-Rules-9-July-2018.pdf"

sections:
  law_clinic_establishment:
    ref: "LPC Rule 36.1"
    value: "Council may grant annual recognition to a law clinic if it complies with LPA s34(8)(a), is properly constituted, organised and controlled"
    effective_from: null
    effective_until: null
    effect: "Law clinics require annual LPC recognition. Must comply with LPA s34(8)(a), be properly constituted and organised to the Council's satisfaction."

  candidate_engagement_supervision:
    ref: "LPC Rule 37.1.1"
    value: "Candidate must be under direct personal supervision of the engaging legal practitioner or another legal practitioner who is a member of the professional staff"
    effective_from: null
    effective_until: null
    effect: "Candidates at law clinics must work under direct personal supervision of the supervising legal practitioner or another professional staff attorney."

  candidate_max_per_supervisor:
    ref: "LPC Rule 37 proviso"
    value: 6
    unit: "candidate legal practitioners per supervisor"
    effective_from: null
    effective_until: null
    effect: "No legal practitioner at a law clinic may engage more than six candidate legal practitioners at any one time."

  clinic_operating_hours:
    ref: "LPC Rule 37.1.2"
    value: 11
    unit: "months per year minimum"
    effective_from: null
    effective_until: null
    effect: "A law clinic engaging candidates must be open for business during normal business hours for not less than eleven months in any year."

  clinic_practice_breadth:
    ref: "LPC Rule 37.1.5"
    value: "Reasonably wide range of work to give candidate exposure to problems a newly qualified practitioner would expect to encounter"
    effective_from: null
    effective_until: null
    effect: "The clinic must handle a reasonably wide range of work. The Council may direct the clinic to require candidates to attend approved training courses in areas not adequately covered."

  annual_fee_practitioner:
    ref: "LPC Rule 4.1.1"
    value: 2500
    currency: "ZAR"
    unit: "per year"
    effective_from: null
    effective_until: null
    effect: "Practising legal practitioners pay R2,500 annual fee to the Council. First-year practitioners pay R1,500."

  annual_fee_first_year:
    ref: "LPC Rule 4.1.1 proviso"
    value: 1500
    currency: "ZAR"
    unit: "per year"
    effective_from: null
    effective_until: null
    effect: "Legal practitioners in their first year of practice pay a reduced annual fee of R1,500."

  duty_to_report_dishonest_conduct:
    ref: "LPC Rule 54.36"
    value: "Every legal practitioner is required to report dishonest or irregular conduct relating to trust money handling"
    effective_from: null
    effective_until: null
    effect: "Legal practitioners must report to the Council any dishonest or irregular conduct by another trust account practitioner in relation to handling or accounting for trust money."

  code_competence_timeliness:
    ref: "LPC Code of Conduct clause 3.11"
    value: "Legal practitioner must use best efforts to carry out work in a competent and timely manner"
    effective_from: null
    effective_until: null
    effect: "Failure to attend to a client's matter competently and timeously is professional misconduct. The most common basis for LPC disciplinary complaints."

  code_no_disrepute:
    ref: "LPC Code of Conduct clause 3.15"
    value: "Legal practitioner must not bring the legal profession into disrepute"
    effective_from: null
    effective_until: null
    effect: "Conduct that brings the profession into disrepute — including allowing claims to prescribe — is a disciplinary offence."
```

- [ ] **Step 3: Create `legal-aid-sa.yaml`**

```yaml
statute: "Legal Aid South Africa Act 39 of 2014"
authority: "Legal Aid South Africa"
last_confirmed: "2026-05-20"
source_url: "https://legal-aid.co.za/wp-content/uploads/2023/10/Legal-Aid-SA-Act-with-effect-from-02-August-2017.pdf"

sections:
  objects:
    ref: "Legal Aid SA Act s3"
    value: "Render or make available legal aid and legal advice; provide legal representation at state expense; provide education and information concerning legal rights"
    effective_from: "2015-03-01"
    effective_until: null
    effect: "Legal Aid South Africa exists to render legal aid, provide state-funded legal representation, and educate people about legal rights."

  client_privilege_protection:
    ref: "Legal Aid SA Act s19"
    value: "Information and documents shared with Legal Aid SA for quality assessment remain privileged against other parties as attorney-client information"
    effective_from: "2015-03-01"
    effective_until: null
    effect: "When a private practitioner instructed by Legal Aid SA shares file documents for quality assessment, those documents remain privileged against third parties."

  court_directed_representation:
    ref: "Legal Aid SA Act s22"
    value: "Court may direct legal representation at state expense in criminal proceedings after considering personal circumstances, nature and gravity of charge, available representation"
    effective_from: "2015-03-01"
    effective_until: null
    effect: "A criminal court may direct Legal Aid SA to provide representation at state expense, considering the accused's circumstances, charge severity, and existing representation."

  civil_legal_aid_criteria:
    ref: "Legal Aid SA Regulations reg 9"
    value: "Legal Aid SA may grant civil legal aid if good prospects of success, good prospects of enforcement, and resources available"
    effective_from: "2017-07-26"
    effective_until: null
    effect: "Civil legal aid requires Legal Aid SA to be satisfied the matter has merit, an enforceable outcome is likely, and resources exist. Based on written merit report."

  means_test:
    ref: "Legal Aid SA Regulations"
    value: "Household income and asset thresholds determine eligibility"
    effective_from: "2017-07-26"
    effective_until: null
    effect: "Legal aid applicants must meet a means test based on household income and assets. Thresholds are updated periodically by regulation."
    note: "Exact thresholds updated periodically — verify against current Legal Aid Manual"
```

- [ ] **Step 4: Run statute validator on new files**

Run: `python3 scripts/validate-za-statutes.py`
Expected: New files pass schema validation (required fields: ref, value, effective_from, effective_until, effect).

- [ ] **Step 5: Commit**

```bash
git add jurisdictions/za/statutes/lpa.yaml jurisdictions/za/statutes/lpc-rules.yaml jurisdictions/za/statutes/legal-aid-sa.yaml
git commit -m "feat(za): add LPA, LPC Rules, Legal Aid SA statute YAML files for legal-clinic overlay"
```

---

## Task 2: Create statute YAML files — practice area statutes (DVA, Maintenance, Children's Act, Small Claims, Criminal Procedure)

**Files:**
- Create: `jurisdictions/za/statutes/dva.yaml`
- Create: `jurisdictions/za/statutes/maintenance.yaml`
- Create: `jurisdictions/za/statutes/childrens-act.yaml`
- Create: `jurisdictions/za/statutes/small-claims.yaml`
- Create: `jurisdictions/za/statutes/criminal-procedure.yaml`

- [ ] **Step 1: Create `dva.yaml`**

```yaml
statute: "Domestic Violence Act 116 of 1998"
authority: "Department of Justice and Constitutional Development"
last_confirmed: "2026-05-20"
source_url: "https://www.saflii.org/za/legis/consol_act/dva1998178/"

sections:
  protection_order_application:
    ref: "DVA s4(1)"
    value: "Any complainant may apply to the court for a protection order in the prescribed manner"
    effective_from: null
    effective_until: null
    effect: "Any person in a domestic relationship who is or has been subjected to domestic violence may apply for a protection order at the Magistrate's Court."

  application_on_behalf:
    ref: "DVA s4(3)"
    value: "Application may be brought by any person with material interest in wellbeing of complainant — counsellor, health provider, SAPS member, social worker, teacher"
    effective_from: null
    effective_until: null
    effect: "A protection order application may be brought on behalf of the complainant by another person with material interest, with written consent (consent not required for minors, mentally retarded, unconscious, or unable persons)."

  urgent_application:
    ref: "DVA s4(5)"
    value: "Application may be brought outside ordinary court hours or on non-court days if undue hardship would result from delay"
    effective_from: null
    effective_until: null
    effect: "Urgent DVA applications can be filed after hours or on weekends/holidays. The court must deal with the application immediately if satisfied the complainant may suffer undue hardship from delay."

  interim_protection_order:
    ref: "DVA s5(2)"
    value: "Court must issue interim order if prima facie evidence of DV and undue hardship without immediate order"
    effective_from: null
    effective_until: null
    effect: "If the court is satisfied there is prima facie evidence of domestic violence and the complainant may suffer undue hardship without immediate protection, it must issue an interim protection order without notice to the respondent."

  return_date_minimum:
    ref: "DVA s5(5)"
    value: 10
    unit: "days minimum after service"
    effective_from: null
    effective_until: null
    effect: "The return date on an interim protection order may not be less than 10 days after service on the respondent. The respondent may anticipate the return date on 24 hours' written notice."

  saps_service_interim:
    ref: "DVA Regulations"
    value: 24
    unit: "hours for SAPS to serve interim order"
    effective_from: null
    effective_until: null
    effect: "SAPS must serve a domestic violence interim protection order within 24 hours of issue."

  final_protection_order:
    ref: "DVA s6(1)"
    value: "Court must issue final order if respondent does not appear on return date, proper service proved, and prima facie evidence exists"
    effective_from: null
    effective_until: null
    effect: "If the respondent fails to appear and the court is satisfied of proper service and prima facie evidence of DV, the court must issue a final protection order."

  mandatory_reporting:
    ref: "DVA s2B"
    value: "Adult who knows or reasonably believes child, older person, or disabled person is experiencing DV must report to social worker or SAPS"
    effective_from: null
    effective_until: null
    effect: "Mandatory reporting obligation for domestic violence against children, older persons, or persons with disability. Must report to a social worker or SAPS as soon as possible."

  warrant_of_arrest:
    ref: "DVA s8"
    value: "Court must issue suspended warrant of arrest when issuing protection order"
    effective_from: null
    effective_until: null
    effect: "A suspended warrant of arrest is issued simultaneously with the protection order. Breach of the order requires SAPS to arrest the respondent immediately."

  jurisdiction:
    ref: "DVA s12"
    value: "Magistrate's Court in area where complainant or respondent resides, works, studies, or where DV occurred"
    effective_from: null
    effective_until: null
    effect: "Application may be made at the Magistrate's Court covering the area where complainant or respondent resides, works, studies, carries on business, or where the DV took place."
```

- [ ] **Step 2: Create `maintenance.yaml`**

```yaml
statute: "Maintenance Act 99 of 1998"
authority: "Department of Justice and Constitutional Development"
last_confirmed: "2026-05-20"
source_url: "https://www.gov.za/documents/maintenance-act"

sections:
  duty_to_maintain:
    ref: "Maintenance Act s2"
    value: "Parent, person who assumed obligation, or any other person with legal duty to maintain another"
    effective_from: null
    effective_until: null
    effect: "A duty of support exists between parents and children (regardless of marital status of parents), and between any persons where a legal duty to maintain exists."

  maintenance_complaint:
    ref: "Maintenance Act s6"
    value: "Any person having interest may lodge complaint with maintenance officer at Magistrate's Court"
    effective_from: null
    effective_until: null
    effect: "A maintenance complaint is lodged with the maintenance officer at the Magistrate's Court. The officer must investigate and attempt mediation before referring to court."

  maintenance_investigation:
    ref: "Maintenance Act s6(1)(a)-(c)"
    value: "Maintenance officer must investigate, obtain information from respondent, and if matter cannot be settled, refer to court"
    effective_from: null
    effective_until: null
    effect: "The maintenance officer investigates the complaint, obtains financial information from the respondent, attempts mediation, and refers unsettled matters to court for a hearing."

  maintenance_order:
    ref: "Maintenance Act s16"
    value: "Court may make maintenance order after considering needs, means, standard of living, and earning capacity"
    effective_from: null
    effective_until: null
    effect: "The court considers the needs of the dependant, the means and obligations of both parties, the standard of living, and earning capacity in making a maintenance order."

  enforcement:
    ref: "Maintenance Act s31"
    value: "Failure to comply with maintenance order is a criminal offence — fine or imprisonment up to 1 year"
    effective_from: null
    effective_until: null
    effect: "Non-compliance with a maintenance order is a criminal offence. The defaulter may be fined or imprisoned for up to one year, or both."
```

- [ ] **Step 3: Create `childrens-act.yaml`**

```yaml
statute: "Children's Act 38 of 2005"
authority: "Department of Social Development"
last_confirmed: "2026-05-20"
source_url: "https://www.saflii.org/za/legis/consol_act/ca2005104/"

sections:
  mandatory_reporting:
    ref: "Children's Act s110(1)"
    value: "Listed professionals who on reasonable grounds conclude a child has been physically abused, sexually abused, or deliberately neglected must report to DCPO, provincial DSD, or police"
    effective_from: "2010-04-01"
    effective_until: null
    effect: "Legal practitioners are mandatory reporters. Must report via Form 22 to a designated child protection organisation, provincial DSD, or SAPS. Good faith reporting = no civil liability. Failure to report = criminal offence, up to 10 years imprisonment."

  mandatory_reporting_sexual_offences:
    ref: "Sexual Offences Act s54"
    value: "Any person who knows a sexual offence was committed against a child must report to police immediately"
    effective_from: null
    effective_until: null
    effect: "All persons (not just listed professionals) must immediately report known sexual offences against children to SAPS. Failure = criminal offence."

  parental_responsibilities:
    ref: "Children's Act s18"
    value: "Parental responsibilities and rights include care, contact, guardianship, and maintenance"
    effective_from: null
    effective_until: null
    effect: "Every parent has responsibilities and rights comprising care of the child, maintaining contact, acting as guardian, and contributing to maintenance."

  unmarried_father_rights:
    ref: "Children's Act s21"
    value: "Biological father not married to mother acquires parental rights if he consents to being identified, contributes to upbringing, or contributes to expenses"
    effective_from: null
    effective_until: null
    effect: "An unmarried biological father acquires full parental responsibilities and rights if he was living with the mother at birth, consented to identification as father, contributed to upbringing for a reasonable period, or contributed to child-related expenses."

  childrens_court:
    ref: "Children's Act s45"
    value: "Every Magistrate's Court is a children's court for its area of jurisdiction"
    effective_from: null
    effective_until: null
    effect: "Every Magistrate's Court has jurisdiction as a children's court. Matters involving care, contact, guardianship, and child protection are heard in the children's court."

  child_in_need_of_care:
    ref: "Children's Act s150"
    value: "A child is in need of care and protection if abandoned, neglected, abused, exploited, living in circumstances that may seriously harm physical/mental/social well-being"
    effective_from: null
    effective_until: null
    effect: "Triggers investigation and possible removal of child. Social workers must investigate and, if confirmed, bring the matter to the children's court."

  best_interests_standard:
    ref: "Children's Act s7"
    value: "In all matters concerning the care, protection, and well-being of a child, the child's best interests are of paramount importance"
    effective_from: null
    effective_until: null
    effect: "The best interests of the child standard is the paramount consideration in all decisions. Section 7 lists the factors to consider."
```

- [ ] **Step 4: Create `small-claims.yaml`**

```yaml
statute: "Small Claims Courts Act 61 of 1984"
authority: "Department of Justice and Constitutional Development"
last_confirmed: "2026-05-20"
source_url: "https://www.saflii.org/za/legis/consol_act/scca1984214/"

sections:
  monetary_jurisdiction:
    ref: "Small Claims Courts Act s15, GG 42282 GoN 296"
    value: 20000
    currency: "ZAR"
    unit: "maximum claim amount"
    effective_from: "2019-04-01"
    effective_until: null
    effect: "Small Claims Courts may hear claims not exceeding R20,000. Previous limit was R15,000."
    gazette_date: "2019-03-05"

  no_legal_representation:
    ref: "Small Claims Courts Act s7"
    value: "No party to proceedings may be assisted or represented by any person acting for or in expectation of any fee, commission or reward"
    effective_from: null
    effective_until: null
    effect: "Legal representation is not permitted in Small Claims Court. Clinics may advise and prepare documents but candidates may not appear on behalf of the client."

  natural_persons_only:
    ref: "Small Claims Courts Act s14(2)"
    value: "No action may be instituted against the State in a court"
    effective_from: null
    effective_until: null
    effect: "Only natural persons may bring claims. Companies, close corporations, trusts, and the State are excluded. Claims against the State are not permitted."

  excluded_matters:
    ref: "Small Claims Courts Act s15"
    value: "Excluded: divorce, wills, mental capacity, specific performance without damages alternative, defamation, malicious prosecution, wrongful arrest, seduction, breach of promise"
    effective_from: null
    effective_until: null
    effect: "Certain categories of claims are excluded regardless of monetary value, including family law, defamation, and specific performance matters."
```

- [ ] **Step 5: Create `criminal-procedure.yaml`**

```yaml
statute: "Criminal Procedure Act 51 of 1977"
authority: "Department of Justice and Constitutional Development"
last_confirmed: "2026-05-20"
source_url: "https://www.saflii.org/za/legis/consol_act/cpa1977188/"

sections:
  bail_application:
    ref: "CPA s60"
    value: "An accused may apply for bail at any stage of proceedings. Court must consider interests of justice."
    effective_from: null
    effective_until: null
    effect: "Bail applications may be brought at any stage. The court weighs flight risk, interference with evidence/witnesses, danger to community, and the interests of justice. Schedule 5 and 6 offences have reverse onus."

  plea_procedure:
    ref: "CPA s112"
    value: "Accused pleads to charge. Court questions accused to confirm understanding and voluntariness."
    effective_from: null
    effective_until: null
    effect: "On a guilty plea, the court must question the accused to satisfy itself the accused understands the charge and the plea is voluntary. Court may refuse to accept a guilty plea."

  right_to_legal_representation:
    ref: "Constitution s35(3)(f), CPA"
    value: "Every accused has right to legal representation; if substantial injustice would result, to state-funded representation"
    effective_from: null
    effective_until: null
    effect: "Constitutional right to legal representation in criminal proceedings. If accused cannot afford representation and substantial injustice would result, the State must provide it (via Legal Aid SA)."

  appeal_magistrate_court:
    ref: "CPA s309"
    value: "Appeal from Magistrate's Court lies to High Court on questions of fact and law"
    effective_from: null
    effective_until: null
    effect: "An appeal from a Magistrate's Court conviction or sentence lies to the High Court. Notice of appeal must be filed within 14 days of sentence."

  suspended_sentence:
    ref: "CPA s297"
    value: "Court may suspend sentence wholly or partly on conditions for up to 5 years"
    effective_from: null
    effective_until: null
    effect: "The court may suspend all or part of a sentence on conditions. If conditions are breached during the suspension period (up to 5 years), the suspended portion may be put into operation."
```

- [ ] **Step 6: Run statute validator on all new files**

Run: `python3 scripts/validate-za-statutes.py`
Expected: All 8 new statute files pass schema validation.

- [ ] **Step 7: Commit**

```bash
git add jurisdictions/za/statutes/dva.yaml jurisdictions/za/statutes/maintenance.yaml jurisdictions/za/statutes/childrens-act.yaml jurisdictions/za/statutes/small-claims.yaml jurisdictions/za/statutes/criminal-procedure.yaml
git commit -m "feat(za): add DVA, Maintenance, Children's Act, Small Claims, Criminal Procedure statute files"
```

---

## Task 3: Extend state-liability.yaml with Act 40 of 2002

**Files:**
- Modify: `jurisdictions/za/statutes/state-liability.yaml`

- [ ] **Step 1: Read the existing file**

Read `jurisdictions/za/statutes/state-liability.yaml` to understand current structure.

- [ ] **Step 2: Add Act 40 of 2002 sections**

Add to the `sections:` block:

```yaml
  notice_before_proceedings:
    ref: "Institution of Legal Proceedings Against Certain Organs of State Act 40 of 2002, s3"
    value: 6
    unit: "months from date debt became due"
    effective_from: null
    effective_until: null
    effect: "No legal proceedings may be instituted against an organ of state unless the creditor has given the organ written notice of the intention to institute proceedings within 6 months from the date the debt became due. Failure to give notice within 6 months may result in the claim being time-barred."

  notice_content:
    ref: "Act 40 of 2002 s3(2)"
    value: "Notice must set out facts giving rise to debt, nature and extent of debt"
    effective_from: null
    effective_until: null
    effect: "The written notice must contain the facts giving rise to the debt and the nature and extent of the debt or claim."

  waiting_period_after_notice:
    ref: "Act 40 of 2002 s3(4)"
    value: 30
    unit: "days after notice before summons may be served"
    effective_from: null
    effective_until: null
    effect: "No summons may be served on an organ of state within 30 days after service of the notice of intended legal proceedings."
```

- [ ] **Step 3: Run validator and commit**

Run: `python3 scripts/validate-za-statutes.py`
Expected: PASS

```bash
git add jurisdictions/za/statutes/state-liability.yaml
git commit -m "feat(za): extend state-liability.yaml with Act 40 of 2002 notice requirements"
```

---

## Task 4: Create topic overlays — clinic-regulatory-framework.md and supervision-and-ethics.md

**Files:**
- Create: `jurisdictions/za/legal-clinic/topics/clinic-regulatory-framework.md`
- Create: `jurisdictions/za/legal-clinic/topics/supervision-and-ethics.md`

- [ ] **Step 1: Create `clinic-regulatory-framework.md`**

Write the full topic overlay covering: LPA s34(8) law clinic definition and requirements, LPC Rules Part IX (Rules 36-37) — accreditation requirements (Rule 36.1), candidate engagement (Rule 37), max 6 candidates per supervisor, 11-month/year operation, practice breadth requirement, candidate legal practitioner terminology and obligations, community service framework (40hr/8hr from 2024-01-01, structures per LPA s29(2)), LPC Code of Conduct key provisions, PVTC framework.

Follow the `dismissal.md` reference pattern: doctrine header explaining the framework, statutory sections with short-form citations (e.g., "LPA s34(8)"), consequence tables, numbered lists for multi-element requirements.

- [ ] **Step 2: Create `supervision-and-ethics.md`**

Write the full topic overlay covering: SA supervision model vs US/ABA model (direct personal supervision per Rule 37.1.1, no delegated supervision concept), LPA s34(8)(b)(i) requirements, candidate practitioner disclosure obligations in correspondence, SA legal professional privilege (two forms: legal advice privilege and litigation privilege, dominant purpose test per *Ibex RSA Holdco v Tiso Blackstar*), no standalone work-product doctrine, AI output privilege per Baker McKenzie guidance (*Mavundla v MEC*, *Northbound Processing*), POPIA client data obligations in clinic context.

Include a high-risk flags sub-table for supervision-related flags (#6 supervision ratio, #12 unauthorised practice).

- [ ] **Step 3: Commit**

```bash
git add jurisdictions/za/legal-clinic/topics/clinic-regulatory-framework.md jurisdictions/za/legal-clinic/topics/supervision-and-ethics.md
git commit -m "feat(za): add clinic-regulatory-framework and supervision-and-ethics topic overlays"
```

---

## Task 5: Create topic overlays — sa-court-system.md and sa-procedural-rules.md

**Files:**
- Create: `jurisdictions/za/legal-clinic/topics/sa-court-system.md`
- Create: `jurisdictions/za/legal-clinic/topics/sa-procedural-rules.md`

- [ ] **Step 1: Create `sa-court-system.md`**

Write the full topic overlay covering: SA court hierarchy (Magistrates' Court district R200k / regional R400k, High Court 9 divisions, SCA, Constitutional Court), specialist courts (Labour Court, Land Claims Court, Equality Court, Small Claims Court R20k, Children's Court), case number formats per division, court captions and headers (SA format, not US), court terms and recess periods (16 Dec–15 Jan — days between 16 December and 15 January excluded from pleading deadlines per Magistrates' Courts Rules Rule 21B).

Include jurisdiction limit table:

```markdown
| Court | Civil jurisdiction | Key limitation |
|---|---|---|
| Small Claims Court | Up to R20,000 | Natural persons only, no legal representation |
| District Magistrate's Court | Up to R200,000 | Cannot hear divorces, wills, mental capacity |
| Regional Magistrate's Court | R200,001–R400,000 | Can hear divorces, maintenance, customary marriage |
| High Court | Unlimited | Original and appeal jurisdiction |
```

- [ ] **Step 2: Create `sa-procedural-rules.md`**

Write the full topic overlay covering: Magistrates' Courts Rules (time computation — Sat/Sun/holidays excluded, service rules — sheriff or registered post deemed 4th day at 10:00, 20-day plea after notice to defend, 10-day application notice or 20 days if State), Uniform Rules of Court for High Court (Rule 6 notice of motion, Rule 43 interim relief, Rule 53 review), common clinic document formats with SA structure (combined summons, Form 6/J480 DVA application, notice of motion, founding affidavit), court hours (08:00–16:00, filing 08:00–15:00, closed weekends/holidays), service between 07:00–19:00.

Include prescription/deadline plausibility table (SA equivalent of the CA/IL bands in the US deadlines skill):

```markdown
| Claim type | Prescription period | Special notice | Statute |
|---|---|---|---|
| Delict / contract (general) | 3 years | — | Prescription Act s11(d) |
| State organ claim | 3 years | 6-month written notice required | Act 40 of 2002 s3 |
| RAF (owner/driver identified) | 3 years to lodge, 5 years to issue summons | 120-day moratorium after lodge | RAF Act s23-24 |
| RAF (hit-and-run) | 2 years to lodge, 5 years to issue summons | 120-day moratorium | RAF Act s23-24 |
| Negotiable instrument | 6 years | — | Prescription Act s11(c) |
| Mortgage bond / judgment | 30 years | — | Prescription Act s11(a) |
| Joint wrongdoer contribution | 12 months from judgment | — | Apportionment of Damages Act s2(6)(b) |
```

- [ ] **Step 3: Commit**

```bash
git add jurisdictions/za/legal-clinic/topics/sa-court-system.md jurisdictions/za/legal-clinic/topics/sa-procedural-rules.md
git commit -m "feat(za): add sa-court-system and sa-procedural-rules topic overlays"
```

---

## Task 6: Create topic overlay — sa-legal-research.md

**Files:**
- Create: `jurisdictions/za/legal-clinic/topics/sa-legal-research.md`

- [ ] **Step 1: Create `sa-legal-research.md`**

Write the full topic overlay covering: SA research databases (SAFLII — free, primary, replaces Westlaw/CourtListener; Juta/JutaStat — subscription, SA Law Reports; LexisNexis SA/Lexis+ — subscription, All SA Law Reports, BCLR, BLLR; Sabinet Legal — legislation), SA citation format (*2020 (3) SA 1 (CC)* for neutral, *[2020] ZACC 1* for SAFLII), reporter abbreviation table, Government Gazette for legislation and threshold updates, key secondary sources (Lawsa, Juta commentaries, De Rebus journal).

Include database comparison table:

```markdown
| Database | Content | Access | SA equivalent of |
|---|---|---|---|
| SAFLII | Case law (all courts), some legislation | Free | CourtListener |
| Juta/JutaStat | SA Law Reports, SACR, ILJ, legislation, commentary | Subscription (university library) | Westlaw |
| LexisNexis SA / Lexis+ | All SA Law Reports, BCLR, BLLR, BALR, legislation | Subscription (university library) | LexisNexis US |
| Sabinet Legal | Consolidated statutes, Government Gazette | Subscription | — |
```

Include reporter abbreviation table:

```markdown
| Abbreviation | Full name | Publisher | Content |
|---|---|---|---|
| SA | South African Law Reports | Juta | General High Court and above |
| SACR | SA Criminal Law Reports | Juta | Criminal cases |
| BCLR | Butterworths Constitutional Law Reports | LexisNexis | Constitutional Court and constitutional matters |
| BLLR | Butterworths Labour Law Reports | LexisNexis | Labour Court and LAC |
| ILJ | Industrial Law Journal | Juta | Labour law |
| BALR | Butterworths Arbitration Law Reports | LexisNexis | CCMA arbitrations |
| All SA | All South African Law Reports | LexisNexis | All courts |
```

- [ ] **Step 2: Commit**

```bash
git add jurisdictions/za/legal-clinic/topics/sa-legal-research.md
git commit -m "feat(za): add sa-legal-research topic overlay"
```

---

## Task 7: Create topic overlays — clinic-practice-areas.md and clinic-client-access.md

**Files:**
- Create: `jurisdictions/za/legal-clinic/topics/clinic-practice-areas.md`
- Create: `jurisdictions/za/legal-clinic/topics/clinic-client-access.md`

- [ ] **Step 1: Create `clinic-practice-areas.md`**

Write the full topic overlay with sections for each common SA law clinic practice area:

**Family & DVA:** DVA s4 protection order (Form 6/J480), interim order (s5: prima facie + undue hardship), return date min 10 days (s5(5)), final order (s6), suspended warrant (s8), urgency (s4(5) — after hours), mandatory reporting (s2B + Children's Act s110). Maintenance Act s6 complaints, maintenance court, enforcement (s31). Children's Act: care/contact/guardianship (ss18-21), unmarried father (s21), children's court (s45), Form 38, best interests standard (s7).

**Housing & Eviction:** PIE Act (Prevention of Illegal Eviction and Unlawful Occupation of Land Act 19 of 1998) — s4 requires court order for any eviction, mandatory consideration of circumstances including availability of alternative accommodation, notice requirements. Rental Housing Act 50 of 1999 — Rental Housing Tribunal (free, informal, no legal representation required), unfair practice complaints.

**Consumer & Debt:** CPA (Consumer Protection Act 68 of 2008) — consumer rights, defective goods, unfair contract terms. NCA (National Credit Act 34 of 2005) — debt counselling referral (s86), reckless credit (s80-83), in duplum rule (s103(5)).

**Criminal & Delict:** Criminal Procedure Act — bail (s60), plea (s112), legal representation right (Constitution s35(3)(f)). Delict — personal injury (motor vehicle accidents, police brutality, medical negligence), damages, letter of demand, prescription (3 years, Prescription Act s11(d)).

**Refugee & Migration:** Refugees Act 130 of 1998 — asylum application, Refugee Appeal Authority (s24), PAJA s6 administrative review, documentation (asylum seeker permit s22).

Include the 14 high-risk flags table from the spec.

- [ ] **Step 2: Create `clinic-client-access.md`**

Write the full topic overlay covering: Legal Aid SA referral interface (means test, eligibility criteria for criminal (s4-8 of Regulations) and civil (s9 of Regulations) matters, justice centres), free services requirement per LPA s34(8)(c) — clinic may only recover disbursements, clinic eligibility criteria, language access (11 official languages: English, Afrikaans, isiZulu, isiXhosa, Sesotho, Setswana, Sepedi, Tshivenda, Xitsonga, isiNdebele, siSwati), plain-language standards for client-facing documents, common referral pathways (Legal Aid SA justice centres, SAHRC, small claims court commissioners, Equality Court clerks, CCMA for labour matters, Rental Housing Tribunal), community service structures per LPA s29(2).

- [ ] **Step 3: Commit**

```bash
git add jurisdictions/za/legal-clinic/topics/clinic-practice-areas.md jurisdictions/za/legal-clinic/topics/clinic-client-access.md
git commit -m "feat(za): add clinic-practice-areas and clinic-client-access topic overlays"
```

---

## Task 8: Create skill router

**Files:**
- Create: `jurisdictions/za/legal-clinic/router.md`

- [ ] **Step 1: Create `router.md`**

```markdown
# Legal-Clinic — South African Skill Router

Maps each skill to the topic overlays and statute files it should load when jurisdiction = ZA.

Topic files resolve to `jurisdictions/za/legal-clinic/topics/{name}.md`.
Statute files resolve to `jurisdictions/za/statutes/{name}.yaml`.

```yaml
cold-start-interview:
  topics: [clinic-regulatory-framework, supervision-and-ethics, clinic-client-access]
  statutes: [lpa, lpc-rules, legal-aid-sa]

build-guide:
  topics: [clinic-regulatory-framework, supervision-and-ethics]
  statutes: [lpa, lpc-rules]

ramp:
  topics: [clinic-regulatory-framework, supervision-and-ethics, sa-court-system, sa-legal-research, clinic-client-access]
  statutes: [lpa, lpc-rules]

client-intake:
  topics: [clinic-practice-areas, clinic-client-access]
  statutes: [dva, maintenance, childrens-act, small-claims, cpa, nca, popia]

draft:
  topics: [clinic-practice-areas, sa-court-system, sa-procedural-rules]
  statutes: [dva, maintenance, childrens-act, criminal-procedure, magistrates-courts, state-liability]

deadlines:
  topics: [sa-procedural-rules, sa-court-system]
  statutes: [prescription, dva, magistrates-courts, state-liability]

research-start:
  topics: [sa-legal-research, sa-court-system]
  statutes: []

memo:
  topics: [sa-legal-research, clinic-practice-areas]
  statutes: [dva, maintenance, childrens-act]

status:
  topics: [sa-court-system, sa-procedural-rules]
  statutes: [magistrates-courts]

supervisor-review-queue:
  topics: [clinic-regulatory-framework, supervision-and-ethics]
  statutes: [lpa, lpc-rules]
```​
```

Note: The closing triple-backtick above must end the fenced YAML block in the actual file. The router validator parses the fenced `yaml` block.

- [ ] **Step 2: Run router validator**

Run: `python3 scripts/validate-za-router.py`
Expected: May fail because legal-clinic is not yet in PRACTICE_AREAS. That's fixed in Task 11. For now, verify the YAML parses correctly:

```bash
python3 -c "
import yaml, re, pathlib
text = pathlib.Path('jurisdictions/za/legal-clinic/router.md').read_text()
m = re.search(r'\`\`\`yaml\n(.*?)\`\`\`', text, re.DOTALL)
data = yaml.safe_load(m.group(1))
print(f'Skills mapped: {len(data)}')
for skill, mapping in data.items():
    print(f'  {skill}: {len(mapping[\"topics\"])} topics, {len(mapping[\"statutes\"])} statutes')
"
```

Expected output: 10 skills mapped, each with topic and statute counts.

- [ ] **Step 3: Commit**

```bash
git add jurisdictions/za/legal-clinic/router.md
git commit -m "feat(za): add legal-clinic ZA skill router"
```

---

## Task 9: Create practice profile template

**Files:**
- Create: `jurisdictions/za/legal-clinic/practice-profile-template.md`

- [ ] **Step 1: Write the ZA practice profile template**

Follow the employment-legal pattern at `jurisdictions/za/employment-legal/practice-profile-template.md`. The template must include:

1. **Configuration location comment block** — identical structure to employment-legal, pointing to `~/.claude/plugins/config/claude-for-legal/legal-clinic/CLAUDE.md`, with the `JURISDICTION OVERLAY` instruction to read the router at `jurisdictions/za/legal-clinic/router.md`.

2. **Title:** `# University Law Clinic Practice Profile — South Africa`

3. **Sections** (matching spec Section 4):
   - `## Who's using this` — Role (Supervising legal practitioner / Candidate legal practitioner / Clinic staff), LPC enrollment, LPC accreditation status
   - `## LPC compliance` — accreditation, community service hours, PVTC
   - `## Available integrations` — CaseLines, document storage, LPC portal
   - `## Clinic profile` — university, practice areas (SA list), candidates, caseload, languages
   - `## Jurisdiction` — province, Magistrate's Court(s), High Court division, specialist courts
   - `## SA court system` — jurisdiction limit quick reference table
   - `## Supervision style` — 3 models with LPA s34(8) framing
   - `## Mandatory reporting obligations` — Children's Act s110, DVA s2B (non-overridable)
   - `## Practice-area templates` — SA document types per practice area
   - `## Legal Aid SA interface` — referral criteria, justice centre
   - `## Language access` — 11 languages, plain-language target
   - `## Semester` — term end, cohort dates
   - `## Seed documents` — SA-specific expectations
   - `## Outputs` — SA work-product header (`[AI-ASSISTED DRAFT — requires candidate analysis and supervising practitioner review before privilege may attach]`), privilege caveat (AI not automatically privileged, Baker McKenzie guidance), SAFLII in reviewer note
   - `## Supervisor guide` — per-practice-area guide path
   - `## Plain-language standards` — reading level, prohibited jargon
   - `## Deadline warnings` — default cadence

4. **Jurisdiction-neutral sections** carried forward from US template: Output safeguards, decision posture, shared guardrails, retrieved-content trust, large input/output handling, proportionality, scaffolding not blinders, ad-hoc questions, verification log.

- [ ] **Step 2: Commit**

```bash
git add jurisdictions/za/legal-clinic/practice-profile-template.md
git commit -m "feat(za): add legal-clinic ZA practice profile template"
```

---

## Task 10: Add cold-start interview ZA fork

**Files:**
- Modify: `legal-clinic/skills/cold-start-interview/SKILL.md`

- [ ] **Step 1: Read the current cold-start interview SKILL.md**

Read the file, locate the Part 0 completion point (where jurisdiction would be determined), and identify where to insert the fork — matching the employment-legal pattern at approximately line 182.

- [ ] **Step 2: Insert ZA jurisdiction fork**

After the Part 0 sections (role check, ethical preconditions), add the jurisdiction detection and SA-specific interview path. Match the employment-legal fork pattern:

```markdown
### Jurisdiction check — South African overlay

After writing the Part 0 sections, check the company profile for jurisdiction:

- Read `~/.claude/plugins/config/claude-for-legal/company-profile.md` → `Primary jurisdiction`
- If the primary jurisdiction is **South Africa** (or ZA, or the user's clinic is SA-based based on the company profile answers):

**Fork to the SA interview path.** The rest of this interview uses SA-specific questions. The output writes to the ZA practice profile template at `${CLAUDE_PLUGIN_ROOT}/../../../jurisdictions/za/legal-clinic/practice-profile-template.md` instead of the US template.

If the primary jurisdiction is NOT South Africa, continue with the US interview path below.

---

#### ZA-1: LPC accreditation status (1 min)

"Is this clinic accredited by the Legal Practice Council under Rule 36?"

Options: Yes / In progress / No (university clinic not requiring accreditation)

If accredited: record status, note candidates can count clinic time toward PVTC.
If not: flag that candidates' time may not count toward PVTC. Note this in the practice profile.

#### ZA-2: Supervising legal practitioner(s) (2 min)

"Who are the supervising legal practitioners?"

For each supervisor, capture:
- Full name
- LPC enrollment number
- Date of admission
- Attorney or advocate?
- Current number of candidate legal practitioners under supervision (max 6 per LPC Rule 37)

Flag if any supervisor is at or above 6 candidates.

#### ZA-3: Province and courts (1 min)

"Which province is the clinic in? Which Magistrate's Court(s) and High Court division does the clinic primarily appear in?"

Capture: Province, primary Magistrate's Court(s) (district name), High Court division, any specialist courts used (Small Claims, Equality Court, Children's Court).

#### ZA-4: Practice areas (1 min)

"Which practice areas does the clinic handle?"

Options (multi-select): Family & DVA / Housing & eviction / Consumer & debt / Criminal & delict / Refugee & migration / Labour / General civil / Other

For each selected area, load the corresponding section in the practice-area templates.

#### ZA-5: Supervision model (2 min)

"Under LPA s34(8), all clinic work must be under the direct personal supervision of an admitted attorney. How do you want to operationalise that supervision within the plugin?"

Present the three models (formal review queue / configurable flags / lighter-touch) with SA-specific framing. If formal or configurable: capture trigger conditions.

#### ZA-6: Mandatory reporting acknowledgment (1 min)

Only if practice areas include Family & DVA, Criminal, or any area likely to involve children:

"You and your candidates have mandatory reporting obligations under Children's Act s110 and DVA s2B. The plugin will flag potential triggers during intake and case status. Is this understood and accepted?"

Capture acknowledgment. This is a non-overridable gate — the plugin flags regardless of response, but the acknowledgment is recorded.

#### ZA-7: Languages (1 min)

"Which of South Africa's 11 official languages can the clinic serve? Do you have interpreter access for others?"

Capture: list of languages served directly + interpreter availability.

#### ZA-8: Legal Aid SA interface (1 min)

"Does the clinic have a relationship with Legal Aid South Africa?"

Options: Active referral partnership / Informal referrals / No relationship
If active or informal: "Which justice centre do you refer to?"

#### ZA-9: Seed documents (3 min)

"Upload your clinic's key documents. Target: 10-20 items. SA-specific documents I'd especially like to see:
- Clinic handbook or operating manual
- Standard intake forms
- DVA Form 6 (J480) blank template
- Magistrates' Courts Rules or practice directives for your division
- Common template letters (demand letters, court correspondence)
- Legal Aid SA means test guide
- Example case file (scrubbed)"

#### ZA-10: Nice-to-haves (if time)

If the supervisor has time, ask about: CaseLines/e-filing, academic calendar, plain-language preferences, Small Claims Court approach, community service hours tracking.

---

Write the completed answers to the ZA practice profile template at `jurisdictions/za/legal-clinic/practice-profile-template.md` → user config path. Confirm with the supervisor before finalising.
```

- [ ] **Step 3: Commit**

```bash
git add legal-clinic/skills/cold-start-interview/SKILL.md
git commit -m "feat(za): add ZA fork to legal-clinic cold-start interview"
```

---

## Task 11: Update validators

**Files:**
- Modify: `scripts/validate-za-router.py`
- Modify: `scripts/validate-za-templates.py`

- [ ] **Step 1: Read current validator files**

Read both files to understand the exact data structures for PRACTICE_AREAS and TEMPLATE_CONFIG.

- [ ] **Step 2: Add legal-clinic to router validator**

In `scripts/validate-za-router.py`, add to the `PRACTICE_AREAS` list:

```python
{
    "name": "legal-clinic",
    "router": REPO_ROOT / "jurisdictions" / "za" / "legal-clinic" / "router.md",
    "skills_dir": REPO_ROOT / "legal-clinic" / "skills",
    "topics_dir": REPO_ROOT / "jurisdictions" / "za" / "legal-clinic" / "topics",
},
```

- [ ] **Step 3: Add legal-clinic to template validator**

In `scripts/validate-za-templates.py`, add to the `TEMPLATE_CONFIG` dict:

```python
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
```

- [ ] **Step 4: Run both validators**

Run: `python3 scripts/validate-za-router.py && python3 scripts/validate-za-templates.py`
Expected: Both PASS for legal-clinic.

- [ ] **Step 5: Commit**

```bash
git add scripts/validate-za-router.py scripts/validate-za-templates.py
git commit -m "feat(za): extend validators for legal-clinic overlay"
```

---

## Task 12: Create eval cases

**Files:**
- Create: 16 YAML files in `jurisdictions/za/evals/legal-clinic/` (subdirectories per skill)

- [ ] **Step 1: Create directory structure**

```bash
mkdir -p jurisdictions/za/evals/legal-clinic/{cold-start-interview,ramp,build-guide,client-intake,draft,memo,status,research-start,deadlines,supervisor-review-queue}
```

- [ ] **Step 2: Create eval cases**

Create all 16 eval case YAML files matching the schema from the employment-legal reference (`name`, `skill`, `input`, `expected_flags`, `expected_statutes`, `must_not_contain`, `notes`). Each case must follow the spec's Section 7 exactly.

The `must_not_contain` list for ALL cases must include: `["ABA", "FRCP", "at-will", "EEOC", "NLRB", "FMLA", "FLSA", "VAWA", "FDCPA", "USCIS", "INA", "Chapter 7", "Chapter 13", "Section 8", "HUD", "Title IV-D", "42 USC", "qualified immunity", "Westlaw", "CourtListener", "Cal. Rules", "state bar"]`

Each case adds practice-area-specific `must_not_contain` items as needed (see spec Section 7 for per-case details).

Write all 16 files per the spec's eval case outline — Cluster 1 (1.1–1.4), Cluster 2 (2.1–2.6), Cluster 3 (3.1–3.4), Cluster 4 (4.1–4.2).

- [ ] **Step 3: Validate YAML syntax**

```bash
python3 -c "import yaml,glob; [yaml.safe_load(open(f)) for f in glob.glob('jurisdictions/za/evals/legal-clinic/**/*.yaml', recursive=True)]; print(f'All {len(glob.glob(\"jurisdictions/za/evals/legal-clinic/**/*.yaml\", recursive=True))} eval cases valid')"
```

Expected: `All 16 eval cases valid`

- [ ] **Step 4: Commit**

```bash
git add jurisdictions/za/evals/legal-clinic/
git commit -m "feat(za): add 16 legal-clinic eval cases"
```

---

## Task 13: Final validation run

**Files:** None (validation only)

- [ ] **Step 1: Run all validators**

```bash
python3 scripts/validate-za-statutes.py
python3 scripts/validate-za-router.py
python3 scripts/validate-za-templates.py
```

Expected: All three PASS.

- [ ] **Step 2: Run JSON/YAML sanity check**

```bash
python3 -c "import json,glob; [json.load(open(f)) for f in glob.glob('**/*.json', recursive=True)]"
python3 -c "import yaml,glob; [yaml.safe_load(open(f)) for f in glob.glob('jurisdictions/za/**/*.yaml', recursive=True)]; print('All YAML valid')"
```

Expected: No errors.

- [ ] **Step 3: Run marketplace + plugin validation**

```bash
claude plugin validate legal-clinic
```

Expected: PASS (the ZA overlay files don't change plugin structure).

- [ ] **Step 4: Verify file count and structure**

```bash
echo "=== Statute files ==="
ls jurisdictions/za/statutes/*.yaml | wc -l
echo "=== Legal-clinic overlay ==="
find jurisdictions/za/legal-clinic/ -type f | sort
echo "=== Eval cases ==="
find jurisdictions/za/evals/legal-clinic/ -type f -name "*.yaml" | wc -l
```

Expected:
- Statute files: 41 (33 existing + 8 new)
- Legal-clinic overlay: router.md, practice-profile-template.md, 7 topic files = 9 files
- Eval cases: 16

- [ ] **Step 5: Final commit (if any fixes were needed)**

```bash
git add -A && git status
# Only commit if there are changes from validation fixes
```
