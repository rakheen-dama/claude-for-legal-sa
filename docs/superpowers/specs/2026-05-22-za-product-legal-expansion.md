# South African Overlay Expansion: product-legal

**Date:** 2026-05-22
**Plugin:** product-legal v1.0.2
**Status:** Spec complete — ready for implementation plan
**Author:** Rakheen Dama + Claude (jurisdiction-expansion interview)

---

## Decision summary

| # | Step | Decision | Source |
|---|---|---|---|
| 1 | Target | product-legal — 7 skills, 5 in scope | user confirmed |
| 2 | Statutes | 6 existing to extend + 4 new. All in v1. | Perplexity + user confirmed |
| 3 | Skill divergence | 3 HIGH, 2 MEDIUM, 2 LOW (no overlay) | Perplexity + user confirmed |
| 4 | Topic overlays | 6 topics | user confirmed |
| 5 | Practice profile | SA-native template with 4 new sections | user confirmed |
| 6 | Cold-start | 8 must-have + 4 nice-to-have questions | user confirmed |
| 7 | High-risk flags | 11 flags | user confirmed |
| 8 | Validation | 15 eval cases + 5 validation rules + expert review gate | user confirmed |

---

## 1. Statute inventory

### Existing statutes to extend

| Statute | File | Sections to add for product-legal |
|---|---|---|
| **Consumer Protection Act 68/2008** | `cpa.yaml` | s22 (plain language), s29 (misleading marketing), s30 (bait marketing), s36 (promotional competitions), s41 (false representations), s48-52 (unfair terms), s55-58 (quality/safety/warnings), s61 (strict product liability) |
| **ECTA 25/2002** | `ecta.yaml` | s43-52 (e-commerce: mandatory disclosures, cooling-off, review opportunity, spam) |
| **POPIA 4/2013** | `popia.yaml` | Minimal — may add s72 context for product data flows |
| **Competition Act 89/1998** | `competition.yaml` | Abuse of dominance for comparative advertising/market power claims |
| **NCA 34/2005** | `nca.yaml` | s60-61 (credit marketing/advertising), s63-66 (disclosure/plain language), s74-80 (reckless credit) |
| **FICA 38/2001** | `fica.yaml` | KYC/accountable institution obligations for fintech product features |

### New statute YAML files

| Statute | File to create | Key sections |
|---|---|---|
| **Lotteries Act 57/1997** | `lotteries.yaml` | Unlawful lottery definition, intersection with CPA s36 promotional competitions, entry fee boundaries, criminal offences |
| **National Gambling Act 7/2004** | `national-gambling.yaml` | Gambling game definitions, closed list of permitted forms, online gambling prohibition, loot box/gamification implications, advertising restrictions (minors, responsible gambling), provincial licensing framework |
| **Merchandise Marks Act 17/1941** | `merchandise-marks.yaml` | False trade descriptions, origin claims, protected marks/symbols, SABS/certification claims without authorization |
| **Films & Publications Act 65/1996** | `films-publications.yaml` | Content classification framework, online content amendments (2019), age-gating requirements, UGC platform obligations, registration requirements for online distributors, prohibited content (CSAM, revenge porn, hate speech) |

### Non-statute frameworks (topic overlay content, not YAML)

- **ARB Code of Advertising Practice** — substantiation requirements, comparative claims, misleading advertising standards
- **DMASA Code of Conduct** — POPIA-compliant direct marketing practices
- **Draft National AI Policy** — emerging, no statute yet; track for 2026/27

### Gazette-published values (temporal)

- CPA s5 juristic person threshold — R2 million (changes periodically)
- CPA s61 product liability — no monetary threshold (strict liability, no cap)
- ECTA e-commerce cooling-off period — 7 days (fixed by statute, s44)
- NCA interest rate caps and thresholds — updated periodically via NCR

---

## 2. Skill divergence matrix

