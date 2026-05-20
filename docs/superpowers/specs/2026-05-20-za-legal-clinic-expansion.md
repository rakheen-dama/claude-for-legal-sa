# ZA Overlay Expansion Spec: legal-clinic

**Date:** 2026-05-20
**Plugin:** legal-clinic v1.0.2
**Target:** South African university law clinics
**Status:** Ready for implementation

---

## Decision Summary

| # | Step | Decision | Source |
|---|---|---|---|
| 1 | Target | legal-clinic — 16 skills, 10 in scope for v1 (8 HIGH + 2 MEDIUM divergence) | user confirmed |
| 2 | Statutes | 8 new YAML files (LPA, LPC Rules, Legal Aid SA, DVA, Maintenance, Children's Act, Small Claims, Criminal Procedure) + 8 existing cross-references | Perplexity + user confirmed |
| 3 | Skill divergence | 8 HIGH (cold-start-interview, build-guide, client-intake, draft, deadlines, research-start, ramp, status), 2 MEDIUM (memo, supervisor-review-queue), 3 MEDIUM deferred, 3 LOW/deprecated | user confirmed |
| 4 | Topic overlays | 7 topic files serving 10 skills | user confirmed |
| 5 | Practice profile | Section-by-section replacement of US template + 5 new SA sections + AI-privilege caveat | Perplexity + user confirmed |
| 6 | Cold-start questions | 10 must-have + 5 nice-to-have, ZA fork after Part 0 jurisdiction branch | user confirmed |
| 7 | High-risk flags | 14 flags (4 🔴, 4 🟠, 6 🟡) covering prescription, mandatory reporting, supervision, DVA urgency, State notice | Perplexity + user confirmed |
| 8 | Validation | 16 eval cases across 4 skill clusters + 5 validation rules + expert review gate | user confirmed |

---

## 1. Statute Inventory

### New statute YAML files

| File | Statute | Key sections | Temporal values |
|---|---|---|---|
| `lpa.yaml` | Legal Practice Act 28 of 2014 | s34(8) law clinics, s29 community service, s24 admission, s26 qualifications | Community service: 40hr/yr practitioners, 8hr/yr candidates (effective 2024-01-01) |
| `lpc-rules.yaml` | LPC Rules (GG 41781, 2018) + Code of Conduct (GG 42127, 2018) | Part IX Rules 36-37 (law clinics, candidate engagement), max 6 candidates per supervisor, Rule 54.36 (duty to report dishonest conduct) | Annual fees: R2,500 practitioners, R1,500 first-year, R800 non-practising |
| `legal-aid-sa.yaml` | Legal Aid South Africa Act 39 of 2014 | s3 objects, s19 client privilege protection, s22 court-directed representation, Regulations: means test, civil/criminal eligibility | Means test thresholds (updated periodically via Regulations) |
| `dva.yaml` | Domestic Violence Act 116 of 1998 | s4 application for protection order, s5 interim order (prima facie + undue hardship), s6 final order, s2B mandatory reporting, s8 warrant of arrest, s12 jurisdiction | Return date min 10 days after service; SAPS must serve interim order within 24 hours |
| `maintenance.yaml` | Maintenance Act 99 of 1998 | s2 duty to maintain, s6 maintenance complaints and investigations, s16 maintenance orders, s31 enforcement | — |
| `childrens-act.yaml` | Children's Act 38 of 2005 | s110 mandatory reporting (Form 22), s18-21 parental responsibilities, s45 children's court, s150 child in need of care | Failure to report per s110: up to 10 years imprisonment |
| `small-claims.yaml` | Small Claims Courts Act 61 of 1984 | s7 no legal representation, s14-15 jurisdiction, s17 incidental jurisdiction | Monetary limit: R20,000 (effective 2019-04-01, GG 42282) |
| `criminal-procedure.yaml` | Criminal Procedure Act 51 of 1977 | s35 bail, s112 plea, s271-276 appeals, s297 suspended sentences | — |

### Existing statute files available for cross-reference

| File | Statute | Relevant to |
|---|---|---|
| `cpa.yaml` | Consumer Protection Act 68 of 2008 | Consumer clinic intake |
| `nca.yaml` | National Credit Act 34 of 2005 | Debt counselling referrals |
| `popia.yaml` | POPIA 4 of 2013 | Client data handling |
| `magistrates-courts.yaml` | Magistrates' Courts Act 32 of 1944 | Court jurisdiction (district R200k, regional R400k) |
| `superior-courts.yaml` | Superior Courts Act 10 of 2013 | High Court matters |
| `prescription.yaml` | Prescription Act 68 of 1969 | Limitation periods (3yr default, 6yr negotiable, 30yr mortgage/judgment) |
| `paia.yaml` | PAIA 2 of 2000 | Access to information |
| `paja.yaml` | PAJA 3 of 2000 | Administrative justice reviews |
| `state-liability.yaml` | State Liability Act | Extend with Act 40 of 2002 (6-month notice for State organ claims) |

---

## 2. Skill Divergence Matrix

| Skill | Divergence | In scope v1 | Reasoning |
|---|---|---|---|
| cold-start-interview | HIGH | Y | Entire setup assumes US: ABA, state student practice rules, US jurisdiction. SA needs LPC, LPA s34(8), candidate legal practitioner model. |
| build-guide | HIGH | Y | References ABA ethics, US clinical education. SA needs LPC Rules, LPA supervision framework. |
| client-intake | HIGH | Y | Practice-area templates reference US law (ICE, US housing/family law). SA needs DVA, Maintenance, Children's Act, Rental Housing Act templates. |
| draft | HIGH | Y | US court captions, FRCP, state law. SA needs Magistrates' Court/High Court formats, Uniform Rules, SA document templates. |
| deadlines | HIGH | Y | FRCP computation, CA/IL plausibility bands. SA uses Magistrates' Courts Rules, Uniform Rules, different time computation. |
| research-start | HIGH | Y | Westlaw, CourtListener. SA uses SAFLII, Juta, LexisNexis SA. Different citation format. |
| ramp | HIGH | Y | US clinic context. SA onboarding needs LPA, LPC, candidate practitioner obligations, SA court system. |
| status | HIGH | Y | US court captions, local rules. SA court headers, case number formats differ. |
| memo | MEDIUM | Y | IRAC portable but jurisdictional framing and doctrine differ. SA legal research methodology needed. |
| supervisor-review-queue | MEDIUM | Y | Queue mechanism portable but LPA supervision model has specific legal requirements (s34(8), Rule 37). |
| client-letter | MEDIUM | N (v2) | Template structure portable. Disclosure requirements differ but work with profile-level SA context. |
| client-comms-log | MEDIUM | N (v2) | Logging process portable. Liability framing differs but not critically. |
| semester-handoff | MEDIUM | N (v2) | Process portable. SA academic calendar similar. |
| customize | LOW | N | Mechanism jurisdiction-neutral. Profile content changes, not the skill. |
| form-generation | LOW | N | DEPRECATED. |
| plain-language-letters | LOW | N | DEPRECATED. |

---

## 3. Topic Overlay Map

| # | Topic file | Skills served | Key content areas |
|---|---|---|---|
| 1 | `clinic-regulatory-framework.md` | cold-start-interview, build-guide, ramp, supervisor-review-queue | LPA s34(8) law clinic definition & requirements; LPC Rules Part IX (Rules 36-37) — accreditation, max 6 candidates per supervisor, 11-month/year operation; candidate legal practitioner terminology; community service obligations (40hr/8hr from 2024-01-01); LPC Code of Conduct; PVTC framework |
| 2 | `supervision-and-ethics.md` | cold-start-interview, build-guide, supervisor-review-queue, ramp | SA supervision model: "direct personal supervision" per Rule 37.1.1; no ABA Formal Op. 512 equivalent — LPC Code of Conduct + LPA governs; candidate practitioner disclosure in correspondence; SA legal professional privilege (narrower than US — no work-product doctrine, in-house commercial/legal distinction); AI output privilege per Baker McKenzie guidance; POPIA client data obligations |
| 3 | `sa-court-system.md` | draft, deadlines, status, research-start | Court hierarchy: Magistrates' Court (district R200k / regional R400k), High Court (9 divisions), SCA, Constitutional Court; specialist courts (Labour, Land Claims, Equality, Small Claims R20k, Children's); case number formats; court captions & headers; court terms/recess (16 Dec–15 Jan) |
| 4 | `sa-procedural-rules.md` | draft, deadlines, status | Magistrates' Courts Rules: time computation (Sat/Sun/public holidays excluded), service rules (sheriff, registered post deemed 4th day at 10:00), 20-day plea, 10-day application notice (20 days if State); Uniform Rules: Rule 6 notice of motion, Rule 43 interim relief, Rule 53 review; common document formats: combined summons, Form 6/J480 DVA, notice of motion, founding affidavit; court hours (08:00–15:00) |
| 5 | `sa-legal-research.md` | research-start, memo | SA databases: SAFLII (free, primary), Juta/JutaStat, LexisNexis SA/Lexis+, Sabinet Legal; citation format (*2020 (3) SA 1 (CC)*, *[2020] ZACC 1*); reporter abbreviations (SA, SACR, BCLR, BLLR, ILJ, BALR, All SA); Government Gazette; key secondary sources (Lawsa, commentaries) |
| 6 | `clinic-practice-areas.md` | client-intake, draft, memo | SA-specific templates: **Family/DVA** — Form 6 (J480) protection order, interim orders (prima facie + undue hardship), return date min 10 days, suspended warrant; Maintenance Act s6, maintenance courts; Children's Act care/contact/guardianship, Form 38. **Housing** — PIE Act s4, Rental Housing Tribunal. **Consumer** — CPA, NCA debt counselling. **Criminal** — bail, plea. **Delict** — personal injury, damages (MVA, police brutality). **Refugee** — Refugees Act 130 of 1998, asylum, Refugee Appeal Board |
| 7 | `clinic-client-access.md` | client-intake, cold-start-interview, ramp | Legal Aid SA referral (means test, eligibility, justice centres); free services per LPA s34(8)(c) — clinic may only recover disbursements; clinic eligibility criteria; language access (11 official languages); referral pathways (Legal Aid SA, SAHRC, small claims commissioners, Equality Court clerks); community service structures per LPA s29(2) |

