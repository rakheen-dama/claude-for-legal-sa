# ZA Litigation-Legal Overlay Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build the South African overlay for the litigation-legal plugin — 8 new statute YAMLs, fix prescription.yaml, 10 topic overlays, skill router, ZA practice profile template, cold-start interview fork, validation extensions, and 21 eval cases.

**Architecture:** Additive overlays in `jurisdictions/za/litigation-legal/` — same pattern as employment-legal (phase 1), commercial-legal (phase 2), and privacy-legal (phase 3). No upstream skill modifications except cold-start-interview. See ADR-001 (`project/decisions/001-sa-overlay-architecture.md`).

**Spec:** `docs/superpowers/specs/2026-05-19-za-litigation-legal-expansion.md` — read this before starting any task.

**Reference implementation:** `jurisdictions/za/employment-legal/` (phase 1).

---

## File Map

### New files

| File | Responsibility |
|---|---|
| `jurisdictions/za/statutes/superior-courts.yaml` | Superior Courts Act 10 of 2013 — appeal timelines, jurisdiction, execution suspension |
| `jurisdictions/za/statutes/magistrates-courts.yaml` | Magistrates' Courts Act 32 of 1944 — monetary jurisdiction limits, enforcement |
| `jurisdictions/za/statutes/arbitration.yaml` | Arbitration Act 42 of 1965 — stay, setting aside, enforcement |
| `jurisdictions/za/statutes/contingency-fees.yaml` | Contingency Fees Act 66 of 1997 — fee caps, formal requirements |
| `jurisdictions/za/statutes/state-liability.yaml` | Institution of Legal Proceedings Against Organs of State Act 40 of 2002 — notice requirements |
| `jurisdictions/za/statutes/civil-evidence.yaml` | Civil Proceedings Evidence Act 25 of 1965 — witness competence, documentary evidence |
| `jurisdictions/za/statutes/evidence-amendment.yaml` | Law of Evidence Amendment Act 45 of 1988 — hearsay admissibility |
| `jurisdictions/za/statutes/enforcement-foreign-judgments.yaml` | Enforcement of Foreign Civil Judgments Act 32 of 1988 — registration, reciprocity |
| `jurisdictions/za/litigation-legal/router.md` | Maps 17 in-scope skills to topic + statute files |
| `jurisdictions/za/litigation-legal/practice-profile-template.md` | ZA practice profile for SA litigation practitioners |
| `jurisdictions/za/litigation-legal/topics/court-structure-and-procedure.md` | Court hierarchy, jurisdiction, procedure phases, judgment types, costs, appeals |
| `jurisdictions/za/litigation-legal/topics/discovery-and-evidence.md` | Rule 35, Hartzenberg, no depositions, witness prep, electronic evidence |
| `jurisdictions/za/litigation-legal/topics/demands-and-settlement.md` | Letter of demand, mora, without-prejudice, prescription interruption |
| `jurisdictions/za/litigation-legal/topics/preservation-and-holds.md` | Common-law preservation, ECTA s16, POPIA retention, hold lifecycle |
| `jurisdictions/za/litigation-legal/topics/subpoenas.md` | Rule 38, registrar-issued, ad testificandum vs duces tecum, contempt |
| `jurisdictions/za/litigation-legal/topics/advocacy-and-citation.md` | Heads of argument, SA citation conventions, authority hierarchy |
| `jurisdictions/za/litigation-legal/topics/elements-and-claims.md` | Delict elements, contract elements, patent litigation, damages |
| `jurisdictions/za/litigation-legal/topics/legal-profession-and-fees.md` | Attorneys vs advocates, tariffs, contingency fees, costs recovery |
| `jurisdictions/za/litigation-legal/topics/risk-and-disclosure.md` | IAS 37, King IV, JSE, SENS triggers, IFRS contingent liabilities |
| `jurisdictions/za/litigation-legal/topics/privilege.md` | SA legal professional privilege, dominant purpose test, in-house capacity |
| `jurisdictions/za/evals/litigation-legal/demand-draft/case-01-standard-payment.yaml` | Eval: payment demand requiring mora |
| `jurisdictions/za/evals/litigation-legal/demand-received/case-02-without-prejudice-offer.yaml` | Eval: inbound WP demand with settlement offer |
| `jurisdictions/za/evals/litigation-legal/demand-draft/case-03-organ-of-state.yaml` | Eval: demand against provincial government |
| `jurisdictions/za/evals/litigation-legal/deposition-prep/case-01-witness-prep-trial.yaml` | Eval: witness preparation (no depositions) |
| `jurisdictions/za/evals/litigation-legal/subpoena-triage/case-02-third-party-docs.yaml` | Eval: third-party bank records |
| `jurisdictions/za/evals/litigation-legal/chronology/case-03-discovery-dispute.yaml` | Eval: fishing expedition objection |
| `jurisdictions/za/evals/litigation-legal/legal-hold/case-01-pre-litigation-popia.yaml` | Eval: pre-litigation hold with POPIA |
| `jurisdictions/za/evals/litigation-legal/legal-hold/case-02-hold-release.yaml` | Eval: hold release after settlement |
| `jurisdictions/za/evals/litigation-legal/legal-hold/case-03-missing-documents.yaml` | Eval: missing documents mid-trial |
| `jurisdictions/za/evals/litigation-legal/privilege-log-review/case-01-in-house-capacity.yaml` | Eval: in-house counsel capacity issue |
| `jurisdictions/za/evals/litigation-legal/privilege-log-review/case-02-privilege-schedule.yaml` | Eval: privilege schedule preparation |
| `jurisdictions/za/evals/litigation-legal/privilege-log-review/case-03-partial-waiver.yaml` | Eval: partial disclosure waiver |
| `jurisdictions/za/evals/litigation-legal/brief-section-drafter/case-01-delict-heads.yaml` | Eval: heads of argument for delictual claim |
| `jurisdictions/za/evals/litigation-legal/claim-chart/case-02-patent-infringement.yaml` | Eval: SA patent claim chart |
| `jurisdictions/za/evals/litigation-legal/brief-section-drafter/case-03-authority-hierarchy.yaml` | Eval: citation with conflicting High Court decisions |
| `jurisdictions/za/evals/litigation-legal/matter-intake/case-01-magistrates-claim.yaml` | Eval: R180k contract claim forum selection |
| `jurisdictions/za/evals/litigation-legal/matter-close/case-02-absolution.yaml` | Eval: absolution from the instance |
| `jurisdictions/za/evals/litigation-legal/portfolio-status/case-03-jse-listed.yaml` | Eval: JSE-listed quarterly portfolio review |
| `jurisdictions/za/evals/litigation-legal/oc-status/case-01-brief-senior-counsel.yaml` | Eval: briefing SC for trial |
| `jurisdictions/za/evals/litigation-legal/subpoena-triage/case-01-third-party-subpoena.yaml` | Eval: subpoena duces tecum on non-party |
| `jurisdictions/za/evals/litigation-legal/subpoena-triage/case-03-contempt-risk.yaml` | Eval: witness non-attendance contempt |

### Modified files

| File | Change |
|---|---|
| `jurisdictions/za/statutes/prescription.yaml` | Correct s11(a) error (6→30 years), add 6 new sections (s11(b), s11(c), s12(3), s14, s15) |
| `scripts/validate-za-router.py` | Add litigation-legal to `PRACTICE_AREAS` list |
| `scripts/validate-za-templates.py` | Add litigation-legal to `TEMPLATE_CONFIG` dict with required sections and SA terms |
| `litigation-legal/skills/cold-start-interview/SKILL.md` | Add ZA fork after Part 0 with 7 must-have questions |

---

## Task 1: Fix and extend `prescription.yaml`

**Files:**
- Modify: `jurisdictions/za/statutes/prescription.yaml`

- [ ] **Step 1: Read the existing file**

```bash
cat jurisdictions/za/statutes/prescription.yaml
```

Confirm the 4 existing sections and the s11(a) error (listed as 6 years, should be 30 years for judgment debts).

- [ ] **Step 2: Correct s11(a) and add new sections**

The existing `other_debt_prescription` entry incorrectly assigns s11(a) = 6 years. Fix: s11(a) = 30 years (judgment debts). The 6-year period belongs to s11(c) (bills of exchange).

Replace the entire file with:

```yaml
statute: "Prescription Act 68 of 1969"
authority: "Department of Justice and Constitutional Development"
last_confirmed: "2025-05-01"
source_url: "https://www.justice.gov.za/legislation/acts/1969-068.pdf"

sections:
  general_debt_prescription:
    ref: "Prescription Act s11(d)"
    value: 3
    unit: "years"
    effective_from: null
    effective_until: null
    effect: "Most ordinary contractual and delictual debts prescribe after 3 years. This is the default period for the majority of civil claims."

  judgment_debt_prescription:
    ref: "Prescription Act s11(a)"
    value: 30
    unit: "years"
    effective_from: null
    effective_until: null
    effect: "Judgment debts and debts secured by mortgage bond prescribe after 30 years. A judgment remains enforceable for 30 years from the date it was granted."

  tax_debt_prescription:
    ref: "Prescription Act s11(b)"
    value: 15
    unit: "years"
    effective_from: null
    effective_until: null
    effect: "Debts owed to the state in respect of taxes, levies, or similar impositions prescribe after 15 years."

  bill_of_exchange_prescription:
    ref: "Prescription Act s11(c)"
    value: 6
    unit: "years"
    effective_from: null
    effective_until: null
    effect: "Debts arising from bills of exchange or other negotiable instruments, and debts arising from notarial contracts, prescribe after 6 years."

  prescription_begins:
    ref: "Prescription Act s12(1)"
    value: "when the debt is due"
    effective_from: null
    effective_until: null
    effect: "Prescription begins to run as soon as the debt is due."

  knowledge_requirement:
    ref: "Prescription Act s12(3)"
    value: "knowledge of debtor identity and facts"
    effective_from: null
    effective_until: null
    effect: "A debt is not due until the creditor has knowledge of the identity of the debtor and of the facts from which the debt arises. A creditor is deemed to have such knowledge if they could have acquired it by exercising reasonable care."
    note: "The 'minimum facts' approach from Truter v Deysel and Stemmet v Mokhethi applies: prescription runs once the creditor knows enough facts to sustain a cause of action, even if they do not yet know the full extent of their loss."

  delay_of_prescription:
    ref: "Prescription Act s13(1)"
    value: true
    effective_from: null
    effective_until: null
    effect: "If the creditor is a minor, insane, or under curatorship, or if the debtor is outside the Republic and cannot be served, the completion of prescription is delayed until the impediment ceases, subject to maximum delay periods."

  interruption_by_acknowledgement:
    ref: "Prescription Act s14"
    value: "prescription runs afresh"
    effective_from: null
    effective_until: null
    effect: "If the debtor acknowledges liability (whether expressly or by conduct such as part payment), prescription is interrupted and begins to run afresh from the date of the acknowledgement."

  interruption_by_service:
    ref: "Prescription Act s15(1)"
    value: "prescription runs afresh"
    effective_from: null
    effective_until: null
    effect: "The service of any process whereby the creditor claims payment of the debt interrupts the running of prescription. Prescription runs afresh from the date on which the interruption ceases (typically when the litigation concludes). Issuing process alone is insufficient — service must occur."
    note: "Service must be effected without culpable delay after issue. If summons is issued close to the prescription date but not served, the claim may still prescribe."
```

- [ ] **Step 3: Run validation**

```bash
python3 scripts/validate-za-statutes.py
```

Expected: PASS — prescription.yaml validates with all 9 sections.

- [ ] **Step 4: Commit**

```bash
git add jurisdictions/za/statutes/prescription.yaml
git commit -m "fix(za): correct prescription.yaml s11(a) and add 6 litigation sections"
```

---

## Task 2: Create court structure statute files

**Files:**
- Create: `jurisdictions/za/statutes/superior-courts.yaml`
- Create: `jurisdictions/za/statutes/magistrates-courts.yaml`

- [ ] **Step 1: Create `superior-courts.yaml`**

```yaml
statute: "Superior Courts Act 10 of 2013"
authority: "Department of Justice and Constitutional Development"
last_confirmed: "2025-05-01"
source_url: "https://www.gov.za/documents/superior-courts-act"

sections:
  leave_to_appeal_time_limit:
    ref: "Superior Courts Act s17(1)"
    value: 15
    unit: "court days"
    effective_from: "2013-08-23"
    effective_until: null
    effect: "Application for leave to appeal must be made within 15 court days of the order or judgment appealed against. Court days exclude weekends, public holidays, and court recess periods."

  leave_to_appeal_test:
    ref: "Superior Courts Act s17(1)(a)"
    value: "reasonable prospect of success or compelling reason"
    effective_from: "2013-08-23"
    effective_until: null
    effect: "Leave to appeal may only be granted where the judge is of the opinion that the appeal would have a reasonable prospect of success, or there is some other compelling reason why the appeal should be heard (e.g. conflicting judgments, important question of law of general public importance)."

  execution_suspension_on_appeal:
    ref: "Superior Courts Act s18(1)"
    value: true
    effective_from: "2013-08-23"
    effective_until: null
    effect: "The operation and execution of a decision which is the subject of an application for leave to appeal or of an appeal is suspended pending the decision of the application or appeal, unless the court orders otherwise."

  execution_suspension_exception:
    ref: "Superior Courts Act s18(3)"
    value: "exceptional circumstances"
    effective_from: "2013-08-23"
    effective_until: null
    effect: "A court may only order that the operation or execution of a decision is not suspended if exceptional circumstances exist, and the applicant would suffer irreversible harm if the order is not made, and the other party would not suffer irreversible harm if the order is made."

  high_court_jurisdiction:
    ref: "Superior Courts Act s19"
    value: "inherent jurisdiction"
    effective_from: "2013-08-23"
    effective_until: null
    effect: "The High Court has inherent jurisdiction over all persons and matters within the area of its division, subject to the Constitution. It has original jurisdiction in all civil and criminal matters, except where jurisdiction is excluded by law."

  sca_jurisdiction:
    ref: "Superior Courts Act s21"
    value: "appeal jurisdiction"
    effective_from: "2013-08-23"
    effective_until: null
    effect: "The Supreme Court of Appeal has jurisdiction to hear and determine an appeal against any decision of a High Court. It is the highest court of appeal except in constitutional matters."
```

- [ ] **Step 2: Create `magistrates-courts.yaml`**