| Skill | Description | Divergence | In scope | Reasoning |
|---|---|---|---|---|
| **launch-review** | Full launch review against framework and risk calibration | HIGH | Yes | Sector overlay table entirely US-centric (COPPA, FTC, GLBA, HIPAA, FERPA, FCRA, ROSCA, CAN-SPAM, TCPA). SA needs CPA, POPIA, ECTA, NCA, Competition Act, ARB Code, National Gambling Act, Films & Publications Act. |
| **marketing-claims-review** | Review marketing copy for claims needing substantiation | HIGH | Yes | Substantiation research targets "FTC, NAD, state UDAP." SA equivalent is ARB Code + CPA s29-41 + ECTA. Claim taxonomy is universal but substantiation standards are jurisdiction-specific. |
| **cold-start-interview** | Sets up practice profile, reads seed docs, builds calibration | HIGH | Yes | Entry point. Needs ZA fork for SA-specific config questions and ZA practice profile template. |
| **feature-risk-assessment** | Deep-dive risk assessment for single features | MEDIUM | Yes | Risk framework portable but regulatory landscape section needs SA regulators (NCC, IR, Competition Commission, ICASA, SAHPRA). |
| **is-this-a-problem** | Fast triage against calibration | MEDIUM | Yes | Triage pattern portable but trap check examples reference US concepts. SA overlay adds SA-specific trap patterns. |
| **customize** | Edit practice profile sections | LOW | No | Infrastructure — works against whatever profile exists. |
| **matter-workspace** | Manage matter workspaces | LOW | No | Pure file management, jurisdiction-neutral. |

---

## 3. Topic overlay map

### Topic files

| Topic file | Skills served | Key content areas |
|---|---|---|
| **consumer-protection.md** | launch-review, feature-risk-assessment, is-this-a-problem | CPA product safety (s55-58), strict product liability (s61), unfair contract terms (s48-52), plain language (s22), cooling-off rights (s16), NCC enforcement, quality warranties (s56) |
| **advertising-and-claims.md** | marketing-claims-review, launch-review (cat 7), is-this-a-problem | ARB Code substantiation framework, CPA marketing provisions (s29-41), comparative advertising rules, puffery vs factual under SA law, promotional competitions (CPA s36 + Lotteries Act), Merchandise Marks Act (origin/quality claims), DMASA Code |
| **e-commerce-and-digital.md** | launch-review, marketing-claims-review, is-this-a-problem | ECTA Chapter VII mandatory disclosures (s43), cooling-off for e-commerce (s44-45), spam/unsolicited communications (s48-50), POPIA s69 electronic direct marketing, interplay between ECTA + CPA + POPIA for online marketing |
| **sector-regulatory-map.md** | launch-review (sector hints), feature-risk-assessment (regulatory landscape), is-this-a-problem | SA regulator map replacing US sector overlay table. Maps product verticals to SA regulatory regimes and regulators (NCC, Information Regulator, Competition Commission, ICASA, SAHPRA, NGB, FPB, FSCA/PA/SARB, ARB) |
| **fintech-and-credit.md** | launch-review (fintech sector), feature-risk-assessment, is-this-a-problem | NCA credit marketing (s60-61), disclosure requirements (s63-66), reckless credit (s74-80), FICA KYC/accountable institutions, FAIS context, Banks Act (deposit-taking), NPS Act (payment systems), credit life insurance |
| **content-and-minors.md** | launch-review (children/gaming sectors), feature-risk-assessment, is-this-a-problem | Films & Publications Act (UGC, age-gating, content classification, 2019 online amendments), Children's Act (best interests, parental consent), National Gambling Act (loot boxes, gamification, prize mechanics), Protection from Harassment Act (online safety) |

### Router mapping