---

## 4. Practice Profile Template Design

### Section replacement table

| US template section | ZA template equivalent |
|---|---|
| `# Law School Clinic Practice Profile` | `# University Law Clinic Practice Profile — South Africa` |
| `## Who's using this` — Supervising attorney, bar admission, bar number, student practice rule (Cal. Rules 9.42) | **Supervising legal practitioner** (admitted attorney per LPA s24), LPC enrollment number, LPC-accredited clinic status per Rule 36. Role options: Supervising legal practitioner / Candidate legal practitioner / Clinic staff. |
| `## Clinic profile` — School, US practice areas | **University**, SA practice areas: family & DVA / housing & eviction / consumer & debt / criminal & delict / refugee & migration / labour / general civil. "Candidate legal practitioners" not "students." |
| `## Jurisdiction` — State, county/district courts | **Province**, Magistrate's Court(s) + High Court division. Small Claims Court status, Equality Court access. |
| `## Supervision style` — 3 models, "professor" | Same 3 models, **"supervising legal practitioner"** throughout. LPA s34(8) direct personal supervision. LPC Rule 37.1.1. |
| `## Practice-area templates` — US document types | SA document types: Form 6/J480 (DVA), maintenance complaint, Children's Court Form 38, PIE Act notice, Rental Housing Tribunal complaint, letter of demand, bail affidavit. |
| `## Outputs` — US work-product header (FRCP 26(b)(3)) | `[AI-ASSISTED DRAFT — requires candidate analysis and supervising practitioner review before privilege may attach]`. SA legal professional privilege explanation. AI-privilege caveat per Baker McKenzie. SAFLII in reviewer note (not CourtListener). |
| `## Seed documents` — US expectations | SA-specific: Magistrates' Courts Rules, practice directives, DVA Form 6 blank, Legal Aid SA means test guide. |

