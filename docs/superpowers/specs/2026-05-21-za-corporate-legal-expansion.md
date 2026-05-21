# ZA Corporate-Legal Expansion — Decision Spec

**Date:** 2026-05-21
**Plugin:** corporate-legal v1.0.2
**Description:** Runs M&A diligence at scale with cited tabular review, builds disclosure schedules and closing checklists, drafts board consents and minutes in house format, and tracks entity compliance deadlines across jurisdictions.
**Skills:** 13 total, 8 in scope
**Interview by:** Rakheen Dama + Claude

---

## 1. Decision Summary

| # | Step | Decision | Source |
|---|---|---|---|
| 1 | Target | corporate-legal — 13 skills, 8 in scope (6 HIGH + 2 MEDIUM) | user confirmed |
| 2 | Statutes | 3 new (companies-act, companies-regulations, close-corporations) + 2 extended (competition, bbbee) + 1 unchanged (fica) | Perplexity + user confirmed |
| 3 | Skill divergence | HIGH: board-minutes, closing-checklist, cold-start-interview, diligence-issue-extraction, entity-compliance, written-consent. MEDIUM: integration-management, material-contract-schedule. | Perplexity + user confirmed |
| 4 | Topic overlays | 5 files: fundamental-transactions, takeover-regulation, board-governance, entity-compliance-cipc, diligence-sa | user confirmed |
| 5 | Practice profile | SA privilege header (no "attorney work product"), AI privilege caveat, 6 new sections, 7 seed documents | Perplexity + user confirmed |
| 6 | Cold-start | 8 must-have + 4 nice-to-have questions, ZA fork after Part 0 | user confirmed |
| 7 | High-risk flags | 14 flags covering M&A, board governance, entity compliance, regulatory approval | Perplexity + user confirmed |
| 8 | Validation | 24 eval cases (3 × 8 skills), 5 validation rules, expert review gate | user confirmed |

---

## 2. Statute Inventory

### New statute files