```yaml
launch-review:
  topics: [consumer-protection, advertising-and-claims, e-commerce-and-digital, sector-regulatory-map]
  statutes: [cpa, ecta, popia, competition, lotteries, merchandise-marks]
  conditional:
    fintech: { topics: [fintech-and-credit], statutes: [nca, fica] }
    children-or-gaming: { topics: [content-and-minors], statutes: [national-gambling, films-publications] }

marketing-claims-review:
  topics: [advertising-and-claims, e-commerce-and-digital]
  statutes: [cpa, ecta, lotteries, merchandise-marks, competition]

feature-risk-assessment:
  topics: [consumer-protection, sector-regulatory-map]
  statutes: [cpa, popia, ecta]
  conditional:
    fintech: { topics: [fintech-and-credit], statutes: [nca, fica] }
    children-or-gaming: { topics: [content-and-minors], statutes: [national-gambling, films-publications] }

is-this-a-problem:
  topics: [consumer-protection, advertising-and-claims, sector-regulatory-map]
  statutes: [cpa, popia, ecta, competition]

cold-start-interview:
  topics: []
  statutes: [cpa, ecta, popia, nca, fica, competition]
```

---

## 4. Practice profile template design

### Section replacement table

| US template section | ZA treatment | Notes |
|---|---|---|
| Configuration preamble | Modify | Add router instruction for `jurisdictions/za/product-legal/router.md` |
| Who we are | Keep + extend | Add B-BBEE level, SA regulatory registration status |
| Who's using this | Modify | Role options: "Admitted attorney or advocate under LPA 28/2014 / Non-lawyer with attorney access / Non-lawyer without attorney access" |
| Available integrations | Keep | Jurisdiction-neutral |
| Outputs / Work-product header | Replace | SA privilege formulation — no "ATTORNEY WORK PRODUCT" doctrine |
| Reviewer note format | Keep | Adjust research connector examples (SAFLII not CourtListener) |
| Decision posture | Keep | Jurisdiction-neutral |
| Shared guardrails | Keep | Adjust examples to SA context (BCEA/CPA not FLSA) |
| Scaffolding / Proportionality | Keep | Jurisdiction-neutral |
| Jurisdiction recognition | Replace | This IS the SA profile; flag non-SA jurisdictions instead |
| Currency watch | Keep + extend | Add SA-specific items (Gazette thresholds, ARB updates, pending AI policy) |
| Matter workspaces | Keep | Jurisdiction-neutral |
| Launch review process | Keep structure | Same PLACEHOLDERs — filled at cold-start |
| Review framework | Replace | Same 8 categories with SA regulatory context (CPA, POPIA, ECTA not FTC/CCPA) |
| Risk calibration | Keep structure | Filled at cold-start from seed reviews |
| Marketing claims | Replace | SA substantiation (ARB Code + CPA s29-41), comparative advertising (ARB + Competition Act), promotional competitions (CPA s36 + Lotteries Act) |
| Escalation | Replace | SA forums: NCC, Information Regulator, Competition Commission, ARB, Consumer Tribunal |
| Connected systems / Seed reviews | Keep | Jurisdiction-neutral structure |

### New SA-specific sections

| Section | Content |
|---|---|
| **Regulatory posture** | SA regulatory bodies map: NCC (consumer), Information Regulator (POPIA), Competition Commission, ARB (advertising), ICASA (if telecom), SAHPRA (if health-tech), NGB/FPB (if gaming/content), FSCA/SARB (if fintech). Current registration/interaction status. |
| **B-BBEE considerations** | B-BBEE level, scorecard status, procurement implications for product launches (supplier/partner selection, public sector sales requirements). |
| **CPA compliance posture** | CPA s5 applicability (juristic person threshold), plain language approach (s22), unfair terms framework for T&Cs/SLAs (s48-52), product liability exposure (s61), product safety monitoring (s60). |
| **Promotional competitions** | Whether company runs promotions, CPA s36 compliance approach, Lotteries Act boundary, standard T&C template location. |

### Work-product header

- **Admitted attorney/advocate:** `PRIVILEGED & CONFIDENTIAL — PREPARED BY/AT THE DIRECTION OF LEGAL COUNSEL FOR THE PURPOSE OF PROVIDING LEGAL ADVICE`
- **Non-lawyer:** `CONFIDENTIAL — NOT LEGAL ADVICE — CONSULT AN ADMITTED ATTORNEY OR ADVOCATE BEFORE ACTING`

