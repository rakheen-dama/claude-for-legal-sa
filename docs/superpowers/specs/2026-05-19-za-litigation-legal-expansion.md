# ZA Overlay Expansion: litigation-legal

**Date:** 2026-05-19
**Status:** Approved — ready for implementation planning
**Plugin:** litigation-legal v1.0.2
**Deciders:** Rakheen Dama

---

## Decision Summary

| # | Step | Decision | Source |
|---|---|---|---|
| 1 | Target | litigation-legal — 19 skills, 17 in scope (all HIGH + MEDIUM) | user confirmed |
| 2 | Statutes | 7 existing shared + 8 new (international-arbitration deferred). `prescription.yaml` needs correction + 6 new sections | Perplexity + user confirmed |
| 3 | Skill divergence | 15 HIGH, 2 MEDIUM, 2 LOW. 5 upgraded from MEDIUM→HIGH after Perplexity verification | Perplexity + user confirmed |
| 4 | Topic overlays | 10 topic files serving 17 skills | user confirmed |
| 5 | Practice profile | Section replacement table, SA work-product header (short + capacity caveat in privilege conventions), costs exposure section, prescription reminder | decided + user confirmed |
| 6 | Cold-start | 7 must-have + 4 nice-to-have questions | user confirmed |
| 7 | High-risk flags | 15 flags cross-referenced with statutes | Perplexity + user confirmed |
| 8 | Eval cases | 21 cases across 7 groupings, 5 validation rules, expert review gate | Perplexity |

---

## 1. Statute Inventory

### Existing statutes to share (in `jurisdictions/za/statutes/`)

| Statute file | Act | Litigation relevance | New sections needed |
|---|---|---|---|
| `prescription.yaml` | Prescription Act 68 of 1969 | Limitation periods, commencement, interruption | **Yes — correction + 6 new sections (see below)** |
| `ecta.yaml` | ECTA 25 of 2002 | Electronic evidence admissibility (ss11-20) | Possibly — evidence-related sections |
| `popia.yaml` | POPIA 4 of 2013 | Legal holds involving personal data, discovery of personal information | Unlikely |
| `cpa.yaml` | Consumer Protection Act 68 of 2008 | Consumer class actions, collective redress | Possibly — class action provisions |
| `conventional-penalties.yaml` | Conventional Penalties Act 15 of 1962 | Penalty clauses in contracts (damages) | No |
| `paia.yaml` | PAIA 2 of 2000 | Access to records before/during litigation | No |
| `competition.yaml` | Competition Act 89 of 1998 | Competition litigation, damages claims | No |

### prescription.yaml — correction and new sections

**Correction:** Current `other_debt_prescription` entry lists s11(a) as 6 years. This is incorrect — s11(a) is 30 years (judgment debts, debts secured by mortgage). The 6-year period is s11(c) (bills of exchange, notarial contracts).

**New sections to add:**

| Section key | Ref | Value | Why litigation needs it |
|---|---|---|---|
| `judgment_debt_prescription` | s11(a) | 30 years | How long a judgment remains enforceable |
| `tax_debt_prescription` | s11(b) | 15 years | State-related litigation |
| `bill_of_exchange_prescription` | s11(c) | 6 years | Commercial litigation (corrects current s11(a) error) |
| `knowledge_requirement` | s12(3) | knowledge of debtor identity + facts | The "discovery rule" — central to prescription defences |
| `interruption_by_acknowledgement` | s14 | prescription runs afresh | Key tactical issue in demand-received and matter-intake |
| `interruption_by_service` | s15 | prescription runs afresh from date process served | Most litigation-critical section — timing of service determines survival of claim |

### New statute YAML files

| File | Act | Key sections | Gazette-published values? |
|---|---|---|---|
| `superior-courts.yaml` | Superior Courts Act 10 of 2013 | s17 (leave to appeal — 15 court days), s18 (suspension of execution pending appeal), ss19-21 (jurisdiction) | Yes — appeal timelines |
| `magistrates-courts.yaml` | Magistrates' Courts Act 32 of 1944 | s29 (monetary jurisdiction limits), s28 (jurisdictional basis), ss65A-J (enforcement of judgment debts), s46A (execution against residential immovable property) | **Yes — monetary jurisdiction thresholds change by Gazette** |
| `arbitration.yaml` | Arbitration Act 42 of 1965 | s3 (reference to arbitration), s6 (stay of proceedings), s14-15 (powers of arbitrators), s30 (setting aside grounds), s31 (making award an order of court) | No temporal values, but structured grounds |
| `contingency-fees.yaml` | Contingency Fees Act 66 of 1997 | s2 (fee caps: max double normal fee, max 25% of amount awarded), s3 (formal requirements for agreement), s5 (void agreements) | Yes — fee cap percentages are statutory |
| `state-liability.yaml` | Institution of Legal Proceedings Against Certain Organs of State Act 40 of 2002 | s3 (6-month written notice requirement before suing state organs), notice content requirements | Yes — notice period is statutory |
| `civil-evidence.yaml` | Civil Proceedings Evidence Act 25 of 1965 | Competence/compellability of witnesses, documentary evidence, without-prejudice privilege | Minimal temporal, structured data useful |
| `evidence-amendment.yaml` | Law of Evidence Amendment Act 45 of 1988 | s3 (hearsay admissibility in civil proceedings) | No temporal |
| `enforcement-foreign-judgments.yaml` | Enforcement of Foreign Civil Judgments Act 32 of 1988 | Registration and enforcement of foreign civil judgments (reciprocity basis) | No temporal |