```yaml
statute: "Magistrates' Courts Act 32 of 1944"
authority: "Department of Justice and Constitutional Development"
last_confirmed: "2025-05-01"
source_url: "https://www.gov.za/documents/magistrates-courts-act-19-may-1944-0000"

sections:
  district_court_monetary_jurisdiction:
    ref: "Magistrates' Courts Act s29(1)(a)"
    value: 200000
    currency: "ZAR"
    unit: "per claim"
    effective_from: "2019-07-01"
    effective_until: null
    effect: "A district magistrates' court has civil jurisdiction where the claim value does not exceed R200,000."
    gazette_date: "2019-07-01"
    note: "Threshold is periodically amended by Government Gazette. Verify current limit before issuing."

  regional_court_monetary_jurisdiction:
    ref: "Magistrates' Courts Act s29(1)(b)"
    value: 400000
    currency: "ZAR"
    unit: "per claim"
    effective_from: "2019-07-01"
    effective_until: null
    effect: "A regional magistrates' court has civil jurisdiction where the claim value does not exceed R400,000."
    gazette_date: "2019-07-01"
    note: "Threshold is periodically amended by Government Gazette. Verify current limit before issuing."

  jurisdictional_basis:
    ref: "Magistrates' Courts Act s28"
    value: "residence, cause of action, or property"
    effective_from: null
    effective_until: null
    effect: "A magistrates' court has jurisdiction where the defendant resides or carries on business, where the cause of action arose, or where the property in dispute is situated."

  consent_to_jurisdiction:
    ref: "Magistrates' Courts Act s45"
    value: true
    effective_from: null
    effective_until: null
    effect: "Parties may consent to the jurisdiction of a magistrates' court that would not otherwise have jurisdiction, provided the court has jurisdiction over the subject matter."

  execution_against_residential_property:
    ref: "Magistrates' Courts Act s46A"
    value: "judicial oversight required"
    effective_from: null
    effective_until: null
    effect: "Execution against a judgment debtor's residential immovable property may only proceed with court authorisation, which requires considering the debtor's circumstances, the availability of alternative means of execution, and proportionality."

  judgment_debt_enforcement:
    ref: "Magistrates' Courts Act s65A-J"
    value: true
    effective_from: null
    effective_until: null
    effect: "Provides mechanisms for enforcement of judgment debts: financial enquiries (s65A), instalment orders (s65E), emoluments attachment orders (s65J), and garnishee orders. Debtor must attend financial enquiry in person."
```

- [ ] **Step 3: Run validation**

```bash
python3 scripts/validate-za-statutes.py
```

Expected: PASS for both new files.

- [ ] **Step 4: Commit**

```bash
git add jurisdictions/za/statutes/superior-courts.yaml jurisdictions/za/statutes/magistrates-courts.yaml
git commit -m "feat(za): add superior-courts and magistrates-courts statute files"
```

---

## Task 3: Create litigation mechanics statute files

**Files:**
- Create: `jurisdictions/za/statutes/arbitration.yaml`
- Create: `jurisdictions/za/statutes/contingency-fees.yaml`
- Create: `jurisdictions/za/statutes/state-liability.yaml`

- [ ] **Step 1: Create `arbitration.yaml`**

```yaml
statute: "Arbitration Act 42 of 1965"
authority: "Department of Justice and Constitutional Development"
last_confirmed: "2025-05-01"
source_url: "https://www.gov.za/documents/arbitration-act-20-may-1965-0000"

sections:
  arbitration_agreement:
    ref: "Arbitration Act s3"
    value: true
    effective_from: null
    effective_until: null
    effect: "Parties may agree to submit any existing or future dispute to arbitration. The arbitration agreement may be contained in the contract or in a separate document."

  stay_of_court_proceedings:
    ref: "Arbitration Act s6"
    value: true
    effective_from: null
    effective_until: null
    effect: "Where a party to an arbitration agreement commences court proceedings, the other party may apply for a stay of those proceedings. The court may stay the proceedings if satisfied there is no sufficient reason why the matter should not be referred to arbitration."
    note: "The application must be made before the applicant takes any further step in the court proceedings, or it may be treated as a waiver of the right to arbitrate."

  powers_of_arbitrator:
    ref: "Arbitration Act s14-15"
    value: true
    effective_from: null
    effective_until: null
    effect: "An arbitrator may administer oaths, make interim awards, and generally conduct proceedings as they see fit, subject to the arbitration agreement and the parties' right to a fair hearing."

  setting_aside_award:
    ref: "Arbitration Act s30"
    value: "limited grounds"
    effective_from: null
    effective_until: null
    effect: "An arbitration award may be set aside by the court on limited grounds: (a) the arbitrator committed misconduct in relation to duties, (b) the arbitrator committed a gross irregularity in the conduct of the proceedings, or (c) the award was improperly obtained."

  making_award_order_of_court:
    ref: "Arbitration Act s31"
    value: true
    effective_from: null
    effective_until: null
    effect: "An arbitration award may, on application to a court of competent jurisdiction, be made an order of court. Once made an order of court, the award is enforceable as if it were a court judgment."
```

- [ ] **Step 2: Create `contingency-fees.yaml`**

```yaml
statute: "Contingency Fees Act 66 of 1997"
authority: "Department of Justice and Constitutional Development"
last_confirmed: "2025-05-01"
source_url: "https://www.gov.za/documents/contingency-fees-act"

sections:
  fee_cap_percentage:
    ref: "Contingency Fees Act s2(2)"
    value: 25
    unit: "percent of amount awarded"
    effective_from: "1999-04-23"
    effective_until: null
    effect: "The total of any fees payable to the legal practitioner in the event of success may not exceed 25% of the total amount awarded or any amount obtained by the client in consequence of the proceedings, excluding costs."

  fee_cap_multiple:
    ref: "Contingency Fees Act s2(2)"
    value: 2
    unit: "times normal fee"
    effective_from: "1999-04-23"
    effective_until: null
    effect: "The total of any fees payable to the legal practitioner in the event of success may not exceed double the fee which that practitioner would normally be entitled to if the matter were not on a contingency basis. The lower of the two caps (25% or double) applies."

  formal_requirements:
    ref: "Contingency Fees Act s3"
    value: true
    effective_from: "1999-04-23"
    effective_until: null
    effect: "A contingency fee agreement must be in writing and signed by both the legal practitioner and the client. It must set out the practitioner's normal fees, the contingency fees payable on success, the reasons for believing a reasonable prospect of success exists, and the client's right to a cooling-off period."

  void_agreements:
    ref: "Contingency Fees Act s5"
    value: true
    effective_from: "1999-04-23"
    effective_until: null
    effect: "An agreement that does not comply with the requirements of s2 and s3 is void. A legal practitioner who entered into a void contingency fee agreement may recover only normal fees, or no fees at all depending on the circumstances."

  court_oversight_settlement:
    ref: "Contingency Fees Act s4"
    value: true
    effective_from: "1999-04-23"
    effective_until: null
    effect: "Where proceedings subject to a contingency fee agreement are settled, the court must be satisfied the settlement is fair and reasonable having regard to the contingency fee agreement. The court may call for information about the agreement and may review its terms."
```

- [ ] **Step 3: Create `state-liability.yaml`**

```yaml
statute: "Institution of Legal Proceedings Against Certain Organs of State Act 40 of 2002"
authority: "Department of Justice and Constitutional Development"
last_confirmed: "2025-05-01"
source_url: "https://www.gov.za/documents/institution-legal-proceedings-against-certain-organs-state-act"

sections:
  notice_period:
    ref: "Institution of Legal Proceedings Against Organs of State Act s3(2)(a)"
    value: 6
    unit: "months"
    effective_from: "2002-11-28"
    effective_until: null
    effect: "No legal proceedings for the recovery of a debt may be instituted against an organ of state unless the creditor has given the organ of state in question notice in writing of the intended legal proceedings within 6 months from the date on which the debt became due."

  notice_content:
    ref: "Institution of Legal Proceedings Against Organs of State Act s3(2)(b)"
    value: true
    effective_from: "2002-11-28"
    effective_until: null
    effect: "The notice must set out the facts giving rise to the debt, the amount of the debt, the person to whom the debt is owed, and must be served on the organ of state."

  condonation:
    ref: "Institution of Legal Proceedings Against Organs of State Act s3(4)"
    value: true
    effective_from: "2002-11-28"
    effective_until: null
    effect: "If the creditor fails to give the required notice within the 6-month period, the court may condone the non-compliance if it is satisfied that the organ of state was not unreasonably prejudiced by the failure, and that the debt has not prescribed."
    note: "Condonation is not automatic. The court exercises a discretion, and unreasonable delay or prejudice to the state may lead to refusal."
```

- [ ] **Step 4: Run validation**

```bash
python3 scripts/validate-za-statutes.py
```

Expected: PASS for all 3 new files.

- [ ] **Step 5: Commit**

```bash
git add jurisdictions/za/statutes/arbitration.yaml jurisdictions/za/statutes/contingency-fees.yaml jurisdictions/za/statutes/state-liability.yaml
git commit -m "feat(za): add arbitration, contingency-fees, and state-liability statute files"
```

---

## Task 4: Create evidence statute files

**Files:**
- Create: `jurisdictions/za/statutes/civil-evidence.yaml`
- Create: `jurisdictions/za/statutes/evidence-amendment.yaml`
- Create: `jurisdictions/za/statutes/enforcement-foreign-judgments.yaml`

- [ ] **Step 1: Create `civil-evidence.yaml`**

```yaml
statute: "Civil Proceedings Evidence Act 25 of 1965"
authority: "Department of Justice and Constitutional Development"
last_confirmed: "2025-05-01"
source_url: "https://www.gov.za/documents/civil-proceedings-evidence-act"

sections:
  competence_compellability:
    ref: "Civil Proceedings Evidence Act s10-11"
    value: true
    effective_from: null
    effective_until: null
    effect: "All persons are competent and compellable to give evidence in civil proceedings, subject to the rules on privilege. A spouse is competent and compellable to give evidence for or against the other spouse."

  without_prejudice_privilege:
    ref: "Civil Proceedings Evidence Act s21"
    value: true
    effective_from: null
    effective_until: null
    effect: "Communications made without prejudice for the purpose of settling a dispute are privileged and may not be tendered in evidence to prove admissions, unless both parties consent or the court determines the privilege does not apply."
    note: "This is a statutory confirmation of the common-law without-prejudice rule. The label 'without prejudice' creates a rebuttable presumption of settlement intent, but the court examines substance over form."

  documentary_evidence:
    ref: "Civil Proceedings Evidence Act s34-36"
    value: true
    effective_from: null
    effective_until: null
    effect: "Provides rules for the admissibility of documentary evidence, including business records, public documents, and certified copies. The maker of a document may be called to authenticate it if its admissibility is challenged."
```

- [ ] **Step 2: Create `evidence-amendment.yaml`**

```yaml
statute: "Law of Evidence Amendment Act 45 of 1988"
authority: "Department of Justice and Constitutional Development"
last_confirmed: "2025-05-01"
source_url: "https://www.gov.za/documents/law-evidence-amendment-act"

sections:
  hearsay_admissibility:
    ref: "Law of Evidence Amendment Act s3"
    value: "admissible in the interests of justice"
    effective_from: "1988-10-03"
    effective_until: null
    effect: "Hearsay evidence may be admitted in civil proceedings if the court is satisfied it is in the interests of justice. The court considers: the nature of the proceedings, the nature of the evidence, the purpose for which it is tendered, the probative value, the reason why the original declarant is not testifying, and any prejudice to the opposing party."
    note: "This is a departure from the common-law prohibition on hearsay. The court retains discretion and weighs the factors case by case."
```

- [ ] **Step 3: Create `enforcement-foreign-judgments.yaml`**

```yaml
statute: "Enforcement of Foreign Civil Judgments Act 32 of 1988"
authority: "Department of Justice and Constitutional Development"
last_confirmed: "2025-05-01"
source_url: "https://www.gov.za/documents/enforcement-foreign-civil-judgments-act"

sections:
  registration_requirement:
    ref: "Enforcement of Foreign Civil Judgments Act s2"
    value: true
    effective_from: "1988-07-08"
    effective_until: null
    effect: "A foreign civil judgment may be enforced in South Africa by registration in a designated court. Registration is only available for judgments from designated countries (reciprocity requirement). Undesignated countries require common-law enforcement proceedings."

  grounds_for_refusal:
    ref: "Enforcement of Foreign Civil Judgments Act s6"
    value: true
    effective_from: "1988-07-08"
    effective_until: null
    effect: "Registration may be refused if: the judgment was obtained by fraud, the judgment debtor did not receive notice and an opportunity to defend, the judgment is not final and conclusive, enforcement would be contrary to public policy, or the judgment conflicts with a prior SA judgment between the same parties."
    note: "For countries not designated under this Act, enforcement follows common-law principles (the foreign judgment creates a cause of action, not a directly enforceable order). The creditor must institute fresh proceedings and prove the foreign judgment."
```

- [ ] **Step 4: Run validation**

```bash
python3 scripts/validate-za-statutes.py
```

Expected: PASS for all 3 new files.

- [ ] **Step 5: Commit**

```bash
git add jurisdictions/za/statutes/civil-evidence.yaml jurisdictions/za/statutes/evidence-amendment.yaml jurisdictions/za/statutes/enforcement-foreign-judgments.yaml
git commit -m "feat(za): add civil-evidence, evidence-amendment, and enforcement-foreign-judgments statute files"
```

---

## Task 5: Create directory structure and router

**Files:**
- Create: `jurisdictions/za/litigation-legal/router.md`
- Create: `jurisdictions/za/litigation-legal/topics/` (directory)

- [ ] **Step 1: Create directory structure**

```bash
mkdir -p jurisdictions/za/litigation-legal/topics
```

- [ ] **Step 2: Create `router.md`**

Write `jurisdictions/za/litigation-legal/router.md`:

```markdown
# Skill Router — South African Litigation Law Overlay

When jurisdiction = ZA, skills load the topic overlays and statute files listed below.

Topic files resolve to: `jurisdictions/za/litigation-legal/topics/{name}.md`
Statute files resolve to: `jurisdictions/za/statutes/{name}.yaml`

```yaml
brief-section-drafter:
  topics: [advocacy-and-citation, privilege]
  statutes: [superior-courts, prescription]

chronology:
  topics: [court-structure-and-procedure, discovery-and-evidence]
  statutes: [prescription]

claim-chart:
  topics: [advocacy-and-citation, elements-and-claims]
  statutes: [prescription]

cold-start-interview:
  topics: [legal-profession-and-fees, risk-and-disclosure]
  statutes: [magistrates-courts, superior-courts, contingency-fees]

customize:
  topics: []
  statutes: []

demand-draft:
  topics: [demands-and-settlement, elements-and-claims]
  statutes: [prescription, state-liability]

demand-intake:
  topics: [demands-and-settlement]
  statutes: [prescription, state-liability]

demand-received:
  topics: [demands-and-settlement, elements-and-claims]
  statutes: [prescription, arbitration]

deposition-prep:
  topics: [discovery-and-evidence]
  statutes: [civil-evidence]

