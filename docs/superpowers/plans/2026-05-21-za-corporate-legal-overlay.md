# ZA Corporate-Legal Overlay Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Adapt the corporate-legal plugin for South African law via additive overlays in `jurisdictions/za/corporate-legal/`, following the same architecture as the employment-legal reference implementation.

**Architecture:** Router-based skill wiring. 3 new statute YAML files + 2 extended existing files provide structured legal data. 5 topic overlay markdown files provide procedural guidance. A practice profile template replaces US-specific sections. The cold-start interview forks after Part 0 for ZA-specific onboarding. Validation scripts and 24 eval cases ensure correctness.

**Tech Stack:** YAML (statutes, evals, router), Markdown (topics, practice profile, cold-start fork), Python 3 (validators)

**Spec:** `docs/superpowers/specs/2026-05-21-za-corporate-legal-expansion.md`
**Reference implementation:** `jurisdictions/za/employment-legal/`

---

## File Map

### New files to create

```
jurisdictions/za/corporate-legal/
├── router.md                          # Maps 8 skills → topics + statutes
├── practice-profile-template.md       # ZA variant of corporate-legal/CLAUDE.md
└── topics/
    ├── fundamental-transactions.md    # Companies Act ss112-116, Competition Act, s197
    ├── takeover-regulation.md         # TRP, mandatory offer, squeeze-out, s126
    ├── board-governance.md            # Directors' duties, meetings, consents, King IV
    ├── entity-compliance-cipc.md      # CIPC annual returns, BO, deregistration
    └── diligence-sa.md               # SA diligence categories, B-BBEE, regulatory

jurisdictions/za/statutes/
├── companies-act.yaml                 # Companies Act 71 of 2008 (NEW)
├── companies-regulations.yaml         # Companies Regulations 2011 (NEW)
└── close-corporations.yaml            # Close Corporations Act 69 of 1984 (NEW)

jurisdictions/za/evals/corporate-legal/
├── board-minutes/
│   ├── case-01-routine-quarterly.yaml
│   ├── case-02-fundamental-transaction-approval.yaml
│   └── case-03-social-ethics-committee.yaml
├── closing-checklist/
│   ├── case-01-intermediate-merger-private.yaml
│   ├── case-02-scheme-of-arrangement-public.yaml
│   └── case-03-mandatory-offer-trigger.yaml
├── cold-start-interview/
│   ├── case-01-jse-listed-all-modules.yaml
│   ├── case-02-private-pty-serial-acquirer.yaml
│   └── case-03-law-firm-multi-client.yaml
├── diligence-issue-extraction/
│   ├── case-01-employment-contracts-s197.yaml
│   ├── case-02-bbbee-mining-rights.yaml
│   └── case-03-government-contracts.yaml
├── entity-compliance/
│   ├── case-01-pty-ltd-cc-mix-overdue.yaml
│   ├── case-02-public-company-health-audit.yaml
│   └── case-03-deregistered-entity-reinstatement.yaml
├── written-consent/
│   ├── case-01-routine-officer-appointment.yaml
│   ├── case-02-financial-assistance-s45-conflict.yaml
│   └── case-03-ma-transaction-major-action.yaml
├── integration-management/
│   ├── case-01-s197-transfer-bbbee-rescoring.yaml
│   ├── case-02-competition-employment-condition.yaml
│   └── case-03-ip-portfolio-cipc-recordals.yaml
└── material-contract-schedule/
    ├── case-01-pa-definition-government-coc.yaml
    ├── case-02-restraint-conventional-penalties.yaml
    └── case-03-government-supply-bbbee.yaml
```

### Existing files to modify

```
jurisdictions/za/statutes/competition.yaml    # Add filing fees, timelines, public interest
jurisdictions/za/statutes/bbbee.yaml          # Add M&A ownership scoring, Mining Charter
scripts/validate-za-router.py                 # Add corporate-legal to PRACTICE_AREAS
scripts/validate-za-templates.py              # Add corporate-legal to TEMPLATE_CONFIG
corporate-legal/skills/cold-start-interview/SKILL.md  # Add ZA fork after Part 0
```

---

## Task 1: Companies Act statute file

**Files:**
- Create: `jurisdictions/za/statutes/companies-act.yaml`

- [ ] **Step 1: Write the statute YAML file**

Create `jurisdictions/za/statutes/companies-act.yaml` with the following sections. Use the exact schema from the reference (`jurisdictions/za/statutes/lra.yaml`): top-level fields `statute`, `authority`, `last_confirmed`, `source_url`, `sections`. Each section requires `ref`, `value`, `effective_from`, `effective_until`, `effect`.

```yaml
statute: "Companies Act 71 of 2008"
authority: "Companies and Intellectual Property Commission"
last_confirmed: "2026-05-21"
source_url: "https://www.gov.za/documents/companies-act"
```

Include these sections (key + ref + value summary):