SA privilege caveat block includes: no US "ATTORNEY WORK PRODUCT" doctrine, in-house commercial-vs-legal capacity distinction, litigation privilege requires contemplation of litigation, no general protection for internal analyses.

Product-legal-specific addition: launch review memos in legal capacity may attract privilege; same memo reframed as "product risk assessment" for cross-functional audience likely does not. Separate legal analysis into standalone privileged memo when document serves both purposes.

### Seed documents for cold-start

| Document | Purpose |
|---|---|
| 3-5 past launch review memos | Build risk calibration table |
| Marketing claims review examples | Learn substantiation standards and rejected claims |
| Standard product T&Cs / Terms of Service | Baseline for unfair terms analysis |
| Promotional competition T&C template | If company runs competitions |
| Company privacy policy | POPIA compliance baseline |
| ARB complaint or ruling (if any) | Learn advertising risk patterns |

---

## 5. Cold-start interview questions

### Must-have (8 questions)

| # | Question | Populates |
|---|---|---|
| 1 | Are you an admitted attorney or advocate under the Legal Practice Act, or a non-lawyer? | `## Who's using this → Role` |
| 2 | Does your company sell to consumers (B2C), businesses (B2B), or both? If B2C/both: are customers above the CPA R2m juristic person threshold? | `## CPA compliance posture` |
| 3 | Which SA regulators has your company interacted with? (NCC, Information Regulator, Competition Commission, ARB, ICASA, SAHPRA, FSCA, NGB/FPB — or none) | `## Regulatory posture` |
| 4 | Does your product involve any of: fintech/payments/credit, health-tech, children/minors, gaming/gamification, content/UGC, telecom/OTT? | `## Review framework` sector overlays, conditional router |
| 5 | Does your company run promotional competitions (prize draws, sweepstakes, giveaways) as part of product marketing? | `## Promotional competitions` |
| 6 | What is your company's B-BBEE level? (1-8, non-compliant, exempted micro-enterprise, unknown) | `## B-BBEE considerations` |
| 7 | Is your launch review process a formal gate (legal must sign off) or advisory? | `## Launch review process → Sign-off` |
| 8 | Who handles NCC complaints, Information Regulator queries, Competition Commission inquiries, ARB complaints? (Names/roles, internal or external counsel) | `## Escalation` |

### Nice-to-have (4 questions)

| # | Question | Populates |
|---|---|---|
| 9 | Is your company a member of the ARB or DMASA? | `## Regulatory posture`, `## Marketing claims` |
| 10 | Does your company have a substantiation file (pre-cleared marketing claims with evidence)? If so, where? | `## Marketing claims → Substantiation standard` |
| 11 | Has your company faced any NCC, ARB, or Competition Commission complaints or rulings? | Seed data for `## Risk calibration` |
| 12 | Does your product process personal information of children under 18? | Conditional topic loading |

### Fork design

Cold-start interview SKILL.md gets ZA fork after Part 0 (orientation):
1. Part 0 runs unchanged (orientation, practice setting, install scope check)
2. Jurisdiction check: if company-profile.md says `jurisdiction: ZA` → fork into ZA path
3. ZA path asks 8 must-have questions + offers 4 nice-to-haves
4. ZA path writes to ZA practice profile template
5. ZA path adds router instruction to configuration preamble
6. Seed document request uses SA-specific seed list

---

## 6. High-risk flag table

