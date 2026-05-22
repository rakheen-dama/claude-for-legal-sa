# South African Product-Legal Overlay — Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build the complete South African overlay for the product-legal plugin — statute files, topic overlays, skill router, practice profile template, cold-start fork, validation, and eval cases.

**Architecture:** Additive overlays in `jurisdictions/za/product-legal/` following ADR-001. Router-based skill wiring: zero upstream SKILL.md changes except cold-start interview. Shared statute YAMLs in `jurisdictions/za/statutes/`, topic overlays organized by legal topic (not per skill), ZA practice profile template replaces US template for SA users.

**Tech Stack:** YAML (statute files, eval cases), Markdown (topic overlays, router, practice profile template), Python (validation script extensions)

**Spec:** `docs/superpowers/specs/2026-05-22-za-product-legal-expansion.md`

**Reference implementation:** `jurisdictions/za/employment-legal/` (phase 1, shipped)

---

## File structure

### New files

```
jurisdictions/za/statutes/
  lotteries.yaml                    # Lotteries Act 57/1997
  national-gambling.yaml            # National Gambling Act 7/2004
  merchandise-marks.yaml            # Merchandise Marks Act 17/1941
  films-publications.yaml           # Films & Publications Act 65/1996

jurisdictions/za/product-legal/
  router.md                         # Maps skills → topic files + statute files
  practice-profile-template.md      # ZA variant of product-legal/CLAUDE.md
  topics/
    consumer-protection.md          # CPA product safety, liability, unfair terms, plain language
    advertising-and-claims.md       # ARB Code, CPA s29-41, promotional competitions
    e-commerce-and-digital.md       # ECTA Chapter VII, POPIA s69, online marketing
    sector-regulatory-map.md        # SA regulator map replacing US sector overlay table
    fintech-and-credit.md           # NCA, FICA, FAIS, Banks Act, NPS Act
    content-and-minors.md           # Films & Publications Act, Children's Act, Gambling Act

jurisdictions/za/evals/product-legal/
  launch-review/
    case-01-b2c-saas-data-collection.yaml
    case-02-fintech-bnpl.yaml
    case-03-promotional-competition.yaml
  marketing-claims-review/
    case-01-performance-claims.yaml
    case-02-compliance-marketing.yaml
    case-03-implied-claims.yaml
    case-04-discount-pricing.yaml
  feature-risk-assessment/
    case-01-ai-recommendation.yaml
    case-02-ugc-platform.yaml
    case-03-iot-firmware.yaml
  is-this-a-problem/
    case-01-customer-logos.yaml
    case-02-auto-enroll-premium.yaml
    case-03-lucky-draw-referrals.yaml
    case-04-popia-compliant-claim.yaml
    case-05-wallet-topup.yaml
```

### Files to modify

```
jurisdictions/za/statutes/cpa.yaml          # Add 8 product-legal sections
jurisdictions/za/statutes/ecta.yaml         # Add e-commerce sections (s43-52)
jurisdictions/za/statutes/competition.yaml  # Add abuse of dominance for advertising
jurisdictions/za/statutes/nca.yaml          # Add credit marketing sections
jurisdictions/za/statutes/fica.yaml         # Add KYC/accountable institution sections
product-legal/skills/cold-start-interview/SKILL.md  # Add ZA fork after Part 0
scripts/validate-za-router.py               # Add product-legal to PRACTICE_AREAS
scripts/validate-za-templates.py            # Add product-legal to TEMPLATE_CONFIG
```

---

## Task 1: New statute YAML files

Create 4 new statute YAML files following the schema in `jurisdictions/za/ARCHITECTURE.md`.

**Files:**
- Create: `jurisdictions/za/statutes/lotteries.yaml`
- Create: `jurisdictions/za/statutes/national-gambling.yaml`
- Create: `jurisdictions/za/statutes/merchandise-marks.yaml`
- Create: `jurisdictions/za/statutes/films-publications.yaml`

- [ ] **Step 1: Create `lotteries.yaml`**

```yaml
statute: "Lotteries Act 57 of 1997"
authority: "National Lotteries Commission"
last_confirmed: "2026-05-22"
source_url: "https://www.gov.za/documents/lotteries-act"

sections:
  lottery_definition:
    ref: "Lotteries Act s1"
    value: "any scheme for distributing prizes by lot or chance"
    effective_from: "2000-03-01"
    effective_until: null
    effect: "A lottery includes any scheme or competition in which prizes are distributed by lot or chance and for which a consideration is paid. This definition determines the boundary between lawful promotional competitions (CPA s36) and unlawful lotteries."
    note: "The key element is consideration — if no purchase or payment is required for entry, the scheme is generally not a lottery under this Act."

  unlawful_lottery:
    ref: "Lotteries Act s54"
    value: "any lottery not authorised under this Act is unlawful"
    effective_from: "2000-03-01"
    effective_until: null
    effect: "No person may conduct a lottery unless authorised under this Act. An unlawful lottery is a criminal offence. Promotional competitions structured under CPA s36 are exempt if they comply with the CPA regulations for promotional competitions."

  promotional_competition_boundary:
    ref: "Lotteries Act s54 read with CPA s36"
    value: "promotional competitions under CPA are not lotteries if entry does not require consideration beyond normal transaction costs"
    effective_from: "2011-04-01"
    effective_until: null
    effect: "Since the CPA came into force, promotional competitions are regulated under CPA s36 and its regulations. A competition is a promotional competition (not a lottery) if entry is free or requires only the cost of standard communication (SMS, data, postage) and the competition is conducted to promote goods or services."
    note: "The line between CPA promotional competition and unlawful lottery turns on whether genuine consideration is required to enter."

  criminal_penalties:
    ref: "Lotteries Act s57"
    value: "fine or imprisonment"
    effective_from: "2000-03-01"
    effective_until: null
    effect: "Any person who contravenes the Act (including conducting an unlawful lottery) is guilty of an offence and liable to a fine or imprisonment. The severity depends on the nature and scale of the contravention."
```

- [ ] **Step 2: Create `national-gambling.yaml`**