| Key | Ref | Value/threshold |
|---|---|---|
| `solvency_and_liquidity_test` | Companies Act s4 | Both limbs: assets ≥ liabilities AND can pay debts as due in 12 months |
| `annual_returns_deadline` | Companies Act s33, Reg 30 | 30 business days after anniversary date |
| `annual_return_fee_tier_1` | Companies Act Reg 30 | R100 (turnover < R1m, within 30 BD) |
| `annual_return_fee_tier_2` | Companies Act Reg 30 | R450 (R1m–R10m, within 30 BD) |
| `annual_return_fee_tier_3` | Companies Act Reg 30 | R2000 (R10m–R25m, within 30 BD) |
| `annual_return_fee_tier_4` | Companies Act Reg 30 | R3000 (R25m+, within 30 BD) |
| `deregistration_trigger` | Companies Act s82(3) | 2 successive years non-filing |
| `beneficial_ownership_declaration` | Companies Act s56 read with GLA Act 22/2022 | Mandatory with annual returns since July 2024; within 10 BD of incorporation or change |
| `distributions_board_authority` | Companies Act s46 | Board must apply s4 solvency & liquidity test; authorise by resolution |
| `board_authority` | Companies Act s66(1) | Business managed by or under direction of board |
| `board_meetings` | Companies Act s73 | Directors may determine time/place; quorum = majority unless MOI provides otherwise |
| `directors_acting_without_meeting` | Companies Act s74 | Round-robin written resolution; must be signed by majority (or MOI-specified number) |
| `shareholders_acting_without_meeting` | Companies Act s60 | Requires sufficient holders to meet quorum AND resolution threshold |
| `personal_financial_interest_declaration` | Companies Act s75 | Must declare at each meeting; interested director cannot vote; failure invalidates resolution |
| `directors_conduct` | Companies Act s76(3) | Good faith, proper purpose, best interests, care/skill/diligence |
| `business_judgment_rule` | Companies Act s76(4) | Safe harbour if: informed, no conflict (or s75 complied), rational basis for belief |
| `director_liability` | Companies Act s77(2) | Personal liability for breach of fiduciary duty (s75, s76) or other provision; joint and several |
| `audit_committee` | Companies Act s94 | Mandatory for public companies, SOC companies, and companies with PI score > threshold |
| `social_ethics_committee` | Companies Act s72(4), Reg 43 | Mandatory for listed public companies, SOC, and companies with PI score ≥ 500 in any 2 of previous 5 years |
| `disposal_of_assets_threshold` | Companies Act s112 | >50% of gross assets (fairly valued, irrespective of liabilities) or >50% of undertaking (fairly valued) |
| `amalgamation_or_merger` | Companies Act s113 | Transaction combining assets/liabilities of 2+ companies; requires s4 test, special resolution per s115, merger agreement |
| `scheme_of_arrangement` | Companies Act s114 | Arrangement between company and holders of any class of securities; requires special resolution per s115 |
| `shareholder_approval_fundamental` | Companies Act s115(2) | Special resolution: ≥75% of voting rights exercised; quorum ≥25% of all voting rights |
| `court_review_trigger` | Companies Act s115(3) | If ≥15% of voting rights exercised opposed AND within 5 BD any dissenter requires court approval; or within 10 BD any dissenter gets court leave |
| `mandatory_offer_threshold` | Companies Act s123 | 35% of voting securities (alone or with concert parties); notice to remaining shareholders within 1 BD |
| `squeeze_out_threshold` | Companies Act s124 | 90% acceptance within 4 months of offer opening; compulsory acquisition within next 2 months |
| `frustrating_action_restrictions` | Companies Act s126 | Board must not issue shares, grant options, dispose material assets, enter non-ordinary contracts, make abnormal distributions without TRP + shareholder approval |
| `appraisal_rights` | Companies Act s164 | Dissenting shareholders who voted against fundamental transaction may demand fair value |
| `regulated_company_private` | Companies Act s118(1)(c)(i) | Private company with >10% shares transferred between unrelated persons in 24 months (NOTE: threshold changing under 2024 amendments — not yet in force) |

- [ ] **Step 2: Run statute validator**

```bash
python3 scripts/validate-za-statutes.py 2>&1 | grep -E "companies-act|FAIL"
```

Expected: `OK: jurisdictions/za/statutes/companies-act.yaml (N sections)`

- [ ] **Step 3: Commit**

```bash
git add jurisdictions/za/statutes/companies-act.yaml
git commit -m "feat(za): add Companies Act 71 of 2008 statute file for corporate-legal"
```

---

## Task 2: Companies Regulations and Close Corporations statute files

**Files:**
- Create: `jurisdictions/za/statutes/companies-regulations.yaml`
- Create: `jurisdictions/za/statutes/close-corporations.yaml`

- [ ] **Step 1: Write companies-regulations.yaml**

```yaml
statute: "Companies Regulations, 2011"
authority: "Department of Trade, Industry and Competition"
last_confirmed: "2026-05-21"
source_url: "https://www.gov.za/sites/default/files/gcis_document/201409/34239rg9526gon351.pdf"
```

Sections to include:

| Key | Ref | Value |
|---|---|---|
| `social_ethics_committee_functions` | Reg 43(5) | Monitor: social/economic development, good corporate citizenship, environment/health/safety, consumer relationships, labour/employment |
| `acting_in_concert` | Reg 84 | Persons who cooperate to obtain/consolidate control; Form TRP 84 disclosure required |
| `mandatory_offer_mechanics` | Reg 86 | Offer within 1 BD of crossing 35%; cash at highest price paid in previous 6 months; bank guarantee or escrow required |
| `change_of_control_pyramids` | Reg 85 (read with s112) | Change of control in pyramid triggers offer to holders of subsidiary regulated company |
| `independent_expert_opinion` | Reg 110 | Independent board must obtain opinion on whether offer is fair and reasonable; split opinion if one but not both |
| `offer_timetable` | Reg 102 | Offer must remain open for minimum 30 business days from posting |
| `break_fee_cap` | TRP Guideline 1/2013 | Break fees may not exceed 1% of total offer value |
| `cash_confirmation` | Reg 111(4) | Cash offer requires irrevocable unconditional bank guarantee or escrow confirmation |
| `trp_filing_fee_listed` | Reg 122 | TRP filing fees for listed companies (schedule in regulations) |
| `trp_filing_fee_unlisted` | Reg 122(4) | Additional R11,400 (VAT incl) for unlisted regulated companies |