### Deferred

- **International Arbitration Act 15 of 2017** — deferred from v1 per user decision. Requirements documented here for v2.

---

## 2. Skill Divergence Matrix

| # | Skill | Divergence | In scope | Reasoning |
|---|---|---|---|---|
| 1 | brief-section-drafter | **HIGH** | ✓ | SA uses "heads of argument" not briefs. Different citation format (SA Law Reports, neutral citations). No jury instructions. Judge-alone system. |
| 2 | chronology | **HIGH** | ✓ | SA discovery is fundamentally narrower — Rule 35 list-based, no depositions, Hartzenberg rule against fishing. Discovery phase structure completely different. |
| 3 | claim-chart | **HIGH** | ✓ | No civil juries, no Markman hearings. SA delict = conduct + wrongfulness + fault + causation + harm. Patents Act 57/1978 governs. No punitive/treble damages. |
| 4 | cold-start-interview | **HIGH** | ✓ | IAS 37 not ASC 450, King IV not SEC, JSE Listings Requirements not 10-K/10-Q, two-tier profession (attorneys + advocates). |
| 5 | customize | **MEDIUM** | ✓ | Mechanism neutral, content US-specific (reserve methodology, board reporting, privilege conventions). |
| 6 | demand-draft | **HIGH** | ✓ | SA letter of demand places debtor in mora (legal prerequisite to some causes of action). Without-prejudice is common-law, not FRE 408. |
| 7 | demand-intake | **HIGH** | ✓ | Mora implications, formal requirements, without-prejudice toggle different from FRE 408. |
| 8 | demand-received | **HIGH** | ✓ | SA delictual/contractual frameworks differ. No FRE 408. |
| 9 | deposition-prep | **HIGH** | ✓ | No depositions in SA. Needs reframing to trial preparation / witness preparation for oral testimony. |
| 10 | legal-hold | **HIGH** | ✓ | No Zubulake/FRCP 37(e). Common-law preservation duty + ECTA s16 + POPIA retention limits. Different framework. |
| 11 | matter-briefing | **MEDIUM** | ✓ | Process portable, terminology and risk framework differ. |
| 12 | matter-close | **HIGH** | ✓ | Absolution from the instance, party-and-party vs attorney-and-client costs scales, leave to appeal (s17 test). Fundamentally different outcome types. |
| 13 | matter-intake | **HIGH** | ✓ | Two-tier profession (attorneys + advocates), IAS 37 not ASC 450, different conflicts clearing, SENS trigger flags. |
| 14 | matter-update | LOW | ✗ | Event logging is jurisdiction-neutral. |
| 15 | matter-workspace | LOW | ✗ | Pure file management, no legal content. |
| 16 | oc-status | **HIGH** | ✓ | Two-tier structure (instructing attorneys + briefed advocates), Legal Practice Act tariffs vs commercial rates, contingency fee caps. |
| 17 | portfolio-status | **HIGH** | ✓ | IAS 37 provisions vs ASC 450, JSE SENS triggers vs SEC 10-K/10-Q, King IV risk governance. |
| 18 | privilege-log-review | **HIGH** | ✓ | No FRCP 26(b)(5)(A) but de facto privilege schedule in complex matters. SA privilege = legal professional privilege only (advice + litigation), no separate work-product doctrine. |
| 19 | subpoena-triage | **HIGH** | ✓ | Registrar-issued, mainly for trial attendance. No FRCP 45-style pre-trial non-party discovery. |

**Total in scope:** 17 skills (15 HIGH + 2 MEDIUM)

---

## 3. Topic Overlay Map

### Topic files