```yaml
statute: "National Gambling Act 7 of 2004"
authority: "National Gambling Board"
last_confirmed: "2026-05-22"
source_url: "https://www.gov.za/documents/national-gambling-act"

sections:
  gambling_game_definition:
    ref: "NGA s1"
    value: "any game, electronic game, scheme, arrangement, system, plan, promotional competition, or device for determining a winner or allocating a prize by chance"
    effective_from: "2004-11-01"
    effective_until: null
    effect: "A gambling game means any game, electronic game, scheme, arrangement, system, plan, promotional competition or other device for determining a winner or allocating a prize by chance between two or more participants, where the winner or prize allocation is determined by the game, scheme, or device. This is the definition that determines whether a product feature constitutes gambling."

  closed_list_permitted_forms:
    ref: "NGA s3"
    value: "only casinos, bingo, betting, limited payout machines, and the national lottery are permitted"
    effective_from: "2004-11-01"
    effective_until: null
    effect: "Only the following forms of gambling are authorised: casino gambling, bingo, betting (including sports and horse-race betting), limited payout machines, and the national lottery. Any gambling activity not on this closed list cannot be licensed by any authority."

  online_gambling_prohibition:
    ref: "NGA s11"
    value: "interactive gambling generally prohibited"
    effective_from: "2004-11-01"
    effective_until: null
    effect: "No person may engage in, make available, or participate in interactive gambling (online gambling) within South Africa, except for licensed online sports betting. This affects loot boxes, virtual currencies with real-money redemption, and prediction markets."
    note: "Online sports betting is licensed at provincial level. All other forms of online gambling remain prohibited. Enforcement is evolving."

  advertising_restrictions:
    ref: "NGA s16"
    value: "gambling advertising must not target minors or promote irresponsible gambling"
    effective_from: "2004-11-01"
    effective_until: null
    effect: "Gambling advertising must not target minors, must include responsible gambling messaging, and must not misrepresent the likelihood of winning. Licensed operators must comply with advertising conditions in their licences."

  loot_box_and_gamification_risk:
    ref: "NGA s1 read with s3, s11"
    value: "loot boxes and gamification features with real-money redemption may constitute gambling"
    effective_from: "2004-11-01"
    effective_until: null
    effect: "In-app purchases that provide randomised rewards with real-money value (loot boxes, mystery boxes, spin-to-win with cash or redeemable prizes) may fall within the definition of gambling game if the outcome is determined by chance and the participant risks consideration. No SA court has ruled definitively on loot boxes, but the risk exists under the current definitions."
    note: "Purely cosmetic, non-tradeable rewards with no real-money redemption path are lower risk. Features where randomised items can be traded, sold, or redeemed for money carry higher risk."
```

- [ ] **Step 3: Create `merchandise-marks.yaml`**

```yaml
statute: "Merchandise Marks Act 17 of 1941"
authority: "Department of Trade, Industry and Competition"
last_confirmed: "2026-05-22"
source_url: "https://www.gov.za/documents/merchandise-marks-act"

sections:
  false_trade_description:
    ref: "MMA s2(1)"
    value: "applying a false trade description to goods is a criminal offence"
    effective_from: "1941-07-01"
    effective_until: null
    effect: "Any person who applies a false trade description to goods, or who sells or exposes for sale goods to which a false trade description is applied, commits an offence. A false trade description includes false indications of origin, composition, quality, strength, quantity, method of manufacture, or fitness for purpose."

  origin_claims:
    ref: "MMA s2(1)(a)"
    value: "false indications of origin are prohibited"
    effective_from: "1941-07-01"
    effective_until: null
    effect: "Goods must not bear false indications of where they were manufactured, produced, or assembled. Claims like 'Made in South Africa' or 'Proudly South African' must be accurate. Misleading origin claims are criminal offences."

  protected_marks_and_symbols:
    ref: "MMA s15"
    value: "certain marks, flags, and symbols are protected from commercial use"
    effective_from: "1941-07-01"
    effective_until: null
    effect: "The use of national flags, coats of arms, and certain official marks in connection with trade or business is restricted. Products must not bear marks that suggest government approval, endorsement, or certification unless actually authorised."
    note: "This includes SABS marks, government certification marks, and similar quality/approval symbols."

  quality_certification_claims:
    ref: "MMA s2(1) read with Standards Act 8 of 2008"
    value: "claiming SABS or NRCS certification without authorisation is prohibited"
    effective_from: "1941-07-01"
    effective_until: null
    effect: "Products must not display SABS marks, NRCS marks, or other certification marks unless the product has been certified by the relevant body. False certification claims are offences under both the MMA and the Standards Act."
```

- [ ] **Step 4: Create `films-publications.yaml`**

```yaml
statute: "Films and Publications Act 65 of 1996"
authority: "Film and Publication Board"
last_confirmed: "2026-05-22"
source_url: "https://www.gov.za/documents/films-and-publications-act"

sections:
  content_classification:
    ref: "FPA s16"
    value: "films, games, and certain publications must be classified before distribution"
    effective_from: "1996-11-01"
    effective_until: null
    effect: "Films, interactive computer games containing certain content, and certain publications must be submitted to the Film and Publication Board for classification before distribution. Classification determines age restrictions and required content advisories."

  online_content_regulation:
    ref: "FPA s24A-24C (as amended by Films and Publications Amendment Act 11 of 2019)"
    value: "online distributors may be required to register and comply with classification obligations"
    effective_from: "2019-10-01"
    effective_until: null
    effect: "Online distributors and platforms hosting user-generated content may be required to comply with classification standards, implement age-verification mechanisms, and take down prohibited or unclassified content. The 2019 amendments extended the FPB's jurisdiction to online content."
    note: "Implementation and enforcement of the 2019 amendments is still evolving. Regulations are expected to clarify specific obligations for platform operators."

  age_gating_requirements:
    ref: "FPA s16 read with Classification Guidelines"
    value: "age-restricted content must not be distributed to persons below the applicable age restriction"
    effective_from: "1996-11-01"
    effective_until: null
    effect: "Content classified with age restrictions (e.g., 13, 16, 18, X18, XX) must not be distributed to or made accessible by persons below the age restriction. Online platforms must implement reasonable age-verification or age-gating mechanisms for age-restricted content."

  prohibited_content:
    ref: "FPA s24B"
    value: "child sexual abuse material, bestiality, and certain extreme content are absolutely prohibited"
    effective_from: "1996-11-01"
    effective_until: null
    effect: "The possession, creation, production, distribution, or facilitation of child sexual abuse material is a criminal offence. Platforms must remove such content immediately upon becoming aware of it and report it to the relevant authorities."

  takedown_obligations:
    ref: "FPA s24C"
    value: "platforms must comply with takedown notices for prohibited or non-compliant content"
    effective_from: "2019-10-01"
    effective_until: null
    effect: "Online platforms and internet service providers must comply with takedown notices issued by the FPB for content that is prohibited, unclassified when classification is required, or distributed in contravention of classification conditions."
```

- [ ] **Step 5: Run statute validation**

Run: `python3 scripts/validate-za-statutes.py 2>&1 | grep -E '(lotteries|national-gambling|merchandise-marks|films-publications)'`

Expected: `OK` for all 4 new files with section counts.

- [ ] **Step 6: Commit**

```bash
git add jurisdictions/za/statutes/lotteries.yaml jurisdictions/za/statutes/national-gambling.yaml jurisdictions/za/statutes/merchandise-marks.yaml jurisdictions/za/statutes/films-publications.yaml
git commit -m "feat(za): add 4 new statute YAMLs for product-legal overlay

Lotteries Act 57/1997, National Gambling Act 7/2004,
Merchandise Marks Act 17/1941, Films & Publications Act 65/1996"
```

---

## Task 2: Extend existing statute YAML files

Add product-legal-relevant sections to 5 existing statute files.