legal-hold:
  topics: [preservation-and-holds, privilege]
  statutes: [ecta, popia]

matter-briefing:
  topics: [court-structure-and-procedure, risk-and-disclosure]
  statutes: [prescription, superior-courts]

matter-close:
  topics: [court-structure-and-procedure, legal-profession-and-fees]
  statutes: [superior-courts, contingency-fees]

matter-intake:
  topics: [court-structure-and-procedure, legal-profession-and-fees, risk-and-disclosure]
  statutes: [prescription, magistrates-courts, arbitration, state-liability]

oc-status:
  topics: [legal-profession-and-fees]
  statutes: [contingency-fees]

portfolio-status:
  topics: [risk-and-disclosure]
  statutes: [prescription]

privilege-log-review:
  topics: [privilege, discovery-and-evidence]
  statutes: [civil-evidence]

subpoena-triage:
  topics: [subpoenas]
  statutes: [civil-evidence]
```
```

- [ ] **Step 3: Commit**

```bash
git add jurisdictions/za/litigation-legal/
git commit -m "feat(za): add litigation-legal directory structure and router"
```

Note: Router validation will fail until topic files are created in Tasks 6-15. That's expected — we build the skeleton first, then fill in content.

---

## Task 6: Topic overlay — court-structure-and-procedure.md

**Files:**
- Create: `jurisdictions/za/litigation-legal/topics/court-structure-and-procedure.md`

**Skills served:** matter-intake, matter-close, matter-briefing, chronology

- [ ] **Step 1: Write the topic overlay**

Write `jurisdictions/za/litigation-legal/topics/court-structure-and-procedure.md`:

```markdown
# Court Structure and Procedure — South African Framework

This overlay covers the SA court hierarchy, civil jurisdiction rules, procedure phases, judgment types, costs orders, and appeals. Loaded by matter-intake, matter-close, matter-briefing, and chronology when jurisdiction = ZA.

---

## 1. Court hierarchy

SA courts are structured hierarchically. Decisions of higher courts bind lower courts.

| Level | Court | Civil jurisdiction | Binding on |
|---|---|---|---|
| 1 (apex) | Constitutional Court (CC) | Constitutional matters; matters where it is in the interests of justice to grant leave (s167(3)) | All courts |
| 2 | Supreme Court of Appeal (SCA) | Highest court of appeal in non-constitutional matters (Superior Courts Act s21) | High Courts, lower courts |
| 3 | High Court | Inherent jurisdiction over all persons and matters in its division (Superior Courts Act s19). No monetary ceiling. | Magistrates' Courts in its area |
| 4 | Magistrates' Courts | Limited by monetary thresholds: district R200,000, regional R400,000 (Magistrates' Courts Act s29) | — |

**Specialist courts** (with exclusive jurisdiction over their subject matter):
- **Labour Court / Labour Appeal Court** — labour disputes (LRA s151)
- **Competition Tribunal / Competition Appeal Court** — competition matters (Competition Act s27)
- **Equality Court** — unfair discrimination (PEPUDA s16)
- **Land Claims Court** — land restitution (Restitution of Land Rights Act)
- **Tax Court** — tax disputes (Tax Administration Act s116)
- **Small Claims Court** — claims up to R20,000 (Small Claims Courts Act 61 of 1984)

---

## 2. Jurisdictional basis

### High Court (Uniform Rules)

The High Court has jurisdiction where:
- The defendant is domiciled or resident in the court's area
- The cause of action arose in the court's area
- The property in dispute is situated in the court's area
- The parties have consented to jurisdiction (including via a contractual clause)

**Divisions:** Gauteng (Johannesburg and Pretoria), Western Cape, KwaZulu-Natal, Eastern Cape (Makhanda and Bhisho), Free State, Limpopo, Mpumalanga, North West, Northern Cape.

### Magistrates' Court (Magistrates' Courts Act s28)

Jurisdiction where:
- The defendant resides, carries on business, or is employed in the court's district
- The cause of action arose in the district
- The property in dispute is situated in the district
- Consent to jurisdiction (s45)

**Monetary limits:** District court R200,000; regional court R400,000. Check current Gazette for updates.

### Forum selection considerations

- If claim exceeds Magistrates' Court limits → High Court
- If claim is within Magistrates' Court limits → consider costs implications (High Court costs are higher, but recovery on party-and-party may be limited if Magistrates' Court would have had jurisdiction)
- Check for exclusive statutory fora (Labour Court, Competition Tribunal) before issuing in any court
- Check for arbitration clauses before issuing in any court

---

## 3. Civil procedure phases

### Action proceedings (plaintiff/defendant)

| Phase | Key rules | Typical timeline |
|---|---|---|
| 1. Issue summons | Uniform Rule 17 (combined summons) | — |
| 2. Service | Rule 4 (personal, domicilium, substituted, edictal) | Within prescribed period after issue |
| 3. Notice of intention to defend | Rule 19 | 10 court days after service |
| 4. Plea (and counterclaim if any) | Rule 22 | 20 court days after notice to defend |
| 5. Replication (if counterclaim) | Rule 25 | 15 court days after plea |
| 6. Close of pleadings | Automatic when last pleading is filed | — |
| 7. Discovery | Rule 35 (list-based; see discovery-and-evidence.md) | After close of pleadings |
| 8. Pre-trial conference | Rule 37 / 37A (judicial case management in some divisions) | Court-directed |
| 9. Set down for trial | Rule 5 (notice of set-down) | After pre-trial complete |
| 10. Trial | Oral evidence, cross-examination | Court allocates dates |
| 11. Judgment | Court delivers (sometimes reserved) | Days to months after trial |

### Application (motion) proceedings (applicant/respondent)

| Phase | Key rules |
|---|---|
| 1. Notice of motion + founding affidavit | Rule 6 |
| 2. Service | Rule 4 |
| 3. Answering affidavit | Rule 6(5)(b) — typically 15 court days |
| 4. Replying affidavit | Rule 6(5)(c) — typically 10 court days |
| 5. Heads of argument | Practice directives (vary by division) |
| 6. Set down and hearing | — |
| 7. Judgment | — |

**Urgent applications:** Rule 6(12) — applicant must show urgency and that ordinary time periods would defeat the object of the application.

---

## 4. Judgment types

| Judgment type | Effect | Re-institution? |
|---|---|---|
| **Judgment on the merits** (for/against plaintiff) | Final determination. Creates res judicata. | No — final |
| **Absolution from the instance** | Plaintiff failed to make prima facie case at close of plaintiff's case. Dismissal without prejudice. | Yes — subject to prescription. May re-institute with better evidence. |
| **Default judgment** | Defendant failed to defend. Granted under Rule 12 (actions) or Rule 27 (Magistrates'). | Defendant may apply for rescission under Rule 42 / Rule 31(2)(b). |
| **Summary judgment** | Granted on liquidated claims or clear debts under Rule 32. | Defendant may apply for leave to defend. |
| **Consent judgment** | Parties agree to terms recorded as a court order (Rule 40). | No — binding as order of court. |
| **Interdict (interim or final)** | Prohibitory or mandatory order. SA equivalent of injunction. | Interim interdicts may be discharged on return day. |

---

## 5. Costs orders

**Default rule:** Costs follow the result — the unsuccessful party pays the successful party's costs.

| Scale | When awarded | What's recoverable |
|---|---|---|
| **Party-and-party** | Standard award to successful party | Costs reasonably necessary for conducting the litigation, assessed by taxing master using tariffs |
| **Attorney-and-client** | Punitive — misconduct, abuse of process, contractual entitlement, special circumstances | Wider range of attorney's charges; more favourable to the recovering party |
| **Attorney-and-own-client** | Rare — even more generous than attorney-and-client | All fees reasonably charged by the attorney |
| **Wasted costs** | Postponement, adjournment, late procedural steps | Costs thrown away by the specific event |
| **De bonis propriis** | Against the attorney personally for egregious conduct, misleading the court, unprofessional behaviour | Attorney personally liable — not the client |
| **Each party bears own costs** | Court discretion; amicable resolution; mixed success | No costs recovery |
| **Costs reserved** | Court defers costs decision to later stage | Decided at final hearing |

**Costs as risk factor:** On every new matter, assess adverse costs exposure. A party that loses bears its own costs PLUS the opponent's party-and-party costs. This fundamentally differs from the US default where each party typically bears its own costs.

---

## 6. Leave to appeal

**No automatic right of appeal** in most civil matters (Superior Courts Act s17).

### Test

Leave may only be granted where:
1. The appeal would have a **reasonable prospect of success**, OR
2. There is some other **compelling reason** why the appeal should be heard (e.g. conflicting judgments on the point, important question of law of general public importance)

### Process

1. Apply to the court that gave the judgment — within **15 court days**
2. If refused → petition the SCA (or full bench, depending on the court level)
3. If SCA refuses → may petition ConCourt if a constitutional issue arises

### Suspension of execution

- Default: noting an appeal suspends execution (s18(1))
- Exception: court may order immediate execution in **exceptional circumstances** (s18(3)) — requires showing irreversible harm to the applicant and no irreversible harm to the other party

---

## 7. Prescription check on intake

**Standing instruction:** Check prescription on every new matter at intake.

1. Identify the **exact cause of action** and the applicable period under Prescription Act s11:
   - 3 years — most contractual and delictual debts (s11(d))
   - 6 years — bills of exchange, notarial contracts (s11(c))
   - 15 years — tax debts (s11(b))
   - 30 years — judgment debts (s11(a))
2. Determine **when prescription began running** — s12(3): not until the creditor has knowledge of the debtor's identity and the facts giving rise to the debt (or could have acquired such knowledge with reasonable care)
3. Check for **interruption** — s15: service of process interrupts prescription (issuing summons is not enough — service must occur)
4. Check for **acknowledgement** — s14: any acknowledgement of liability (express or by conduct) restarts the clock
5. If close to the line: **issue and serve urgently**. Diarise conservative dates.
```

- [ ] **Step 2: Run router validation to check cross-reference**

```bash
python3 scripts/validate-za-router.py
```

Expected: Will still show errors for other missing topic files — that's fine. Verify that `court-structure-and-procedure` no longer appears as missing.

- [ ] **Step 3: Commit**

```bash
git add jurisdictions/za/litigation-legal/topics/court-structure-and-procedure.md
git commit -m "feat(za): add court-structure-and-procedure topic overlay"
```

---

## Task 7: Topic overlay — discovery-and-evidence.md

**Files:**
- Create: `jurisdictions/za/litigation-legal/topics/discovery-and-evidence.md`

**Skills served:** chronology, privilege-log-review, deposition-prep

- [ ] **Step 1: Write the topic overlay**

Write `jurisdictions/za/litigation-legal/topics/discovery-and-evidence.md`:

```markdown
# Discovery and Evidence — South African Framework

This overlay covers SA discovery (Rule 35), the Hartzenberg rule, the absence of depositions, witness preparation, and electronic evidence. Loaded by chronology, privilege-log-review, and deposition-prep when jurisdiction = ZA.

---

## 1. SA discovery model — Rule 35

SA discovery is **list-based**, not the broad request-for-production model of US FRCP 26-37. It is narrower in scope and less adversarial.

### How it works

1. After close of pleadings, either party may request discovery (Rule 35(1))
2. The responding party swears a **discovery affidavit** (Rule 35(2)) listing:
   - All documents in their possession relating to any matter in question
   - Documents previously in their possession (what happened to them)
   - Documents over which privilege is claimed (with sufficient description to support the claim)
3. The other party may inspect and copy discovered documents (Rule 35(6))

### Key differences from US FRCP

| US FRCP | SA Uniform Rules |
|---|---|
| Multiple discovery tools (interrogatories, RFP, depositions, RFA) | Primarily document discovery (Rule 35). Interrogatories require court leave. |
| Broad "relevant to any party's claim or defense and proportional" | "Relating to any matter in question" — tied to pleaded issues |
| Routine depositions (FRCP 30) | **No depositions.** Evidence is by affidavit (applications) or oral testimony at trial. |
| Iterative discovery phases | Typically one round of discovery after close of pleadings |
| Detailed ESI protocols (FRCP 26(f)) | No formal ESI protocol rules; handled through practice directives in some divisions |

### Hartzenberg rule

From *Swissborough Diamond Mines v Government of the Republic of South Africa* 1999 (2) SA 279 (T):

**Discovery is not a fishing expedition.** Parties must identify the issues in their pleadings and show relevance for requested documents. Overbroad, speculative discovery requests are not allowed. The court will refuse oppressive or irrelevant requests.

**Practical impact:** Every discovery request should be linked to a specific pleaded issue. The skill should flag requests that appear to go beyond the pleadings.

---

## 2. Specific discovery mechanisms

### Rule 35(3) — Further discovery / specific documents

A party may deliver a notice calling on the other party to make discovery on oath of specific documents or categories. If the recipient objects, the requesting party may apply to court for an order compelling discovery.

### Rule 35(12) — Documents referred to in pleadings

A party may require the other to produce documents referred to in their pleadings or affidavits.

### Rule 35(14) — Non-party document production

A party may apply to court for an order compelling a non-party to produce documents. This requires a court application — there is no equivalent of US FRCP 45 subpoena for pre-trial non-party document discovery as of right.

### Interrogatories (Rule 35(1)-(5))

Written questions to another party. Key points:
- **Leave of court is required** unless parties agree — interrogatories are not automatic
- Must relate to matters in question on the pleadings
- Answered on oath by the party (or corporate representative)
- Courts will limit or refuse oppressive interrogatories
- Rarely used in practice compared to document discovery

---

## 3. No depositions in SA

**SA does not have US-style depositions** (oral examination of parties/witnesses before trial under oath as of right).

Evidence is taken:
- **By affidavit** in application (motion) proceedings
- **Orally at trial** under examination-in-chief and cross-examination

Pre-trial oral examination is exceptional and limited to:
- Perpetuation of testimony (seriously ill witness)
- Cross-border evidence (letters of request / commissions rogatoire)
- Commissioners appointed by the court for specific purposes

### Witness preparation in SA

Witnesses are prepared **informally** by their attorneys:
- Attorney consults with the witness, takes a proof of evidence (internal statement)
- Reviews relevant documents with the witness
- Explains trial procedure (examination-in-chief, cross-examination, re-examination)
- No formal deposition or recorded pre-trial testimony

**When the deposition-prep skill runs in ZA context:** Reframe as trial preparation / witness preparation. The output should be a witness preparation outline, not a deposition outline. Key differences:
- No impeachment by prior deposition testimony (because there is no deposition)
- Focus on preparing for cross-examination by opposing counsel at trial
- Documents the witness should be familiar with before testifying
- Key facts and chronology the witness covers

---

## 4. Electronic evidence

### ECTA ss11-20

The Electronic Communications and Transactions Act 25 of 2002 gives legal recognition to electronic documents:
- Data messages are admissible as evidence (s15)
- Electronic signatures are recognised (s13)
- Retention in electronic form satisfies statutory retention requirements if accessible and in original format (s16)

### Admissibility

Electronic evidence (emails, messages, database records) is admissible under:
- ECTA s15 (data messages)
- Law of Evidence Amendment Act s3 (hearsay — if original declarant unavailable, electronic record may be admitted in interests of justice)
- Civil Proceedings Evidence Act (documentary evidence rules)

**Practical impact:** WhatsApp messages, emails, and electronic records are routinely admitted in SA courts. Authentication is the key issue — metadata (sender, timestamp, chain of custody) matters.

---

## 5. Pre-trial conference (Rule 37)

Mandatory in most divisions. The presiding officer or registrar convenes parties to:
- Narrow the issues in dispute
- Agree on facts and documents not in dispute
- Identify witnesses each party intends to call
- Set a trial timetable
- Explore settlement

**Rule 37A — Judicial case management:** In some divisions (notably Gauteng), judges manage cases more actively, setting directions for discovery, pre-trial, and trial dates.

**Chronology impact:** SA litigation has fewer discovery milestones than US litigation. A typical timeline:
1. Pleadings (summons → plea → replication)
2. Discovery (one round of Rule 35)
3. Pre-trial conference
4. Trial

Not: initial disclosures → written discovery → depositions → expert reports → summary judgment motions → pre-trial → trial (as in US FRCP).
```