| # | Topic file | Skills served | Key content areas |
|---|---|---|---|
| 1 | `court-structure-and-procedure.md` | matter-intake, matter-close, matter-briefing, chronology | SA court hierarchy (Magistrates' → High Court → SCA → ConCourt), monetary jurisdiction limits, civil procedure phases (summons → pleadings → discovery → pre-trial → trial → judgment), judgment types (absolution from the instance), costs orders (party-and-party vs attorney-and-client), leave to appeal (s17 test), loser-pays default |
| 2 | `discovery-and-evidence.md` | chronology, privilege-log-review, deposition-prep | Rule 35 list-based discovery, Hartzenberg rule (no fishing), interrogatories (rare, court-controlled), no depositions, witness preparation for trial, electronic evidence (ECTA ss11-20), Civil Proceedings Evidence Act, pre-trial conferences (Rule 37) |
| 3 | `demands-and-settlement.md` | demand-draft, demand-intake, demand-received | SA letter of demand (interpellatio), mora debitoris (legal default), formal requirements, open vs without-prejudice toggle, without-prejudice as common-law (not FRE 408), prescription interruption by demand, consequences of non-compliance, "without prejudice save as to costs" |
| 4 | `preservation-and-holds.md` | legal-hold | Common-law preservation duty (no Zubulake/FRCP 37(e)), adverse inference for destruction, ECTA s16 (electronic retention requirements), POPIA storage limitation + litigation exception, hold lifecycle adapted for SA, spoliation doctrine |
| 5 | `subpoenas.md` | subpoena-triage | SA subpoena mechanics (Rule 38 High Court, Rule 33 Magistrates'), registrar-issued (not attorney-issued), subpoena ad testificandum vs duces tecum, mainly for trial attendance, no pre-trial non-party document discovery as of right, contempt for non-compliance, court application for non-party production orders |
| 6 | `advocacy-and-citation.md` | brief-section-drafter, claim-chart | Heads of argument (not briefs) — issues-driven, succinct structure, SA citation conventions (SA Law Reports format, neutral citations e.g. [2015] ZACC 12), authority hierarchy (CC > SCA > High Court divisions), no jury instructions, judge-alone system, court practice directives |
| 7 | `elements-and-claims.md` | claim-chart, demand-draft, demand-received | SA delict elements (conduct, wrongfulness, fault, causation, harm), SA contract elements, patent litigation under Patents Act 57/1978 (Commissioner of Patents, no Markman), no civil juries, no punitive/treble damages, interdict vs injunction terminology, damages assessment (actual damages + reasonable royalty, no enhanced) |
| 8 | `legal-profession-and-fees.md` | oc-status, matter-intake, matter-close, cold-start-interview | Two-tier profession (attorneys = solicitors, advocates = barristers), instructing vs briefing counsel, Legal Practice Act tariffs, party-and-party vs attorney-and-client costs recovery, Contingency Fees Act (25% of award / double normal fee cap), commercial vs tariff rates, senior counsel (SC) vs junior counsel |
| 9 | `risk-and-disclosure.md` | portfolio-status, matter-intake, cold-start-interview, matter-briefing | IAS 37 provisions (not ASC 450), King IV risk governance (not SEC), JSE Listings Requirements, SENS trigger flags (price-sensitive information), IFRS contingent liabilities disclosure, no 10-K/10-Q style legal proceedings item, integrated reporting |
| 10 | `privilege.md` | privilege-log-review, legal-hold, brief-section-drafter | SA legal professional privilege (advice privilege + litigation privilege, no separate work-product doctrine), dominant purpose test for litigation privilege, in-house counsel (legal vs commercial capacity — privilege only when acting as legal adviser), de facto privilege schedule in complex matters (no FRCP 26(b)(5)(A)), without-prejudice privilege for settlement, partial disclosure waives privilege on subject matter |

### Skill-to-topic router

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

### Overlap with existing practice areas

- `privilege.md` overlaps thematically with `employment-legal/topics/investigation-privilege.md` (SA legal professional privilege, Protected Disclosures Act, POPIA). Litigation version focuses on litigation-specific privilege (privilege logs, discovery, dominant purpose test). Employment version focuses on workplace investigations. Separate files appropriate.
- No other significant overlaps.

---

## 4. Practice Profile Template Design

### Section replacement table

| US template section | Action | ZA template equivalent |
|---|---|---|
| Company profile | Minor adapt | Add Province, BEE level. Replace "Delaware corporation" with "company incorporated under Companies Act 71 of 2008". |
| Who's using this | Minor adapt | "Lawyer / legal professional" → "Legal practitioner" per Legal Practice Act. |
| Practice role | Minor adapt | Add firm-associate vocabulary note for SA two-tier system (instructing attorney vs briefed advocate). |
| Side | Minor adapt | Add SA terminology: "applicant/respondent" (motion), "plaintiff/defendant" (action). |
| Available integrations | Minor adapt | Replace iManage/NetDocuments with SA-relevant options. Add SAFLII (deferred MCP). Remove Ironclad CLM. |
| **Outputs — work-product header** | **Replace** | See header below. |
| Outputs — reviewer note | Keep | Format is jurisdiction-neutral. |
| Decision posture | Keep | Jurisdiction-neutral. |
| **Shared guardrails — source tags** | Minor adapt | Replace "Westlaw / CourtListener" with "SAFLII / Juta / LexisNexis SA". |
| Scaffolding, proportionality, jurisdiction recognition | Keep | Already multi-jurisdiction aware. |
| Matter workspaces | Keep | Neutral. |
| Severity vocabulary map | Keep | Neutral. |
| 1. Risk calibration — appetite + matrix | Keep structure | Neutral — user fills in. |
| **1. Risk calibration — Materiality thresholds** | **Replace** | ASC 450 → IAS 37. 10-Q/10-K → JSE SENS + integrated reporting. |
| 1. Risk calibration — Settlement authority | Minor adapt | USD → ZAR. Structure neutral. |
| 1. Risk calibration — Insurance profile | Minor adapt | Same types exist in SA. Add note re: SA short-term insurance regulatory framework. |
| 2. Landscape — Business context | Keep | User fills in. |
| 2. Landscape — Dispute patterns | Keep structure | Add "Constitutional/public interest" row. |
| 2. Landscape — Frequent adversaries | Keep | Neutral. |
| **2. Landscape — Outside counsel bench** | **Replace** | Two-tier: instructing firm (attorneys) + briefed counsel (advocates, senior/junior). Separate fee columns. |
| **2. Landscape — Frequent fora** | **Replace** | SA examples: Gauteng Division, Western Cape Division, KZN Division, SCA, ConCourt, AFSA arbitration, Magistrates' Courts. |
| 2. Landscape — Document storage | Keep | Neutral. |
| 2. Landscape — Conflicts clearance | Keep structure | Add note re: SA professional conduct rules under Legal Practice Act. |
| 3. House style — Board/audit committee memo | Minor adapt | King IV framing, integrated report style. |
| **3. House style — Reserve memo** | **Replace** | IAS 37 provision assessment: present obligation, probable outflow, reliable estimate. Not ASC 450. |
| 3. House style — Outside counsel directives | Minor adapt | Add advocate briefing conventions, tariff vs commercial rates, separate budget lines for attorney + counsel fees. |
| **3. House style — Privilege conventions** | **Replace** | "Legal professional privilege" (not "attorney-client / work product"). Dominant purpose test. In-house legal vs commercial capacity caveat. |
| 3. House style — Legal hold | Keep structure | Template pointer — SA-adapted hold template. |
| **3. House style — Demand-letter practice** | **Replace** | Without-prejudice (common-law) vs open. Mora implications. No FRE 408. Add "without prejudice save as to costs". |
| Seed documents | Adapt | SA-specific list (see below). |

### Work-product header

**If Role = Legal practitioner:**

> PRIVILEGED & CONFIDENTIAL — PREPARED AT THE DIRECTION OF A LEGAL PRACTITIONER

**If Role = Non-lawyer:**

> CONFIDENTIAL — NOT LEGAL ADVICE — REVIEW WITH A LEGAL PRACTITIONER BEFORE ACTING

The in-house commercial-vs-legal capacity caveat lives in the **privilege conventions** section of the practice profile (not in the header itself):

> **In-house counsel capacity:** SA legal professional privilege attaches only when in-house counsel acts in a legal advisory capacity. Work product created by in-house counsel acting in a commercial or managerial capacity (business strategy, commercial negotiations, operational decisions) is not privileged. Before asserting privilege over in-house work product, confirm the dominant purpose was obtaining or providing legal advice or preparing for litigation. Documents created for dual purposes (legal + commercial) are assessed on the dominant purpose test. When in doubt, assert privilege and flag for review — under-marking waives privilege (one-way door); over-marking is corrected in review (two-way door).

### New SA-specific sections to add

| Section | Content |
|---|---|
| **Costs exposure** | SA loser-pays default (costs follow the result). Party-and-party scale (standard), attorney-and-client scale (punitive), wasted costs, de bonis propriis (against attorney personally). Costs as a litigation risk factor on every matter. |
| **SA court hierarchy and forum selection** | Divisions of the High Court (Gauteng, Western Cape, KZN, etc.), Magistrates' Court monetary jurisdiction limits (from `magistrates-courts.yaml`), specialist courts (Labour Court, Equality Court, Competition Tribunal). Forum selection considerations. |
| **SA legal profession structure** | Attorneys (instructed by client, manage litigation) vs advocates (briefed by attorney, appear in High Court, draft heads). Senior counsel (SC) vs junior. Brief fee structure. |
| **Prescription awareness** | Standing instruction: "Check prescription on every new matter at intake." 3-year general (s11(d)), knowledge requirement (s12(3)), interruption by service (s15). |
| **SA discovery model** | Rule 35 list-based discovery. No depositions. Hartzenberg rule against fishing. Interrogatories require leave of court. Pre-trial conference (Rule 37). |
| **Dispute resolution landscape** | AFSA arbitration, mediation (voluntary), statutory dispute resolution (CCMA for employment, National Consumer Tribunal, Competition Tribunal). |

### Seed documents

| Doc | Location / pointer | Notes |
|---|---|---|
| Risk framework memo (King IV aligned) | [PLACEHOLDER] | IAS 37 provision methodology |
| Board/audit committee reporting template | [PLACEHOLDER] | King IV format, integrated reporting |
| Sample IAS 37 provision assessment | [PLACEHOLDER] | Replaces ASC 450 reserve memo |
| Outside counsel guidelines (SA) | [PLACEHOLDER] | Attorney + advocate fee structure, tariff reference |
| Legal hold template (SA-adapted) | [PLACEHOLDER] | Common-law preservation, ECTA s16, POPIA |
| Insurance summary | [PLACEHOLDER] | SA short-term insurance market |
| Sample contingency fee agreement | [PLACEHOLDER] | Contingency Fees Act compliant |
| Standard arbitration clause (AFSA) | [PLACEHOLDER] | Arbitration Act 42/1965 |

---

## 5. Cold-Start Interview Questions

### Must-have (SA fork after Part 0)

| # | Question | Why high-leverage | Writes to |
|---|---|---|---|
| 1 | Province where company is registered / primary operations? | Determines High Court division for default forum. | `## Company profile` — Core jurisdictions |
| 2 | JSE-listed or private? | Drives disclosure framework: JSE → IAS 37 + SENS + integrated reporting. Private → simpler. | `## 1. Risk calibration — Materiality thresholds` |
| 3 | Do you use attorneys only, or do you also brief advocates (counsel)? | Determines OC bench structure: one-tier vs two-tier. Shapes fee tracking, budget, OC status templates. | `## 2. Landscape — Outside counsel bench` |
| 4 | Who is your default instructing firm (if any)? | Seeds the OC bench. | `## 2. Landscape — Outside counsel bench` |
| 5 | General costs posture: do you typically seek costs orders, or each party bears own? | SA default is loser-pays, but commercial disputes sometimes agree otherwise. Calibrates risk assessment. | `## Costs exposure` (new section) |
| 6 | Do you use arbitration (AFSA or ad hoc) for any dispute types? | Routes matter-intake to arbitration vs court workflow. | `## Dispute resolution landscape` (new section) |
| 7 | Currency for thresholds and settlement authority? | Almost certainly ZAR, but multinational subsidiaries may use USD/EUR. | `## 1. Risk calibration — Settlement authority ladder` |

### Nice-to-have

| # | Question | Why useful but deferrable |
|---|---|---|
| 8 | Do you have a contingency fee arrangement with any outside counsel? | Triggers Contingency Fees Act compliance tracking. Rare for corporate. |
| 9 | Do you have existing legal hold templates adapted for SA (ECTA/POPIA)? | Lets hold skill use existing templates. |
| 10 | Do you subscribe to SAFLII alerts or any SA case law monitoring service? | Informs research tool availability. Deferred until MCP connectors. |
| 11 | King IV — does your board have a dedicated risk/audit committee that receives litigation reports? | Shapes board reporting template. Can be inferred from JSE-listed status. |

---

## 6. High-Risk Flag Table

| # | Flag | Why high-risk | What to check | Statute cross-ref |
|---|---|---|---|---|
| 1 | **prescription-near-expiry** | Claim prescribes and becomes unenforceable. Irreversible. | Calculate exact prescription date using s11 period + s12(3) knowledge date. Check for interruption (s15 service) or delay (s13). Diarise conservative deadline. | Prescription Act s11, s12, s13, s15 |
| 2 | **state-organ-s3-notice** | Suing organs of state requires 6-month written notice. Missing it can bar the claim entirely. | Check if defendant is "organ of state" per Act 40/2002. Verify notice sent, received, compliant. Check if 6-month period lapsed. | Institution of Legal Proceedings Against Organs of State Act s3 |
| 3 | **mora-not-established** | If debtor is not in mora, cause of action may be incomplete. Summons without prior demand can fail. | Is obligation due on a fixed date (mora ex re) or on demand? If on demand, was compliant letter of demand sent? Did deadline expire? | Common law — mora debitoris |
| 4 | **arbitration-clause-present** | Filing in court when arbitration clause exists → stay application, wasted costs, prescription risk on re-filing. | Check all relevant contracts for arbitration clauses. Determine scope. Check multi-tier (negotiate/mediate first). Raise or respond immediately. | Arbitration Act s3, s6 |
| 5 | **forum-jurisdiction-mismatch** | Wrong court → dismissal, delay, prescription risk. Magistrates' Court monetary limits are strict. | Verify: (a) monetary jurisdiction, (b) territorial jurisdiction (domicilium, cause of action, defendant's residence), (c) exclusive statutory fora. | Magistrates' Courts Act s28-s30; Superior Courts Act s19-21 |
| 6 | **defective-service** | Defective service renders proceedings voidable. Default judgments can be rescinded. Delays risk prescription. | Verify correct address (CIPC records, contractual domicilium). Check return of service completeness. Foreign defendants: Hague Convention / edictal citation. | Uniform Rules Rule 4; Magistrates' Courts Rules Rule 4 |
| 7 | **privilege-waiver-risk** | Unintentional waiver loses privilege permanently (one-way door). | Check: (a) third parties copied on legal advice, (b) in-house counsel in commercial capacity, (c) partial disclosure waiving balance, (d) privileged docs annexed to affidavits without reservation. | Common law — legal professional privilege |
| 8 | **no-litigation-hold** | Document destruction after litigation foreseeable → adverse inferences, costs sanctions, spoliation relief. | Issue hold notice to all custodians. Suspend routine IT deletion. Identify data sources. Record what was held and when. | Common law; ECTA s16; POPIA storage limitation |
| 9 | **loser-pays-costs-exposure** | SA default: costs follow the result. Attorney-and-client scale for misconduct. De bonis propriis against attorney personally. | Assess merits before proceeding. Quantify adverse costs exposure. Warn client in writing. Ensure procedural compliance. | Common law — costs follow the result |
| 10 | **constitutional-rights-implicated** | Commercial litigators miss Bill of Rights implications → unexpected constitutional defences or proportionality requirements. | Screen for: s25 (property), s33/PAJA (administrative action), s34 (access to courts), s14 (privacy), s26 (housing — PIE Act). | Constitution ss14, 25, 33, 34, 36 |
| 11 | **class-action-exposure** | Developing area — certification criteria from *Children's Resource Centre* / *Nkala*. Large-scale liability if class certified. | Assess: viable cause of action, identifiable class, common issues, suitable representative, class action as appropriate procedure. Track prescription for class members. | Constitution s38 |
| 12 | **contingency-fee-non-compliance** | Non-compliant contingency fee agreement is void. Practitioner may recover nothing. | Verify: (a) in writing, (b) signed by both parties, (c) fee within caps (25% / double), (d) prescribed disclosures included. | Contingency Fees Act s2, s3, s5 |
| 13 | **discovery-deficiency** | Incomplete discovery → adverse inferences, striking out, trial adjournment, costs sanctions. | Structured discovery process: custodians, data sources, date ranges. Accurate discovery affidavit. Respond to Rule 35(3) and 35(12) substantively. | Uniform Rules Rule 35 |
| 14 | **leave-to-appeal-threshold** | No automatic right of appeal. Must show reasonable prospect of success or compelling reason. | Apply to court that gave judgment. If refused, petition SCA. Time limit: 15 court days. | Superior Courts Act s17 |
| 15 | **competition-regulatory-parallel** | Competition investigation + civil damages claim run in parallel. Admissions in one forum used in the other. | Instruct competition specialists early. Document hold immediately. Consider settlement wording to limit civil exposure. | Competition Act 89/1998 |

---

## 7. Eval Case Outlines

### 7.1 Demands & settlement (demand-draft, demand-intake, demand-received)

**D-01: Standard payment demand**
- **Input:** Client owed R850,000 under services agreement. Debtor unpaid 90 days. No fixed payment date in contract.
- **Expected flags:** mora-not-established, prescription-near-expiry (check s11(d))
- **Expected statutes:** Prescription Act s11(d), s12(1)
- **Must NOT contain:** FRE 408, "cease and desist", FDCPA, state-specific demand requirements

**D-02: Inbound demand with without-prejudice offer**
- **Input:** Company receives R2.5M demand marked "without prejudice" alleging breach of contract. Settlement offer of R1.2M.
- **Expected flags:** arbitration-clause-present (check contract), loser-pays-costs-exposure
- **Expected statutes:** Prescription Act s15, Arbitration Act s6
- **Must NOT contain:** FRE 408, "subject to Rule 408", "settlement privilege under federal rules"

**D-03: Demand against organ of state**
- **Input:** Client demands R3.2M from provincial government department for unpaid construction services, 4 months overdue.
- **Expected flags:** state-organ-s3-notice, prescription-near-expiry, forum-jurisdiction-mismatch
- **Expected statutes:** Institution of Legal Proceedings Against Organs of State Act s3
- **Must NOT contain:** "FTCA", "sovereign immunity", "Tucker Act", "Court of Federal Claims"

### 7.2 Discovery & evidence / deposition-prep

**DE-01: Witness preparation for trial**
- **Input:** Senior employee is key witness in commercial dispute. Trial in 6 weeks.
- **Expected flags:** None (routine)
- **Expected statutes:** Civil Proceedings Evidence Act, Uniform Rules Rule 37
- **Must NOT contain:** "deposition", "FRCP 30", "deposition outline", "deponent", "videotaped deposition"

**DE-02: Third-party document production**
- **Input:** Need financial records from non-party bank. Records critical to proving damages.
- **Expected flags:** None (procedural)
- **Expected statutes:** Uniform Rules Rule 38 (subpoena duces tecum), Rule 35(14)
- **Must NOT contain:** "FRCP 45 subpoena", "non-party subpoena", "100-mile rule", "cost-shifting under Rule 45"

**DE-03: Discovery dispute — fishing expedition objection**
- **Input:** Opposing party serves broad Rule 35(3) notice requesting "all documents relating to company's financial performance for 10 years."
- **Expected flags:** discovery-deficiency
- **Expected statutes:** Uniform Rules Rule 35(3), Hartzenberg principle
- **Must NOT contain:** "FRCP 26(b)(1) proportionality", "Rule 34 request for production", "FRCP 33"

### 7.3 Preservation & holds / legal-hold

**LH-01: Pre-litigation hold with POPIA intersection**
- **Input:** Company anticipates product liability claim after customer injury. No demand yet.
- **Expected flags:** no-litigation-hold, privilege-waiver-risk
- **Expected statutes:** ECTA s16, POPIA s14
- **Must NOT contain:** "Zubulake", "FRCP 37(e)", "safe harbor", "litigation hold trigger under Zubulake"

**LH-02: Hold release after matter close**
- **Input:** Matter settled 6 months ago. Legal hold in place 2 years, 15 custodians.
- **Expected flags:** None (routine close)
- **Expected statutes:** POPIA s14 (storage limitation), ECTA s16
- **Must NOT contain:** "FRCP 37(e) safe harbor", "Sedona Conference"

**LH-03: Missing documents discovered mid-trial**
- **Input:** Key emails destroyed by routine IT deletion 8 months after dispute foreseeable. No hold issued.
- **Expected flags:** no-litigation-hold, discovery-deficiency
- **Expected statutes:** Uniform Rules Rule 35, common law adverse inference
- **Must NOT contain:** "Zubulake factors", "FRCP 37(e)(1) vs 37(e)(2)", "intent to deprive"

### 7.4 Privilege / privilege-log-review

**P-01: In-house counsel capacity issue**
- **Input:** In-house counsel drafted product recall report with legal analysis. Circulated to marketing team.
- **Expected flags:** privilege-waiver-risk, constitutional-rights-implicated
- **Expected statutes:** Common law — legal professional privilege, dominant purpose test
- **Must NOT contain:** "work product doctrine", "FRCP 26(b)(3)", "opinion vs ordinary work product", "substantial need test"

**P-02: Privilege log preparation**
- **Input:** Complex commercial litigation. 450 documents withheld on privilege. Must prepare schedule.
- **Expected flags:** None (procedural)
- **Expected statutes:** Uniform Rules Rule 35(2), common law LPP
- **Must NOT contain:** "FRCP 26(b)(5)(A)", "privilege log requirements under federal rules", "Vaughn index"

**P-03: Partial disclosure waiver**
- **Input:** Client annexed legal opinion to founding affidavit for urgent interdict. Opposing party demands all related advice.
- **Expected flags:** privilege-waiver-risk
- **Expected statutes:** Common law — waiver by partial disclosure
- **Must NOT contain:** "FRE 502", "FRE 502(a)", "selective waiver"

### 7.5 Advocacy & claims (brief-section-drafter, claim-chart)

**A-01: Heads of argument — delictual claim**
- **Input:** Draft heads for High Court trial, delictual damages from construction defect. R4.5M claimed.
- **Expected flags:** loser-pays-costs-exposure
- **Expected statutes:** Common law — delict (conduct, wrongfulness, fault, causation, harm)
- **Must NOT contain:** "negligence per se", "Restatement of Torts", "CACI jury instructions", "comparative fault statute"

**A-02: Patent claim chart — infringement**
- **Input:** Claim chart mapping patent claims against accused product. SA patent under Patents Act 57/1978.
- **Expected flags:** None
- **Expected statutes:** Patents Act 57/1978, Commissioner of Patents procedure
- **Must NOT contain:** "Markman hearing", "claim construction order", "CAFC", "jury verdict form", "treble damages"

**A-03: Citation and authority hierarchy**
- **Input:** Brief section citing conflicting High Court decisions on contractual interpretation. SCA has not ruled.
- **Expected flags:** None
- **Expected statutes:** Superior Courts Act s17, Constitution s166
- **Must NOT contain:** "circuit split", "en banc", "SCOTUS cert petition", "Bluebook citation format"

### 7.6 Court procedure & matter management

**M-01: New matter intake — R180,000 contract claim**
- **Input:** Client sues for R180,000 breach of contract. Defendant in Johannesburg. No forum clause.
- **Expected flags:** forum-jurisdiction-mismatch (within Magistrates' Court limit)
- **Expected statutes:** Magistrates' Courts Act s29
- **Must NOT contain:** "small claims court limit", "federal diversity jurisdiction", "amount in controversy", "Erie doctrine"

**M-02: Matter close — absolution from the instance**
- **Input:** Trial concluded with absolution at close of plaintiff's case. Close matter, assess options.
- **Expected flags:** leave-to-appeal-threshold
- **Expected statutes:** Superior Courts Act s17, common law absolution
- **Must NOT contain:** "directed verdict", "JMOL", "Rule 50(a)", "res judicata (absolute)"

**M-03: Portfolio status — JSE-listed company**
- **Input:** Quarterly review for JSE-listed company. 12 active matters, 3 above R10M exposure.
- **Expected flags:** constitutional-rights-implicated (check any constitutional dimension)
- **Expected statutes:** IAS 37, JSE Listings Requirements, King IV
- **Must NOT contain:** "ASC 450", "10-Q Item 103", "SEC risk factors", "SOX", "Sarbanes-Oxley"

### 7.7 Outside counsel & subpoenas

**OC-01: Briefing senior counsel for trial**
- **Input:** Brief SC for 5-day High Court trial. Instructing attorneys managing matter. Budget both fees.
- **Expected flags:** None (routine)
- **Expected statutes:** Legal Practice Act 28/2014, Contingency Fees Act s2 (if applicable)
- **Must NOT contain:** "partner billing rate", "LEDES billing", "AFA under ABA guidelines"

**S-01: Subpoena served on company as third party**
- **Input:** Company (non-party) receives subpoena duces tecum for financial records at trial in 3 weeks.
- **Expected flags:** privilege-waiver-risk
- **Expected statutes:** Uniform Rules Rule 38, Rule 35(14)
- **Must NOT contain:** "FRCP 45", "motion to quash under Rule 45(d)", "100-mile rule"

**S-02: Contempt risk — witness non-attendance**
- **Input:** Former employee indicates they will not attend trial despite subpoena ad testificandum.
- **Expected flags:** None (escalation issue)
- **Expected statutes:** Uniform Rules Rule 38, common law contempt
- **Must NOT contain:** "material witness warrant", "body attachment", "FRCP 45(g)"

### Validation rules (applied across all cases)

1. No US civil procedure: FRCP, FRE, Bluebook, JMOL, directed verdict, circuit split, federal jurisdiction, state law
2. No US privilege doctrine: work product, FRCP 26(b)(3), FRE 502, Vaughn index
3. No US accounting/disclosure: ASC 450, 10-K/10-Q, SOX, SEC
4. No US litigation vocabulary where SA differs: deposition (as routine procedure), interrogatories "as of right", pattern jury instructions, punitive/treble damages
5. SA-specific terminology must appear: heads of argument (not briefs), legal practitioner (not attorney-at-law), delict (not tort), interdict (not injunction), applicant/respondent (in motion proceedings)

### Expert review gate

Before release, an SA litigation practitioner reviews:
- Topic overlay procedures against current Uniform Rules and case law
- High-risk flag table against current court practice and referral patterns
- Practice profile template for completeness and correctness
- Eval case expected outputs for legal accuracy
- Statute YAML values against current Government Gazette and published thresholds

---

## 8. Source Provenance Log

| Step | Item | Source | Tag |
|---|---|---|---|
| 2 | SA litigation statutes inventory | Perplexity search — comprehensive list of applicable Acts | [Perplexity — verify] |
| 2 | Prescription Act s11 periods, s12(3), s14, s15 | Perplexity + model knowledge | [Perplexity — verify] |
| 2 | Superior Courts Act s17 (leave to appeal) | Perplexity | [Perplexity — verify] |
| 2 | Magistrates' Courts Act s29 (monetary jurisdiction) | Perplexity | [Perplexity — verify] |
| 2 | Contingency Fees Act s2 caps (25% / double) | Perplexity | [Perplexity — verify] |
| 2 | State Liability Act s3 (6-month notice) | Perplexity | [Perplexity — verify] |
| 2 | prescription.yaml s11(a) error (listed as 6 years, should be 30 years) | Perplexity cross-reference | [Perplexity — verify] |
| 3 | Skill divergence — all 19 skills assessed | SKILL.md frontmatter read + Perplexity verification | [Perplexity + user confirmed] |
| 3 | SA discovery narrower than US (Hartzenberg rule) | Perplexity | [Perplexity — verify] |
| 3 | No civil depositions in SA | Perplexity | [Perplexity — verify] |
| 3 | Two-tier profession (attorneys + advocates) | Perplexity | [Perplexity — verify] |
| 3 | IAS 37 vs ASC 450 | Perplexity | [Perplexity — verify] |
| 3 | King IV vs SEC governance | Perplexity | [Perplexity — verify] |
| 5 | SA work-product header — no work-product doctrine | Perplexity + model knowledge | [Perplexity — verify] |
| 5 | In-house counsel capacity distinction | Perplexity | [Perplexity — verify] |
| 7 | All 15 high-risk flags | Perplexity comprehensive risk research | [Perplexity — verify] |
| 7 | *Children's Resource Centre* / *Nkala* class action criteria | Perplexity | [Perplexity — verify] |
| 7 | Absolution from the instance | Perplexity | [Perplexity — verify] |
| 7 | Party-and-party vs attorney-and-client costs | Perplexity | [Perplexity — verify] |
| 7 | De bonis propriis costs against attorney | Perplexity | [Perplexity — verify] |
| 7 | Mora debitoris requirements | Perplexity | [Perplexity — verify] |
| 8 | SA delict elements (conduct, wrongfulness, fault, causation, harm) | Perplexity | [Perplexity — verify] |
| 8 | SA citation conventions (SA Law Reports, neutral citations) | Perplexity | [Perplexity — verify] |

---

## Implementation Sequence

Following the same task structure as the employment-legal build:

1. Statute YAML files (8 new + extend `prescription.yaml`)
2. Topic overlay markdown files (10 files)
3. Skill router (`jurisdictions/za/litigation-legal/router.md`)
4. Practice profile template (`jurisdictions/za/litigation-legal/practice-profile-template.md`)
5. Cold-start interview fork (add ZA branch to `litigation-legal/skills/cold-start-interview/SKILL.md`)
6. Validation scripts (extend existing validators for litigation-legal)
7. Scenario eval cases (21 cases in `jurisdictions/za/evals/litigation-legal/`)
8. Final validation run