### New sections

| Section | Purpose |
|---|---|
| `## LPC compliance` | Accreditation status, community service hours, PVTC contracts, annual reporting |
| `## SA court system` | Quick reference: court hierarchy, jurisdiction limits, specialist courts |
| `## Legal Aid SA interface` | Referral criteria, nearest justice centre, handoff process |
| `## Language access` | Languages served (11 official), plain-language target, interpreter arrangements |
| `## Mandatory reporting obligations` | Children's Act s110, DVA s2B — non-overridable triggers |

### Work-product header

```
[AI-ASSISTED DRAFT — requires candidate analysis and supervising practitioner review before privilege may attach]
```

**Privilege caveat:** AI-generated output is not automatically privileged under SA law. Legal advice privilege requires a qualified legal adviser; litigation privilege requires the dominant purpose test (*Ibex RSA Holdco v Tiso Blackstar*). Privilege likely attaches only once the supervising legal practitioner has applied professional skill and judgment to verify and adopt the text. SA courts have shown zero tolerance for AI-generated fictitious citations (*Mavundla v MEC; Northbound Processing v SA Diamond Regulator*).

For litigation-related work: `PRIVILEGED — PREPARED IN CONTEMPLATION OF LITIGATION UNDER THE DIRECTION OF [SUPERVISING PRACTITIONER]`