- [ ] **Step 2: Commit**

```bash
git add jurisdictions/za/litigation-legal/topics/discovery-and-evidence.md
git commit -m "feat(za): add discovery-and-evidence topic overlay"
```

---

## Task 8: Topic overlay — demands-and-settlement.md

**Files:**
- Create: `jurisdictions/za/litigation-legal/topics/demands-and-settlement.md`

**Skills served:** demand-draft, demand-intake, demand-received

- [ ] **Step 1: Write the topic overlay**

Write `jurisdictions/za/litigation-legal/topics/demands-and-settlement.md`:

```markdown
# Demands and Settlement — South African Framework

This overlay covers SA letters of demand, mora, without-prejudice rules, and settlement communication. Loaded by demand-draft, demand-intake, and demand-received when jurisdiction = ZA.

---

## 1. Letter of demand (interpellatio)

In SA law, a letter of demand is not just a strategic tool — it can be a **legal prerequisite** to completing a cause of action.

### When a demand is required

- **Mora ex persona (default by demand):** Where the contract does not specify a fixed due date for performance, the debtor must be placed in mora by a demand (interpellatio). Without the demand, the cause of action may be incomplete and summons premature.
- **Mora ex re (automatic default):** Where the contract sets a fixed due date and time is of the essence, default occurs automatically on non-performance. No demand is required, but one is still good practice.

### Legal consequences of a demand

1. **Places debtor in mora** — completes the cause of action (if mora ex persona)
2. **Starts running of interest** as damages for late performance (mora interest)
3. **Evidence of notice** — demonstrates the creditor attempted amicable resolution
4. **Prescription awareness** — the demand date is relevant to prescription analysis (though the demand itself does not interrupt prescription — only service of process does under s15)

### Formal requirements

No rigid statutory form for most demands, but best practice:

| Element | Required content |
|---|---|
| Parties | Creditor and debtor clearly identified (names, addresses, contract reference) |
| Cause of action | Concise description of the legal basis, obligation, relevant dates and amounts |
| Demand | Clear demand for specific performance or payment, with a time period to comply (typically 7-14 days) |
| Consequences | That legal proceedings will or may be instituted without further notice |
| Costs | Demand for costs of the letter (recoverable on taxation in many cases) |
| Banking details | For payment demands |

### Special statutory requirements

- **Organs of state:** Institution of Legal Proceedings Against Organs of State Act — 6-month written notice with prescribed content before suing (s3)
- **National Credit Act:** Specific notice requirements before debt enforcement
- **Consumer Protection Act:** Notice requirements for certain consumer disputes

---

## 2. Without-prejudice communications

### SA common-law rule

Communications genuinely aimed at settlement are privileged from being tendered in evidence to prove admissions. This is a **common-law rule**, not a statutory rule like US FRE 408.

### Key principles

| Principle | SA position |
|---|---|
| Source | Common law (confirmed in Civil Proceedings Evidence Act s21) |
| Label | "Without prejudice" label creates a **rebuttable presumption** of settlement intent, but is not decisive — court examines purpose and context |
| Scope | Covers communications genuinely aimed at settlement — not communications that merely carry the label |
| Waiver | Can be waived by agreement; may be waived impliedly by conduct |
| Exceptions | Without-prejudice communications may be used to prove that a settlement was concluded, or on the issue of costs |

### Open vs without-prejudice

| Type | Effect | When to use |
|---|---|---|
| **Open letter** | Admissible in evidence. Admissions and positions stated can be used against the writer in court. | When you want the court to see the demand (e.g., to prove notice, mora, refusal to pay) |
| **Without prejudice** | Privileged from admission into evidence to prove admissions. | When making a settlement offer or inviting compromise — protects admissions made in the course of negotiation |
| **Without prejudice save as to costs** | Privileged on the merits, but may be disclosed on the issue of costs. | Calderbank-style offer: if the recipient rejects and achieves a worse result at trial, the court may penalise them on costs |

### Skill impact

- **demand-draft:** Toggle between open and without-prejudice marking. Default for pure payment demands: open (to prove mora and notice). Default for settlement offers: without prejudice.
- **demand-received:** Assess whether the incoming demand is open or WP. If WP, note that admissions cannot be used in evidence.
- **demand-intake:** Capture the intended marking and explain the consequences.

---

## 3. Prescription and demands

A letter of demand **does not interrupt prescription**. Only service of process interrupts prescription (Prescription Act s15).

However, demands are relevant to prescription analysis because:
- The demand date may establish when the creditor first knew about the claim (s12(3) knowledge)
- An acknowledgement of liability in response to a demand interrupts prescription (s14)
- The demand establishes the date the debtor was placed in mora, which may be relevant to when the cause of action was complete

**Critical point:** Do not rely on a demand letter to "stop the clock" on prescription. Only service of summons (or equivalent process) interrupts prescription.
```

- [ ] **Step 2: Commit**

```bash
git add jurisdictions/za/litigation-legal/topics/demands-and-settlement.md
git commit -m "feat(za): add demands-and-settlement topic overlay"
```

---

## Task 9: Topic overlay — preservation-and-holds.md

**Files:**
- Create: `jurisdictions/za/litigation-legal/topics/preservation-and-holds.md`

- [ ] **Step 1: Write the topic overlay**

Write `jurisdictions/za/litigation-legal/topics/preservation-and-holds.md`:

```markdown
# Preservation and Legal Holds — South African Framework

This overlay covers SA preservation obligations, the absence of Zubulake/FRCP 37(e), ECTA/POPIA intersection, and the adapted hold lifecycle. Loaded by legal-hold when jurisdiction = ZA.

---

## 1. Preservation obligations in SA

### Common-law duty

SA does not have a codified preservation framework like US FRCP 37(e) or the Zubulake line. Preservation obligations arise from:

1. **Common-law duty of good faith** — once litigation is pending or reasonably contemplated, parties must not destroy relevant documents
2. **Discovery obligations** — Rule 35 requires disclosure of documents in possession or that were in possession; deliberate destruction to avoid discovery is sanctionable
3. **Spoliation doctrine** — protects possession and discourages self-help destruction of evidence

### Consequences of destruction

| Consequence | When applied |
|---|---|
| **Adverse inference** | Court may infer that destroyed documents were unfavourable to the destroying party |
| **Costs sanctions** | Wasted costs, punitive costs orders for discovery abuse |
| **Striking out of pleadings** | In extreme cases, as a sanction for deliberate destruction |
| **Professional misconduct** | Attorney involvement in destruction may lead to disciplinary proceedings |

### Trigger for preservation

Preservation obligation arises when litigation is **reasonably contemplated** — not just when summons is served. Indicators:
- Receipt of a letter of demand
- Awareness of facts giving rise to a potential claim
- Regulatory investigation or enquiry
- Internal complaint or report suggesting potential dispute

---

## 2. ECTA s16 — Electronic retention

ECTA s16 provides that statutory retention requirements may be met by electronic retention if:
- Documents are **accessible** for subsequent reference
- Documents are retained in the **format in which they were generated, sent, or received** (or an accurate representation)
- Information enabling identification of **origin, destination, date, and time** is retained

**Hold implication:** Electronic archives (email, cloud storage, databases) qualify as compliant retention. The hold must ensure these are not overwritten or purged during the hold period.

---

## 3. POPIA — Storage limitation and litigation exception

### Storage limitation (POPIA s14)

Personal information must not be retained longer than necessary for the purpose for which it was collected, UNLESS:
- Retention is required or authorised by law
- The responsible party reasonably requires it for a **lawful purpose related to its functions** (including legal proceedings)
- Retention is required by a contract
- The data subject has consented

### Litigation exception

Active or reasonably contemplated litigation is a **lawful purpose** justifying extended retention of personal information. The hold notice should:
- Document the litigation or potential litigation justifying retention
- Scope the personal information held to what is relevant to the dispute
- Be reviewed and released when the litigation purpose ends

### Post-matter POPIA obligations

When a legal hold is released after matter close:
1. Review held personal information
2. If no other lawful basis for retention → delete or de-identify
3. Document the release and any deletion in the hold log
4. POPIA s14(4): records may be retained in a form that does not identify data subjects (de-identified retention)

---

## 4. Legal hold lifecycle for SA

### Issue

1. Identify the triggering event (demand received, dispute foreseeable, regulatory enquiry)
2. Identify **custodians** — persons likely to have relevant documents (email, files, physical records, WhatsApp/messaging)
3. Draft hold notice:
   - Plain language description of the dispute or potential dispute
   - Obligation to preserve all potentially relevant documents and communications
   - Specific data sources to preserve (email, messaging apps, cloud storage, physical files, financial records)
   - Prohibition on deleting, altering, or disposing of relevant materials
   - Suspension of routine destruction/archival policies for the specified data
   - Contact person for questions
4. Issue to all identified custodians
5. Log: date issued, custodians notified, data sources in scope

### Refresh

Refresh holds at regular intervals (every 6-12 months or when material developments occur):
- Remind custodians of their ongoing obligations
- Update the scope if the dispute has evolved
- Add new custodians if additional relevant persons are identified
- Record refresh date in the hold log

### Release

1. Confirm matter is concluded (settled, judgment entered, appeal period expired)
2. Review POPIA obligations — does held personal information need to be deleted?
3. Notify custodians that the hold is lifted
4. Document release in the hold log (date, reason, any data deleted)

---

## 5. What NOT to replicate from US practice

| US concept | SA status |
|---|---|
| Zubulake factors | Do not apply. No structured proportionality test for preservation. |
| FRCP 37(e) safe harbor | Does not exist. There is no statutory safe harbor for good-faith loss of ESI. |
| FRCP 37(e)(1) vs 37(e)(2) | No distinction between sanctions requiring/not requiring intent to deprive. |
| Sedona Conference principles | Not adopted in SA courts. Use SA common-law preservation principles. |
| Proportionality factors for ESI | No formal ESI rules. Court applies general discovery principles. |
```

- [ ] **Step 2: Commit**

```bash
git add jurisdictions/za/litigation-legal/topics/preservation-and-holds.md
git commit -m "feat(za): add preservation-and-holds topic overlay"
```

---

## Task 10: Topic overlay — subpoenas.md

**Files:**
- Create: `jurisdictions/za/litigation-legal/topics/subpoenas.md`

- [ ] **Step 1: Write the topic overlay**

Write `jurisdictions/za/litigation-legal/topics/subpoenas.md`:

```markdown
# Subpoenas — South African Framework

This overlay covers SA subpoena mechanics, the registrar-issued model, and differences from US FRCP 45. Loaded by subpoena-triage when jurisdiction = ZA.

---

## 1. SA subpoena mechanics

### Types

| Type | Purpose | Rule |
|---|---|---|
| **Subpoena ad testificandum** | Compel witness attendance to testify at trial or hearing | Uniform Rule 38; Magistrates' Courts Rule 33 |
| **Subpoena duces tecum** | Compel production of documents at trial or hearing | Uniform Rule 38; Magistrates' Courts Rule 33 |

### Issue and service

- Subpoenas are **issued by the registrar or clerk of the court**, not by attorneys unilaterally
- Served by the sheriff (or authorised person)
- Must specify: the court, the case, the date and time of attendance, and (for duces tecum) the documents to be produced

### Scope

SA subpoenas are primarily for **attendance at trial or hearing** — not for free-standing pre-trial document discovery from non-parties.

For pre-trial non-party document production:
- Apply to court under **Rule 35(14)** for an order compelling a non-party to produce documents
- This requires a court application — no self-executing pre-trial subpoena right against non-parties

---

## 2. Objecting to a subpoena

A witness or non-party may apply to court to:
- **Set aside** a subpoena that is oppressive, irrelevant, or improper
- **Limit** the scope of a subpoena duces tecum to relevant documents only
- **Assert privilege** over specific documents (legal professional privilege, without-prejudice privilege)

There is no formal "motion to quash" procedure like US FRCP 45(d). The application is made on notice to the party who obtained the subpoena.

---

## 3. Non-compliance

Failure to obey a lawful subpoena is **contempt of court**:
- May result in a fine or imprisonment
- The court may issue a warrant for the arrest of a defaulting witness
- Before seeking contempt, the issuing party should confirm proper service and that the witness had no reasonable excuse for non-attendance

---

## 4. What NOT to replicate from US practice

| US concept | SA status |
|---|---|
| FRCP 45 subpoena (broad pre-trial, attorney-issued) | Does not exist. Subpoenas are registrar-issued, primarily for trial. |
| Place of compliance limits (100-mile rule) | No equivalent. Witness must attend the court specified. |
| Cost-shifting for non-party compliance | No formal cost-shifting framework. Court may order costs on an application. |
| Civil Investigative Demand (CID) | No equivalent. Regulatory investigation subpoenas are governed by sector-specific legislation. |
| Grand jury subpoenas | No equivalent. SA does not have grand juries. |
| Deposition subpoenas | No depositions in SA. |
```

- [ ] **Step 2: Commit**

```bash
git add jurisdictions/za/litigation-legal/topics/subpoenas.md
git commit -m "feat(za): add subpoenas topic overlay"
```

---

## Task 11: Topic overlay — advocacy-and-citation.md

**Files:**
- Create: `jurisdictions/za/litigation-legal/topics/advocacy-and-citation.md`