**Files:**
- Modify: `jurisdictions/za/statutes/cpa.yaml`
- Modify: `jurisdictions/za/statutes/ecta.yaml`
- Modify: `jurisdictions/za/statutes/competition.yaml`
- Modify: `jurisdictions/za/statutes/nca.yaml`
- Modify: `jurisdictions/za/statutes/fica.yaml`

- [ ] **Step 1: Extend `cpa.yaml` — add 8 product-legal sections**

Append the following sections after the existing `industry_codes` section in `jurisdictions/za/statutes/cpa.yaml`:

```yaml
  plain_language:
    ref: "CPA s22"
    value: "notices, documents and visual representations must be in plain and understandable language"
    effective_from: "2011-04-01"
    effective_until: null
    effect: "A producer, importer, distributor or retailer must not market, supply, or offer goods or services in a manner that is misleading. All notices, documents and visual representations must be in plain and understandable language as described in s22(2). The National Consumer Commission may prescribe standards for plain language."

  misleading_marketing:
    ref: "CPA s29(b)"
    value: "marketing must not be misleading, fraudulent or deceptive in any way"
    effective_from: "2011-04-01"
    effective_until: null
    effect: "A supplier must not market goods or services in a manner that is reasonably likely to imply a false or misleading representation concerning those goods or services, or that constitutes a deceptive, misleading or fraudulent representation, or an unconscionable, unfair, unreasonable or unjust practice."

  bait_marketing:
    ref: "CPA s30"
    value: "advertising goods at a price the supplier does not intend to offer in reasonable quantities is prohibited"
    effective_from: "2011-04-01"
    effective_until: null
    effect: "A supplier must not advertise goods or services at a specified price if the supplier does not intend to offer those goods or services at that price for a reasonable period and in reasonable quantities. The supplier bears the onus of establishing that adequate quantities were available."

  promotional_competitions:
    ref: "CPA s36"
    value: "promotional competitions must comply with prescribed requirements"
    effective_from: "2011-04-01"
    effective_until: null
    effect: "Promotional competitions (prize draws, sweepstakes, giveaways tied to product promotion) must comply with the regulations made under s36. Requirements include: written rules, no entry fee beyond standard communication costs, disclosure of closing date and prize details, independent verification, POPIA-compliant data handling. Non-compliance is an offence."

  false_representations:
    ref: "CPA s41"
    value: "false, misleading or deceptive representations are prohibited"
    effective_from: "2011-04-01"
    effective_until: null
    effect: "A supplier must not make any false, misleading or deceptive representation concerning a material fact to a consumer by words, depiction, or conduct. This includes representations about the nature, properties, advantages, uses, quality, standard, grade, style, origin, or characteristics of goods or services."

  unfair_contract_terms:
    ref: "CPA s48-52"
    value: "unfair, unreasonable or unjust contract terms are prohibited"
    effective_from: "2011-04-01"
    effective_until: null
    effect: "A supplier must not supply goods or services under terms that are unfair, unreasonable or unjust (s48). Notice is required for terms that limit liability, assume risk, impose indemnity, or are unusual or adverse (s49). Certain terms are outright prohibited (s51), including terms that waive CPA rights or purport to exclude strict product liability under s61."

  product_quality_safety:
    ref: "CPA s55-58"
    value: "consumers have the right to safe, good quality goods"
    effective_from: "2011-04-01"
    effective_until: null
    effect: "Every consumer has the right to receive goods that are reasonably suitable for their purpose, of good quality, in good working order, and free of defects (s55). There is an implied warranty of quality for 6 months (s56). Suppliers must provide adequate safety warnings (s58) including clear instructions for safe handling and notification of any hazardous or unsafe characteristics."

  strict_product_liability:
    ref: "CPA s61"
    value: "strict, no-fault liability for harm caused by defective goods"
    effective_from: "2011-04-01"
    effective_until: null
    effect: "The producer, importer, distributor and retailer are each liable jointly and severally for any harm caused wholly or partly by a product defect, product failure, hazard or unsafe product characteristic, or inadequate instructions or warnings. Liability is strict (no fault required). Harm includes death, injury, illness, and loss of or physical damage to property. This liability cannot be excluded or limited by contract (s51(1)(c))."
    note: "The application of s61 to pure software/SaaS is untested in SA courts. For hardware with embedded software, firmware, and IoT devices, s61 clearly applies."
```

- [ ] **Step 2: Extend `ecta.yaml` — add e-commerce consumer protection sections**

Append after the existing `cryptography_provider_registration` section:

```yaml
  ecommerce_mandatory_disclosures:
    ref: "ECTA s43(1)"
    value: "online suppliers must display specified information on their website"
    effective_from: "2002-08-30"
    effective_until: null
    effect: "Any person offering goods or services for sale by way of an electronic transaction must make the following information available on the website: full name and legal status, registration number, physical address for service, telephone number, email address, website address, membership of self-regulatory bodies, terms and conditions, return/refund policy, security procedures and privacy policy, and full price including taxes and delivery."
    note: "Failure to comply with s43 is a criminal offence under s43(5). Non-compliance may also undermine enforceability of T&Cs."

  ecommerce_review_and_correct:
    ref: "ECTA s43(2)"
    value: "consumer must be given opportunity to review and correct errors before placing order"
    effective_from: "2002-08-30"
    effective_until: null
    effect: "A supplier must provide the consumer with an opportunity to review the entire transaction, including all terms, and to correct any errors, before the order is finally placed."

  ecommerce_cooling_off:
    ref: "ECTA s44"
    value: 7
    unit: "days"
    effective_from: "2002-08-30"
    effective_until: null
    effect: "A consumer is entitled to cancel a transaction concluded by way of electronic communication within 7 days of receiving the goods or agreeing to the service, without reason or penalty. The supplier must return all payments within 30 days of cancellation. This right applies to natural persons only."
    note: "More generous than the CPA direct marketing cooling-off (5 business days under s16). ECTA and CPA apply in parallel."

  ecommerce_performance:
    ref: "ECTA s46"
    value: 30
    unit: "days"
    effective_from: "2002-08-30"
    effective_until: null
    effect: "A supplier must perform the obligations under an electronic transaction within 30 days of the date on which the order was placed, unless the parties agreed otherwise. If the supplier is unable to perform, the supplier must notify the consumer and refund all payments within 30 days."

  spam_unsolicited_communications:
    ref: "ECTA s45"
    value: "unsolicited electronic communications must include opt-out and source identification"
    effective_from: "2002-08-30"
    effective_until: null
    effect: "Any person who sends unsolicited commercial communications must provide the consumer with an option to cancel the subscription and identify the source from which the consumer's contact details were obtained. No binding agreement may be concluded solely on the basis of unsolicited communication where the consumer has not responded."
    note: "Overlaps with POPIA s69 for electronic direct marketing. Both regimes must be complied with."
```

- [ ] **Step 3: Extend `competition.yaml` — add abuse of dominance for advertising context**

Append after the existing `national_security_review` section:

```yaml
  abuse_of_dominance_exclusionary:
    ref: "Competition Act s8(1)(d)"
    value: "dominant firms must not engage in exclusionary acts"
    effective_from: "1999-09-01"
    effective_until: null
    effect: "A dominant firm may not engage in an exclusionary act unless the firm can show that the act is technologically justified, efficiency-enhancing, or pro-competitive. Relevant for tech platforms: self-preferencing in search/rankings, restricting interoperability, tying services, imposing unfair trading conditions on third-party sellers or app developers."
    note: "The Competition Commission has conducted market inquiries into digital platforms, including e-commerce marketplaces, app stores, and food delivery platforms."

  comparative_advertising_competition:
    ref: "Competition Act s8(1)(d) read with CPA s29"
    value: "comparative advertising by dominant firms may constitute exclusionary conduct"
    effective_from: "1999-09-01"
    effective_until: null
    effect: "Comparative advertising that denigrates competitors or uses market dominance to unfairly disadvantage them may constitute exclusionary conduct under s8. Even non-dominant firms must ensure comparative claims are truthful and substantiated under CPA s29 and the ARB Code."
```

- [ ] **Step 4: Extend `nca.yaml` — add credit marketing and disclosure sections**

Append after the existing `administrative_fines` section:

```yaml
  credit_marketing_advertising:
    ref: "NCA s74-76"
    value: "credit marketing must comply with disclosure and fairness requirements"
    effective_from: "2007-06-01"
    effective_until: null
    effect: "Advertising and marketing of credit must include clear disclosure of interest rates, fees, total cost of credit, and material terms. Prohibited practices include: misleading statements about the cost, nature, or risk of credit; pressure selling; and targeting consumers who are likely to be unable to repay."
    note: "Applies to BNPL, salary advance, revolving credit, and instalment products. Products that defer payment or charge interest/fees contingent on time are likely credit agreements under the NCA."

  credit_disclosure_plain_language:
    ref: "NCA s63-66"
    value: "pre-agreement statements and quotations must be in plain language"
    effective_from: "2007-06-01"
    effective_until: null
    effect: "Before a credit agreement is entered into, the credit provider must provide the consumer with a pre-agreement statement and quotation that sets out the proposed terms in plain and understandable language, including the interest rate, fees, total cost of credit, and the consumer's rights."

  reckless_credit_assessment:
    ref: "NCA s80-81"
    value: "credit provider must conduct an affordability assessment before granting credit"
    effective_from: "2007-06-01"
    effective_until: null
    effect: "A credit provider must take reasonable steps to assess whether the consumer understands the risks and costs of the proposed credit, and whether the consumer can afford the credit without becoming over-indebted. Failure to conduct an affordability assessment renders the agreement reckless credit. A court or the NCR may set aside a reckless credit agreement."
    note: "This is the highest-risk provision for fintech BNPL products. If the product is classified as credit, every transaction needs an affordability assessment."
```

- [ ] **Step 5: Extend `fica.yaml` — add KYC and accountable institution sections for product context**

Append after the existing sections:

```yaml
  accountable_institution_definition:
    ref: "FICA Schedule 1"
    value: "banks, financial services providers, and other designated entities are accountable institutions"
    effective_from: "2003-02-01"
    effective_until: null
    effect: "Schedule 1 lists the categories of accountable institutions, including banks, mutual banks, long-term and short-term insurers, financial services providers under FAIS, persons who carry on the business of dealing in foreign exchange, and other designated entities. If a fintech product provider falls within Schedule 1, it must comply with all FICA obligations."
    note: "Crypto asset service providers are being brought into the FICA framework via regulatory amendments."

  customer_due_diligence:
    ref: "FICA s21"
    value: "accountable institutions must identify and verify the identity of clients"
    effective_from: "2017-10-02"
    effective_until: null
    effect: "An accountable institution must establish and verify the identity of all prospective clients before establishing a business relationship or concluding a single transaction above the prescribed threshold. Verification must be on a risk-sensitive basis. This affects product onboarding flows, KYC UX design, and data collection requirements."
```

- [ ] **Step 6: Run statute validation**

Run: `python3 scripts/validate-za-statutes.py`

Expected: `OK` for all statute files, including the extended ones with their new section counts.

- [ ] **Step 7: Commit**

```bash
git add jurisdictions/za/statutes/cpa.yaml jurisdictions/za/statutes/ecta.yaml jurisdictions/za/statutes/competition.yaml jurisdictions/za/statutes/nca.yaml jurisdictions/za/statutes/fica.yaml
git commit -m "feat(za): extend 5 statute YAMLs with product-legal sections

CPA: s22, s29-30, s36, s41, s48-52, s55-58, s61
ECTA: s43-46 e-commerce consumer protection
Competition: abuse of dominance, comparative advertising
NCA: s63-66, s74-76, s80-81 credit marketing
FICA: accountable institutions, KYC for fintech"
```

---

## Task 3: Topic overlay markdown files

Create 6 topic overlay files. Each follows the pattern established by `jurisdictions/za/employment-legal/topics/dismissal.md` — markdown with SA statute references, procedural checklists, and flag tables. No US legal concepts.

**Files:**
- Create: `jurisdictions/za/product-legal/topics/consumer-protection.md`
- Create: `jurisdictions/za/product-legal/topics/advertising-and-claims.md`
- Create: `jurisdictions/za/product-legal/topics/e-commerce-and-digital.md`
- Create: `jurisdictions/za/product-legal/topics/sector-regulatory-map.md`
- Create: `jurisdictions/za/product-legal/topics/fintech-and-credit.md`
- Create: `jurisdictions/za/product-legal/topics/content-and-minors.md`

Each topic file must:
- Start with a heading and one-liner explaining what it covers and which skills load it
- Use SA statute references in short format (CPA s29, POPIA s22, ECTA s43)
- Include flag tables matching the format in the spec's high-risk flag table
- Reference no US legal concepts (FTC, NAD, CCPA, COPPA, HIPAA, GLBA, CFPB, CAN-SPAM, TCPA, ROSCA, state UDAP, FRCP 26(b)(3), "at-will")

- [ ] **Step 1: Create `consumer-protection.md`**

Write `jurisdictions/za/product-legal/topics/consumer-protection.md`. Structure:

```markdown
# Consumer Protection — South African Framework

This overlay covers the CPA consumer protection framework for product launches,
feature risk, and triage. Loaded by launch-review, feature-risk-assessment,
and is-this-a-problem skills when jurisdiction = ZA.

---

## 1. CPA applicability

[CPA s5 scope. Juristic person R2m threshold. Natural persons always covered.
When CPA does and does not apply to B2B SaaS.]

## 2. Product quality and safety (CPA s55-58)

[Right to safe, good quality goods. Implied warranty of quality (s56, 6 months).
Safety warnings requirement (s58). Product safety monitoring obligation (s60).]

## 3. Strict product liability (CPA s61)

[Strict no-fault liability. Joint and several across supply chain. Cannot contract
out (s51). Application to digital products. Harm covered: death, injury, property
damage. The s61 flag table from the spec.]

## 4. Unfair contract terms (CPA s48-52)

[Prohibition on unfair, unreasonable, unjust terms. Notice requirements for adverse
terms (s49). Prohibited terms (s51). SaaS T&C common pitfalls: overbroad liability
exclusions, one-sided termination, unfair auto-renewal, hidden fees, dense legalese
violating s22 plain language.]

## 5. Plain language requirement (CPA s22)

[All notices, documents, visual representations must be in plain and understandable
language. Applies to T&Cs, privacy policies, product disclosures, marketing.]

## 6. Cooling-off rights

[CPA s16 direct marketing cooling-off (5 business days). ECTA s44 e-commerce
cooling-off (7 days). How they interact. When each applies.]

## 7. NCC enforcement

[NCC complaint procedure (s71). Compliance notices. Referral to National Consumer
Tribunal. Administrative fines (s112 — up to R1m or 10% turnover). Recent
enforcement trends (62+ compliance notices 2025-26).]

## 8. High-risk flag checklist

[Flags 1, 2, 9 from the spec's flag table, formatted as a checklist for product
counsel reviewing a launch or feature.]
```

Reference the spec (section 6, high-risk flags 1, 2, 9) for the flag table content. Reference Perplexity research from the spec's source provenance log for enforcement examples.

Target length: 150-200 lines, matching employment-legal topic files.

- [ ] **Step 2: Create `advertising-and-claims.md`**

Write `jurisdictions/za/product-legal/topics/advertising-and-claims.md`. Structure:

```markdown
# Advertising & Marketing Claims — South African Framework

This overlay covers advertising regulation and marketing claims review for SA
product counsel. Loaded by marketing-claims-review, launch-review (category 7),
and is-this-a-problem skills when jurisdiction = ZA.

---

## 1. Statutory framework

[CPA s29 (misleading marketing), s30 (bait marketing), s41 (false representations).
This is the statutory backstop — enforceable by NCC with penalties.]

## 2. ARB Code of Advertising Practice

[Self-regulatory, not statutory. Based on International Code of Advertising Practice.
Core principles: legal, decent, honest, truthful. ARB rulings force ad withdrawal.
Widely followed — broadcasters and publishers require compliance.]

### 2.1 Substantiation requirements

[ARB substantiation clause. Documentary evidence held before publication.
Independent, objective, adequate evidence. Puffery exception. When claims
are objectively verifiable.]

### 2.2 Comparative advertising

[Comparisons must be fair, objective, substantiated. Products promoted on own
merits, not demerits of competitors. Competition Act intersection for dominant
firms (s8(1)(d)).]

## 3. Claim taxonomy under SA law

[Same categories as upstream (puffery, factual, comparative, implied, absolute)
but with SA substantiation standards and enforcement bodies. SA-specific examples
for each category.]

## 4. Promotional competitions (CPA s36 + Lotteries Act)

[When a competition is lawful under CPA s36 vs unlawful lottery. Requirements:
free entry (or standard communication cost only), written rules, prize disclosure,
independent oversight. POPIA obligations for entrant data.]

## 5. Merchandise Marks Act

[False trade descriptions. Origin claims. Protected marks and symbols.
SABS/NRCS certification claims.]

## 6. High-risk flag checklist

[Flags 3, 5, 11 from the spec's flag table.]
```

Target length: 180-220 lines.

- [ ] **Step 3: Create `e-commerce-and-digital.md`**

Write `jurisdictions/za/product-legal/topics/e-commerce-and-digital.md`. Structure:

```markdown
# E-Commerce & Digital Transactions — South African Framework

This overlay covers ECTA e-commerce obligations and the POPIA/CPA/ECTA interplay
for online product marketing. Loaded by launch-review, marketing-claims-review,
and is-this-a-problem skills when jurisdiction = ZA.

---

## 1. ECTA mandatory disclosures (s43)

[Full list of required website disclosures. Criminal offence for non-compliance
(s43(5)). Enforceability impact — non-compliant T&Cs may be unenforceable.]

## 2. Transaction mechanics

[Review-and-correct (s43(2)). Cooling-off 7 days (s44). Performance within 30 days
(s46). Refund obligations.]

## 3. Spam and unsolicited communications (ECTA s45 + POPIA s69)

[ECTA requirements: opt-out, source identification. POPIA s69: consent for
electronic direct marketing. DMASA Code. How the three frameworks overlap.
Non-customers vs existing customers.]

## 4. The triple-compliance problem

[ECTA + CPA + POPIA apply in parallel for online marketing. Compliance with one
does not excuse non-compliance with others. Practical checklist for ensuring
all three are satisfied.]

## 5. High-risk flag checklist

[Flag 6 from the spec's flag table.]
```

Target length: 120-160 lines.

- [ ] **Step 4: Create `sector-regulatory-map.md`**

Write `jurisdictions/za/product-legal/topics/sector-regulatory-map.md`. This is the SA replacement for the US sector overlay hints table in the launch-review skill. Structure:

```markdown
# SA Sector Regulatory Map — Product Legal

This overlay replaces the US sector overlay hints table in launch-review. When
jurisdiction = ZA, use this table instead of the US-centric COPPA/FTC/GLBA/HIPAA
sector overlays. Loaded by launch-review, feature-risk-assessment, and
is-this-a-problem skills when jurisdiction = ZA.

---

## Sector overlay table

| Sector | SA regulatory regimes to surface | Key statutes | Regulator(s) |
|---|---|---|---|
| **Children / minors** | [Children's Act, POPIA s34-35, Films & Publications Act, Protection from Harassment Act] | [statutes] | [FPB, Information Regulator] |
| **Gaming / loot boxes / gamification** | [National Gambling Act, Lotteries Act, CPA s36, provincial gambling acts] | [statutes] | [NGB, provincial gambling boards] |
| **Financial / fintech** | [NCA, FICA, FAIS, Banks Act, NPS Act, Insurance Act, CISCA] | [statutes] | [FSCA, SARB, NCR] |
| **Health** | [Medicines Act, NHA, Health Professions Act, Medical Schemes Act] | [statutes] | [SAHPRA, HPCSA] |
| **Consumer / retail / marketing** | [CPA s29-41, ARB Code, ECTA, Merchandise Marks Act, Lotteries Act (promotional competitions)] | [statutes] | [NCC, ARB, Consumer Tribunal] |
| **Content / UGC platforms** | [Films & Publications Act, Cybercrimes Act, ECTA takedown, Protection from Harassment Act] | [statutes] | [FPB, ICASA] |
| **Telecom / OTT** | [Electronic Communications Act, ICASA regulations, CPA] | [statutes] | [ICASA] |

## Regulator contact and posture map

[For each major regulator (NCC, Information Regulator, Competition Commission, ARB,
ICASA, SAHPRA, FSCA/SARB, NGB, FPB): one-paragraph summary of what they enforce,
current enforcement posture, and how product counsel typically interacts with them.]

## Multi-regulator escalation pattern

[Flag 8 from the spec — same conduct triggers multiple regulators. How to coordinate.]
```