- [ ] **Step 2: Write close-corporations.yaml**

```yaml
statute: "Close Corporations Act 69 of 1984"
authority: "Companies and Intellectual Property Commission"
last_confirmed: "2026-05-21"
source_url: "https://www.cipc.co.za/?page_id=2721"
```

Sections to include:

| Key | Ref | Value |
|---|---|---|
| `annual_return_deadline` | CC Act s15A, Reg 16 | From first day of anniversary month up to end of month thereafter |
| `annual_return_fee_under_50m` | CC Act Reg 16 | R100 (within 2 months of anniversary); R150 penalty per late lodgment |
| `annual_return_fee_over_50m` | CC Act Reg 16 | R4000 (within 2 months); R150 penalty |
| `conversion_to_company` | CC Act read with Companies Act | Form CoR18.1; no annual return obligation if conversion received before anniversary month |
| `member_governance` | CC Act s46 | Members' agreement governs internal relations; all members have equal say unless agreement provides otherwise |
| `deregistration` | CC Act read with Companies Act s82 | Same deregistration process as companies; CIPC bulk deregistrations apply equally |
| `beneficial_ownership` | CC Act read with GLA Act 22/2022 | Same BO declaration requirements as companies since July 2024 |

- [ ] **Step 3: Run statute validator**

```bash
python3 scripts/validate-za-statutes.py 2>&1 | grep -E "companies-regulations|close-corporations|FAIL"
```

Expected: Both files OK.

- [ ] **Step 4: Commit**

```bash
git add jurisdictions/za/statutes/companies-regulations.yaml jurisdictions/za/statutes/close-corporations.yaml
git commit -m "feat(za): add Companies Regulations 2011 and Close Corporations Act statute files"
```

---

## Task 3: Extend existing competition.yaml and bbbee.yaml

**Files:**
- Modify: `jurisdictions/za/statutes/competition.yaml`
- Modify: `jurisdictions/za/statutes/bbbee.yaml`

- [ ] **Step 1: Add sections to competition.yaml**

Read the existing file first. Append these new sections after the existing entries (the file already has `intermediate_merger_threshold`, `large_merger_threshold`, `horizontal_practices_prohibited`, `vertical_practices_test`, `minimum_resale_price_maintenance`, `administrative_penalty_max`):

| Key | Ref | Value |
|---|---|---|
| `intermediate_merger_filing_fee` | Competition Commission Rules | 165000 (ZAR) |
| `large_merger_filing_fee` | Competition Commission Rules | 550000 (ZAR) |
| `intermediate_investigation_timeline` | Competition Act s14(1) | 20 business days initial; extension once to 40 BD at Commission discretion |
| `large_investigation_timeline` | Competition Act s14A(1) | 40 business days initial; extensions of max 15 BD each with Tribunal consent |
| `public_interest_assessment` | Competition Act s12A(3) | Equal status to competition assessment; factors: employment, ability of SMMEs, ability of firms in specific sector/region, ability to compete internationally, greater spread of ownership |
| `greater_spread_of_ownership` | Competition Act s12A(3)(e) | Commission interprets as requiring positive effect; neutral/negative effect requires remedy (ESOP, HDP disposal) |
| `small_merger_call_in` | Competition Act s13(3) | Commission may require notification within 6 months of implementation if may substantially prevent/lessen competition or cannot be justified on public interest |
| `national_security_review` | Competition Act s18A | Minister may prohibit merger on national security grounds via Gazette notice; Commission/Tribunal cannot approve prohibited merger |

- [ ] **Step 2: Add sections to bbbee.yaml**

Read the existing file. Append these sections after existing entries:

| Key | Ref | Value |
|---|---|---|
| `ownership_element_ma` | B-BBEE Codes, Statement 100 | Ownership element scores: 25% + 1 vote black ownership = maximum ownership points; flow-through principle applies to indirect ownership |
| `equity_equivalents` | B-BBEE Codes, Statement 103 | Multinationals and entities unable to sell equity may use equity equivalent contributions (enterprise/supplier development contributions) |
| `mining_charter_existing` | Mining Charter 2018, clause 2.1 | Existing mining right holders: minimum 26% BEE shareholding for duration of right |
| `mining_charter_new_applicant` | Mining Charter 2018, clause 2.1 | New applicants: minimum 30% BEE shareholding |
| `competition_merger_conditions` | Competition Act s12A(3)(e) read with B-BBEE Act | Competition authorities increasingly impose B-BBEE ownership conditions on mergers; replacement BEE shareholder may be required |

- [ ] **Step 3: Run statute validator**

```bash
python3 scripts/validate-za-statutes.py 2>&1 | grep -E "competition|bbbee|FAIL"
```

Expected: Both files OK with increased section counts.

- [ ] **Step 4: Commit**

```bash
git add jurisdictions/za/statutes/competition.yaml jurisdictions/za/statutes/bbbee.yaml
git commit -m "feat(za): extend competition and B-BBEE statute files for corporate-legal"
```

---