| # | Flag | Why high-risk | What to check |
|---|---|---|---|
| 1 | **CPA strict product liability (s61)** | Strict no-fault liability. Cannot contract out (s51). Joint and several across supply chain. | Does product qualify as "goods"? Adequate warnings/instructions? Safety monitoring (s60) in place? Insurance clear for software liability? |
| 2 | **Unfair contract terms (s48-52)** | NCC can declare terms void. 62+ compliance notices issued 2025-26. US/EU template imports frequently violate CPA. | Overbroad liability exclusions? One-sided termination? Unfair auto-renewal? Hidden fee changes? Dense legalese violating s22? |
| 3 | **Misleading marketing (s29-41 + ARB)** | Low evidentiary bar. ARB forces ad withdrawal. NCC penalties up to R1m or 10% turnover. | Overstated performance? "Free" with hidden charges? Dark patterns? Inflated discounts? Unsubstantiated comparative claims? |
| 4 | **POPIA breach notification failure (s19-22)** | IR actively enforcing (Lancet R100k, Blouberg R500k, WhatsApp enforcement). Non-notification judged harsher than breach. Fines up to R10m. | Incident response plan? Notification timelines? Complete notices? Vendor breach obligations in processing agreements? |
| 5 | **Promotional competition non-compliance (CPA s36 + Lotteries Act)** | Criminal offence risk. Public-facing = fast escalation to NCC + social media. | Complete official rules? Entry genuinely free (not unlawful lottery)? POPIA-compliant data collection? Prizes honoured? |
| 6 | **ECTA e-commerce disclosure failures (s43-52)** | Criminal offence (s43(5)). Non-compliance undermines T&C enforceability. ECTA + CPA apply in parallel. | Physical address? Full pricing? Complaint procedure? Security/privacy disclosures? Review-and-correct step? Cooling-off honoured? 30-day performance? |
| 7 | **NCA credit marketing violations (fintech)** | Agreements declared void. BNPL may be regulated credit without registration. | Product functionally credit? Registered credit provider? APR/fees/total cost displayed? Pre-agreement disclosures? Affordability assessment? |
| 8 | **Multi-regulator escalation** | Same conduct triggers multiple regulators simultaneously. Multiplicative exposure. | Assessed against all applicable regulators? Escalation matrix populated per regulator? Single coordination point? |
| 9 | **Product safety monitoring gap (s60)** | Delayed remediation + knowledge = aggravated liability. Class-style exposure for mass-market tech. | Safety monitoring process? Recall procedure? Post-sale notices reaching users? Upstream supplier obligations? |
| 10 | **Cross-border data transfer without safeguards (POPIA s72)** | Cloud/CDN/support = transfers. IR investigated WhatsApp/Meta on this. | Transfers documented? Adequate safeguards? Operator agreements? Privacy notice discloses transfers? Sub-processor chains mapped? |
| 11 | **"POPIA compliant" / "FSCA approved" claims** | Asserting regulatory compliance without substantiation is both misleading (CPA s29) and advertising violation (ARB). | Claim matches registration/approval status? Specific compliance substantiated? Current status or one-time certification? |

### Cross-reference: flags to statutes

| Flag | Primary statute sections |
|---|---|
| 1 | CPA s55-58, s60-61, s51 |
| 2 | CPA s22, s48-52 |
| 3 | CPA s29-41, s112-113; ARB Code |
| 4 | POPIA s19-22, s107, s109-111 |
| 5 | CPA s36; Lotteries Act 57/1997 |
| 6 | ECTA s43-52 |
| 7 | NCA s60-61, s63-66, s74-80 |
| 8 | Cross-cutting |
| 9 | CPA s58, s60 |
| 10 | POPIA s72 |
| 11 | CPA s29; ARB Code |

---

## 7. Eval case outlines

### launch-review (3 cases)

**LR-01: B2C SaaS launch with new data collection**
- Input: SaaS product launching feature collecting location data from SA consumers for personalized recommendations. Below CPA threshold. Marketing says "AI-powered."
- Expected flags: Privacy (POPIA new collection), CPA product safety, AI governance, marketing claims ("AI-powered" substantiation)
- Expected statutes: POPIA s9-14, CPA s29, CPA s55
- Must NOT contain: FTC, CCPA, COPPA, HIPAA, state-specific references, FRCP 26(b)(3)

**LR-02: Fintech feature adding BNPL**
- Input: Existing product adding BNPL checkout for SA users. Copy: "0% interest — pay later, stress-free."
- Expected flags: NCA credit compliance, NCA marketing (APR disclosure), CPA unfair terms (s48-52), POPIA (financial data)
- Expected statutes: NCA s60-61, s74-80, CPA s22, FICA
- Must NOT contain: CFPB, Reg Z, Reg E, TILA, state money transmission, GLBA