Target length: 150-180 lines.

- [ ] **Step 5: Create `fintech-and-credit.md`**

Write `jurisdictions/za/product-legal/topics/fintech-and-credit.md`. Structure:

```markdown
# Fintech & Credit — South African Framework

This overlay covers NCA, FICA, and related financial regulation for product features
involving payments, credit, or stored value. Conditionally loaded by launch-review
and feature-risk-assessment when the product touches fintech verticals.

---

## 1. Is this credit? (NCA applicability)

[When a product feature constitutes credit under the NCA. BNPL, salary advance,
instalment, revolving credit. The key test: deferred payment or fees contingent
on time. Registration requirement (s40).]

## 2. Credit marketing obligations (NCA s74-76)

[Disclosure requirements: APR, fees, total cost. Prohibition on misleading
credit advertising. "0% interest" with hidden fees. Pre-agreement statements.]

## 3. Reckless credit (NCA s80-81)

[Affordability assessment requirement. Consequences: agreement set aside.
Impact on BNPL product design.]

## 4. FICA obligations

[Accountable institutions (Schedule 1). KYC/CDD requirements. Suspicious
transaction reporting. Product onboarding flow implications.]

## 5. Stored value and payment systems

[Banks Act (deposit-taking). NPS Act (payment system participation).
When a wallet/stored-value feature needs a banking licence or partnership.]

## 6. High-risk flag checklist

[Flag 7 from the spec's flag table.]
```

Target length: 140-170 lines.

- [ ] **Step 6: Create `content-and-minors.md`**

Write `jurisdictions/za/product-legal/topics/content-and-minors.md`. Structure:

```markdown
# Content Moderation & Minors — South African Framework

This overlay covers Films & Publications Act, Children's Act, and gambling
regulation for product features involving content, UGC, or minors. Conditionally
loaded by launch-review and feature-risk-assessment for children/gaming verticals.

---

## 1. Films & Publications Act framework

[Content classification. Online content amendments (2019). Age-gating.
Platform registration obligations. Takedown obligations.]

## 2. Children's Act obligations

[Best interests standard. Parental consent. Capacity and guardianship
intersecting with POPIA "competent person" concept. Reporting obligations.]

## 3. POPIA children's data (s34-35)

[Special processing conditions for children's data. Definition of child
(under 18). Competent person consent. Prior authorisation from Information
Regulator for certain processing.]

## 4. Gambling and gamification

[National Gambling Act definitions. Closed list of permitted forms. Online
gambling prohibition. Loot box risk analysis. Prize mechanics assessment
framework.]

## 5. Online safety features

[Protection from Harassment Act. Cybercrimes Act harmful communications.
Platform design obligations: reporting tools, blocking, moderation.]
```

Target length: 130-160 lines.

- [ ] **Step 7: Commit**

```bash
git add jurisdictions/za/product-legal/topics/
git commit -m "feat(za): add 6 product-legal topic overlay files

consumer-protection, advertising-and-claims, e-commerce-and-digital,
sector-regulatory-map, fintech-and-credit, content-and-minors"
```

---

## Task 4: Skill router

Create the router mapping skills to topic files and statute files.

**Files:**
- Create: `jurisdictions/za/product-legal/router.md`

- [ ] **Step 1: Create `router.md`**

Follow the exact format of `jurisdictions/za/employment-legal/router.md`:

```markdown
# Skill Router — South African Product Law Overlay

When jurisdiction = ZA, skills load the topic overlays and statute files listed below.

Topic files resolve to: `jurisdictions/za/product-legal/topics/{name}.md`
Statute files resolve to: `jurisdictions/za/statutes/{name}.yaml`

```yaml
launch-review:
  topics: [consumer-protection, advertising-and-claims, e-commerce-and-digital, sector-regulatory-map]
  statutes: [cpa, ecta, popia, competition, lotteries, merchandise-marks]

marketing-claims-review:
  topics: [advertising-and-claims, e-commerce-and-digital]
  statutes: [cpa, ecta, lotteries, merchandise-marks, competition]

feature-risk-assessment:
  topics: [consumer-protection, sector-regulatory-map]
  statutes: [cpa, popia, ecta]

is-this-a-problem:
  topics: [consumer-protection, advertising-and-claims, sector-regulatory-map]
  statutes: [cpa, popia, ecta, competition]

cold-start-interview:
  topics: []
  statutes: [cpa, ecta, popia, nca, fica, competition]
```
```

Note: the conditional loading for fintech and content/minors topics is documented in `sector-regulatory-map.md` — when a launch or feature touches those verticals, the skill loads the additional topic file. The router lists the base topics; conditional topics are loaded per the sector map.

- [ ] **Step 2: Run router validation**

Run: `python3 scripts/validate-za-router.py 2>&1 | grep product-legal`

Expected: `FAIL` — product-legal is not yet in the validator's PRACTICE_AREAS list. This is expected and fixed in Task 6.

- [ ] **Step 3: Commit**

```bash
git add jurisdictions/za/product-legal/router.md
git commit -m "feat(za): add product-legal skill router"
```

---

## Task 5: Practice profile template

Create the ZA practice profile template. Follow the pattern of `jurisdictions/za/employment-legal/practice-profile-template.md`.

**Files:**
- Create: `jurisdictions/za/product-legal/practice-profile-template.md`

- [ ] **Step 1: Write the practice profile template**

The template must include:
1. Configuration preamble with `JURISDICTION OVERLAY` instruction pointing to `jurisdictions/za/product-legal/router.md`
2. `# Product Legal Practice Profile — South Africa` heading
3. `## Who we are` — company info + B-BBEE level
4. `## Who's using this` — role with SA legal practitioner options ("Admitted attorney or advocate under Legal Practice Act 28 of 2014")
5. `## Available integrations` — same as US template
6. `## Outputs` — SA work-product header with privilege caveat block (follow employment-legal pattern exactly):
   - Attorney: `PRIVILEGED & CONFIDENTIAL — PREPARED BY/AT THE DIRECTION OF LEGAL COUNSEL FOR THE PURPOSE OF PROVIDING LEGAL ADVICE`
   - Non-lawyer: `CONFIDENTIAL — NOT LEGAL ADVICE — CONSULT AN ADMITTED ATTORNEY OR ADVOCATE BEFORE ACTING`
   - SA privilege caveat: no "ATTORNEY WORK PRODUCT" doctrine, in-house commercial-vs-legal capacity, litigation privilege, product-legal-specific note about launch review memos