## Task 4: Topic overlay files (5 files)

**Files:**
- Create: `jurisdictions/za/corporate-legal/topics/fundamental-transactions.md`
- Create: `jurisdictions/za/corporate-legal/topics/takeover-regulation.md`
- Create: `jurisdictions/za/corporate-legal/topics/board-governance.md`
- Create: `jurisdictions/za/corporate-legal/topics/entity-compliance-cipc.md`
- Create: `jurisdictions/za/corporate-legal/topics/diligence-sa.md`

Follow the topic file format from the reference: `jurisdictions/za/employment-legal/topics/dismissal.md`. Each file starts with `# [Topic] — South African Framework`, an opening paragraph listing which skills load it, a horizontal rule, then numbered sections with statute references inline.

- [ ] **Step 1: Create topics directory**

```bash
mkdir -p jurisdictions/za/corporate-legal/topics
```

- [ ] **Step 2: Write fundamental-transactions.md**

**Title:** `# Fundamental Transactions — South African Framework`
**Skills served:** closing-checklist, diligence-issue-extraction, integration-management, material-contract-schedule

**Required sections (## headings):**
1. `## 1. Statutory framework` — Companies Act Chapter 5 Part A overview (ss112-116)
2. `## 2. Disposal of all or greater part of assets (s112)` — >50% gross assets or undertaking; special resolution per s115; NOT a scheme/merger — different mechanics
3. `## 3. Amalgamation or merger (s113)` — definition, merger agreement requirements, solvency & liquidity test, automatic vesting of assets/liabilities, creditor notice (15 BD objection window per s116), CIPC filing (notice of merger)
4. `## 4. Scheme of arrangement (s114)` — arrangement between company and holders of any class; special resolution per s115; most common structure for public company acquisitions
5. `## 5. Shareholder approval (s115)` — 75% special resolution; 25% quorum; acquiring party votes excluded; court review if ≥15% opposed (5 BD) or court grants leave (10 BD); court sets aside only if manifestly unfair or materially tainted
6. `## 6. Appraisal rights (s164)` — dissenting shareholders demand fair value; procedural requirements; court determination of fair value if parties disagree
7. `## 7. Competition Commission merger control` — three tiers (small/intermediate/large); thresholds; mandatory notification for intermediate + large; suspensory regime; timelines; filing fees; public interest assessment (s12A(3)); national security review (s18A)
8. `## 8. B-BBEE conditions` — ownership dilution risk; Competition Commission "greater spread of ownership"; replacement BEE shareholder; sector-specific minimums (Mining Charter)
9. `## 9. LRA s197 — automatic employee transfer` — transfer of business as going concern; employees transfer automatically on same terms; no consent required; transferor and transferee jointly liable for 12 months
10. `## 10. SA conditions precedent checklist` — table format mapping each CP to statute, responsible party, timeline, and failure consequence. Include: Competition Commission approval, TRP compliance certificate (if regulated), shareholder approval (s115), exchange control (SARB), solvency & liquidity certificate, creditor notice period, sector-specific approvals (MPRDA, Prudential Authority, FSCA)

**Key references inline:** Companies Act s112-116, s164, s4; Competition Act s11-14A, s12A(3); LRA s197; B-BBEE Act; MPRDA

- [ ] **Step 3: Write takeover-regulation.md**

**Title:** `# Takeover Regulation — South African Framework`
**Skills served:** closing-checklist, diligence-issue-extraction

**Required sections:**
1. `## 1. Regulatory framework` — TRP authority (s119), Companies Act Chapter 5 Parts B & C, Takeover Regulations
2. `## 2. Regulated companies (s118)` — public companies, SOC, qualifying private (>10% transfers in 24 months or MOI opt-in); note 2024 amendment (not yet in force) changing to 10+ shareholders + Minister threshold
3. `## 3. Affected transactions (s117)` — definition, 7 types listed; compliance certificate required before implementation (s119(4))
4. `## 4. Mandatory offer (s123)` — 35% trigger, concert party aggregation, 1 BD notice, cash at highest price in 6 months, bank guarantee/escrow, waiver by >50% independent shareholders, TRP exemption
5. `## 5. Squeeze-out (s124)` — 90% acceptance within 4 months, compulsory acquisition within next 2 months, dissenting shareholder may apply to court within 30 BD
6. `## 6. Acting in concert` — definition, Form TRP 84, inadvertent aggregation risks, collaborative engagement guidance
7. `## 7. Frustrating action restrictions (s126)` — prohibited actions list, TRP + shareholder approval required, pre-existing obligation defence, poison pills effectively prohibited
8. `## 8. Disclosure requirements (s122)` — 5%/10%/15%+ thresholds, 3 BD notification to target, target announces to market
9. `## 9. Independent expert opinion` — fair and reasonable; split opinion; independent board role
10. `## 10. Offer mechanics` — timetable (30 BD minimum open), break fee cap (1%), cash confirmation (Reg 111), 12-month cooling-off, 6-month price parity

**Flag table:** Include the 14 high-risk flags from the spec (section 7) formatted as a reference table with: flag name, trigger, check, statute ref.

- [ ] **Step 4: Write board-governance.md**

**Title:** `# Board Governance — South African Framework`
**Skills served:** board-minutes, written-consent

**Required sections:**
1. `## 1. Board authority and structure` — s66(1), MOI as governing document, unitary board (no supervisory board), King IV apply-and-explain
2. `## 2. Board meetings (s73)` — notice requirements, quorum (majority unless MOI differs), voting (majority unless MOI differs), electronic participation permitted
3. `## 3. Round-robin resolutions (s74)` — directors acting other than at meeting; signed by majority (or MOI number); effective when last required signature obtained; MOI may restrict
4. `## 4. Shareholder resolutions without meeting (s60)` — sufficient holders for quorum AND resolution threshold; MOI may restrict
5. `## 5. Director duties` — s76(3) (good faith, proper purpose, best interests, care/skill/diligence), s76(4) business judgment rule (informed + no conflict + rational), s76(2) (no misuse of position or information)
6. `## 6. Personal financial interests (s75)` — declaration at each meeting; interested director cannot vote; failure invalidates resolution; ongoing duty
7. `## 7. Director liability (s77)` — personal liability for breach of fiduciary duty or other provision; joint and several; s77(2)(a) common law delict; delinquency orders
8. `## 8. Audit committee (s94)` — mandatory for public/SOC/high-PI-score; minimum 3 members; all non-executive; majority independent; prescribed functions
9. `## 9. Social & ethics committee (s72(4), Reg 43)` — mandatory for listed public, SOC, >500 PI score; 2024 amendment: majority must be non-executive directors; prescribed monitoring functions
10. `## 10. King IV governance principles` — apply-and-explain (not comply-or-explain); mandatory for JSE-listed via Listings Requirements; 17 principles; key governance outcomes; recommended practices for board composition, independence, diversity

**Tables:** Include committee comparison table (audit vs social & ethics vs remuneration — when mandatory, composition, functions).

- [ ] **Step 5: Write entity-compliance-cipc.md**

**Title:** `# Entity Compliance — CIPC Framework`
**Skills served:** entity-compliance

**Required sections:**
1. `## 1. CIPC overview` — registrar function, entity types registered
2. `## 2. SA entity types` — table: Pty Ltd (private), Ltd (public), SOC (state-owned), NPC (non-profit), Inc (personal liability), CC (close corporation), external company. For each: governance framework, audit requirements, filing requirements
3. `## 3. Annual returns (s33)` — 30 BD after anniversary; electronic filing only; fee tiers by turnover; late penalties; non-compliance → deregistration
4. `## 4. Beneficial ownership declarations` — mandatory since July 2024; hard stop (cannot file AR without BO); within 10 BD of incorporation or change; criminal offence for false information
5. `## 5. AFS/FAS filing` — audited AFS for public/SOC; reviewed or FAS for private per Reg 28/29; public interest score thresholds; 2024 amendment: access restrictions for low-PI-score companies
6. `## 6. Close corporation specifics` — CC Act s15A; anniversary month + 1 month; fee structure; conversion to company (CoR18.1); member governance differences
7. `## 7. Deregistration (s82)` — 2 successive years non-filing; CIPC bulk deregistration (Jan-Feb 2025, ~800k entities); consequences: legal personality withdrawn, bank accounts frozen, directors personally liable
8. `## 8. Reinstatement` — CoR40.5; evidence of economic activity required; 30 BD to file all outstanding; reinstatement not guaranteed
9. `## 9. CoR amendment forms` — table of common forms: CoR39 (director changes), CoR21.1 (address change), CoR15.2 (MOI amendment), CoR18.1 (CC conversion)
10. `## 10. Compliance calendar template` — sample YAML structure for entity-compliance skill tracker showing entity type, anniversary date, filing status, BO status, next deadline

- [ ] **Step 6: Write diligence-sa.md**

**Title:** `# SA-Specific Diligence — South African Framework`
**Skills served:** diligence-issue-extraction, material-contract-schedule, integration-management

**Required sections:**
1. `## 1. SA diligence request categories` — mapping US standard categories to SA equivalents; additional SA-specific categories
2. `## 2. Regulatory compliance categories` — B-BBEE (certificate verification, scorecard, fronting risk), POPIA (data transfer in mergers, responsible party obligations), NEMA (environmental authorisations, waste management licences), Competition Act (pre-notification analysis, small merger call-in risk), Exchange control (SARB, cross-border capital flows), MPRDA (mining rights, water use licences), Financial services (Banks Act 15% threshold, FAIS, insurance)
3. `## 3. B-BBEE due diligence` — certificate validity, scorecard breakdown, ownership element, fronting indicators, sector code, government contract B-BBEE requirements, impact on Competition Commission public interest assessment
4. `## 4. SA contract law conventions` — conventional penalties (Act 15/1962, court may reduce if penalty disproportionate), restraint of trade (enforceable if reasonable — *Basson v Chilwan* factors: proprietary interest, prejudice to party, interest of public, reasonable in time/area/scope), cession and delegation (SA law distinguishes cession of rights from delegation of obligations), mora (late performance), breach and cancellation (lex commissoria)
5. `## 5. SA materiality framing` — Companies Act s112 (>50% assets/undertaking), PA-specific Material Contract definitions, B-BBEE thresholds, government contract thresholds, sector-specific regulatory thresholds
6. `## 6. Post-close integration (SA-specific items)` — CIPC CoR filings (director changes, registered address, MOI amendments), B-BBEE re-scoring (new ownership, management control changes), IP recordals at CIPC (trademarks, patents, designs), LRA s197 compliance (terms preserved, 12-month joint liability), Competition condition monitoring, exchange control reporting
7. `## 7. US concepts that must not appear in SA outputs` — WARN Act, COBRA, at-will employment, FLSA, FAR/DFARS, SBA, CERCLA, EPA (US), state-specific rules, dollar-denominated thresholds

- [ ] **Step 7: Commit all topic files**

```bash
git add jurisdictions/za/corporate-legal/topics/
git commit -m "feat(za): add 5 topic overlay files for corporate-legal overlay"
```

---

## Task 5: Skill router

**Files:**
- Create: `jurisdictions/za/corporate-legal/router.md`

- [ ] **Step 1: Write the router file**

Follow the exact format from `jurisdictions/za/employment-legal/router.md`: markdown heading, description paragraph, resolution rules, then a fenced YAML block.

```markdown
# Skill Router — South African Corporate Law Overlay

When jurisdiction = ZA, skills load the topic overlays and statute files listed below.

Topic files resolve to: `jurisdictions/za/corporate-legal/topics/{name}.md`
Statute files resolve to: `jurisdictions/za/statutes/{name}.yaml`

```yaml
board-minutes:
  topics: [board-governance]
  statutes: [companies-act, companies-regulations]

closing-checklist:
  topics: [fundamental-transactions, takeover-regulation]
  statutes: [companies-act, companies-regulations, competition]

cold-start-interview:
  topics: []
  statutes: [companies-act, companies-regulations, competition, bbbee, close-corporations]

diligence-issue-extraction:
  topics: [fundamental-transactions, takeover-regulation, diligence-sa]
  statutes: [companies-act, competition, bbbee, popia]

entity-compliance:
  topics: [entity-compliance-cipc]
  statutes: [companies-act, close-corporations]

integration-management:
  topics: [fundamental-transactions, diligence-sa]
  statutes: [companies-act, competition, bbbee, lra]

material-contract-schedule:
  topics: [fundamental-transactions, diligence-sa]
  statutes: [companies-act, competition]

written-consent:
  topics: [board-governance]
  statutes: [companies-act, companies-regulations]
```
```

- [ ] **Step 2: Commit**

```bash
git add jurisdictions/za/corporate-legal/router.md
git commit -m "feat(za): add corporate-legal skill router"
```

---

## Task 6: Practice profile template

**Files:**
- Create: `jurisdictions/za/corporate-legal/practice-profile-template.md`

- [ ] **Step 1: Write the practice profile template**

Base structure on the US template at `corporate-legal/CLAUDE.md` (479 lines). The ZA template keeps jurisdiction-neutral sections unchanged and replaces/adds SA-specific sections per the spec (section 5).

**Sections to include (in order):**

1. **Configuration location comment** — same as US but referencing ZA template and router: `After loading context, read jurisdictions/za/corporate-legal/router.md and load the listed overlays for this skill.`
2. **Corporate Practice Profile header** — same format, `[DATE]`, active modules
3. **Company profile** — same placeholder structure as US
4. **Who's using this** — same
5. **Statutory baseline** (NEW) — Companies Act 71 of 2008, Companies Regulations 2011, King IV apply-and-explain, router instruction
6. **Entity landscape** (NEW) — SA entity types table, CIPC as registrar, how type affects governance/filing/audit
7. **Available integrations** — same as US
8. **Outputs** — REPLACE work-product header with SA privilege formulation from spec section 5. Keep reviewer note format, decision tree, dashboard offer unchanged.
9. **Decision posture** — same as US
10. **Shared guardrails** — same as US (no silent supplement, currency trigger, etc.)
11. **M&A regulatory landscape** (NEW) — Competition Commission, TRP, B-BBEE, SARB exchange control
12. **Board governance framework** (NEW) — Companies Act s66-78, s94, s72(4), King IV, MOI
13. **B-BBEE and ownership** (NEW) — scoring, M&A impact, fronting, Mining Charter
14. **Proportionality** — same as US
15. **Jurisdiction recognition** — FLIPPED: SA-first, detect non-SA
16. **Scaffolding, not blinders** — same
17. **Ad-hoc questions** — same
18. **Retrieved-content trust** — same
19. **Large input / Large output** — same
20. **Matter workspaces** — same structure
21. **Active modules** — same 4 modules (M&A, Board & Secretary, Public Company, Entity Management) with SA-specific field labels:
    - M&A: replace HSR with Competition Commission; add TRP, B-BBEE conditions
    - Board: replace Delaware/state references with Companies Act/MOI; add social & ethics committee; add King IV
    - Public Company: replace SEC/§16 with JSE Listings Requirements; replace NYSE/Nasdaq with JSE Main Board/AltX
    - Entity Management: replace Delaware franchise tax with CIPC annual returns; replace CT Corp with CIPC; replace state-by-state with entity-type-by-type
22. **Escalation** (NEW) — table: CIPC, Competition Commission/Tribunal, TRP, Companies Tribunal, Labour Court, JSE, external counsel
23. **Seed documents** — 7 items from spec section 5

- [ ] **Step 2: Commit**

```bash
git add jurisdictions/za/corporate-legal/practice-profile-template.md
git commit -m "feat(za): add corporate-legal ZA practice profile template"
```

---

## Task 7: Cold-start interview ZA fork

**Files:**
- Modify: `corporate-legal/skills/cold-start-interview/SKILL.md`

- [ ] **Step 1: Read current file and identify insertion point**

The ZA fork inserts after Part 0 (ends around line 195) and before Part 0.5: Module selection (line 196). Follow the employment-legal pattern: check company profile jurisdiction, fork to SA path if ZA.

- [ ] **Step 2: Insert ZA jurisdiction check**

After Part 0 (the role/practice setting determination) and before `### Part 0.5: Module selection`, insert:

```markdown
### Jurisdiction check — South African overlay

After writing the Part 0 sections, check the company profile for jurisdiction:

- Read `~/.claude/plugins/config/claude-for-legal/company-profile.md` → `Primary jurisdiction`
- If the primary jurisdiction is **South Africa** (or ZA, or the user's company is SA-based based on the company profile answers):

**Fork to the SA interview path.** The SA-specific questions below replace the US-default module questions. The output writes to the ZA practice profile template sourced from `jurisdictions/za/corporate-legal/practice-profile-template.md` instead of the US template.

If the primary jurisdiction is NOT South Africa, continue with the US interview path below (Part 0.5 onwards as written).

---

#### SA Part 0.5: Module selection

Same as US Part 0.5 — the 4 modules (M&A, Board & Secretary, Public Company, Entity Management) apply equally. Proceed with module selection, then branch to SA-specific questions per module below.

#### SA Part 1: Statutory footprint (must-have, ~3 min)

These 8 questions anchor the SA overlay. Ask them in order:

1. **Company type and listing status:** "What type of company is this — Pty Ltd, Ltd, SOC, NPC, or personal liability (Inc)? And is it JSE-listed (Main Board, AltX, or unlisted)?"
2. **MOI governance:** "Is the MOI standard (Table 1 — CoR15.1A/B) or customised? Any non-standard governance provisions I should know about — entrenched provisions, special voting thresholds, restrictions on board consent in lieu of meetings, pre-emptive rights?"
3. **B-BBEE status:** "What is the company's current B-BBEE level and applicable sector code? (Level 1-8, non-compliant, or exempt EME/QSE — and generic codes or sector-specific?)"
4. **Deal size relative to Competition thresholds:** "What's the typical deal size relative to Competition Act merger thresholds? Below lower threshold (small), intermediate (combined R600m+ and target R100m+), or large (combined R6.6b+ and target R190m+)?"
5. **Cross-border element:** "Do deals typically involve a cross-border element requiring SARB exchange control approval? (Inbound, outbound, both, no, or occasionally?)"
6. **Social & ethics committee:** "Is a social & ethics committee in place? (Required under s72(4) + Reg 43, exempted, voluntarily established, or not in place?)"
7. **Entity portfolio:** "What does the entity portfolio look like? How many entities, what types (Pty Ltd, CC, Ltd, NPC, external company), and what's the CIPC compliance status — all current, some overdue, or unknown?"
8. **Written consent practice:** "How are board resolutions typically passed outside of meetings? (s74 round-robin resolutions routinely, occasionally, not used because MOI restricts, or don't know?)"

If the user seems knowledgeable and time permits, ask the nice-to-have questions:

9. "Is the company TRP-regulated? (For private companies: have 10%+ of shares been transferred between unrelated parties in the last 24 months?)"
10. "Is a company secretary appointed?"
11. "Who is the auditor / audit firm?"
12. "Does the company apply King IV? (Mandatory if JSE-listed/SOC, voluntarily, or not applied?)"

#### SA Part 2: Seed documents

Ask for these (must-have first, then nice-to-have):

**Must-have:**
- Prior board minutes (1-2 examples) — to learn house format
- MOI (Memorandum of Incorporation) — governance provisions

**Nice-to-have (based on active modules):**
- Prior written consent (if Board module active)
- Prior M&A issues memo (if M&A module active)
- Diligence request list (if M&A module active)
- Entity org chart or subsidiary register (if Entity module active)
- CIPC company search printout (if Entity module active)

#### SA Part 3: Build configuration

- Use the ZA practice profile template at `jurisdictions/za/corporate-legal/practice-profile-template.md`
- Populate from interview answers + seed documents
- Write to `~/.claude/plugins/config/claude-for-legal/corporate-legal/CLAUDE.md`
- Show tailored capability summary listing the 8 SA-overlaid skills

---
```

- [ ] **Step 3: Commit**

```bash
git add corporate-legal/skills/cold-start-interview/SKILL.md
git commit -m "feat(za): add ZA fork to corporate-legal cold-start interview"
```

---

## Task 8: Extend validation scripts

**Files:**
- Modify: `scripts/validate-za-router.py` (lines 27-70, PRACTICE_AREAS list)
- Modify: `scripts/validate-za-templates.py` (lines 19-213, TEMPLATE_CONFIG dict)

- [ ] **Step 1: Add corporate-legal to validate-za-router.py**

In `scripts/validate-za-router.py`, add this entry to the `PRACTICE_AREAS` list (after the `legal-clinic` entry, before the closing `]`):

```python
    {
        "name": "corporate-legal",
        "router": REPO_ROOT / "jurisdictions" / "za" / "corporate-legal" / "router.md",
        "skills_dir": REPO_ROOT / "corporate-legal" / "skills",
        "topics_dir": REPO_ROOT / "jurisdictions" / "za" / "corporate-legal" / "topics",
    },
```

- [ ] **Step 2: Add corporate-legal to validate-za-templates.py**

In `scripts/validate-za-templates.py`, add this entry to the `TEMPLATE_CONFIG` dict (after the `"legal-clinic"` entry):

```python
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
```

- [ ] **Step 3: Run both validators**

```bash
python3 scripts/validate-za-router.py
python3 scripts/validate-za-templates.py
```

Expected: corporate-legal entries appear as OK.

- [ ] **Step 4: Commit**

```bash
git add scripts/validate-za-router.py scripts/validate-za-templates.py
git commit -m "feat(za): extend validators for corporate-legal overlay"
```

---

## Task 9: Scenario eval cases (24 cases)

**Files:**
- Create: 24 YAML files under `jurisdictions/za/evals/corporate-legal/`

Follow the exact eval case schema from the reference (`jurisdictions/za/evals/employment-legal/termination-review/case-01-misconduct-no-hearing.yaml`): `name`, `skill`, `input` (multi-line `|`), `expected_flags`, `expected_statutes`, `must_not_contain`, `notes`.

- [ ] **Step 1: Create directory structure**

```bash
mkdir -p jurisdictions/za/evals/corporate-legal/{board-minutes,closing-checklist,cold-start-interview,diligence-issue-extraction,entity-compliance,written-consent,integration-management,material-contract-schedule}
```

- [ ] **Step 2: Write board-minutes eval cases (3 files)**

Create each file per the case outlines in spec section 8. Example for case-01:

```yaml
# jurisdictions/za/evals/corporate-legal/board-minutes/case-01-routine-quarterly.yaml
name: "Routine quarterly board meeting with standard resolutions"
skill: board-minutes
input: |
  Draft minutes for a quarterly board meeting of a Pty Ltd company.
  Agenda items: (1) officer appointment — new CFO, (2) approval of
  annual financial statements, (3) declaration of interim dividend
  of R500,000. Five directors present, quorum met per MOI. One
  director has a personal financial interest in the CFO appointment
  (the candidate is a family member).

expected_flags:
  - "s75 personal financial interest declaration required"
  - "Solvency and liquidity test for distribution"
  - "Interested director cannot vote on CFO appointment"

expected_statutes:
  - "Companies Act s73"
  - "Companies Act s75"
  - "Companies Act s46"
  - "Companies Act s4"

must_not_contain:
  - "Robert's Rules"
  - "DGCL"
  - "bylaws"
  - "Delaware"

notes: |
  The director with a family connection to the CFO candidate must
  declare the personal financial interest under s75 before the board
  considers the appointment. The interested director cannot vote on
  that resolution. The dividend declaration requires the board to
  apply the solvency and liquidity test (s4) and authorise the
  distribution by resolution (s46). Minutes should reference the
  MOI for quorum and voting requirements, not bylaws.
```

Write case-02 (fundamental transaction — s112 disposal triggering s115(2)(b) holding company approval) and case-03 (social & ethics committee — s72(4), Reg 43, King IV) following the same schema with the scenarios from the spec.

- [ ] **Step 3: Write remaining 21 eval cases**

Write eval cases for the remaining 7 skills (3 each), following the case outlines in spec section 8. Each file must include all 6 fields (`name`, `skill`, `input`, `expected_flags`, `expected_statutes`, `must_not_contain`, `notes`).

Key patterns to verify for each skill:
- **closing-checklist**: Competition Commission route, TRP certificate, SARB, shareholder approval mechanics
- **cold-start-interview**: SA-specific module questions, no US module references
- **diligence-issue-extraction**: LRA s197, B-BBEE, MPRDA, government contracts
- **entity-compliance**: CIPC deadlines, CC Act, deregistration, reinstatement
- **written-consent**: s74, s75, s45, MOI restrictions
- **integration-management**: s197, B-BBEE re-scoring, Competition conditions, CIPC CoR filings
- **material-contract-schedule**: SA PA definitions, conventional penalties, government supply B-BBEE

- [ ] **Step 4: Commit**

```bash
git add jurisdictions/za/evals/corporate-legal/
git commit -m "feat(za): add 24 corporate-legal eval cases"
```

---

## Task 10: Final validation run

**Files:** None created — validation only.

- [ ] **Step 1: Run statute validator**

```bash
python3 scripts/validate-za-statutes.py
```

Expected: All statute files OK, including 3 new files (companies-act, companies-regulations, close-corporations) and 2 extended files (competition, bbbee).

- [ ] **Step 2: Run router validator**

```bash
python3 scripts/validate-za-router.py
```

Expected: `OK: [corporate-legal] 8 skills, all references resolve` — verifies all 8 skills exist as directories, all 5 topic files exist, all 8 statute files exist.

- [ ] **Step 3: Run template validator**

```bash
python3 scripts/validate-za-templates.py
```

Expected: `OK: [corporate-legal] practice-profile-template.md` — verifies required sections present, SA terms present, no US terms outside privilege caveat.

- [ ] **Step 4: Run upstream plugin validation**

```bash
claude plugin validate corporate-legal
```

Expected: Valid (the only upstream file modified is cold-start-interview/SKILL.md, which should still pass frontmatter validation).

- [ ] **Step 5: Run JSON/YAML sanity check**

```bash
python3 -c "import yaml; from pathlib import Path; [yaml.safe_load(f.read_text()) for f in Path('jurisdictions/za').rglob('*.yaml')]"
```

Expected: No errors — all YAML files parse cleanly.

- [ ] **Step 6: Verify directory structure matches plan**

```bash
find jurisdictions/za/corporate-legal -type f | sort
find jurisdictions/za/evals/corporate-legal -type f | sort
```

Expected output matches the file map at the top of this plan.

- [ ] **Step 7: Final commit (if any fixes were needed)**

```bash
git status
# If clean: no commit needed
# If fixes: git add <files> && git commit -m "fix(za): address validation issues in corporate-legal overlay"
```