- [ ] **Step 1: Write the topic overlay**

Write `jurisdictions/za/litigation-legal/topics/advocacy-and-citation.md`:

```markdown
# Advocacy and Citation — South African Framework

This overlay covers heads of argument, SA citation conventions, and the authority hierarchy. Loaded by brief-section-drafter and claim-chart when jurisdiction = ZA.

---

## 1. Heads of argument (not briefs)

SA written advocacy takes the form of **heads of argument** — concise, issues-driven written submissions. They are NOT US-style briefs.

### Structure

| Section | Content |
|---|---|
| **Issues** | The specific questions the court must decide, framed crisply |
| **Summary of facts** | Relevant facts with record references (page, paragraph, line) |
| **Legal arguments** | Organised under headings, one per issue, with pinpoint citations |
| **Relief sought** | Specific order requested |
| **Costs** | Costs order sought and scale |

### Conventions

- **Succinct, not exhaustive.** Heads should be points, not a treatise. Judges read them in advance and form preliminary views.
- **Issues-driven.** Lead with the question, not the answer.
- **Record references.** Every factual assertion must cite the record (affidavit paragraph, trial transcript page and line).
- **Authority references.** Every legal proposition must cite authority (case law or statute).
- **Page limits.** Practice directives in many divisions impose page or word limits. Check the specific division's directives.

### Judge-alone system

SA has **no civil jury trials**. All civil matters are decided by a judge (or magistrate). There are no pattern jury instructions, verdict forms, or jury-friendliness considerations. Advocacy is directed at a legally trained decision-maker.

---

## 2. SA citation conventions

### Case law

**SA Law Reports format (primary):**

> *Party A v Party B* YEAR (volume) SA page (court abbreviation)

Example: *S v Makwanyane* 1995 (3) SA 391 (CC)

**Neutral citation format (recent cases):**

> [YEAR] COURT-ID case-number

Example: [2015] ZACC 12

**Court abbreviations:**

| Abbreviation | Court |
|---|---|
| CC | Constitutional Court |
| SCA | Supreme Court of Appeal |
| GJ | Gauteng Division, Johannesburg |
| GP | Gauteng Division, Pretoria |
| WCC | Western Cape Division |
| KZD / KZP | KwaZulu-Natal Division (Durban / Pietermaritzburg) |
| ECG / ECM | Eastern Cape Division (Makhanda / Bhisho) |
| FB | Free State Division |
| MN | Mpumalanga Division |
| NWM | North West Division |
| NC | Northern Cape Division |
| LCC | Land Claims Court |
| LC | Labour Court |
| LAC | Labour Appeal Court |

### Statutes

> Full statute name NUMBER of YEAR

Example: Prescription Act 68 of 1969

Section references: Act name sNUMBER(subsection)
Example: Prescription Act s11(d), LRA s188(1)(a)(i)

### Report series priority

1. **SA** — South African Law Reports (most commonly cited)
2. **BCLR** — Butterworths Constitutional Law Reports
3. **SACR** — South African Criminal Reports
4. **ILJ** — Industrial Law Journal (labour matters)

When parallel citations exist, cite SA as primary.

---

## 3. Authority hierarchy

Decisions of higher courts **bind** lower courts. This is strict — not merely persuasive.

| Level | Binding effect |
|---|---|
| Constitutional Court | Binds all courts on all matters (since 17th Amendment) |
| SCA | Binds all High Courts and lower courts on non-constitutional matters |
| High Court (full bench) | Binds single judges of the same division |
| High Court (single judge) | Persuasive to other single judges; binds Magistrates' Courts in the division |
| High Court (other division) | Persuasive only — a Gauteng decision does not bind Western Cape |

### When authorities conflict

- Conflicting High Court decisions from **different divisions**: neither binds the other. Choose the more persuasive. Flag the conflict.
- Conflicting High Court decisions from the **same division**: later full bench decision prevails over earlier single judge decision.
- If SCA has not ruled: acknowledge the uncertainty and present the competing positions.

### Foreign authority

Foreign case law (English, Australian, US, etc.) is **persuasive only**. It may be cited to support a proposition, but SA courts are not bound by it. When citing foreign authority, note: "cf." or "See also" (not "following" or "applying").

---

## 4. What NOT to replicate from US practice

| US concept | SA status |
|---|---|
| Bluebook citation format | Not used. SA follows SA Law Reports / neutral citation format. |
| Circuit splits | No circuits. Conflicting High Court division decisions are the SA equivalent. |
| En banc rehearing | SA equivalent: referral to full bench or SCA. |
| SCOTUS cert petition | SA equivalent: application for leave to appeal to ConCourt (under s167(3)). |
| Pattern jury instructions (CACI, NYPJI) | No civil juries. No pattern instructions. |
| Amicus curiae briefs | SA courts accept amicus briefs, but the procedure differs (court must grant leave). |
```

- [ ] **Step 2: Commit**

```bash
git add jurisdictions/za/litigation-legal/topics/advocacy-and-citation.md
git commit -m "feat(za): add advocacy-and-citation topic overlay"
```

---

## Task 12: Topic overlay — elements-and-claims.md

**Files:**
- Create: `jurisdictions/za/litigation-legal/topics/elements-and-claims.md`

- [ ] **Step 1: Write the topic overlay**

Write `jurisdictions/za/litigation-legal/topics/elements-and-claims.md`:

```markdown
# Elements and Claims — South African Framework

This overlay covers SA delict elements, contract elements, patent litigation, and damages. Loaded by claim-chart, demand-draft, and demand-received when jurisdiction = ZA.

---

## 1. Elements of delict (SA negligence)

SA delict has **5 elements**, not the US 4-element negligence test.

| # | Element | Test | US rough equivalent |
|---|---|---|---|
| 1 | **Conduct** | Positive act or omission where there is a legal duty to act | (Part of duty/breach) |
| 2 | **Wrongfulness** | Objective unreasonableness — breach of a legal duty or infringement of a legally protected right. Constitutional values (dignity, equality, freedom) inform the test. | Duty of care (but broader and more policy-laden) |
| 3 | **Fault** | Intention (dolus) or negligence (culpa). Negligence: would a reasonable person in the defendant's position have foreseen harm and taken steps to prevent it? | Breach of duty |
| 4 | **Causation** | Factual: but-for test (conditio sine qua non). Legal: reasonable foreseeability / directness / policy (flexible test per *S v Mokgethi*) | Cause-in-fact + proximate cause |
| 5 | **Harm** | Patrimonial loss (financial), non-patrimonial loss (pain and suffering, loss of amenities), or personality infringement | Damages |

### Key differences from US tort

- **Wrongfulness is a separate element.** In US negligence, "wrongfulness" is collapsed into duty and breach. In SA, wrongfulness is an independent, constitutional-values-driven policy inquiry.
- **No strict liability in general delict.** Strict liability exists in specific statutory contexts but is not a general feature of SA delict law (unlike US strict product liability).
- **No punitive damages** in ordinary private-law delict. SA damages are compensatory only. Punitive damages are not available (with very narrow exceptions in defamation).

---

## 2. Elements of contractual claim

| # | Element |
|---|---|
| 1 | **Existence of a valid contract** (consensus, capacity, legality, formalities if applicable, possibility of performance) |
| 2 | **Terms of the contract** (express terms, tacit terms, implied terms by law) |
| 3 | **Breach** (mora debitoris, mora creditoris, positive malperformance, repudiation, prevention of performance) |
| 4 | **Damages or specific performance** (creditor's election: claim damages or enforce the contract) |

### Types of breach

| Type | Description |
|---|---|
| **Mora debitoris** | Debtor's failure to perform timeously (late performance) |
| **Mora creditoris** | Creditor's failure to cooperate / accept performance |
| **Positive malperformance** | Performance rendered but defective |
| **Repudiation** | Party indicates intention not to perform (anticipatory breach) |
| **Prevention of performance** | Party makes performance impossible |

---

## 3. Patent litigation (Patents Act 57 of 1978)

### Forum

Patent infringement and invalidity proceedings are heard by the **Commissioner of Patents** — a High Court judge sitting in that capacity. Appeals go to a full bench, then SCA, then ConCourt on constitutional issues.

### No Markman hearing

There is no separate claim construction hearing. Claim interpretation is done by the trial judge as part of the judgment, applying the principles in *Gentiruco AG v Firestone SA (Pty) Ltd* 1972 (1) SA 589 (A) and subsequent case law.

### Claim construction principles

- Claims are interpreted **purposively** — the specification is read as a whole
- The notional skilled addressee (person skilled in the art) is the interpretive lens
- Reference to the specification (description) to construe claims
- Pith and marrow doctrine (functional equivalents) may extend claim scope

### Remedies

| Remedy | Available? |
|---|---|
| Interdict (injunction) | Yes |
| Damages (actual loss) | Yes |
| Reasonable royalty | Yes |
| Account of profits | Yes (in some circumstances) |
| Enhanced / treble damages | **No** |
| Attorneys' fees | Only via costs order (party-and-party or attorney-and-client scale) |

### No civil jury

All patent cases are judge-alone. No jury verdict forms, no pattern instructions, no jury-friendliness considerations.

---

## 4. Damages in SA litigation

### General principles

- SA damages are **compensatory**, not punitive
- The purpose is to place the injured party in the position they would have been in had the wrong not occurred
- Plaintiff must prove damages on a balance of probabilities

### Types of damages

| Type | Description |
|---|---|
| **Special damages** | Quantifiable financial loss (medical expenses, loss of earnings, repair costs). Must be specifically pleaded and proved. |
| **General damages** | Non-patrimonial loss (pain and suffering, loss of amenities of life, disfigurement). Assessed by the court. |
| **Consequential damages** | Financial loss flowing from the wrong (loss of profits, future loss of earnings). Must be proved with reasonable certainty. |

### What's NOT available

- **Punitive / exemplary damages** — not available in ordinary SA private law
- **Treble damages** — no statutory treble damages mechanism
- **Class action damages** — developing area; no established opt-out class damages framework
- **Attorneys' fees as damages** — not available; costs recovery is via costs orders on taxation

---

## 5. Terminology mapping

| US term | SA equivalent |
|---|---|
| Injunction | **Interdict** (interim or final) |
| Tort | **Delict** |
| Tortfeasor | **Wrongdoer** or **delictual actor** |
| Directed verdict / JMOL | **Absolution from the instance** |
| Summary judgment | **Summary judgment** (Rule 32 — similar concept but narrower scope) |
| Complaint | **Summons** (combined summons in actions) or **Notice of motion** (applications) |
| Answer | **Plea** (actions) or **Answering affidavit** (applications) |
```

- [ ] **Step 2: Commit**

```bash
git add jurisdictions/za/litigation-legal/topics/elements-and-claims.md
git commit -m "feat(za): add elements-and-claims topic overlay"
```

---

## Task 13: Topic overlay — legal-profession-and-fees.md

**Files:**
- Create: `jurisdictions/za/litigation-legal/topics/legal-profession-and-fees.md`

- [ ] **Step 1: Write the topic overlay**

Write `jurisdictions/za/litigation-legal/topics/legal-profession-and-fees.md`:

```markdown
# Legal Profession and Fees — South African Framework

This overlay covers the two-tier profession, tariffs, contingency fees, and costs recovery. Loaded by oc-status, matter-intake, matter-close, and cold-start-interview when jurisdiction = ZA.

---

## 1. Two-tier profession

### Attorneys

- Directly instructed by clients
- Manage litigation end-to-end: client communication, discovery, evidence gathering, court filings, settlement negotiations
- May appear in Magistrates' Courts and (with right of appearance) in High Court
- Regulated by the Legal Practice Council under the Legal Practice Act 28 of 2014
- Organised in law firms (sole, partnership, incorporated)

### Advocates (counsel)

- Briefed by attorneys (not directly by clients, with limited exceptions for trust account advocates)
- Specialise in: drafting complex pleadings, heads of argument, and opinions; appearing in High Court, SCA, and ConCourt
- Organised in independent Bars (e.g. Johannesburg Bar, Cape Bar, KZN Bar)
- **Senior Counsel (SC)** — appointed by the President on recommendation of the relevant Bar and Chief Justice. Indicates seniority and expertise.
- **Junior counsel** — advocates who are not SC. Often briefed alongside SC (the "junior/senior" team).

### Instructing vs briefing

| Term | Meaning |
|---|---|
| **Instruct** | Client instructs an attorney (or attorney instructs on the client's behalf) |
| **Brief** | Attorney briefs an advocate — delivers the brief (file of documents + fee arrangement + instructions) |
| **Brief fee** | The fee payable to the advocate for the specific instruction (separate from attorney's fees) |

### Outside counsel management impact

The OC bench has a **two-tier structure**:
- **Instructing firm** (attorneys) — manages the matter, coordinates with client
- **Briefed counsel** (advocates) — handles courtroom advocacy, drafts heads of argument

Budget and cost tracking should separate attorney fees from counsel fees. Status requests go to the instructing firm, not directly to counsel (unless specifically arranged).

---

## 2. Fee structures

### Attorney fees

| Type | Description |
|---|---|
| **Hourly rate** | Most common for commercial litigation |
| **Fixed fee** | For defined scope work (opinions, simple applications) |
| **Tariff rate** | Legal Practice Act / Rules Board tariffs — baseline for taxation of costs |
| **Contingency fee** | Permitted under Contingency Fees Act (see below) |

### Advocate fees

| Type | Description |
|---|---|
| **Brief fee** | Fee for the specific instruction (e.g., "draft heads of argument" or "appear at trial for 3 days") |
| **Daily rate** | For trial appearances (per day of trial) |
| **Refresher fee** | Additional daily fee for trial days beyond the first |
| **Consultation fee** | For pre-trial consultations with attorneys and witnesses |
| **Marking fee** | For reviewing and marking a brief (initial review of the file) |

### Contingency Fees Act 66 of 1997

| Rule | Detail |
|---|---|
| Cap (percentage) | Max **25% of amount awarded** to client (excluding costs) |
| Cap (multiple) | Max **double the normal fee** the practitioner would have charged |
| Which applies? | The **lower** of the two caps |
| Formal requirements | Must be in writing, signed by both parties, with prescribed disclosures and cooling-off notice |
| Void if non-compliant | Non-compliant agreement is void; practitioner may recover normal fees or nothing |
| Court oversight | Settlement subject to court scrutiny for fairness (s4) |
| Typical use | Personal injury, medical negligence, consumer claims. Rare in corporate litigation. |

---

## 3. Costs recovery

### Taxation

After a costs order, the successful party's bill of costs is **taxed** (assessed) by the taxing master:
- Disallows items not reasonably necessary for the litigation
- Applies tariff rates for party-and-party taxation
- Attorney-and-client taxation allows a wider range of charges

### Costs as a strategic factor

- **Loser pays** is the default — this fundamentally changes litigation risk
- Before commencing or defending, quantify adverse costs exposure
- Disproportionate claims (e.g., High Court for a small claim) may result in a reduced costs order
- Offer to settle (Uniform Rule 34 / "without prejudice save as to costs") affects costs — if the opponent achieves a worse result at trial than the offer, they may bear costs from the date of the offer
```