7. Reviewer note format (same as US)
8. Decision posture (same as US)
9. Shared guardrails — SA-adjusted (example: BCEA/CPA not FLSA in "verify user-stated facts")
10. `## Regulatory posture` — **NEW** — NCC, Information Regulator, Competition Commission, ARB, ICASA, SAHPRA, NGB/FPB, FSCA/SARB with PLACEHOLDERs
11. `## B-BBEE considerations` — **NEW** — level, scorecard, procurement implications
12. `## CPA compliance posture` — **NEW** — s5 applicability, plain language, unfair terms, product liability, safety monitoring
13. `## Promotional competitions` — **NEW** — whether company runs them, compliance approach, T&C template
14. Scaffolding, proportionality, jurisdiction recognition (SA-adjusted — flag non-SA jurisdictions)
15. `## Launch review process` — same structure, PLACEHOLDERs
16. `## Review framework` — 8 categories with SA regulatory context
17. `## Risk calibration` — same structure, PLACEHOLDERs
18. `## Marketing claims` — SA substantiation standard (ARB + CPA s29-41), comparative advertising, promotional competitions
19. `## Escalation` — SA forums: NCC, Information Regulator, Competition Commission, ARB, Consumer Tribunal
20. `## Connected systems` — same as US
21. `## Seed reviews` — same as US
22. Currency watch, matter workspaces, large input/output, retrieved-content trust (carried from US, SA-adjusted where needed)

Use the US template (`product-legal/CLAUDE.md`) as the starting scaffold and the ZA employment-legal template (`jurisdictions/za/employment-legal/practice-profile-template.md`) as the ZA-specific pattern reference.

- [ ] **Step 2: Verify template has no US-specific terms outside privilege caveat**

Run a manual grep for US-forbidden terms:

```bash
grep -inE '\bFTC\b|\bNAD\b|\bCCPA\b|\bCOPPA\b|\bHIPAA\b|\bGLBA\b|\bCFPB\b|\bCAN-SPAM\b|\bTCPA\b|\bROSCA\b|\bat-will\b|\bFRCP\b|\bFMLA\b|\bFLSA\b' jurisdictions/za/product-legal/practice-profile-template.md
```

Expected: no matches, or matches only within the privilege caveat section explaining that "ATTORNEY WORK PRODUCT" is a US doctrine.

- [ ] **Step 3: Commit**

```bash
git add jurisdictions/za/product-legal/practice-profile-template.md
git commit -m "feat(za): add product-legal ZA practice profile template"
```

---

## Task 6: Extend validation scripts

Add product-legal to the router validator and template validator.

**Files:**
- Modify: `scripts/validate-za-router.py`
- Modify: `scripts/validate-za-templates.py`

- [ ] **Step 1: Add product-legal to `validate-za-router.py`**

Add the following entry to the `PRACTICE_AREAS` list in `scripts/validate-za-router.py`, after the `corporate-legal` entry:

```python
    {
        "name": "product-legal",
        "router": REPO_ROOT / "jurisdictions" / "za" / "product-legal" / "router.md",
        "skills_dir": REPO_ROOT / "product-legal" / "skills",
        "topics_dir": REPO_ROOT / "jurisdictions" / "za" / "product-legal" / "topics",
    },
```

- [ ] **Step 2: Add product-legal to `validate-za-templates.py`**

Add the following entry to the `TEMPLATE_CONFIG` dict in `scripts/validate-za-templates.py`:

```python
    "product-legal": {
        "path": ROOT / "jurisdictions" / "za" / "product-legal" / "practice-profile-template.md",
        "required_sections": [
            "Who we are", "Who's using this", "Regulatory posture",
            "B-BBEE considerations", "CPA compliance posture",
            "Promotional competitions", "Review framework",
            "Risk calibration", "Marketing claims",
            "Escalation", "Outputs", "Seed reviews",
        ],
        "sa_required_terms": [
            "CPA", "POPIA", "ECTA", "ARB", "NCC", "B-BBEE",
            "admitted attorney", "legal professional privilege",
            "Information Regulator", "Consumer Tribunal",
        ],
        "us_forbidden": [
            (r"\bFTC\b", "FTC"), (r"\bNAD\b", "NAD"),
            (r"\bCCPA\b", "CCPA"), (r"\bCOPPA\b", "COPPA"),
            (r"\bHIPAA\b", "HIPAA"), (r"\bGLBA\b", "GLBA"),
            (r"\bCFPB\b", "CFPB"), (r"\bCAN-SPAM\b", "CAN-SPAM"),
            (r"\bTCPA\b", "TCPA"), (r"\bROSCA\b", "ROSCA"),
            (r"\bFMLA\b", "FMLA"), (r"\bFLSA\b", "FLSA"),
            (r"\bat-will\b", "at-will"),
        ],
    },
```

- [ ] **Step 3: Run all three validators**

```bash
python3 scripts/validate-za-statutes.py && python3 scripts/validate-za-router.py && python3 scripts/validate-za-templates.py
```

Expected: all three pass with `OK` for product-legal entries.

- [ ] **Step 4: Commit**

```bash
git add scripts/validate-za-router.py scripts/validate-za-templates.py
git commit -m "feat(za): extend validators for product-legal overlay"
```

---

## Task 7: Cold-start interview fork

Add the ZA fork to the product-legal cold-start interview.

**Files:**
- Modify: `product-legal/skills/cold-start-interview/SKILL.md`

- [ ] **Step 1: Read the current cold-start interview SKILL.md completely**

Read `product-legal/skills/cold-start-interview/SKILL.md` in full to find the fork point. The ZA fork goes after Part 0 (orientation, practice setting, install scope check), following the same pattern as the employment-legal cold-start.

- [ ] **Step 2: Add ZA jurisdiction fork**

After the Part 0 section (look for the orientation/fork preamble that ends with the 2-minute vs 15-minute choice), insert a jurisdiction detection and fork block. The fork should:

1. Check `company-profile.md` for `jurisdiction: ZA`
2. If ZA: route into the ZA-specific question path (8 must-have + 4 nice-to-have questions from the spec, section 5)
3. Write to the ZA practice profile template at `jurisdictions/za/product-legal/practice-profile-template.md` instead of the US template
4. Add the router instruction to the configuration preamble

Follow the exact same fork pattern used in the employment-legal cold-start. The fork text should be clearly marked with comments like `<!-- ZA JURISDICTION FORK — START -->` and `<!-- ZA JURISDICTION FORK — END -->` for maintainability.

The 8 must-have ZA questions (from spec section 5):
1. Role (admitted attorney/advocate vs non-lawyer) — maps to `## Who's using this`
2. B2C/B2B/both + CPA juristic person threshold — maps to `## CPA compliance posture`
3. SA regulator interactions (NCC, IR, Competition Commission, ARB, etc.) — maps to `## Regulatory posture`
4. Product verticals (fintech, health-tech, children, gaming, content, telecom) — maps to router conditional topics
5. Promotional competitions Y/N — maps to `## Promotional competitions`
6. B-BBEE level — maps to `## B-BBEE considerations`
7. Formal gate vs advisory — maps to `## Launch review process → Sign-off`
8. Escalation contacts per regulator — maps to `## Escalation`

The 4 nice-to-have ZA questions:
9. ARB/DMASA membership
10. Substantiation file location
11. Past NCC/ARB/Competition Commission complaints
12. Children's data processing