**LR-03: Promotional competition with prize draw**
- Input: "Spin-the-wheel" website promotion. Entry via signup. Grand prize R50,000 voucher.
- Expected flags: Promotional competition compliance (CPA s36 + Lotteries Act), POPIA (data collection), ECTA (disclosures)
- Expected statutes: CPA s36, Lotteries Act 57/1997, POPIA s69, ECTA s43
- Must NOT contain: State sweepstakes law, FTC, CAN-SPAM, ROSCA

### marketing-claims-review (4 cases)

**MC-01: Performance claims**
- Input: "South Africa's fastest project management tool. 10x faster than legacy solutions. Trusted by 500+ SA companies."
- Expected flags: "Fastest" = comparative (ARB), "10x faster" = factual, "500+" = verify count
- Expected statutes: ARB Code, CPA s29, Competition Act
- Must NOT contain: FTC Act § 5, Lanham Act, NAD, state UDAP

**MC-02: Compliance marketing**
- Input: "Fully POPIA compliant. FSCA approved. Your data is 100% safe with us."
- Expected flags: Regulatory compliance claim (Flag #11), "100% safe" = absolute claim
- Expected statutes: CPA s29, s41, ARB Code, POPIA, FAIS/FSCA
- Must NOT contain: FTC Endorsement Guides, SEC, FINRA

**MC-03: Implied claims**
- Input: "Finally, a secure alternative to [Competitor]. Built for healthcare."
- Expected flags: Comparative (implies competitor insecure), health regulatory compliance implied
- Expected statutes: ARB Code, CPA s29, Medicines Act 101/1965
- Must NOT contain: HIPAA, FDA SaMD, FTC Health Breach Notification Rule

**MC-04: Discount pricing**
- Input: "Was R999/month — now R299/month. Limited time. Save 70%."
- Expected flags: Bait marketing risk (CPA s30), "limited time" needs end date, "was" price must be genuine
- Expected statutes: CPA s29-30, ARB Code, ECTA s43
- Must NOT contain: FTC Guides Against Deceptive Pricing, state UDAP

### feature-risk-assessment (3 cases)

**FR-01: AI recommendation engine**
- Input: ML recommends products to consumers based on browsing. Flagged as novel from launch review.
- Expected flags: POPIA automated decision-making, CPA s29, product safety (algorithmic harm), cross-border if model hosted outside SA
- Expected statutes: POPIA s11, s71, s72, CPA s55-58
- Must NOT contain: CCPA opt-out, GDPR Art. 22, Colorado AI Act, EU AI Act

**FR-02: User-generated content platform**
- Input: Feature for SA users to upload/share video. Content moderation risk flagged.
- Expected flags: Films & Publications Act (classification, age-gating), Children's Act, Cybercrimes Act, CPA product safety
- Expected statutes: Films & Publications Act 65/1996, Children's Act 38/2005, Cybercrimes Act 19/2020, CPA s60
- Must NOT contain: CDA § 230, DMCA, COPPA safe harbor, EU Digital Services Act

**FR-03: IoT firmware update risk**
- Input: OTA firmware update for smart home devices. Previous update bricked 200 units. Assessing next rollout.
- Expected flags: CPA strict product liability (s61), safety monitoring (s60), class-style exposure, insurance
- Expected statutes: CPA s55-61, ECTA
- Must NOT contain: US product liability (Restatement Third), CPSC, state lemon laws

### is-this-a-problem (5 cases)

**ITP-01: Customer logos on pricing page**
- Expected: ⚠️ Needs a look
- Trap: "What does the contract say about publicity?" — cite CPA s11

**ITP-02: Auto-enroll users in premium tier with converting free trial**
- Expected: 🛑 Hold
- Trap: Dark pattern risk (CPA s48, ECTA cooling-off). Conversion clearly disclosed? Cooling-off honoured?

**ITP-03: Lucky draw for referrals**
- Expected: ⚠️ Needs a look
- Trap: CPA s36 + Lotteries Act. Entry genuinely free? Official rules? Lawful promotional competition or unlawful lottery?

**ITP-04: "We're POPIA compliant" on website**
- Expected: ⚠️ Needs a look
- Trap: Flag #11. Can you substantiate? Marketing claim or contractual representation? ARB precedent.

**ITP-05: Adding wallet top-up payment feature**
- Expected: 🛑 Hold
- Trap: NCA + FICA + Banks Act. Stored-value product? Deposit-taking? Registration needed?

### Validation rules

1. No US regulatory concepts in ZA outputs (FTC, NAD, CCPA, COPPA, HIPAA, GLBA, CFPB, CAN-SPAM, TCPA, ROSCA, state UDAP, state-specific rules, FRCP 26(b)(3), "at-will", US case law)
2. SA statute references use correct short format (CPA s29, POPIA s22, ECTA s43)
3. ARB Code referenced as self-regulatory, not statutory
4. Privilege header uses SA formulation, never "ATTORNEY WORK PRODUCT"
5. Promotional competition advice distinguishes CPA s36 (lawful) from Lotteries Act (unlawful lottery boundary)

### Expert review gate

Before release, an SA practitioner with product/commercial law experience reviews:
- Topic overlay procedures against current CPA, ECTA, ARB Code
- Statute YAML values against current Government Gazette (especially CPA juristic person threshold)
- High-risk flag table against current NCC complaint patterns and ARB rulings
- Marketing claims framework against current ARB substantiation standards
- Practice profile template for completeness and correctness

---

## 8. Source provenance log

| Item | Source | Tag |
|---|---|---|
| CPA sections (s22, s29-41, s48-52, s55-61) | Perplexity search + model knowledge | [Perplexity — verify] |
| ECTA Chapter VII (s43-52) | Perplexity search | [Perplexity — verify] |
| POPIA enforcement examples (Lancet, Blouberg, WhatsApp) | Perplexity search citing Michalsons, CDH, Covington | [Perplexity — verify] |
| NCC complaint patterns and enforcement (Vodacom fine, 62 compliance notices) | Perplexity search citing NCC notices | [Perplexity — verify] |
| ARB Code substantiation requirements | Perplexity search citing ARB, De Rebus | [Perplexity — verify] |
| NCA credit marketing provisions (s60-61, s74-80) | Perplexity search | [Perplexity — verify] |
| Lotteries Act / National Gambling Act applicability | Perplexity search citing Cronje Law, gov.za | [Perplexity — verify] |
| Films & Publications Act online amendments | Perplexity search | [Perplexity — verify] |
| Merchandise Marks Act applicability | Perplexity search | [Perplexity — verify] |
| Competition Commission digital platform inquiries | Perplexity search | [Perplexity — verify] |
| B-BBEE relevance to product launches | Perplexity search | [Perplexity — verify] |
| Draft National AI Policy timeline (2026/27) | Perplexity search citing Michalsons, Baker McKenzie, White & Case | [Perplexity — verify] |
| Existing statute YAML file contents | Direct file reads | [confirmed] |
| Skill SKILL.md content and divergence assessment | Direct file reads | [confirmed] |
| Employment-legal ZA practice profile template pattern | Direct file read | [confirmed] |
| Architecture and ADR decisions | Direct file reads of ARCHITECTURE.md and ADR-001 | [confirmed] |

---

## Implementation task sequence

Following the architecture guide (`jurisdictions/za/ARCHITECTURE.md`):

1. Statute YAML files — 4 new + extend 6 existing
2. Topic overlay markdown files — 6 files
3. Skill router (`jurisdictions/za/product-legal/router.md`)
4. Practice profile template (`jurisdictions/za/product-legal/practice-profile-template.md`)
5. Cold-start interview fork
6. Validation scripts — extend existing validators for product-legal
7. Scenario eval cases — 15 cases across 4 skills
8. Final validation run