- [ ] **Step 2: Commit**

```bash
git add jurisdictions/za/litigation-legal/topics/legal-profession-and-fees.md
git commit -m "feat(za): add legal-profession-and-fees topic overlay"
```

---

## Task 14: Topic overlay — risk-and-disclosure.md

**Files:**
- Create: `jurisdictions/za/litigation-legal/topics/risk-and-disclosure.md`

- [ ] **Step 1: Write the topic overlay**

Write `jurisdictions/za/litigation-legal/topics/risk-and-disclosure.md`:

```markdown
# Risk and Disclosure — South African Framework

This overlay covers IAS 37, King IV, JSE requirements, and SENS triggers. Loaded by portfolio-status, matter-intake, cold-start-interview, and matter-briefing when jurisdiction = ZA.

---

## 1. IAS 37 — Provisions, contingent liabilities, contingent assets

SA-listed and most large SA companies apply **IFRS**, not US GAAP. IAS 37 governs litigation-related accounting, replacing US ASC 450.

### Recognition

| Classification | Test | Accounting treatment |
|---|---|---|
| **Provision** | Present obligation (legal or constructive) + probable outflow (>50%) + reliable estimate | Recognise in financial statements (balance sheet liability) |
| **Contingent liability** | Possible obligation OR present obligation where outflow is not probable or not reliably measurable | **Disclose** in notes (unless outflow is remote) |
| **Remote** | Outflow is remote | No recognition, no disclosure required |

### Key differences from ASC 450

| ASC 450 (US GAAP) | IAS 37 (IFRS / SA) |
|---|---|
| "Probable" often interpreted as ~70%+ | "Probable" = more likely than not (>50%) |
| "Reasonably possible" triggers disclosure | "Possible" (not remote) triggers disclosure |
| Range: accrue low end if no better estimate | Best estimate; expected value for large populations |
| No discounting (generally) | Discount if time value of money is material |

### Practical impact for portfolio-status

- Each active matter should be classified as: provision (accrue), contingent liability (disclose), or remote (neither)
- Classification drives the IFRS notes in the annual financial statements
- Review classification quarterly (or when material developments occur)

---

## 2. King IV — Corporate governance

SA corporate governance is guided by the **King IV Report on Corporate Governance** (2016) — a principle-based, apply-and-explain code. It is not a statute, but JSE Listings Requirements incorporate it.

### Litigation relevance

- **Principle 11 (Risk governance):** The board should govern risk in a way that supports the organisation in setting and achieving its strategic objectives. Litigation is a key risk category.
- **Principle 15 (Assurance):** The board should ensure assurance results in an adequate and effective control environment. Legal risk assurance includes litigation monitoring.
- **Governing body responsibilities:** The board (or its risk/audit committee) should be informed of material litigation risks and their potential impact.

### Board reporting

King IV does not prescribe a specific litigation report format (unlike SEC Item 103). Instead:
- Litigation risk is reported as part of the **integrated report** (risk management section)
- Material matters are reported to the **audit and risk committee** at each meeting
- The standard is **apply-and-explain** — explain how litigation risk is governed, not line-item disclosure

---

## 3. JSE Listings Requirements

### Price-sensitive information and SENS

**SENS (Stock Exchange News Service)** is the JSE's platform for mandatory announcements.

A litigation development must be announced via SENS if it constitutes **price-sensitive information** — information that a reasonable investor would consider material to their investment decision.

| Trigger | Example |
|---|---|
| New material claim filed against the company | Class action, regulatory enforcement, claim exceeding materiality threshold |
| Material adverse judgment | Judgment that significantly impacts financial position or operations |
| Material settlement | Settlement exceeding materiality threshold |
| Regulatory investigation outcome | Fine, sanction, or finding with material impact |

### SENS trigger flag

On every matter-update with a material development, ask: **"Does this development require a SENS announcement?"**

Factors:
- Quantitative: does the exposure/outcome exceed the company's materiality threshold?
- Qualitative: does it affect core operations, licences, key contracts, or reputation?
- Timing: immediate disclosure required — cannot wait for the next quarterly report

### Periodic reporting

- **Annual financial statements:** IAS 37 notes on provisions and contingent liabilities
- **Integrated report:** Risk management section covering litigation risk governance
- **Interim results:** Update on material litigation developments

---

## 4. What NOT to replicate from US practice

| US concept | SA status |
|---|---|
| ASC 450 | Use IAS 37 (different probability thresholds, discounting, measurement) |
| SEC 10-K Item 103 (Legal Proceedings) | No equivalent line-item. Disclosure via IFRS notes + integrated report. |
| SEC 10-Q quarterly filing | SA has interim (half-year) and annual reporting. No quarterly 10-Q. |
| SOX / Sarbanes-Oxley | No equivalent. SA uses King IV (apply-and-explain) and Companies Act governance. |
| SEC risk factors (Item 105) | No equivalent. Risk disclosure is principle-based under King IV. |
| PCAOB audit standards | SA uses IRBA (Independent Regulatory Board for Auditors) and ISA standards. |
```

- [ ] **Step 2: Commit**

```bash
git add jurisdictions/za/litigation-legal/topics/risk-and-disclosure.md
git commit -m "feat(za): add risk-and-disclosure topic overlay"
```

---

## Task 15: Topic overlay — privilege.md

**Files:**
- Create: `jurisdictions/za/litigation-legal/topics/privilege.md`

- [ ] **Step 1: Write the topic overlay**

Write `jurisdictions/za/litigation-legal/topics/privilege.md`:

```markdown
# Privilege — South African Framework

This overlay covers SA legal professional privilege, the dominant purpose test, in-house counsel capacity, and privilege in discovery. Loaded by privilege-log-review, legal-hold, and brief-section-drafter when jurisdiction = ZA.

---

## 1. SA legal professional privilege

SA privilege is primarily **common-law**, constitutionally reinforced (Constitution s14 privacy, s34 access to courts). There is no single codifying statute.

### Two branches

| Branch | Scope | Test |
|---|---|---|
| **Advice privilege** | Confidential communications between client and legal adviser for the purpose of obtaining or giving legal advice | (1) Communication between client and legal adviser, (2) made for the purpose of legal advice, (3) intended to be confidential |
| **Litigation privilege** | Communications and documents prepared for the dominant purpose of pending or contemplated litigation | (1) Litigation pending or reasonably contemplated, (2) communication/document prepared for the **dominant purpose** of that litigation, (3) confidential |

### No work-product doctrine

SA does not have a separate "work product" doctrine (US FRCP 26(b)(3)). What US law calls "attorney work product" falls under **litigation privilege** in SA, which uses the dominant purpose test. There is no distinction between "opinion work product" and "ordinary work product" and no "substantial need" exception.

---

## 2. In-house counsel — legal vs commercial capacity

This is the critical SA-specific issue. Privilege attaches to in-house counsel **only when acting in a legal advisory capacity**.

| Capacity | Privileged? | Example |
|---|---|---|
| **Legal** | Yes | Legal opinion on regulatory compliance, advice on litigation strategy, analysis of contractual obligations |
| **Commercial** | No | Business strategy memo, commercial negotiation notes, operational decision-making, marketing input |
| **Mixed** | Dominant purpose test | If dominant purpose was legal advice → privileged. If dominant purpose was commercial → not privileged. |

### Red flags for privilege loss

- In-house counsel copied on commercial emails "for information" — does not create privilege
- Report drafted by in-house counsel but circulated to non-legal stakeholders for business input — privilege may be waived
- In-house counsel attending meetings in a management (not legal) capacity — notes not privileged

### Practical guidance

- Clearly delineate legal advice from business advice in communications
- Mark legal advice as "Privileged and Confidential — Legal Advice"
- Limit circulation of legal advice to those who need it for the purpose of obtaining the advice
- When in-house counsel acts in both capacities, keep legal advice in separate communications from commercial input

---

## 3. Privilege in discovery (Rule 35)

### Discovery affidavit

When asserting privilege in discovery (Rule 35(2)), the discovery affidavit must:
- **List** the documents over which privilege is claimed (sufficient description to identify the document)
- **State the basis** of privilege (advice privilege, litigation privilege, without-prejudice)
- **Not disclose** the content of the privileged communication

### De facto privilege schedule

While there is no formal privilege log requirement (no FRCP 26(b)(5)(A) equivalent), complex matters commonly use a **privilege schedule** — a table listing:
- Document date
- Author / recipient
- Document type / description (without revealing content)
- Basis of privilege claimed

This is **best practice**, not a rule requirement. Courts may order a more detailed schedule if privilege claims are disputed.

### Challenging privilege claims

The opposing party may:
- Request further particulars of the privilege claim
- Apply to court for an order requiring a more detailed schedule
- Request **in camera inspection** — the court reviews the documents without disclosing them to the other party and rules on privilege

### Over-claiming privilege

Courts are sceptical of blanket privilege assertions. Over-claiming (asserting privilege over non-privileged documents) can result in:
- Costs orders
- Adverse findings on credibility
- Court-ordered disclosure of improperly claimed documents

---

## 4. Waiver of privilege

### Express waiver

Client may expressly waive privilege (privilege belongs to the client, not the lawyer).

### Implied waiver

| Scenario | Effect |
|---|---|
| **Partial disclosure** | Disclosing part of a privileged communication waives privilege over the remainder on the same subject matter. Selective disclosure is not permitted. |
| **Annexing to affidavit** | Annexing a privileged document to an affidavit filed in court waives privilege over that document. |
| **Circulation to third parties** | Circulating privileged advice to persons outside the attorney-client relationship (consultants, PR firms, funders) may waive privilege unless they are within the "necessary circle" for obtaining legal advice. |
| **Putting advice in issue** | If a party relies on legal advice as part of their case (e.g., "we acted on legal advice"), they waive privilege on that advice. |

### One-way door

Privilege waiver is **irreversible**. Once waived, the privilege cannot be reclaimed. This is why the practice profile defaults to over-marking (assert privilege and flag for review) rather than under-marking.

---

## 5. Without-prejudice privilege

Separate from legal professional privilege. Communications genuinely aimed at settlement are privileged from being tendered in evidence.

See `demands-and-settlement.md` for detailed coverage of without-prejudice rules.

---

## 6. What NOT to replicate from US practice

| US concept | SA status |
|---|---|
| Work product doctrine (FRCP 26(b)(3)) | No equivalent. Litigation privilege covers this ground via dominant purpose test. |
| Opinion vs ordinary work product | No distinction. All litigation privilege is assessed on dominant purpose. |
| Substantial need exception | No equivalent. Litigation privilege is not qualified in this way. |
| FRE 502 (waiver rules) | SA waiver follows common-law principles, not a statutory framework. |
| FRCP 26(b)(5)(A) privilege log | No mandatory privilege log. De facto privilege schedule is best practice. |
| Vaughn index | No equivalent. In camera inspection is the SA mechanism. |
| Crime-fraud exception | SA recognises that privilege does not extend to communications in furtherance of crime or fraud, but the doctrine is less developed than in US law. |
```

- [ ] **Step 2: Commit**

```bash
git add jurisdictions/za/litigation-legal/topics/privilege.md
git commit -m "feat(za): add privilege topic overlay"
```

---

## Task 16: Practice profile template

**Files:**
- Create: `jurisdictions/za/litigation-legal/practice-profile-template.md`

This is the largest single file. It follows the structure of the US `litigation-legal/CLAUDE.md` template but with SA-specific sections replacing US-specific ones. See spec Section 4 for the complete design.

- [ ] **Step 1: Write the practice profile template**

Write `jurisdictions/za/litigation-legal/practice-profile-template.md`. The file is substantial — it replaces the US template's jurisdiction-specific sections while keeping jurisdiction-neutral sections (outputs format, guardrails, scaffolding, proportionality, matter workspaces, severity map).

Key sections to write from scratch (SA-specific):
- Work-product header (SA formulation)
- Source tags (SAFLII / Juta / LexisNexis SA)
- Privilege conventions (legal professional privilege, dominant purpose, in-house capacity caveat)
- Risk calibration — materiality thresholds (IAS 37, JSE SENS, King IV)
- Outside counsel bench (two-tier: attorneys + advocates)
- Frequent fora (SA court divisions)
- Reserve memo (IAS 37 provision assessment)
- Demand-letter practice (without-prejudice, mora)
- New sections: costs exposure, court hierarchy, prescription awareness, discovery model, dispute resolution landscape, SA legal profession structure

Use the US template (`litigation-legal/CLAUDE.md`) as the structural reference. Read it first, then write the ZA variant following the section replacement table in the spec.

**Note to implementer:** This file is ~500 lines. Read the spec Section 4 (Practice Profile Template Design) for every section replacement decision. Read the US template for the structure to follow. The ZA template keeps all jurisdiction-neutral sections verbatim and replaces only the jurisdiction-specific ones.

- [ ] **Step 2: Run template validation**

```bash
python3 scripts/validate-za-templates.py
```

Note: This will fail until the validation script is extended to include litigation-legal (Task 18). For now, manually verify the template has all required sections.

- [ ] **Step 3: Commit**

```bash
git add jurisdictions/za/litigation-legal/practice-profile-template.md
git commit -m "feat(za): add litigation-legal ZA practice profile template"
```

---

## Task 17: Cold-start interview fork

**Files:**
- Modify: `litigation-legal/skills/cold-start-interview/SKILL.md`

- [ ] **Step 1: Read the existing cold-start interview**

```bash
cat litigation-legal/skills/cold-start-interview/SKILL.md
```

Locate the end of Part 0 (role, integrations, practice setting). The ZA fork goes immediately after Part 0, before the US-specific interview questions.

- [ ] **Step 2: Add the ZA fork**

After the Part 0 section (where jurisdiction is determined from company-profile.md), add a jurisdiction check and ZA interview path. Follow the exact pattern from `employment-legal/skills/cold-start-interview/SKILL.md` lines 182-275.

Insert the following after the Part 0 completion point:

```markdown
---

## Jurisdiction fork

After Part 0, check the company profile's primary jurisdiction:
- Read `~/.claude/plugins/config/claude-for-legal/company-profile.md`
- Check the `jurisdiction` or `Core jurisdictions` field

**If PRIMARY JURISDICTION = "South Africa" (or "ZA" or matches SA):** fork to the SA interview path below.
**Otherwise:** continue with the standard interview.

---

## SA Interview Path — Litigation Practice

*This path runs instead of the US-specific interview when jurisdiction = ZA.*

### Part 1: SA Litigation Footprint (3-5 minutes)

**Q1: Province** — "Which province is your company registered in, and where are your primary operations? This determines your default High Court division."
- Options: Gauteng, Western Cape, KwaZulu-Natal, Eastern Cape, Free State, Limpopo, Mpumalanga, North West, Northern Cape, Multiple
- Writes to: `## Company profile — Core jurisdictions`