- [ ] **Step 3: Commit**

```bash
git add product-legal/skills/cold-start-interview/SKILL.md
git commit -m "feat(za): add ZA fork to product-legal cold-start interview"
```

---

## Task 8: Scenario eval cases

Create 15 eval case YAML files following the format in `jurisdictions/za/evals/regulatory-legal/`.

**Files:**
- Create: 15 YAML files under `jurisdictions/za/evals/product-legal/`

Each eval case uses this schema:
```yaml
name: "descriptive name"
skill: skill-name
input: |
  fact pattern description
expected_flags:
  - "flag description"
expected_statutes:
  - "statute reference"
must_not_contain:
  - "US concept that must not appear"
notes: |
  What this case tests.
```

- [ ] **Step 1: Create launch-review eval cases (3 files)**

Create `jurisdictions/za/evals/product-legal/launch-review/` directory and the 3 case files using the exact scenarios from spec section 7:

**`case-01-b2c-saas-data-collection.yaml`** — B2C SaaS launch with new location data collection, "AI-powered" marketing claim. Tests: POPIA new collection, CPA product safety, AI governance flag, marketing claims substantiation. Must not contain: FTC, CCPA, COPPA, HIPAA.

**`case-02-fintech-bnpl.yaml`** — BNPL checkout with "0% interest" copy. Tests: NCA credit compliance, NCA marketing disclosure, CPA unfair terms, POPIA financial data. Must not contain: CFPB, Reg Z, Reg E, TILA, GLBA.

**`case-03-promotional-competition.yaml`** — Spin-the-wheel with R50k prize. Tests: CPA s36, Lotteries Act, POPIA s69, ECTA s43. Must not contain: State sweepstakes law, FTC, CAN-SPAM, ROSCA.

- [ ] **Step 2: Create marketing-claims-review eval cases (4 files)**

Create `jurisdictions/za/evals/product-legal/marketing-claims-review/` directory and 4 case files from spec section 7:

**`case-01-performance-claims.yaml`** — "SA's fastest", "10x faster", "500+ companies". Must not contain: FTC Act § 5, Lanham Act, NAD, state UDAP.

**`case-02-compliance-marketing.yaml`** — "Fully POPIA compliant. FSCA approved. 100% safe." Must not contain: FTC Endorsement Guides, SEC, FINRA.

**`case-03-implied-claims.yaml`** — "Secure alternative to [Competitor]. Built for healthcare." Must not contain: HIPAA, FDA SaMD, FTC Health Breach Notification Rule.

**`case-04-discount-pricing.yaml`** — "Was R999 — now R299. Limited time. Save 70%." Must not contain: FTC Guides Against Deceptive Pricing, state UDAP.

- [ ] **Step 3: Create feature-risk-assessment eval cases (3 files)**

Create `jurisdictions/za/evals/product-legal/feature-risk-assessment/` directory and 3 case files:

**`case-01-ai-recommendation.yaml`** — ML product recommendations. Must not contain: CCPA opt-out, GDPR Art. 22, Colorado AI Act, EU AI Act.

**`case-02-ugc-platform.yaml`** — Video upload/sharing feature. Must not contain: CDA § 230, DMCA, COPPA safe harbor, EU Digital Services Act.

**`case-03-iot-firmware.yaml`** — OTA firmware update, 200 previously bricked units. Must not contain: US product liability (Restatement Third), CPSC, state lemon laws.

- [ ] **Step 4: Create is-this-a-problem eval cases (5 files)**

Create `jurisdictions/za/evals/product-legal/is-this-a-problem/` directory and 5 case files:

**`case-01-customer-logos.yaml`** — "Can we use customer logos on pricing page?" Expected: ⚠️ Needs a look. Trap: CPA s11.

**`case-02-auto-enroll-premium.yaml`** — Auto-enroll in converting free trial. Expected: 🛑 Hold. Trap: CPA s48, ECTA cooling-off, dark patterns.

**`case-03-lucky-draw-referrals.yaml`** — Lucky draw for referrals. Expected: ⚠️ Needs a look. Trap: CPA s36 + Lotteries Act.

**`case-04-popia-compliant-claim.yaml`** — "We're POPIA compliant" on website. Expected: ⚠️ Needs a look. Trap: Flag #11, ARB precedent.

**`case-05-wallet-topup.yaml`** — Adding wallet top-up feature. Expected: 🛑 Hold. Trap: NCA + FICA + Banks Act.

- [ ] **Step 5: Run statute validation to confirm eval files are well-formed YAML**

```bash
python3 -c "import yaml; import glob; [yaml.safe_load(open(f)) for f in glob.glob('jurisdictions/za/evals/product-legal/**/*.yaml', recursive=True)]; print('All eval YAML files valid')"
```

Expected: `All eval YAML files valid`

- [ ] **Step 6: Commit**

```bash
git add jurisdictions/za/evals/product-legal/
git commit -m "feat(za): add 15 product-legal eval cases

3 launch-review, 4 marketing-claims-review, 3 feature-risk-assessment,
5 is-this-a-problem scenarios covering SA-specific fact patterns"
```

---

## Final validation

After all 8 tasks are complete, run the full validation suite:

- [ ] **Step 1: Run all validators**

```bash
python3 scripts/validate-za-statutes.py && python3 scripts/validate-za-router.py && python3 scripts/validate-za-templates.py
```

Expected: all three pass. Product-legal entries show `OK`.

- [ ] **Step 2: Run JSON/YAML sanity check**

```bash
python3 -c "import json,glob; [json.load(open(f)) for f in glob.glob('**/*.json', recursive=True)]"
python3 -c "import yaml,glob; [yaml.safe_load(open(f)) for f in glob.glob('jurisdictions/za/**/*.yaml', recursive=True)]"
```

Expected: no errors.

- [ ] **Step 3: Verify file structure matches spec**

```bash
find jurisdictions/za/product-legal -type f | sort
```

Expected output:
```
jurisdictions/za/product-legal/practice-profile-template.md
jurisdictions/za/product-legal/router.md
jurisdictions/za/product-legal/topics/advertising-and-claims.md
jurisdictions/za/product-legal/topics/consumer-protection.md
jurisdictions/za/product-legal/topics/content-and-minors.md
jurisdictions/za/product-legal/topics/e-commerce-and-digital.md
jurisdictions/za/product-legal/topics/fintech-and-credit.md
jurisdictions/za/product-legal/topics/sector-regulatory-map.md
```

- [ ] **Step 4: Verify no US legal concepts leaked into ZA files**

```bash
grep -rnE '\bFTC\b|\bNAD\b|\bCCPA\b|\bCOPPA\b|\bHIPAA\b|\bGLBA\b|\bCFPB\b|\bat-will\b|\bFMLA\b|\bFLSA\b' jurisdictions/za/product-legal/
```

Expected: no matches (or matches only within the privilege caveat explaining what SA does NOT have).