| Statute | File | Key sections | Temporal values |
|---|---|---|---|
| Companies Act 71 of 2008 | `companies-act.yaml` | s4 (solvency & liquidity test), s33 (annual returns — 30 BD), s46 (distributions), s60 (shareholders acting without meeting), s66 (board authority), s73 (board meetings), s74 (directors acting without meeting — round-robin), s75 (personal financial interests), s76 (directors' conduct / business judgment rule), s77 (director liability), s82 (deregistration), s94 (audit committee), s112 (disposal >50% assets), s113 (amalgamation/merger), s114 (scheme of arrangement), s115 (shareholder approval — 75% special resolution, 15% court review trigger), s118 (TRP application — regulated companies), s123 (mandatory offer — 35%), s124 (squeeze-out — 90%/4 months), s126 (frustrating action restrictions), s164 (appraisal rights) | Annual return deadlines, filing fee tiers by turnover |
| Companies Regulations 2011 | `companies-regulations.yaml` | Reg 43 (social & ethics committee prescribed functions), Reg 81-88 (TRP definitions, acting in concert, change of control, mandatory offer mechanics), Reg 106-110 (offer timetables, independent expert opinions — fair & reasonable), Reg 111 (cash confirmation/bank guarantee), TRP filing fees | TRP offer timetables |
| Close Corporations Act 69 of 1984 | `close-corporations.yaml` | s15A (annual returns — anniversary month + 1 month), Reg 16 (filing periods), conversion to company (CoR18.1), member governance, deregistration | Annual return anniversary month deadlines |

### Existing statute files to extend

| Statute | File | Sections to ADD |
|---|---|---|
| Competition Act 89 of 1998 | `competition.yaml` | Filing fees (R165k intermediate, R550k large), investigation timelines (20 BD intermediate, 40 BD large with 15 BD extensions), public interest factors s12A(3) (employment, B-BBEE ownership spread, SMME impact, industrial sector/region), small merger notification guidelines (revised Dec 2022) |
| B-BBEE Act 53 of 2003 | `bbbee.yaml` | Ownership element scoring for M&A transactions, equity equivalents, Mining Charter BEE shareholding requirements (26% existing / 30% new applicants), Competition Commission "greater spread of ownership" requirement |

### Existing statute files — no changes needed

| Statute | File | Reason |
|---|---|---|
| FICA 38 of 2001 | `fica.yaml` | Beneficial ownership (s21B) and CDD sections already sufficient for M&A diligence |

### Key thresholds

| Threshold | Value | Source |
|---|---|---|
| Mandatory offer trigger | 35% of voting securities | Companies Act s123 |
| Squeeze-out | 90% acceptance within 4 months | Companies Act s124 |
| Shareholder approval (fundamental transactions) | 75% special resolution | Companies Act s115 |
| Court review trigger | 15% of voting rights exercised opposed | Companies Act s115(3) |
| Asset disposal threshold | >50% of gross assets or undertaking | Companies Act s112 |
| Competition — intermediate merger | Combined R600m + target R100m | GN 1254, GG 41245 (Oct 2017) |
| Competition — large merger | Combined R6.6b + target R190m | GN 1254, GG 41245 (Oct 2017) |
| Competition filing fee — intermediate | R165,000 | Competition Commission |
| Competition filing fee — large | R550,000 | Competition Commission |
| Competition investigation — intermediate | 20 BD (ext. once to 40 BD) | Competition Act s14(1) |
| Competition investigation — large | 40 BD (ext. 15 BD per extension) | Competition Act s14A(1) |
| Annual returns deadline (companies) | 30 business days after anniversary date | Companies Act s33 |
| Annual returns deadline (CCs) | Anniversary month + 1 month | CC Act s15A |
| CIPC deregistration trigger | 2 successive years non-filing | Companies Act s82(3) |
| Break fee cap (TRP) | 1% of total transaction value | TRP Guideline 1/2013 |
| Mining Charter BEE shareholding | 26% existing / 30% new applicant | Mining Charter 2018 |

---

## 3. Skill Divergence Matrix

| # | Skill | Divergence | In scope | Reasoning |
|---|---|---|---|---|
| 1 | ai-tool-handoff | LOW | N | Infrastructure — tool handoff logic is jurisdiction-neutral |
| 2 | board-minutes | HIGH | Y | SA board governance: Companies Act s73, King IV, mandatory social & ethics committee (s72(4)), MOI-specific requirements |
| 3 | closing-checklist | HIGH | Y | US assumes HSR; SA needs Competition Commission, TRP compliance certificate, CIPC filings, B-BBEE conditions |
| 4 | cold-start-interview | HIGH | Y | Public Company module references SEC §16 / Form 4 / filer status; Entity module references Delaware franchise tax |
| 5 | customize | LOW | N | Infrastructure — edits whatever sections exist in the profile |
| 6 | deal-team-summary | LOW | N | Summarization skill — content jurisdiction depends on underlying diligence |
| 7 | diligence-issue-extraction | HIGH | Y | SA diligence categories: B-BBEE, Competition Act, TRP, s112-116, POPIA, LRA s197, NEMA |
| 8 | entity-compliance | HIGH | Y | Most jurisdiction-specific. Every deadline, fee, entity type is US-state-centric. SA needs CIPC, beneficial ownership, CC Act |
| 9 | integration-management | MEDIUM | Y | Process portable but SA-specific: LRA s197, B-BBEE re-scoring, CIPC CoR amendments, Competition condition monitoring |
| 10 | material-contract-schedule | MEDIUM | Y | Mechanics universal but SA PAs define materiality differently — s112, B-BBEE, SA regulatory categories |
| 11 | matter-workspace | LOW | N | Pure infrastructure — file management jurisdiction-neutral |
| 12 | tabular-review | LOW | N | Schema-driven extraction — framework jurisdiction-neutral |
| 13 | written-consent | HIGH | Y | SA consent: s74 round-robin, s60 shareholder resolutions, MOI restrictions, statutory committee differences |

---

## 4. Topic Overlay Map

### Topic files

| Topic file | Skills served | Key content areas |
|---|---|---|
| `fundamental-transactions.md` | closing-checklist, diligence-issue-extraction, integration-management, material-contract-schedule | Companies Act s112-116 (disposal of assets, amalgamation/merger, scheme of arrangement), shareholder approval (s115, 75% special resolution), 15% court review trigger (s115(3)), appraisal rights (s164), Competition Commission merger notification & timelines, B-BBEE conditions precedent, LRA s197 automatic employee transfer, solvency & liquidity test (s4), creditor objection window (15 BD), SA-specific conditions precedent checklist |
| `takeover-regulation.md` | closing-checklist, diligence-issue-extraction | TRP authority (s119) & regulated companies (s118 — public, SOC, qualifying private), affected transactions (s117), mandatory offer (35% threshold, s123, 1 BD notice), squeeze-out (90%/4 months, s124), acting in concert (Reg 84, Form TRP 84), frustrating action restrictions (s126 — poison pills prohibited), disclosure thresholds (5%/10%/15%, s122), independent expert opinions (fair & reasonable), offer timetables, TRP compliance certificate, break fee cap (1%), cash offer must be fully funded (Reg 111), 12-month cooling-off after failed offer |
| `board-governance.md` | board-minutes, written-consent | Board authority (s66), meetings (s73 — notice, quorum, voting), round-robin resolutions (s74), shareholder resolutions without meeting (s60), director duties & conflicts (s75 — declaration at each meeting, interested director cannot vote), directors' conduct (s76 — good faith, proper purpose, best interests, care/skill/diligence), business judgment rule (s76(4) — informed, no conflict, rational basis), director liability (s77 — joint and several), audit committee (s94 — mandatory for public/SOC/high-PI-score companies), social & ethics committee (s72(4) + Reg 43 — mandatory for public/SOC/>500 PI score), King IV "apply and explain" (mandatory for JSE-listed via Listings Requirements), MOI as governing document (replaces bylaws/charter), committee structures |
| `entity-compliance-cipc.md` | entity-compliance | CIPC annual returns (s33, 30 BD after anniversary), beneficial ownership declarations (mandatory since July 2024, hard stop — cannot file AR without BO), AFS/FAS filing (audited for public; reviewed or FAS for private per Reg 28/29), close corporation filing (CC Act s15A, anniversary month + 1 month), SA entity types (Pty Ltd private, Ltd public, SOC state-owned, NPC non-profit, personal liability Inc, close corporation CC), deregistration (s82 — 2 successive years, ~800k entities deregistered Jan-Feb 2025), reinstatement (CoR40.5 — evidence of economic activity, 30 BD to file all outstanding), filing fee tiers by turnover, CoR amendment forms (director changes, registered address, etc.), beneficial ownership register (General Laws Amendment Act 22 of 2022), public interest score calculation |
| `diligence-sa.md` | diligence-issue-extraction, material-contract-schedule, integration-management | SA-specific diligence request categories, regulatory compliance (B-BBEE scorecard verification, POPIA data transfer assessment, NEMA environmental authorisations, Competition Act pre-notification analysis, exchange control/SARB for cross-border, MPRDA mining rights change-of-control, FSRA for financial institutions — Prudential Authority 15% threshold), SA contract law conventions (conventional penalties — Act 15/1962, restraint of trade — *Basson v Chilwan* reasonableness factors), SA materiality framing in purchase agreements (s112 >50% assets definition, B-BBEE thresholds), post-close integration items (CIPC CoR filings, B-BBEE re-scoring, IP recordals at CIPC, LRA s197 employee transfer compliance, Competition condition monitoring) |

### Skill-to-topic-and-statute routing

| Skill | Topics | Statutes |
|---|---|---|
| board-minutes | board-governance | companies-act, companies-regulations |
| closing-checklist | fundamental-transactions, takeover-regulation | companies-act, companies-regulations, competition |
| cold-start-interview | _(no topics)_ | companies-act, companies-regulations, competition, bbbee, close-corporations |
| diligence-issue-extraction | fundamental-transactions, takeover-regulation, diligence-sa | companies-act, competition, bbbee, popia |
| entity-compliance | entity-compliance-cipc | companies-act, close-corporations |
| integration-management | fundamental-transactions, diligence-sa | companies-act, competition, bbbee, lra |
| material-contract-schedule | fundamental-transactions, diligence-sa | companies-act, competition |
| written-consent | board-governance | companies-act, companies-regulations |

---

## 5. Practice Profile Template Design

### Sections unchanged (jurisdiction-neutral infrastructure)

- Configuration location block
- Quiet mode for client-facing deliverables
- Available integrations table
- Reviewer note format
- Next steps decision tree
- Dashboard offer for data-heavy outputs
- Decision posture on subjective legal calls
- Shared guardrails (no silent supplement, currency trigger, verify user-stated facts, source tags, destination check, cross-skill severity floor, file access failures, verification log)
- Scaffolding, not blinders
- Ad-hoc questions in this domain
- Proportionality
- Retrieved-content trust
- Large input / Large output
- Matter workspaces structure

### Sections replaced (US → SA)

| US section | ZA replacement | Rationale |
|---|---|---|
| Work-product header — "ATTORNEY WORK PRODUCT" (FRCP 26(b)(3)) with EU/UK caveats | SA legal professional privilege header with AI caveat | SA has no "attorney work product" doctrine. Two forms: legal advice privilege + litigation privilege. In-house counsel: commercial vs. legal capacity distinction. AI output not automatically privileged. |
| Jurisdiction recognition — "default frameworks are often US-centric" | SA-first with non-SA detection | SA is home jurisdiction, not the exception |

### Work-product header formulation

**For lawyers (in-house or firm):**

> `PRIVILEGED & CONFIDENTIAL — PREPARED FOR THE PURPOSE OF OBTAINING OR GIVING LEGAL ADVICE`
>
> `[Note: (1) SA legal professional privilege attaches to communications made for the dominant purpose of obtaining or giving legal advice (Thint v NDPP). Privilege must be claimed — it is not automatic. (2) In-house counsel: privilege applies only when acting in a legal advisory capacity, not a commercial or executive role (Mohamed v President of SA). (3) This document was generated with AI assistance. AI-generated output is not automatically privileged — privilege attaches only once a qualified legal adviser has applied professional judgment to verify and adopt the content. Mark as reviewed before relying on the privilege marking.]`

**For non-lawyers:**

> `RESEARCH NOTES — NOT LEGAL ADVICE — REVIEW WITH A LICENSED ATTORNEY, SOLICITOR, BARRISTER, OR OTHER AUTHORISED LEGAL PROFESSIONAL IN YOUR JURISDICTION BEFORE ACTING`

### New sections (SA-specific)

| Section | Content | Referenced by |
|---|---|---|
| Statutory baseline | Companies Act 71 of 2008 as governing statute, Companies Regulations 2011, King IV "apply and explain." Router instruction to load overlays. | All skills |
| Entity landscape | SA entity types (Pty Ltd, Ltd, SOC, NPC, Inc, CC). How type affects governance, filing, audit. CIPC as registrar. | entity-compliance, cold-start-interview |
| M&A regulatory landscape | Competition Commission (intermediate/large thresholds), TRP for affected transactions, B-BBEE conditions, SARB exchange control for cross-border. Which bodies must approve before closing. | closing-checklist, diligence-issue-extraction, integration-management |
| Board governance framework | Companies Act s66-78, s94, s72(4). King IV principles. MOI as governing document (replaces bylaws). | board-minutes, written-consent |
| B-BBEE and ownership | B-BBEE scoring in M&A (ownership element, equity equivalents), diligence (certificate verification), integration (re-scoring). Fronting risk. Mining Charter minimums. Competition Commission "greater spread of ownership." | diligence-issue-extraction, closing-checklist, integration-management |
| Escalation | CIPC (entity), Competition Commission / Tribunal (merger control), TRP (affected transactions), Companies Tribunal (disputes), Labour Court (s197), JSE (listed), external corporate counsel. | All skills |

### Seed documents

| Document | Purpose | Module |
|---|---|---|
| Prior board minutes (1-2 examples) | Learn house minutes format, resolution language, discussion depth | Board & Secretary |
| Prior written consent | Learn consent format, recital depth, resolution language | Board & Secretary |
| Prior M&A issues memo | Learn finding format, severity scheme, category structure | M&A |
| Diligence request list | Seed request categories for extraction | M&A |
| Entity org chart or subsidiary register | Seed entity table, company types, jurisdictions | Entity Management |
| CIPC company search printout | Confirm entity details, registration numbers, director details | Entity Management |
| MOI (Memorandum of Incorporation) | Governance provisions, share capital, board powers | Board & Secretary, M&A |

---

## 6. Cold-Start Interview Questions

### Must-have (8)

| # | Question | Anchors | Module |
|---|---|---|---|
| 1 | What type of company is this, and is it JSE-listed? (Pty Ltd / Ltd / SOC / NPC / Inc + JSE Main Board / AltX / unlisted) | Governance tier, audit obligations, CIPC filing fees, King IV, TRP-regulated status, public company module | All |
| 2 | Is the MOI standard (Table 1 — CoR15.1A/B) or customised? Any non-standard governance provisions? (entrenched provisions, special voting thresholds, restrictions on board consent, pre-emptive rights) | Board-minutes, written-consent: MOI permissions/restrictions. Closing-checklist: shareholder approval mechanics. | Board, M&A |
| 3 | What is the company's current B-BBEE level and applicable sector code? (Level 1-8 / non-compliant / exempt EME/QSE + generic or sector-specific) | M&A diligence, integration re-scoring, closing conditions | M&A, Integration |
| 4 | What is the typical deal size relative to Competition Act merger thresholds? (Below lower — small / Intermediate: combined R600m+ and target R100m+ / Large: combined R6.6b+ and target R190m+) | Closing-checklist: Competition Commission notification route, fees, timelines | M&A |
| 5 | Do deals typically involve a cross-border element requiring SARB exchange control approval? (Yes — inbound / outbound / both / No / Occasionally) | Closing-checklist: SARB condition precedent. Diligence: exchange control compliance. | M&A |
| 6 | Is a social & ethics committee in place? (Required under s72(4) + Reg 43 / Exempted / Voluntarily established / Not in place) | Board-minutes: committee coverage. Board governance overlay. | Board |
| 7 | What does the entity portfolio look like? (Number of entities, types — Pty Ltd / CC / Ltd / NPC / external company, CIPC compliance status — all current / some overdue / unknown) | Entity-compliance: filing calendar, entity types, baseline compliance | Entity Management |
| 8 | How are board resolutions typically passed outside of meetings? (s74 round-robin written resolutions routinely used / Occasionally / Not used — MOI restricts / Don't know) | Written-consent skill: default approach, MOI constraints | Board |

### Nice-to-have (4)

| # | Question | Anchors |
|---|---|---|
| 9 | Is the company TRP-regulated? (For private companies: have 10%+ shares transferred between unrelated parties in 24 months? Note: threshold changing under 2024 amendments — not yet in force) | Takeover regulation topic |
| 10 | Is a company secretary appointed? (Mandatory for public companies per s86; recommended by King IV) | Board governance — statutory records |
| 11 | Who is the auditor / audit firm? | Board module — audit committee, AFS |
| 12 | Does the company apply King IV? (Mandatory — JSE-listed/SOC / Voluntarily / Not applied) | Governance framework |

---

## 7. High-Risk Flag Table

| # | Flag | Why high-risk | What to check | Statute |
|---|---|---|---|---|
| 1 | Mandatory offer trigger (35%) | Acquiring 35%+ of voting securities triggers mandatory offer to all remaining shareholders within 1 business day. Concert party holdings aggregated. Failure = TRP can compel via court. | Acquirer + concert party aggregate pre/post. Waiver by >50% independent shareholders. Non-voting preference share carve-out. | Companies Act s123; Reg 86 |
| 2 | TRP compliance certificate missing | Affected transactions involving regulated companies cannot be implemented without TRP compliance certificate. Implementation without it is void. | Is target regulated? (Public, SOC, private with >10% transfers in 24 months or MOI opt-in). If yes → hard condition precedent. | Companies Act s119(4); s118 |
| 3 | Competition Commission gun-jumping | Intermediate/large mergers cannot be implemented before approval. Penalty: up to 10% annual turnover + potential unwinding. Suspensory regime. | Combined turnover/assets vs thresholds. Small mergers can be called in within 6 months post-implementation. | Competition Act s13, s13A, s59 |
| 4 | Solvency and liquidity test not applied | Boards must apply s4 test before distributions (s46), share buybacks (s48), financial assistance (s44/45), mergers (s113). Failure = director personal liability under s77. | Board resolution records s4 application. Both limbs: (1) assets > liabilities, (2) can pay debts as due in next 12 months. | Companies Act s4, s46, s77 |
| 5 | B-BBEE ownership dilution | Transaction reducing B-BBEE ownership below required levels. Mining: 26%/30% minimum or risk mining rights suspension. Government contracts: loss of supplier status. Competition authorities impose B-BBEE conditions. | Target's certificate and ownership element. Replacement BEE shareholder if exiting. Sector code minimums. Competition Commission "greater spread of ownership." | B-BBEE Act s10; Mining Charter |
| 6 | CIPC deregistration of target/subsidiary | Entity deregistered for non-compliance with annual returns or beneficial ownership. Ceases to exist — bank accounts frozen, directors personally liable. ~800k entities deregistered Jan-Feb 2025 bulk action. | CIPC status check all group entities. Annual returns current? BO declarations filed? Status "in business"? | Companies Act s33, s82; GLA Act 22/2022 |
| 7 | Director personal financial interest undisclosed (s75) | Must declare at each meeting. Failure invalidates board resolution + personal liability (s77). Critical for M&A board approvals, related-party transactions. | Board minutes for s75 declarations. Interested director cannot vote. Director on both acquirer + target boards = presumed non-independent under Takeover Regs. | Companies Act s75, s77 |
| 8 | Shareholder appraisal rights / court review | Dissenting shareholders can demand fair value (s164). If ≥15% vote against → within 5 BD any dissenting shareholder can require court approval. Within 10 BD any dissenter can apply for court leave for review (regardless of %). *Marble Head*: 10 BD deadline can be condoned. | Model expected dissent %. Appraisal rights cap as CP. ≥15% triggers court review. Court sets aside only if manifestly unfair or materially tainted. | Companies Act s164, s115(3) |
| 9 | Frustrating action by target board | s126 prohibits target board from issuing shares, granting options, disposing material assets, entering non-ordinary-course contracts, making abnormal distributions — without TRP + shareholder consent. Poison pills effectively prohibited. | All board actions during offer period vs s126 list. Pre-existing obligation defence. | Companies Act s126 |
| 10 | Acting in concert — inadvertent aggregation | Concert party holdings aggregated for 35% threshold. Collaboration on board strategy may trigger mandatory offer. One additional share after crossing 35% triggers offer. Form TRP 84 disclosure required. | Map all related/concert party relationships. Collaborative engagement → concert party status? | Companies Act s117; Reg 84 |
| 11 | Exchange control (SARB) approval missing | Cross-border transactions require Financial Surveillance Dept (SARB) approval via authorised dealer. Proceeding without = violation of Exchange Control Regulations. | Any cross-border capital flow: foreign acquirer, offshore consideration, foreign subsidiaries, loop structures. | Exchange Control Regulations |
| 12 | Competition public interest conditions | Employment impact, B-BBEE ownership spread, SMME impact, industrial sector/region — all grounds for conditions or prohibition. "Greater spread of ownership" interpreted as requiring positive effect — neutral/negative requires remedy (ESOP, HDP share disposal). | Public interest submission. Employment impact model. B-BBEE ownership plan. Sector-specific regulator approvals. | Competition Act s12A(3) |
| 13 | Creditor objection to statutory merger | Within 15 BD of merger notice, creditor may seek court leave to review on material prejudice grounds. Can delay implementation. | Identify materially prejudiced creditors. Check loan covenant CoC triggers. Solvency certificate for creditor protection. | Companies Act s116(6) |
| 14 | Companies Amendment Act 2024 — pending TRP threshold changes | New s118(1)(c)(i): private company TRP regulation changes from ">10% shares transferred in 24 months" to "10+ shareholders AND Minister-determined financial threshold." NOT YET IN EFFECT (assented July 2024, gazetted 30 July 2024, thresholds not yet set). | Check if new thresholds in force at transaction time. Build flexibility for threshold changes if structuring now for future closing. | Companies Amendment Act 16 of 2024 |

---

## 8. Eval Case Outlines

### board-minutes (3 cases)

**Case 1 — Routine quarterly board meeting.** Standard resolutions: officer appointment, AFS approval, dividend declaration. Expected: s75 conflict declarations, solvency & liquidity test for distribution, quorum per MOI. Must NOT contain: Robert's Rules, DGCL, "bylaws."

**Case 2 — Fundamental transaction board approval.** Disposal of >50% subsidiary assets triggers s112, holding company shareholder approval under s115(2)(b). Expected: s112 threshold, s115 shareholder approval, s75 conflicts, holding company resolution. Must NOT contain: "authorized under bylaws," HSR.

**Case 3 — Social & ethics committee meeting.** Reports on B-BBEE, employment equity, environmental compliance. Expected: s72(4), King IV, Reg 43 prescribed functions. Must NOT contain: "compensation committee" (should be "remuneration committee"), SEC references.

### closing-checklist (3 cases)

**Case 1 — Private company intermediate merger.** Combined R800m, target R150m. Target not TRP-regulated. Expected: Competition Commission notification, 20 BD timeline, R165k fee, solvency test, no TRP certificate. Must NOT contain: HSR, FTC, state AG.

**Case 2 — Public company scheme of arrangement.** TRP-regulated, large merger, cross-border acquirer. Expected: TRP compliance certificate, large merger (40 BD + Tribunal), SARB approval, 75% shareholder approval, appraisal rights, independent expert. Must NOT contain: SEC, CFIUS, Delaware appraisal.

**Case 3 — Mandatory offer trigger.** Acquirer crosses 35% via share purchase + concert party aggregation. Expected: mandatory offer within 1 BD, Form TRP 84, cash confirmation, 6-month price parity. Must NOT contain: Williams Act, Schedule 14D-9.

### cold-start-interview (3 cases)

**Case 1 — JSE-listed in-house counsel, all 4 modules.** Expected: King IV mandatory, social & ethics committee, TRP-regulated, CIPC annual returns, JSE Listings Requirements. Must NOT contain: SEC filer status, Delaware franchise tax, NYSE/Nasdaq.

**Case 2 — Private Pty Ltd, M&A + Entity, 3 subsidiaries (2 Pty Ltd + 1 CC).** Expected: CIPC filing calendar for Pty Ltd + CC, Competition thresholds, B-BBEE scoring. Must NOT contain: public company references, §16 reporting.

**Case 3 — Law firm (Inc), Board + Entity, multi-client.** Expected: matter workspaces enabled, personal liability company, conflicts management. Must NOT contain: in-house counsel references, single-company assumptions.

### diligence-issue-extraction (3 cases)

**Case 1 — Employment contracts and property leases, 200 employees.** Expected: LRA s197 automatic transfer, restraint of trade (SA common law), BCEA conditions. Must NOT contain: WARN Act, COBRA, at-will, FLSA.

**Case 2 — B-BBEE Level 4, mining rights, environmental authorisations, foreign acquirer.** Expected: B-BBEE dilution risk, MPRDA change-of-control, NEMA transfer, SARB exchange control. Must NOT contain: EPA, OSHA (US), CERCLA.

**Case 3 — Government contracts with B-BBEE requirements and CoC clauses.** Expected: government B-BBEE minimum, CoC consent, Competition public interest, preferential procurement. Must NOT contain: FAR/DFARS, SBA.

### entity-compliance (3 cases)

**Case 1 — 5 Pty Ltd + 2 CCs, one CC 2 years overdue.** Expected: CC deregistration risk, beneficial ownership for all, CC conversion option (CoR18.1). Must NOT contain: Delaware franchise tax, state annual report, CT Corp.

**Case 2 — Public company (Ltd), 12 subsidiaries, health audit.** Expected: CIPC annual returns for all 13, audited AFS, beneficial ownership, 30 BD deadline, public interest score. Must NOT contain: state-by-state filing, franchise tax methods.

**Case 3 — Entity deregistered in Jan 2025 bulk action, reinstatement needed.** Expected: CoR40.5 application, evidence of economic activity, 30 BD to file all outstanding. Must NOT contain: dissolution/revival under state corporation law.

### written-consent (3 cases)

**Case 1 — Routine: officer appointment + auditor.** Expected: s74 round-robin, MOI restriction check. Must NOT contain: DGCL §141(f), unanimous consent requirement.

**Case 2 — Financial assistance to subsidiary (s45), director conflict.** Expected: s45, s4 solvency test, s75 conflict (interested director cannot sign). Must NOT contain: upstream guarantee under state law.

**Case 3 — M&A transaction approval, major action.** Expected: major action flag, s75 all directors, solvency test, s112/s113/s114 trigger check. Must NOT contain: "authorized under charter and bylaws."

### integration-management (3 cases)

**Case 1 — 150 employees transferring under s197, B-BBEE re-scoring.** Expected: s197 automatic transfer (terms preserved), B-BBEE re-scoring, CIPC CoR amendments. Must NOT contain: WARN Act, COBRA, I-9.

**Case 2 — Competition condition: no retrenchments for 3 years.** Expected: condition monitoring, moratorium tracking, reporting to Competition Commission. Must NOT contain: FTC consent decree, DOJ remedies.

**Case 3 — IP portfolio integration, CIPC recordals.** Expected: trademark/patent/design assignment recordals at CIPC. Must NOT contain: USPTO assignment, TTAB.

### material-contract-schedule (3 cases)

**Case 1 — PA defines Material Contract as >R5m or government contract or CoC.** Expected: mechanical application, government B-BBEE flag, CoC consent flag. Must NOT contain: dollar thresholds, federal contract novation.

**Case 2 — Restraint of trade + conventional penalties clauses.** Expected: SA common law reasonableness (*Basson v Chilwan*), Conventional Penalties Act 15/1962. Must NOT contain: non-compete by state, liquidated damages (US).

**Case 3 — Government supply contracts with B-BBEE requirements.** Expected: preferential procurement, B-BBEE certificate requirements, cancellation risk. Must NOT contain: FAR/DFARS, SBA set-aside, Buy American.

### Practice-area-specific validation rules

1. No US corporate law concepts in ZA outputs (DGCL, Delaware bylaws, HSR, SEC §16, WARN, COBRA, at-will, state franchise tax, Robert's Rules, US case law)
2. MOI not bylaws — SA companies governed by Memorandum of Incorporation
3. B-BBEE context — every M&A output touching SA must consider B-BBEE implications
4. TRP-regulated check — every fundamental transaction must verify regulated company status
5. Solvency and liquidity test — every distribution, financial assistance, or merger must reference s4

### Expert review gate

Before release, an SA corporate law practitioner reviews:
- Statute YAML values against current Companies Act (including 2024 amendments status)
- Competition Act thresholds against current Government Gazette
- Topic overlay procedures against current TRP practice and guidelines
- High-risk flag table against current deal practice and recent case law
- B-BBEE scoring and sector code accuracy against current Codes of Good Practice
- Entity compliance procedures against current CIPC practice notes (rapidly evolving)

---

## 9. Source Provenance Log

| Item | Source | Tag |
|---|---|---|
| SA legal professional privilege framework | Baker McKenzie Global Privilege Guide (SA chapter), *Thint v NDPP*, *Mohamed v President of SA*, *Ibex RSA Holdco v Tiso Blackstar* | [Perplexity — verify] |
| AI output not automatically privileged | Baker McKenzie Global Privilege Guide (SA chapter, Section 07 — AI) | [Perplexity — verify] |
| Companies Act Chapter 5 structure (ss112-127) | SAFLII consolidated act, gov.za gazette, BRICS Law Journal (2020) | [Perplexity — verify] |
| Mandatory offer 35% threshold | Companies Act s123, CMS Expert Guide, Chambers Corporate M&A 2025/2026 | [Perplexity — verify] |
| Competition Act merger thresholds | Competition Commission website (compcom.co.za), SAFLII consolidated regulations | [Perplexity — verify] |
| Competition filing fees (R165k/R550k) | Competition Commission website, Webber Wentzel quick facts | [Perplexity — verify] |
| Competition investigation timelines | Competition Act s14(1), s14A(1), Competition Commission filing guidelines | [Perplexity — verify] |
| CIPC annual returns and deregistration | CIPC FAQ, Practice Note 1/2025, Media Statement 1/2025, CIPC website | [Perplexity — verify] |
| Beneficial ownership since July 2024 | CIPC Beneficial Ownership page, General Laws Amendment Act 22/2022 | [Perplexity — verify] |
| ~800k entities deregistered Jan-Feb 2025 | CIPC Practice Note, ghostmail.co.za (2025 corporate law review) | [Perplexity — verify] |
| Directors' duties and business judgment rule | Werksmans analysis, CMS expert guide, multiple academic sources | [Perplexity — verify] |
| s115(3) court review — 15% threshold | Companies Act s115(3), FluidRock analysis, *Capital Appreciation v FNN* (SCA), Cliffe Dekker Hofmeyr alert | [Perplexity — verify] |
| s126 frustrating action restrictions | Companies Act s126, Lawtons Africa analysis, CMS Expert Guide, Chambers M&A 2025 | [Perplexity — verify] |
| Companies Amendment Act 2024 — TRP threshold changes | Act 16 of 2024 (gazetted 30 July 2024), Polity.org.za analysis, Bowmans insight, Webber Wentzel brochure, Spencer West analysis | [Perplexity — verify] |
| TRP threshold section NOT YET IN EFFECT | Webber Wentzel (March 2025), Bowmans (March 2025) — Minister has not set financial thresholds | [Perplexity — verify] |
| Break fee cap 1% | CMS Expert Guide, TRP Guideline 1/2013 | [Perplexity — verify] |
| King IV and JSE Listings Requirements | UKZN thesis, Chambers M&A guides, Baker McKenzie guide | [Perplexity — verify] |
| Close Corporations Act annual returns | CIPC FAQ, Information Guide | [Perplexity — verify] |
| B-BBEE in M&A context | Baker McKenzie Global Private M&A Guide, Chambers M&A 2025/2026 | [Perplexity — verify] |
| Mining Charter BEE shareholding (26%/30%) | Baker McKenzie guides, Chambers M&A 2025 | [Perplexity — verify] |
| PwC Statutory Merger Guide SA | PwC publication | [Perplexity — verify] |