**Q2: Listed status** — "Is your company listed on the JSE, or is it a private company?"
- Options: JSE-listed, Private, Subsidiary of listed company
- If JSE-listed: sets materiality framework to IAS 37 + SENS triggers + integrated reporting
- If private: simpler reporting framework
- Writes to: `## 1. Risk calibration — Materiality thresholds`

**Q3: Legal profession structure** — "Do you use attorneys only, or do you also brief advocates (counsel) for court appearances and complex pleadings?"
- Options: Attorneys only, Attorneys + advocates (two-tier), Varies by matter
- Writes to: `## 2. Landscape — Outside counsel bench`

**Q4: Default instructing firm** — "Do you have a default instructing firm (attorney firm) for litigation matters?"
- Free text: firm name or "none / ad hoc"
- Writes to: `## 2. Landscape — Outside counsel bench` (first row)

**Q5: Costs posture** — "What is your general approach to costs orders: do you typically seek costs against the other party (SA default: loser pays), or do you tend to agree each party bears own costs?"
- Options: Seek costs (loser pays default), Each party bears own (by agreement), Depends on matter
- Writes to: `## Costs exposure`

**Q6: Arbitration** — "Do you use arbitration (AFSA or ad hoc) for any categories of dispute?"
- Options: Yes (specify which types), No, Occasionally
- Writes to: `## Dispute resolution landscape`

**Q7: Currency** — "What currency do you use for settlement authority thresholds and severity bands?"
- Options: ZAR, USD, EUR, Other
- Writes to: `## 1. Risk calibration — Settlement authority ladder`

### Part 2: Build the configuration

- Use ZA practice profile template from `jurisdictions/za/litigation-legal/practice-profile-template.md`
- Populate sections from interview answers
- Write to `~/.claude/plugins/config/claude-for-legal/litigation-legal/CLAUDE.md`
- Include the overlay loading instruction: "After loading context, read `jurisdictions/za/litigation-legal/router.md` and load the listed overlays for this skill."
```

- [ ] **Step 3: Commit**

```bash
git add litigation-legal/skills/cold-start-interview/SKILL.md
git commit -m "feat(za): add ZA fork to litigation-legal cold-start interview"
```

---

## Task 18: Extend validation scripts

**Files:**
- Modify: `scripts/validate-za-router.py`
- Modify: `scripts/validate-za-templates.py`

- [ ] **Step 1: Read current validation scripts to find extension points**

```bash
grep -n "PRACTICE_AREAS\|practice_areas\|employment-legal\|commercial-legal\|privacy-legal" scripts/validate-za-router.py
grep -n "TEMPLATE_CONFIG\|template_config\|employment-legal\|commercial-legal\|privacy-legal" scripts/validate-za-templates.py
```

- [ ] **Step 2: Add litigation-legal to router validator**

In `scripts/validate-za-router.py`, find the `PRACTICE_AREAS` list and add `"litigation-legal"`:

```python
PRACTICE_AREAS = [
    "employment-legal",
    "commercial-legal",
    "privacy-legal",
    "litigation-legal",  # Phase 4
]
```

- [ ] **Step 3: Add litigation-legal to template validator**

In `scripts/validate-za-templates.py`, find the `TEMPLATE_CONFIG` dict and add:

```python
"litigation-legal": {
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
    "required_terms": [
        "IAS 37",
        "King IV",
        "CCMA",
        "LRA",
        "Uniform Rules",
        "Rule 35",
        "heads of argument",
        "legal practitioner",
        "advocate",
        "attorney",
        "party-and-party",
        "without prejudice",
    ],
    "forbidden_terms": [
        r"\bFRCP\b",
        r"\bFRE 408\b",
        r"\bASC 450\b",
        r"\b10-K\b",
        r"\b10-Q\b",
        r"\bSOX\b",
        r"\bZubulake\b",
        r"\bBluebook\b",
        r"\bFMLA\b",
        r"\bat-will\b",
    ],
},
```

- [ ] **Step 4: Run both validators**

```bash
python3 scripts/validate-za-router.py && python3 scripts/validate-za-templates.py
```

Expected: PASS — all topic/statute references resolve, template has required sections and terms, no forbidden terms.

- [ ] **Step 5: Commit**

```bash
git add scripts/validate-za-router.py scripts/validate-za-templates.py
git commit -m "feat(za): extend validators for litigation-legal overlay"
```

---

## Task 19: Eval cases — demands, discovery, preservation

**Files:**
- Create: 9 eval case YAML files in `jurisdictions/za/evals/litigation-legal/`

- [ ] **Step 1: Create eval directories**

```bash
mkdir -p jurisdictions/za/evals/litigation-legal/{demand-draft,demand-received,deposition-prep,chronology,legal-hold,subpoena-triage}
```

- [ ] **Step 2: Write demand eval cases**

Write `jurisdictions/za/evals/litigation-legal/demand-draft/case-01-standard-payment.yaml`:

```yaml
name: "Standard payment demand requiring mora"
skill: demand-draft
input: |
  Client is owed R850,000 under a services agreement. Debtor has not paid despite
  invoice being 90 days overdue. No fixed payment date in the contract (payment is
  "on demand" or "within a reasonable time"). No arbitration clause. Debtor is a
  Johannesburg company.

expected_flags:
  - "mora"
  - "prescription"
  - "letter of demand"

must_not_contain:
  - "FRE 408"
  - "cease and desist"
  - "FDCPA"
  - "state-specific demand"
  - "Rule 408"

notes: |
  Because there is no fixed payment date, the debtor must be placed in mora by
  interpellatio (letter of demand) before the cause of action is complete. The
  skill should identify that a demand is a legal prerequisite, not just a
  strategic choice. It should also flag prescription (3-year period under s11(d))
  and calculate when the claim might prescribe.
```

Write `jurisdictions/za/evals/litigation-legal/demand-received/case-02-without-prejudice-offer.yaml`:

```yaml
name: "Inbound demand with without-prejudice settlement offer"
skill: demand-received
input: |
  Company receives a R2.5M demand letter marked "without prejudice" from a former
  supplier alleging breach of a services agreement. The letter includes a settlement
  offer of R1.2M if resolved within 30 days. The underlying contract contains an
  AFSA arbitration clause.

expected_flags:
  - "arbitration"
  - "without prejudice"
  - "costs"

must_not_contain:
  - "FRE 408"
  - "subject to Rule 408"
  - "settlement privilege under federal rules"
  - "state settlement communication"

notes: |
  The skill should identify: (1) the without-prejudice marking means admissions in
  the letter cannot be used in evidence (common-law rule, not FRE 408), (2) the
  arbitration clause means court proceedings would likely be stayed under Arbitration
  Act s6, (3) the costs exposure under SA loser-pays default should be assessed.
```

Write `jurisdictions/za/evals/litigation-legal/demand-draft/case-03-organ-of-state.yaml`:

```yaml
name: "Demand against provincial government department"
skill: demand-draft
input: |
  Client needs to demand payment from the Gauteng Department of Infrastructure
  Development for unpaid construction services (R3.2M, 4 months overdue under a
  fixed-price contract). The contract specifies payment within 30 days of invoice.

expected_flags:
  - "organ of state"
  - "section 3 notice"
  - "prescription"

must_not_contain:
  - "FTCA"
  - "sovereign immunity"
  - "Tucker Act"
  - "Court of Federal Claims"
  - "government claim"

notes: |
  The skill must flag the Institution of Legal Proceedings Against Organs of State
  Act s3 — a 6-month written notice is required before suing. The client is only
  4 months into the 6-month window. The skill should advise sending the s3 notice
  alongside or as part of the demand, and track the 6-month deadline. Even though
  the contract has a fixed payment date (30 days), the statutory notice requirement
  is separate from mora.
```

- [ ] **Step 3: Write discovery and witness prep eval cases**

Write `jurisdictions/za/evals/litigation-legal/deposition-prep/case-01-witness-prep-trial.yaml`:

```yaml
name: "Witness preparation for trial — no depositions"
skill: deposition-prep
input: |
  Senior employee (operations director) is the key witness in a commercial dispute
  over a construction contract. Trial is in 6 weeks in the Gauteng Division. The
  employee authored key emails and project reports that are in the trial bundle.

expected_flags: []

must_not_contain:
  - "deposition"
  - "FRCP 30"
  - "deposition outline"
  - "deponent"
  - "videotaped"
  - "oral examination before trial"

notes: |
  SA does not have depositions. The skill should reframe as trial preparation /
  witness preparation. Output should be a witness preparation outline covering:
  (1) key documents the witness should review, (2) chronology of events the witness
  covers, (3) anticipated cross-examination topics, (4) preparation for
  examination-in-chief and re-examination. No deposition-specific artifacts.
```

Write `jurisdictions/za/evals/litigation-legal/subpoena-triage/case-02-third-party-docs.yaml`:

```yaml
name: "Third-party bank document production"
skill: subpoena-triage
input: |
  We need financial records from First National Bank for the past 3 years. The bank
  is not a party to our litigation (commercial dispute in the Gauteng Division).
  The records are critical to proving damages.

expected_flags: []

must_not_contain:
  - "FRCP 45"
  - "non-party subpoena"
  - "100-mile rule"
  - "cost-shifting under Rule 45"
  - "place of compliance"

notes: |
  SA does not have FRCP 45-style pre-trial non-party subpoenas. The skill should
  advise: (1) apply to court under Rule 35(14) for an order compelling the bank
  to produce documents, or (2) issue a subpoena duces tecum under Rule 38 for
  production at trial. A court application is required for pre-trial non-party
  production — there is no self-executing right.
```

Write `jurisdictions/za/evals/litigation-legal/chronology/case-03-discovery-dispute.yaml`:

```yaml
name: "Discovery dispute — fishing expedition objection"
skill: chronology
input: |
  Opposing party has served a broad Rule 35(3) notice requesting "all documents
  relating to the company's financial performance, strategy documents, board minutes,
  and management reports for the past 10 years." Our pleadings relate to a specific
  breach of a supply agreement in 2024.

expected_flags:
  - "discovery"

must_not_contain:
  - "FRCP 26(b)(1)"
  - "proportionality"
  - "Rule 34 request for production"
  - "FRCP 33"
  - "interrogatories as of right"

notes: |
  The Hartzenberg rule applies — discovery is not a fishing expedition. The skill
  should advise that the request goes far beyond the pleaded issues (specific breach
  of a supply agreement). Respond substantively to Rule 35(3), objecting to
  irrelevant categories while discovering documents relevant to the pleaded issues.
  The court will refuse oppressive or speculative requests.
```

- [ ] **Step 4: Write preservation eval cases**

Write `jurisdictions/za/evals/litigation-legal/legal-hold/case-01-pre-litigation-popia.yaml`:

```yaml
name: "Pre-litigation hold with POPIA intersection"
skill: legal-hold
input: |
  A customer was injured using our product 2 weeks ago. No demand letter yet, but
  the customer's attorney has been in contact. We need to preserve relevant documents
  including customer personal data, product testing records, quality control reports,
  and internal communications about the product.

expected_flags:
  - "litigation hold"
  - "preservation"
  - "POPIA"

must_not_contain:
  - "Zubulake"
  - "FRCP 37(e)"
  - "safe harbor"
  - "litigation hold trigger under Zubulake"
  - "Sedona Conference"

notes: |
  Litigation is reasonably contemplated (attorney contact). The skill should:
  (1) issue a hold immediately covering all identified data sources, (2) note that
  the hold notice itself should be privileged, (3) address POPIA — the litigation
  exception (s14) justifies extended retention of customer personal data, but scope
  should be limited to what is relevant to the potential claim.
```

Write `jurisdictions/za/evals/litigation-legal/legal-hold/case-02-hold-release.yaml`:

```yaml
name: "Hold release after settlement with POPIA review"
skill: legal-hold
input: |
  A product liability matter was settled 6 months ago. The legal hold has been in
  place for 2 years, covering 15 custodians. We need to release the hold and
  review our POPIA obligations regarding the held personal information.

expected_flags: []

must_not_contain:
  - "FRCP 37(e) safe harbor"
  - "proportionality factors"
  - "Sedona Conference"
  - "Zubulake"

notes: |
  The skill should: (1) confirm the matter is concluded and no appeal is pending,
  (2) release the hold and notify all 15 custodians, (3) review POPIA s14 — with
  no ongoing litigation purpose, personal information held beyond its original
  retention period should be reviewed for deletion or de-identification, (4) document
  the release in the hold log.
```

Write `jurisdictions/za/evals/litigation-legal/legal-hold/case-03-missing-documents.yaml`:

```yaml
name: "Missing documents discovered mid-trial preparation"
skill: legal-hold
input: |
  During trial preparation, we discovered that key emails between the project manager
  and the client were destroyed 8 months ago by routine IT email archiving. The
  dispute was foreseeable at that time (we had already received a letter of demand).
  No litigation hold was ever issued.

expected_flags:
  - "litigation hold"
  - "adverse inference"
  - "discovery"

must_not_contain:
  - "Zubulake factors"
  - "FRCP 37(e)(1)"
  - "FRCP 37(e)(2)"
  - "intent to deprive"
  - "spoliation sanctions under federal rules"

notes: |
  The failure to issue a hold when the dispute was foreseeable is a serious issue.
  The skill should: (1) flag the risk of adverse inference if the opposing party
  raises the destruction, (2) advise disclosing the destruction in the discovery
  affidavit (what documents existed, when and how they were destroyed, what efforts
  were made to retrieve them), (3) assess whether backup copies exist, (4) prepare
  for a potential costs sanction or adverse inference application.
```

- [ ] **Step 5: Commit**

```bash
git add jurisdictions/za/evals/litigation-legal/
git commit -m "feat(za): add 9 litigation-legal eval cases (demands, discovery, preservation)"
```

---

## Task 20: Eval cases — privilege, advocacy, matter management, OC, subpoenas

**Files:**
- Create: 12 remaining eval case YAML files

- [ ] **Step 1: Create remaining eval directories**

```bash
mkdir -p jurisdictions/za/evals/litigation-legal/{privilege-log-review,brief-section-drafter,claim-chart,matter-intake,matter-close,portfolio-status,oc-status}
```

- [ ] **Step 2: Write privilege eval cases**

Write `jurisdictions/za/evals/litigation-legal/privilege-log-review/case-01-in-house-capacity.yaml`:

```yaml
name: "In-house counsel capacity issue — product recall report"
skill: privilege-log-review
input: |
  In-house legal counsel drafted a report on a product recall. The report includes
  legal analysis of potential liability under the Consumer Protection Act, as well
  as recommendations for the marketing team's communications strategy. The report
  was circulated to the marketing director and the head of operations for input.