### Seed documents (requested at cold-start)

1. Clinic handbook / operating manual
2. Magistrates' Courts Rules (or SAFLII link)
3. Division-specific practice directives
4. Standard intake forms
5. DVA Form 6 (J480) blank template
6. Common template letters (demand, court correspondence)
7. Legal Aid SA means test guide / referral checklist
8. Example case file (scrubbed)
9. Clinic's disciplinary / complaints procedure
10. University's ethical clearance for AI-assisted clinical work (if applicable)

---

## 5. Cold-Start Interview Questions

### Must-have (10)

| # | Question | Configures |
|---|---|---|
| 1 | Is this clinic accredited by the Legal Practice Council under Rule 36? | `## LPC compliance` |
| 2 | Supervising legal practitioner(s): Name(s), LPC enrollment number(s), date of admission, attorney or advocate? | `## Who's using this` |
| 3 | How many candidate legal practitioners does each supervisor currently oversee? (max 6 per Rule 37) | `## Clinic profile` + ratio check |
| 4 | Which province, and which Magistrate's Court(s) and High Court division? | `## Jurisdiction` |
| 5 | Which practice areas? (Family & DVA / Housing & eviction / Consumer & debt / Criminal & delict / Refugee & migration / Labour / General civil / Other) | `## Clinic profile` + `## Practice-area templates` |
| 6 | Supervision model? (Formal review queue / Configurable flags / Lighter-touch) — framed with LPA s34(8) context | `## Supervision style` |
| 7 | Does the clinic handle matters involving children? → mandatory reporting acknowledgment (Children's Act s110) | `## Mandatory reporting obligations` |
| 8 | Which languages can the clinic serve? (11 official + interpreter availability) | `## Language access` |
| 9 | Relationship with Legal Aid South Africa? (Active / Informal / None) → nearest justice centre | `## Legal Aid SA interface` |
| 10 | Seed document upload (target 10-20 items, SA-specific prompts) | `## Seed documents` |

### Nice-to-have (5)

| # | Question | Configures |
|---|---|---|
| 11 | CaseLines or e-filing system? | `## Available integrations` |
| 12 | Academic calendar: term end, next cohort start? | `## Semester` |
| 13 | Plain-language target reading level? Prohibited jargon? | `## Plain-language standards` |
| 14 | Small Claims Court: advice-only or document preparation? | `## SA court system` |
| 15 | LPC community service hours tracking: in-plugin or external? | `## LPC compliance` |

### Flow

```
Part 0 (shared): Role check → ethical preconditions → jurisdiction detection
  ↓ jurisdiction = ZA
ZA-1: LPC accreditation (Q1)
ZA-2: Supervising practitioner + candidate ratio (Q2, Q3)
ZA-3: Province + courts (Q4)
ZA-4: Practice areas (Q5)
ZA-5: Supervision model (Q6)
ZA-6: Mandatory reporting (Q7) — if children/DVA practice areas selected
ZA-7: Languages (Q8)
ZA-8: Legal Aid SA (Q9)
ZA-9: Seed documents (Q10)
ZA-10 (if time): Nice-to-haves (Q11-15)
  ↓
Write ZA practice profile template → confirm → done
```

---

## 6. High-Risk Flag Table

| # | Flag | Level | Why high-risk | Check | Statute |
|---|---|---|---|---|---|
| 1 | Prescription approaching | 🔴 | Claim extinguished if missed. Most common malpractice ground. | 3yr default (s11(d)); special periods for RAF (3yr/5yr), COIDA (12mo). Flag at 6/3/1 months. | Prescription Act s11-12 |
| 2 | State organ notice period | 🔴 | 6-month notice required before suing State organs. Clinic clients commonly claim against SAPS, hospitals, municipalities. | Is opposing party a State organ? Has notice been served per Act 40 of 2002? | Act 40 of 2002 s3 |
| 3 | DVA urgency — client safety | 🔴 | DVA s4(5) allows urgent applications outside court hours. Delay endangers client. | Immediate safety risk? Same-day filing. SAPS serves within 24 hours. | DVA ss4-5 |
| 4 | Mandatory reporting — child | 🔴 | Legal practitioners are mandatory reporters (s110(1)). Failure = criminal offence, up to 10yr imprisonment. | Physical injury, sexual abuse, or deliberate neglect of child revealed? Report via Form 22. | Children's Act s110(1) |
| 5 | Mandatory reporting — DVA | 🔴 | DVA s2B requires reporting DV against children, elderly, disabled. | DV against child/older person/disabled person? Report required. | DVA s2B |
| 6 | Supervision ratio breach | 🟠 | LPC Rule 37 caps at 6 candidates per supervisor. Breach jeopardises accreditation. | Current count per supervisor. Flag at 5, block at 7. | LPC Rule 37 |
| 7 | Conflict of interest | 🟠 | Clinics serve concentrated communities. Opposing parties may both approach clinic. | Screen client + opposing party names against case register at intake. | LPC Code of Conduct 3.3-3.4 |
| 8 | Semester handoff — urgent matter | 🟠 | Active urgent matters can fall through during candidate transitions. | Audit all cases for deadlines within 60 days of handoff. | — (operational) |
| 9 | RAF procedural trap | 🟠 | RAF claims: 3yr lodge (2yr hit-and-run), 5yr summons, 120-day moratorium. | Motor vehicle claim? Apply RAF Act timelines, not generic Prescription Act. | RAF Act 56 of 1996 s23-24 |
| 10 | Small Claims representation bar | 🟡 | No legal representation permitted. Sending candidate to appear = procedural nullity. | Small Claims matter? Limit to advice + document prep only. R20,000 limit. | Small Claims Courts Act s7 |
| 11 | Client communication gap | 🟡 | Most common LPC complaint. Student-supervisor-client chain adds delay. | Each active client updated within 30 days? Flag 30+ day gaps. | LPC Code of Conduct 3.11 |
| 12 | Unauthorised practice | 🟡 | Candidate giving independent advice or signing without supervision = unauthorised practice. | Client-facing output bypassing supervision gate? Flag. | LPA s34(8)(b)(i), Rule 37.1.1 |
| 13 | POPIA — client data | 🟡 | Clinic collects sensitive PI (ID, income, medical, immigration). Special PI requires explicit consent. | Intake collecting only necessary info? Secure storage? Retention policy? | POPIA ss9-12, 26-27 |
| 14 | Court date clash | 🟡 | Candidate with multiple matters may have overlapping dates. Missed appearance = default/struck. | Cross-reference all court dates per candidate. Flag within 7 days of each other. | — (operational) |

---

## 7. Eval Case Outline

### Cluster 1: Setup & onboarding

| Case | Skill | Scenario | Expected |
|---|---|---|---|
| 1.1 | cold-start-interview | LPC-accredited Wits clinic, 4 supervisors, 18 candidates, 5 units | LPC confirmed, ratio OK (4.5 avg), mandatory reporting triggered. No ABA/US references. |
| 1.2 | cold-start-interview | Non-accredited new university clinic, 1 supervisor, 3 candidates, consumer only | Flag: no LPC accreditation, PVTC not countable. |
| 1.3 | ramp | First-semester candidate, Gauteng, family & DVA matters | Covers LPA obligations, s110 mandatory reporting, DVA urgency, Magistrates' Court, SAFLII. No Westlaw/US content. |
| 1.4 | build-guide | Housing & Eviction unit supervisor guide, pedagogy "guide" | PIE Act s4, Rental Housing Tribunal, supervisor review for all filings. No US housing law. |

### Cluster 2: Case work

| Case | Skill | Scenario | Expected |
|---|---|---|---|
| 2.1 | client-intake | Woman reporting DV, 2 minor children, threatened eviction from shared home | DVA urgency 🔴, mandatory reporting (DVA s2B, children exposed), protection order pathway. No VAWA/US DV. |
| 2.2 | client-intake | Client owes R45k on credit agreement, debt collector threatening, earns R8k/month | NCA debt counselling, CPA rights, Magistrates' Court (district), prescription check. No FDCPA/US bankruptcy. |
| 2.3 | draft | DVA protection order (Form 6/J480) for client from 2.1 | Form 6 format, founding affidavit, interim order requirements, return date min 10 days. No FRCP/US caption. |
| 2.4 | draft | Letter of demand for SAPS assault during arrest | State notice flag 🔴 (Act 40 of 2002, 6 months), prescription (3yr delict). No 42 USC § 1983/qualified immunity. |
| 2.5 | memo | IRAC: Can unmarried mother claim maintenance from estranged father? | Maintenance Act s2, Children's Act ss18-21, maintenance court procedure. No UIFSA/Title IV-D. |
| 2.6 | status | Court-ready status for eviction, Johannesburg Magistrate's Court | SA court caption, case number, procedural status. No US court caption. |

### Cluster 3: Research & deadlines

| Case | Skill | Scenario | Expected |
|---|---|---|---|
| 3.1 | research-start | Does landlord's eviction right survive 6+ month occupation? | SAFLII terms, PIE Act s4, relevant cases (*Ndlovu*, *Blue Moonlight*). No Westlaw/US law. |
| 3.2 | research-start | Refugee asylum rejection, wants to appeal | SAFLII terms, Refugees Act s24, PAJA s6. No US immigration/INA/USCIS. |
| 3.3 | deadlines | Personal injury vs municipality, assault by metro police 2024-08-15 | Prescription 3yr (2027-08-15), State notice 6mo URGENT, plausibility check. No FRCP computation. |
| 3.4 | deadlines | DVA return date, interim order served 2026-05-15, return 2026-05-30 | Return date OK (10+ days), anticipation on 24hr notice, flag at 7/3 days. No US DV scheduling. |

### Cluster 4: Supervision

| Case | Skill | Scenario | Expected |
|---|---|---|---|
| 4.1 | supervisor-review-queue | Candidate submits draft client letter, DVA + 3 children | Mandatory review, s110 check, plain language, candidate ID in letter. No ABA/professor. |
| 4.2 | supervisor-review-queue | 8 queue items, 1 supervisor, 6 candidates | Ratio at cap (Rule 37), prioritise by risk, suggest delegation. No US supervision rules. |

### Validation rules

- **No US legal concepts in ZA output:** FMLA, FLSA, FRCP, at-will, EEOC, NLRB, ABA, state bar, Cal. Rules, VAWA, FDCPA, INA, USCIS, Chapter 7/13, Section 8, HUD, Title IV-D, 42 USC § 1983, qualified immunity
- **SA terminology:** "legal practitioner" not "attorney at law"; "candidate legal practitioner" not "law student" (legal context); "delict" not "tort"; "prescription" not "statute of limitations"; "interdict" not "injunction"
- **Research sources:** SAFLII not Westlaw/CourtListener; SA citation format
- **Court formatting:** SA court captions, SA case number conventions
- **Privilege:** No FRCP 26(b)(3); SA legal professional privilege framing; AI-privilege caveat

---

## 8. Source Provenance Log

| Claim | Source | Status |
|---|---|---|
| LPA s34(8) law clinic definition and supervision requirements | Perplexity search → saflii.org/za/legis/consol_act/lpa2014120.pdf, dev.acts.co.za | verified |
| LPC Rules Part IX (Rules 36-37) — clinic accreditation, max 6 candidates | Perplexity search → lssa.org.za/wp-content/uploads/2020/01/LPC-Rules-9-July-2018.pdf | verified |
| Community service: 40hr practitioners, 8hr candidates from 2024-01-01 | Perplexity search → financialinstitutionslegalsnapshot.com (LPC Guidelines/Regulations 4A-4B) | verified |
| Legal Aid SA Act 39 of 2014 — objects, privilege, court-directed representation | Perplexity search → legal-aid.co.za, gov.za | verified |
| DVA s4-6 protection order procedure, s2B mandatory reporting | Perplexity search → justice.gov.za/legislation/acts/1998-116.pdf, saflii.org | verified |
| Children's Act s110 mandatory reporting — "legal practitioner" in listed reporters | Perplexity search → knowledgehub.health.gov.za, scielo.org.za | verified |
| Court jurisdiction: district R200k, regional R400k (2014), small claims R20k (2019-04-01) | Perplexity search → justice.gov.za/about/sa-courts.html, GG 42282 | verified |
| SA legal professional privilege — two forms, no work-product doctrine | Perplexity search → Baker McKenzie Global Privilege Guide (SA chapter), derebus.org.za, saflii.org | verified |
| AI output not automatically privileged in SA, zero tolerance for fictitious citations | Perplexity search → Baker McKenzie (resourcehub.bakermckenzie.com), *Mavundla*, *Northbound Processing* | verified |
| Prescription Act s11 — 3yr default, 6yr negotiable, 30yr mortgage/judgment | Perplexity search → gov.za/sites/default/files/gcis_document/201505/act-68-1969.pdf | verified |
| Act 40 of 2002 — 6-month notice for State organ claims | model knowledge — verify |
| RAF Act — 3yr lodge, 5yr summons, 120-day moratorium, 2yr hit-and-run | model knowledge — verify |
| SA university law clinic practice areas (Wits units, UJ, UP, UCT) | Perplexity search → wits.ac.za/lawclinic, saulca.co.za, uj.ac.za | verified |
| SA legal research: SAFLII, Juta, LexisNexis SA, citation format | Perplexity search → libguides.ukzn.ac.za, saflii.org, libguides.lib.uct.ac.za | verified |
| Magistrates' Courts Rules — time computation, service, deadlines | Perplexity search → justice.gov.za, saflii.org | verified |
| LPC disciplinary process — striking off, common complaints | Perplexity search → saflii.org (ZAWCHC/2025/60, ZAGPPHC/2024/617, ZAGPPHC/2024/1233) | verified |