expected_flags:
  - "privilege"
  - "in-house capacity"
  - "waiver"

must_not_contain:
  - "work product doctrine"
  - "FRCP 26(b)(3)"
  - "opinion work product"
  - "ordinary work product"
  - "substantial need test"

notes: |
  The skill should identify: (1) the legal analysis portions may be privileged
  (advice privilege) but the commercial/marketing portions are not, (2) circulation
  to non-legal stakeholders for business input risks waiver, (3) the dominant
  purpose test applies — if the dominant purpose was legal advice, privilege
  attaches; if commercial, it does not. The in-house counsel capacity distinction
  is the key SA-specific issue.
```

Write `jurisdictions/za/evals/litigation-legal/privilege-log-review/case-02-privilege-schedule.yaml`:

```yaml
name: "Privilege schedule preparation for complex commercial matter"
skill: privilege-log-review
input: |
  Complex commercial litigation in the Gauteng Division. We are withholding 450
  documents on privilege grounds in our Rule 35(2) discovery affidavit. Opposing
  counsel has requested a detailed privilege schedule.

expected_flags: []

must_not_contain:
  - "FRCP 26(b)(5)(A)"
  - "privilege log requirements under federal rules"
  - "Vaughn index"

notes: |
  There is no mandatory privilege log under SA rules (no FRCP 26(b)(5)(A)).
  However, a de facto privilege schedule is best practice in complex matters. The
  skill should produce a schedule with: document date, author/recipient, document
  type/description (without revealing content), and basis of privilege (advice,
  litigation, without-prejudice). The discovery affidavit must list and describe
  withheld documents sufficiently for the court to assess the claim.
```

Write `jurisdictions/za/evals/litigation-legal/privilege-log-review/case-03-partial-waiver.yaml`:

```yaml
name: "Partial disclosure waiver — opinion annexed to affidavit"
skill: privilege-log-review
input: |
  Our client annexed a legal opinion from external counsel to a founding affidavit
  in support of an urgent interdict application. The opinion addressed the merits
  of the underlying claim. Opposing party now demands all related legal advice on
  the same subject matter, arguing waiver by partial disclosure.

expected_flags:
  - "privilege"
  - "waiver"

must_not_contain:
  - "FRE 502"
  - "FRE 502(a)"
  - "selective waiver"
  - "subject matter waiver under federal rules"

notes: |
  SA common law: partial disclosure of privileged communications waives privilege
  over the remainder on the same subject matter. By annexing the opinion, the
  client has likely waived privilege over all related advice on that subject. The
  skill should assess whether the waiver extends to all advice on the underlying
  claim or only the specific topic of the annexed opinion.
```

- [ ] **Step 3: Write advocacy and claims eval cases**

Write `jurisdictions/za/evals/litigation-legal/brief-section-drafter/case-01-delict-heads.yaml`:

```yaml
name: "Heads of argument for delictual claim — construction defect"
skill: brief-section-drafter
input: |
  Draft heads of argument for a High Court trial in the Gauteng Division. Delictual
  (negligence) damages claim arising from a construction defect in a commercial
  building. R4.5M claimed for repair costs and consequential loss of rental income.
  Defendant is the main contractor.

expected_flags:
  - "costs"

must_not_contain:
  - "negligence per se"
  - "Restatement of Torts"
  - "CACI jury instructions"
  - "comparative fault statute"
  - "brief"

notes: |
  The output should be structured as heads of argument (not a brief). It must use
  SA delict elements: conduct (what the contractor did/failed to do), wrongfulness
  (breach of duty of care — objective reasonableness), fault (negligence — would
  reasonable contractor have foreseen?), causation (but-for + legal causation),
  harm (R4.5M damages). SA citation conventions must be used.
```

Write `jurisdictions/za/evals/litigation-legal/claim-chart/case-02-patent-infringement.yaml`:

```yaml
name: "SA patent claim chart — infringement analysis"
skill: claim-chart
input: |
  Prepare a claim chart mapping our client's SA patent claims (registered under
  Patents Act 57 of 1978) against an accused product. The patent covers a novel
  water purification membrane. The accused product is manufactured and sold in
  South Africa by a Johannesburg-based company.

expected_flags: []

must_not_contain:
  - "Markman hearing"
  - "claim construction order"
  - "CAFC"
  - "FRCP"
  - "jury verdict form"
  - "enhanced damages"
  - "treble damages"

notes: |
  SA patent litigation is heard by the Commissioner of Patents (a High Court judge).
  No Markman hearing — claim construction is done at trial. Remedies are interdict
  (not injunction), actual damages, reasonable royalty. No enhanced or treble
  damages. No civil jury. The claim chart should map claim elements against the
  accused product using SA claim construction principles (purposive interpretation).
```

Write `jurisdictions/za/evals/litigation-legal/brief-section-drafter/case-03-authority-hierarchy.yaml`:

```yaml
name: "Citation with conflicting High Court decisions"
skill: brief-section-drafter
input: |
  Draft a section of heads of argument addressing a contractual interpretation
  point. The Gauteng Division (Johannesburg) and the Western Cape Division have
  reached conflicting conclusions on the interpretation of a standard force
  majeure clause. The SCA has not ruled on the point.

expected_flags: []

must_not_contain:
  - "circuit split"
  - "en banc"
  - "SCOTUS cert petition"
  - "Bluebook"
  - "federal vs state law"

notes: |
  This tests SA authority hierarchy handling. Conflicting High Court divisions are
  the SA equivalent of a US circuit split. Neither division binds the other. The
  skill should: (1) present both positions, (2) argue which is more persuasive,
  (3) note that the SCA has not resolved the conflict, (4) use SA citation format
  (SA Law Reports or neutral citations), (5) if appropriate, suggest this may
  warrant a full bench referral or SCA appeal to resolve.
```

- [ ] **Step 4: Write matter management eval cases**

Write `jurisdictions/za/evals/litigation-legal/matter-intake/case-01-magistrates-claim.yaml`:

```yaml
name: "New matter intake — R180k contract claim, forum selection"
skill: matter-intake
input: |
  Client wants to sue for R180,000 breach of a supply contract. The defendant is
  a company registered and operating in Johannesburg. The contract has no forum
  selection or arbitration clause. Client is based in Cape Town.

expected_flags:
  - "forum"
  - "jurisdiction"

must_not_contain:
  - "small claims court limit"
  - "federal diversity jurisdiction"
  - "amount in controversy"
  - "Erie doctrine"
  - "removal"

notes: |
  R180,000 is within the district Magistrates' Court limit (R200,000). The skill
  should flag: (1) Magistrates' Court has jurisdiction (R180k < R200k limit), (2)
  High Court also has jurisdiction but costs may be disproportionate, (3) territorial
  jurisdiction — defendant is in Johannesburg, so the Johannesburg Magistrates'
  Court or Gauteng Division would have jurisdiction. Cape Town courts would need a
  jurisdictional basis (cause of action arising there, or consent).
```

Write `jurisdictions/za/evals/litigation-legal/matter-close/case-02-absolution.yaml`:

```yaml
name: "Matter close — absolution from the instance"
skill: matter-close
input: |
  Trial concluded in the Gauteng Division. The judge granted absolution from the
  instance at the close of the plaintiff's case, finding that the plaintiff had
  not made out a prima facie case on causation. We are the plaintiff. Need to
  close the matter and assess options.

expected_flags:
  - "leave to appeal"
  - "prescription"

must_not_contain:
  - "directed verdict"
  - "JMOL"
  - "Rule 50(a)"
  - "summary judgment at trial"
  - "res judicata"

notes: |
  Absolution from the instance = dismissal WITHOUT PREJUDICE. The plaintiff may
  re-institute (subject to prescription). The skill should: (1) explain absolution
  is not a final judgment on the merits — it means the plaintiff failed to make a
  prima facie case, (2) assess leave to appeal under s17 — reasonable prospect of
  success on the causation finding, (3) assess whether re-institution with better
  evidence is viable (check prescription), (4) record costs order.
```

Write `jurisdictions/za/evals/litigation-legal/portfolio-status/case-03-jse-listed.yaml`:

```yaml
name: "Quarterly portfolio review for JSE-listed company"
skill: portfolio-status
input: |
  Quarterly litigation portfolio review for a JSE-listed financial services company.
  12 active matters: 3 with exposure above R10M (a class action, a regulatory
  investigation by the FSCA, and a commercial dispute), 5 medium-exposure matters,
  4 low-exposure matters. Annual results are due in 6 weeks.

expected_flags:
  - "SENS"
  - "IAS 37"
  - "King IV"

must_not_contain:
  - "ASC 450"
  - "10-Q Item 103"
  - "SEC risk factors"
  - "SOX"
  - "Sarbanes-Oxley"
  - "PCAOB"

notes: |
  The skill should: (1) classify each matter under IAS 37 (provision / contingent
  liability / remote), (2) flag any developments requiring SENS announcements
  (price-sensitive information), (3) prepare audit/risk committee reporting under
  King IV, (4) for the 3 high-exposure matters, assess whether provisions should be
  recognised or notes updated in the upcoming annual financial statements.
```

- [ ] **Step 5: Write OC and subpoena eval cases**

Write `jurisdictions/za/evals/litigation-legal/oc-status/case-01-brief-senior-counsel.yaml`:

```yaml
name: "Briefing senior counsel for High Court trial"
skill: oc-status
input: |
  We need to brief a senior advocate (SC) for a 5-day High Court trial in the
  Gauteng Division starting in 8 weeks. Our instructing attorneys (a Johannesburg
  firm) have been managing the matter. We need to budget for both attorney fees
  and advocate fees, and prepare a status update for the board.

expected_flags: []

must_not_contain:
  - "partner billing rate"
  - "associate rate"
  - "LEDES billing"
  - "AFA under ABA guidelines"
  - "BigLaw"

notes: |
  The skill should model the two-tier fee structure: (1) instructing attorney
  fees (hourly or fixed for trial preparation and attendance), (2) advocate fees
  (brief fee + daily refresher for 5 trial days + consultation fees + marking
  fee). Budget should separate the two. Status update format should follow King IV
  / board reporting conventions, not US-style quarterly litigation reports.
```

Write `jurisdictions/za/evals/litigation-legal/subpoena-triage/case-01-third-party-subpoena.yaml`:

```yaml
name: "Subpoena duces tecum served on non-party company"
skill: subpoena-triage
input: |
  Our company (a technology services provider) has been served with a subpoena
  duces tecum to produce financial records and client communications at a trial
  between two other parties in 3 weeks. Some of the requested documents may
  contain privileged legal advice from our attorneys.

expected_flags:
  - "privilege"

must_not_contain:
  - "FRCP 45"
  - "motion to quash under Rule 45(d)"
  - "place of compliance limit"
  - "100-mile rule"
  - "undue burden under federal rules"

notes: |
  The skill should: (1) identify the subpoena was issued by the registrar under
  Rule 38, (2) advise reviewing the requested documents for privilege before
  producing, (3) if privileged documents are included, advise applying to court
  to limit the subpoena scope or asserting privilege over specific documents,
  (4) note that non-compliance is contempt of court.
```

Write `jurisdictions/za/evals/litigation-legal/subpoena-triage/case-03-contempt-risk.yaml`:

```yaml
name: "Witness non-attendance — contempt risk"
skill: subpoena-triage
input: |
  A former employee who is a key witness has been served with a subpoena ad
  testificandum to attend trial in the Western Cape Division next week. The
  former employee has informed us (through their attorney) that they do not
  intend to attend, citing personal inconvenience.

expected_flags: []

must_not_contain:
  - "material witness warrant"
  - "body attachment"
  - "FRCP 45(g)"
  - "federal contempt statute"
  - "deposition in lieu of appearance"

notes: |
  The skill should: (1) confirm the subpoena was properly served, (2) advise
  that failure to comply with a lawful subpoena is contempt of court — the
  witness may face a fine or imprisonment, (3) "personal inconvenience" is not
  a valid excuse, (4) the court may issue a warrant for the arrest of the
  defaulting witness, (5) consider whether approaching the witness's attorney
  to negotiate attendance or a statement is a practical alternative.
```

- [ ] **Step 6: Commit**

```bash
git add jurisdictions/za/evals/litigation-legal/
git commit -m "feat(za): add 12 litigation-legal eval cases (privilege, advocacy, matters, OC, subpoenas)"
```

---

## Task 21: Final validation run

- [ ] **Step 1: Run all validators**

```bash
python3 scripts/validate-za-statutes.py && echo "--- Statutes OK ---"
python3 scripts/validate-za-router.py && echo "--- Router OK ---"
python3 scripts/validate-za-templates.py && echo "--- Templates OK ---"
```

Expected: All three PASS.

- [ ] **Step 2: Verify file counts**

```bash
echo "=== Statute files ===" && ls jurisdictions/za/statutes/*.yaml | wc -l
echo "=== Topic overlays ===" && ls jurisdictions/za/litigation-legal/topics/*.md | wc -l
echo "=== Eval cases ===" && find jurisdictions/za/evals/litigation-legal -name "*.yaml" | wc -l
echo "=== Router ===" && ls jurisdictions/za/litigation-legal/router.md
echo "=== Practice profile ===" && ls jurisdictions/za/litigation-legal/practice-profile-template.md
```

Expected:
- Statute files: 22 (14 existing + 8 new)
- Topic overlays: 10
- Eval cases: 21
- Router: exists
- Practice profile: exists

- [ ] **Step 3: Run marketplace validation**

```bash
claude plugin validate .claude-plugin/marketplace.json 2>/dev/null; echo "exit: $?"
claude plugin validate litigation-legal 2>/dev/null; echo "exit: $?"
```

Expected: Both PASS (overlay files don't affect plugin structure validation).

- [ ] **Step 4: Verify no US concepts leaked into ZA files**

```bash
grep -rl "FRCP\|FRE 408\|ASC 450\|Zubulake\|FMLA\|at-will\|Bluebook\|10-K\|10-Q\|SOX" jurisdictions/za/litigation-legal/ jurisdictions/za/evals/litigation-legal/ || echo "No US concepts found — CLEAN"
```

Expected: "No US concepts found — CLEAN" (or matches only in `must_not_contain` fields of eval cases, which is expected).

- [ ] **Step 5: Final commit if any fixes were needed**

```bash
git status
# If clean: no commit needed
# If fixes: git add <files> && git commit -m "fix(za): address validation findings in litigation-legal overlay"
```
