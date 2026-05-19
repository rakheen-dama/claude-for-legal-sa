# ZA Overlay Expansion: ip-legal

**Date:** 2026-05-19
**Status:** Approved — ready for implementation planning
**Plugin:** ip-legal v1.0.2
**Deciders:** Rakheen Dama

---

## Decision Summary

| # | Step | Decision | Source |
|---|---|---|---|
| 1 | Target | ip-legal — 12 skills, 11 in scope (9 HIGH + 2 MEDIUM) | user confirmed |
| 2 | Statutes | 6 existing shared (copyright + ecta need extensions) + 4 new | Perplexity + user confirmed |
| 3 | Skill divergence | 9 HIGH, 2 MEDIUM, 1 LOW | Perplexity + user confirmed |
| 4 | Topic overlays | 6 topic files serving 11 skills | user confirmed |
| 5 | Practice profile | Section replacement table, SA header (drop patent agent privilege), 5 new SA sections, 8 seed docs | decided + user confirmed |
| 6 | Cold-start | 7 must-have + 3 nice-to-have questions | user confirmed |
| 7 | High-risk flags | 13 flags cross-referenced with statutes | Perplexity + user confirmed |
| 8 | Eval cases | 18 cases across 6 groupings, 5 validation rules, expert review gate | Perplexity |

---

## 1. Statute Inventory

### Existing statutes to share (in `jurisdictions/za/statutes/`)

| Statute file | Act | IP relevance | New sections needed |
|---|---|---|---|
| `copyright.yaml` | Copyright Act 98 of 1978 | Core — subsistence, infringement, permitted use, duration | **Yes — 8+ new sections** (s2 categories, s3-4 subsistence, s12 fair dealing, s23 infringement, s24 remedies, s22 duration, s20 moral rights) |
| `ecta.yaml` | ECTA 25 of 2002 | Takedowns — Chapter XI, s77 notice-and-takedown | **Yes — s77 takedown provisions** |
| `cybercrimes.yaml` | Cybercrimes Act 19 of 2020 | Trade secret theft via unauthorized computer access (s2-6) | No — already covered |
| `prescription.yaml` | Prescription Act 68 of 1969 | Limitation periods for IP claims (3 years general) | No — already extended for litigation-legal |
| `competition.yaml` | Competition Act 89 of 1998 | IP/competition intersection | No |
| `popia.yaml` | POPIA 4 of 2013 | Data protection in IP context | No |

### copyright.yaml — extensions needed

Current coverage: 3 sections (employer ownership s21(1)(d), assignment writing s22(3), computer-generated works s1/s21(1)(c)).

**New sections to add:**

| Section key | Ref | What it covers |
|---|---|---|
| `categories_of_works` | Copyright Act s2 | 9 categories: literary, musical, artistic, cinematograph, sound recording, broadcast, programme-carrying signal, published edition, computer program |
| `subsistence_conditions` | Copyright Act s3-4 | Original work + qualified person (SA citizen/resident, first publication in SA/Berne country) |
| `duration_literary` | Copyright Act s3(2)(a) | Life of author + 50 years (literary, musical, artistic works) |
| `fair_dealing` | Copyright Act s12 | Closed list of permitted purposes: research/private study, criticism/review, reporting current events. NOT open-ended like US fair use. |
| `infringement_direct` | Copyright Act s23(1) | Doing any restricted act without licence or authorization |
| `infringement_secondary` | Copyright Act s23(2)-(3) | Dealing in infringing copies |
| `remedies` | Copyright Act s24 | Damages, reasonable royalty, interdicts, delivery up |
| `moral_rights` | Copyright Act s20 | Right of paternity and integrity. Cannot be assigned, only waived. |

### ecta.yaml — extension needed

**New section to add:**

| Section key | Ref | What it covers |
|---|---|---|
| `takedown_notice` | ECTA s77 | Notice-and-takedown procedure: complainant sends notice to service provider's designated agent with full details, description of infringement, statement of ownership, signature. No statutory counter-notice regime. |

### New statute YAML files

| File | Act | Key sections | Temporal values? |
|---|---|---|---|
| `trade-marks.yaml` | Trade Marks Act 194 of 1993 | s9 (registrability — capable of distinguishing), s10 (unregistrable — absolute/relative grounds), s11 (well-known marks, Paris Convention), s34 (infringement: (a) identical, (b) similar, (c) dilution), s35 (well-known unregistered marks), s36 (defences), s37 (duration: 10 years, renewable) | Yes — registration fees change |
| `patents.yaml` | Patents Act 57 of 1978 | s25 (patentability + exclusions + "as such" qualification), s30 (specification requirements), s45 (term: 20 years), s56 (compulsory licences), s65-66 (infringement), s67 (damages/royalties), s68 (declaration of non-infringement) | No temporal thresholds |
| `designs.yaml` | Designs Act 195 of 1993 | s1 (aesthetic vs functional definitions), s14 (registrability), s20 (rights), s21 (infringement), s27 (term: aesthetic 15 years, functional 10 years) | Yes — design terms are statutory |
| `counterfeit-goods.yaml` | Counterfeit Goods Act 37 of 1997 | Search and seizure powers, criminal enforcement for counterfeit TM/copyright goods, inspector powers | No temporal |

### Deferred

- Merchandise Marks Act 17 of 1941 — niche, referenced in topic overlays where relevant
- Performers' Protection Act 11 of 1967 — out of scope for v1
- Plant Breeders' Rights Act 15 of 1976 — agricultural IP, out of scope
- IP from Publicly Financed R&D Act 51 of 2008 — niche, referenced in topic overlays

---

## 2. Skill Divergence Matrix

| # | Skill | Divergence | In scope | Reasoning |
|---|---|---|---|---|
| 1 | cease-desist | **HIGH** | ✓ | TTAB references (US-specific). SA enforcement uses CIPC opposition + High Court. Interdict threats, not TTAB cancellation. |
| 2 | clearance | **HIGH** | ✓ | Du Pont/Polaroid/Sleekcraft are US circuit-specific confusion tests. SA uses global appreciation test under s34. CIPC registry, not USPTO. Well-known marks (s35), passing off (common law). |
| 3 | cold-start-interview | **HIGH** | ✓ | US bar dates (1-year grace period), USPTO-specific concepts. SA needs: CIPC registration, absolute novelty (no grace period), SA patent attorney profession. |
| 4 | customize | **MEDIUM** | ✓ | Mechanism neutral but profile content is US-specific (enforcement references US remedies, portfolio references USPTO). |
| 5 | fto-triage | **HIGH** | ✓ | Doctrine of equivalents, willfulness/treble damages are US patent concepts. SA infringement under s65-66. No treble damages. Purposive claim construction. |
| 6 | infringement-triage | **HIGH** | ✓ | US circuit confusion tests (TM), DMCA safe harbor (CR), substantial similarity + fair use (CR), DOE + treble damages (PA). SA uses different tests for each IP type. |
| 7 | invention-intake | **HIGH** | ✓ | § 101 eligibility is US-specific. SA uses s25 with different exclusions. SA requires absolute novelty — no 1-year grace period. Bar dates completely different. |
| 8 | ip-clause-review | **HIGH** | ✓ | Work-for-hire doctrine is US copyright (17 USC § 101). SA uses employer ownership (Copyright Act s21(1)(d)). Moral rights differ. Assignment formalities differ. |
| 9 | matter-workspace | LOW | ✗ | Pure file management, no legal content. |
| 10 | oss-review | **MEDIUM** | ✓ | OSS licensing largely jurisdiction-neutral, but SA fair dealing (s12, closed list) vs US fair use (§107, open-ended) differs. Copyleft edge cases may diverge. |
| 11 | portfolio | **HIGH** | ✓ | §8 declarations (US TM maintenance), USPTO TSDR. SA uses CIPC renewal (TM 10yr, patent annual annuities from year 3, design aesthetic 15yr/functional 10yr). |
| 12 | takedown | **HIGH** | ✓ | DMCA §512 is US-only. SA uses ECTA Chapter XI s77. Completely different statutory framework. No statutory counter-notice. |

**Total in scope:** 11 skills (9 HIGH + 2 MEDIUM)

---

## 3. Topic Overlay Map

### Topic files

| # | Topic file | Skills served | Key content areas |
|---|---|---|---|
| 1 | `trademarks.md` | clearance, infringement-triage, cease-desist | SA s34 confusion test (global appreciation, not du Pont/Polaroid/Sleekcraft), CIPC searching and examination, well-known marks (s35, Paris Convention), passing off (common-law delict: reputation + misrepresentation + damage), defences (s36), first-to-file system, CIPC examination process (10-12 months) |
| 2 | `patents.md` | invention-intake, fto-triage, infringement-triage | SA patentability (s25), **absolute novelty** (no grace period), s25(2)-(3) exclusions with "as such" qualification, software/business method patents (European-style technical effect test), infringement (s65-66, purposive claim construction), compulsory licences (s56), no treble damages, depository system (no substantive examination — validity tested in litigation), Commissioner of Patents as forum |
| 3 | `copyright-and-fair-dealing.md` | takedown, infringement-triage, oss-review | SA Copyright Act categories (s2), subsistence (s3-4), fair dealing (s12, **closed list of permitted purposes** — research/private study, criticism/review, news reporting — NOT open-ended US fair use), ECTA s77 notice-and-takedown (not DMCA §512), no statutory counter-notice, duration (life+50, not life+70), computer programs explicitly protected, moral rights (s20) |
| 4 | `ip-registration-and-renewal.md` | portfolio, cold-start-interview | CIPC as registrar (TM/patent/design), TM renewal (10yr from filing, 6-month pre-expiry window, 6-month grace with penalty), patent maintenance (annual annuities from year 3 to year 20), design terms (aesthetic 15yr, functional 10yr), depository patent system (formal examination only — validity tested in litigation), no §8 declarations, no USPTO TSDR equivalent, Nice classification, non-use cancellation (5 years) |
| 5 | `ip-ownership-and-clauses.md` | ip-clause-review, cold-start-interview | SA employer ownership (Copyright Act s21(1)(d)) vs US work-for-hire, assignment must be in writing and signed (s22(3)), moral rights (s20 — paternity and integrity, cannot be assigned only waived), background vs foreground IP in SA contracts, IP from Publicly Financed R&D Act (university/research IP), restraint of trade enforceability (SA common law — reasonable and necessary) |
| 6 | `ip-enforcement.md` | cease-desist, infringement-triage, fto-triage | Interdicts (interim and final — not injunctions), damages (compensatory only — **no treble/punitive**), reasonable royalty, account of profits, delivery up/destruction, Anton Piller orders (ex parte search and seizure — strong prima facie case + risk of destruction), Counterfeit Goods Act (criminal enforcement — raids, seizure, prosecution), Commissioner of Patents (patent forum), loser-pays costs |

### Skill-to-topic router

```yaml
cease-desist:
  topics: [trademarks, ip-enforcement]
  statutes: [trade-marks, counterfeit-goods]

clearance:
  topics: [trademarks]
  statutes: [trade-marks]

cold-start-interview:
  topics: [ip-registration-and-renewal, ip-ownership-and-clauses]
  statutes: [trade-marks, patents, designs, copyright]

customize:
  topics: []
  statutes: []

fto-triage:
  topics: [patents, ip-enforcement]
  statutes: [patents]

infringement-triage:
  topics: [trademarks, patents, copyright-and-fair-dealing, ip-enforcement]
  statutes: [trade-marks, patents, copyright, ecta]

invention-intake:
  topics: [patents]
  statutes: [patents]

ip-clause-review:
  topics: [ip-ownership-and-clauses]
  statutes: [copyright]

oss-review:
  topics: [copyright-and-fair-dealing]
  statutes: [copyright]

portfolio:
  topics: [ip-registration-and-renewal]
  statutes: [trade-marks, patents, designs]

takedown:
  topics: [copyright-and-fair-dealing]
  statutes: [copyright, ecta]
```

### Overlap with existing practice areas

- `copyright-and-fair-dealing.md` shares the Copyright Act with `copyright.yaml` (existing statute file, being extended). No topic overlap with other practice areas.
- `ip-enforcement.md` references interdicts and costs — thematic overlap with litigation-legal's overlays, but IP enforcement is domain-specific enough to warrant a separate file.
- No other significant overlaps.

---

## 4. Practice Profile Template Design

### Section replacement table

| US template section | Action | ZA template equivalent |
|---|---|---|
| Company profile | Minor adapt | Add Province. Replace US examples with SA. |
| **Who's using this** | **Replace** | "Registered patent agent" → "Patent attorney" (SA term). Drop In re Queen's University privilege note. Add "patent attorney registered with CIPC." |
| **Available integrations** | Adapt | CourtListener/Descrybe → SAFLII/Juta/LexisNexis SA. Add CIPC online services. Keep PatSnap/Solve Intelligence (generic). |
| **Outputs — work-product header** | **Replace** | SA legal professional privilege formulation. Drop entire patent agent privilege section (US-only doctrine). |
| Outputs — reviewer note, quiet mode, decision tree | Keep | Jurisdiction-neutral. |
| **Shared guardrails — source tags** | Adapt | Replace Westlaw/CourtListener/USPTO with SAFLII/Juta/CIPC. |
| Scaffolding, proportionality, jurisdiction recognition | Keep | Neutral. |
| **IP practice profile — Registered in** | **Replace** | SA registrations (CIPC for TM/patent/design), Madrid Protocol, PCT, ARIPO. Not USPTO/EUIPO. |
| **IP practice profile — Outside counsel roster** | Adapt | SA: patent attorneys (CIPC-registered) + advocates for Commissioner of Patents/High Court. |
| **IP portfolio — register** | Adapt | SA deadlines: TM (10yr renewal), patent (annual annuities from year 3), design (aesthetic 15yr, functional 10yr). Drop §8 declarations. |
| Brand protection | Keep structure | Replace watch jurisdictions with SA + regional. |
| **Enforcement posture** | Adapt | Drop TTAB. Replace with CIPC opposition + High Court. Interdict (not injunction). No treble damages. Add Counterfeit Goods Act option. |
| **Enforcement posture — approval matrix** | Adapt | Drop "TTAB cancellation". Add "Counterfeit Goods Act raid". Replace "DMCA takedown" with "ECTA s77 takedown". |
| Matter workspaces | Keep | Neutral. |

### Work-product header (SA)

**If Role = Legal practitioner / Patent attorney:**

> PRIVILEGED & CONFIDENTIAL — PREPARED AT THE DIRECTION OF A LEGAL PRACTITIONER

**If Role = Non-lawyer:**

> CONFIDENTIAL — NOT LEGAL ADVICE — REVIEW WITH A LEGAL PRACTITIONER BEFORE ACTING

Drop the entire US patent agent privilege section. SA patent attorneys are legal practitioners under the Legal Practice Act — standard SA legal professional privilege applies. No separate patent-agent-specific privilege doctrine.

### New SA-specific sections to add

| Section | Content |
|---|---|
| **SA IP registration landscape** | CIPC as registrar (TM, patent, design). Depository patent system (no substantive examination — validity tested in litigation). Nice classification for TM. No copyright registration system (copyright arises automatically). |
| **SA patentability notes** | Absolute novelty (no 1-year grace period). s25(2)-(3) exclusions with "as such" qualification. Software/business methods: European-style technical effect test. Standing instruction: flag any prior public disclosure as a bar date risk. |
| **SA trademark framework** | s34 global appreciation test (not US multi-factor). First-to-file. Well-known marks (s35). Passing off (common law). |
| **SA copyright and takedowns** | Fair dealing (s12, closed list) — not open-ended fair use. ECTA s77 takedowns (not DMCA). No statutory counter-notice. Duration life+50 (not life+70). |
| **SA enforcement landscape** | Interdicts (not injunctions). Compensatory damages only — no treble/punitive. Anton Piller orders. Counterfeit Goods Act (criminal). Commissioner of Patents (patent forum). Loser-pays costs. |

### Seed documents

| Doc | Location / pointer | Notes |
|---|---|---|
| SA trademark portfolio register | [PLACEHOLDER] | CIPC registration numbers, renewal dates |
| SA patent portfolio register | [PLACEHOLDER] | Annual annuity schedule |
| Design registrations | [PLACEHOLDER] | Aesthetic vs functional, renewal dates |
| C&D template (SA-adapted) | [PLACEHOLDER] | Interdict threat language, no TTAB |
| OSS policy | [PLACEHOLDER] | SA fair dealing context |
| IP assignment template (SA) | [PLACEHOLDER] | s22(3) writing requirement, moral rights |
| Brand guidelines | [PLACEHOLDER] | Watched marks for SA market |
| ECTA s77 takedown template | [PLACEHOLDER] | Replaces DMCA template |

---

## 5. Cold-Start Interview Questions

### Must-have (SA fork after Part 0)

| # | Question | Why high-leverage | Writes to |
|---|---|---|---|
| 1 | Which IP types does your SA practice cover? (trademark, patent, design, copyright, trade secret, OSS, all) | Scopes the overlay — determines relevant topic overlays. | `## IP practice profile — Practice area mix` |
| 2 | Do you hold SA registrations at CIPC? If yes: TM numbers, patent numbers, design numbers? | Seeds portfolio register with SA-specific assets and renewal deadlines. | `## IP portfolio` |
| 3 | Patent practice: are you aware that SA requires absolute novelty (no grace period)? | Critical flag — #1 difference from US patent practice. | `## SA patentability notes` |
| 4 | Do you use patent attorneys registered with CIPC, or do you also brief advocates for Commissioner of Patents proceedings? | Determines OC bench structure. | `## IP practice profile — Outside counsel roster` |
| 5 | Enforcement posture for SA market: do you use the Counterfeit Goods Act (criminal raids) in addition to civil interdicts? | Shapes enforcement workflow. | `## Enforcement posture` |
| 6 | Do you file ECTA s77 takedown notices for online infringement, or rely on platform-specific (DMCA-style) processes? | Determines takedown framework. | `## SA copyright and takedowns` |
| 7 | Currency for IP budgets and enforcement thresholds? | Sets budget and approval matrix currency. | `## Enforcement posture — approval matrix` |

### Nice-to-have

| # | Question | Why useful but deferrable |
|---|---|---|
| 8 | Do you subscribe to a trademark watch service for SA? (Corsearch, CompuMark, internal) | Informs brand protection section. |
| 9 | Do you have existing relationships with CIPC or knowledge of current examination backlogs? | Practical context for timelines. |
| 10 | Do you file internationally via Madrid Protocol or PCT from SA? | Scopes portfolio beyond SA-only. |

---

## 6. High-Risk Flag Table

| # | Flag | Why high-risk | What to check | Statute cross-ref |
|---|---|---|---|---|
| 1 | **absolute-novelty-breach** | SA has no grace period. Any public disclosure before filing destroys novelty. Irreversible. | Check for: conference presentations, demos, website launches, social media, investor decks, academic publications, product samples — all before the priority date. | Patents Act s25(1) |
| 2 | **well-known-mark-conflict** | Foreign brands not registered in SA can attack under s35 (Paris Convention). Register-only clearance will miss this. | Search beyond the register: international use, online presence, SA market reputation. Check if mark is "well known in the relevant sector of the SA public." | Trade Marks Act s35 |
| 3 | **passing-off-risk** | Unregistered common-law rights can block use even without registration. CIPC search alone is insufficient. | Check: market use, company names (CIPC), domain names (.co.za via ZADNA), social media, local directories. Assess reputation + misrepresentation + damage. | Common law — passing off |
| 4 | **depository-patent-granted** | SA grants patents without substantive examination. Registration ≠ validity. | Treat grant as starting point. Do prior-art screening before relying on patent. Draft with invalidity attacks in mind. In transactions, check prosecution file. | Patents Act (depository system) |
| 5 | **copyright-ownership-gap** | Payment does not equal ownership. Contractor work requires written assignment (s22(3)). Missing formality = no transfer. | Verify: (a) employee vs contractor, (b) written assignment exists and is signed, (c) covers specific works, (d) moral rights consent obtained (s20). | Copyright Act s21, s22(3), s20 |
| 6 | **ecta-takedown-deficiency** | ECTA s77 notice missing required particulars → ISP may ignore. No statutory counter-notice means legitimate content can be removed with no recourse. | Verify notice has: full contact details, precise URL/location, description of infringed right, statement of ownership/authority, signature. Preserve evidence before sending. | ECTA s77 |
| 7 | **design-category-misclassification** | Aesthetic vs functional design filed in wrong category → reduced protection, wrong term, invalidity arguments. | Analyse whether design is judged by eye (aesthetic, Part A, 15yr) or function (functional, Part F, 10yr). Consider dual filing if both elements matter. | Designs Act s1, s14, s27 |
| 8 | **compulsory-licence-exposure** | Failure to work patent in SA can trigger compulsory licence application under s56. Passive holding is vulnerable. | Document why patent is not being worked locally. Review licensing/import strategy. Assess local manufacture, distribution, or partnership needs. | Patents Act s56 |
| 9 | **ip-clause-missing-assignment** | Contract lacks express IP assignment → commissioning party doesn't own the work it paid for. Licensing chains collapse. | Check all contracts for: present assignment clause, background vs foreground IP definition, further assurances obligation, moral rights waiver, future works coverage. | Copyright Act s22(3) |
| 10 | **trade-secret-no-protection** | SA has no dedicated trade secrets statute. Without contracts + operational controls, secrets have weak legal protection. | Verify: NDAs in place, access controls, marking/segregation of confidential info, exit procedures, vendor confidentiality management. | Common law + Cybercrimes Act s2-6 |
| 11 | **fair-dealing-not-fair-use** | SA fair dealing (s12) is a narrow, closed list of permitted purposes — not open-ended US fair use. Uses defended as fair use in the US may be infringing in SA. | Apply s12 enumerated purposes only (research, private study, criticism, review, news reporting). Do NOT apply US 4-factor test. | Copyright Act s12 |
| 12 | **counterfeit-raid-overreach** | Counterfeit Goods Act raids with inadequate evidence or defective warrants → wrongful seizure exposure, damages claims, reputational harm. | Before raid: sufficient evidence of rights, clear identification criteria, proper warrant, chain-of-custody procedures, budget for follow-through. | Counterfeit Goods Act 37/1997 |
| 13 | **renewal-lapse** | Missing CIPC renewal deadlines → registration lapses. TM (10yr), patent (annual annuities from year 3), design (periodic). Grace periods exist but with penalties. | Portfolio skill must track SA-specific deadlines. Flag approaching renewals. Verify against CIPC records. | Trade Marks Act s37; Patents Act s46; Designs Act s27 |

---

## 7. Eval Case Outlines

### 7.1 Trademark clearance & enforcement (clearance, cease-desist, infringement-triage)

**TM-01: Clearance with well-known foreign mark**
- **Input:** Client wants to launch "AURORA" for cosmetics in SA. Not on CIPC register, but Aurora is a well-known international cosmetics brand.
- **Expected flags:** well-known-mark-conflict, passing-off-risk
- **Expected statutes:** Trade Marks Act s35 (well-known marks)
- **Must NOT contain:** "du Pont factors", "Polaroid test", "Sleekcraft", "likelihood of confusion under Lanham Act"

**TM-02: Inbound C&D from SA rights holder**
- **Input:** Company receives C&D alleging trademark infringement under s34(1)(a) for confusingly similar mark on identical goods.
- **Expected flags:** loser-pays costs exposure
- **Expected statutes:** Trade Marks Act s34(1)(a)
- **Must NOT contain:** "TTAB cancellation", "Lanham Act §32", "federal registration", "US district court"

**TM-03: Passing off claim — unregistered mark**
- **Input:** Competitor using confusingly similar trading name for 5 years, no registration. Client wants to assert rights.
- **Expected flags:** passing-off-risk
- **Expected statutes:** Common law passing off
- **Must NOT contain:** "Lanham Act §43(a)", "federal unfair competition", "state unfair competition statute"

### 7.2 Patent (invention-intake, fto-triage)

**PA-01: Invention disclosure — prior conference presentation**
- **Input:** Engineer disclosed invention at a Johannesburg industry conference 3 months ago. Now wants to file a patent.
- **Expected flags:** absolute-novelty-breach
- **Expected statutes:** Patents Act s25(1)
- **Must NOT contain:** "one-year grace period", "§102(a)(1)", "inventor's own disclosure exception", "35 USC"

**PA-02: FTO triage — software method**
- **Input:** Software startup wants to launch fintech payment processing method in SA. Competitor has SA patent on related method.
- **Expected flags:** depository-patent-granted
- **Expected statutes:** Patents Act s25, s65-66
- **Must NOT contain:** "Alice/Mayo test", "35 USC §101", "abstract idea", "CAFC", "doctrine of equivalents", "willfulness/treble damages"

**PA-03: Compulsory licence risk**
- **Input:** Foreign pharma company holds SA patent but only imports, no local manufacture. Generic manufacturer threatening s56 application.
- **Expected flags:** compulsory-licence-exposure
- **Expected statutes:** Patents Act s56
- **Must NOT contain:** "Hatch-Waxman", "ANDA", "Paragraph IV certification", "FDA Orange Book"

### 7.3 Copyright & takedowns (takedown, infringement-triage, oss-review)

**CR-01: ECTA s77 takedown notice**
- **Input:** Client's copyrighted photographs used on SA-hosted website without permission. Need to send takedown notice.
- **Expected flags:** ecta-takedown-deficiency (verify notice completeness)
- **Expected statutes:** ECTA s77, Copyright Act s23
- **Must NOT contain:** "DMCA §512(c)(3)", "designated DMCA agent", "§512(f) perjury", "Lenz v Universal"

**CR-02: Fair dealing edge case**
- **Input:** SA company wants to use excerpts from competitor's technical manual in a comparative review published on their website.
- **Expected flags:** fair-dealing-not-fair-use
- **Expected statutes:** Copyright Act s12
- **Must NOT contain:** "fair use four-factor test", "transformative use", "§107", "Campbell v Acuff-Rose"

**CR-03: OSS copyleft obligation**
- **Input:** SA SaaS company discovers AGPL-licensed code in backend. No binary distribution but service accessed over a network.
- **Expected flags:** None (routine OSS analysis)
- **Expected statutes:** Copyright Act (underlying framework)
- **Must NOT contain:** "fair use defence to copyleft", "§107 applies to licence obligations"

### 7.4 IP registration & portfolio (portfolio, cold-start-interview)

**REG-01: Trademark renewal approaching**
- **Input:** SA trademark registration expiring in 4 months. Confirm renewal process and deadline.
- **Expected flags:** renewal-lapse
- **Expected statutes:** Trade Marks Act s37
- **Must NOT contain:** "§8 declaration", "§8 and §9 affidavit", "USPTO TSDR", "Section 8 maintenance"

**REG-02: Design registration — dual filing question**
- **Input:** Product with both aesthetic appeal (curved shape) and functional features (ventilation slots). Need to register in SA.
- **Expected flags:** design-category-misclassification
- **Expected statutes:** Designs Act s1, s14, s27
- **Must NOT contain:** "US design patent", "35 USC §171", "ornamental design", "utility patent"

### 7.5 IP clauses & ownership (ip-clause-review)

**CL-01: Contractor agreement missing assignment**
- **Input:** Reviewing software development agreement with independent contractor. No IP assignment clause. Contractor building custom SA platform.
- **Expected flags:** ip-clause-missing-assignment, copyright-ownership-gap
- **Expected statutes:** Copyright Act s21, s22(3)
- **Must NOT contain:** "work made for hire", "17 USC §101", "work for hire categories", "employer owns under US copyright"

**CL-02: Trade secret NDA review**
- **Input:** Reviewing NDA for potential JV partner. Assess whether it adequately protects trade secrets under SA law.
- **Expected flags:** trade-secret-no-protection
- **Expected statutes:** Common law + Cybercrimes Act s2-6
- **Must NOT contain:** "DTSA (Defend Trade Secrets Act)", "18 USC §1836", "inevitable disclosure doctrine"

### 7.6 Enforcement (cease-desist, infringement-triage)

**ENF-01: Counterfeit goods — criminal enforcement**
- **Input:** Large-scale counterfeiting of client's trademarked clothing at Johannesburg market. Client wants combined civil and criminal enforcement.
- **Expected flags:** counterfeit-raid-overreach
- **Expected statutes:** Counterfeit Goods Act 37/1997, Trade Marks Act s34
- **Must NOT contain:** "customs seizure under 19 USC", "ITC exclusion order", "Section 337 investigation"

**ENF-02: Anton Piller order application**
- **Input:** Need evidence preservation order against suspected trade secret thief (former employee). Risk of evidence destruction.
- **Expected flags:** trade-secret-no-protection
- **Expected statutes:** Common law (Anton Piller), Cybercrimes Act s2-6
- **Must NOT contain:** "TRO under DTSA", "ex parte seizure under 18 USC §1836", "federal trade secret injunction"

### Validation rules (applied across all cases)

1. No US patent law: 35 USC, §101, §102, Alice/Mayo, doctrine of equivalents, treble damages, Hatch-Waxman
2. No US trademark law: Lanham Act, du Pont/Polaroid/Sleekcraft, TTAB, §8 declarations, USPTO TSDR
3. No US copyright law: DMCA §512, §107 fair use, work made for hire (17 USC §101), DTSA
4. No US citation/procedure: Bluebook, FRCP, federal court
5. SA-specific terminology must appear: interdict (not injunction), CIPC (not USPTO), s34 (not Lanham Act), fair dealing (not fair use), ECTA s77 (not DMCA), legal practitioner (not attorney-at-law), patent attorney (not patent agent)

### Expert review gate

Before release, an SA IP practitioner reviews:
- Topic overlay content against current Trade Marks Act, Patents Act, Copyright Act, Designs Act
- CIPC procedures and current examination timelines
- High-risk flag table against current SA IP practice
- Eval case expected outputs for legal accuracy

---

## 8. Source Provenance Log

| Step | Item | Source | Tag |
|---|---|---|---|
| 2 | SA IP statutes inventory (Trade Marks Act, Patents Act, Copyright Act, Designs Act, Counterfeit Goods Act) | Perplexity search | [Perplexity — verify] |
| 2 | Trade Marks Act s9-s37 section references | Perplexity | [Perplexity — verify] |
| 2 | Patents Act s25 patentability and exclusions | Perplexity | [Perplexity — verify] |
| 2 | Copyright Act s2-s24 section references | Perplexity | [Perplexity — verify] |
| 2 | Designs Act aesthetic (15yr) vs functional (10yr) terms | Perplexity | [Perplexity — verify] |
| 2 | ECTA s77 takedown provisions | Perplexity | [Perplexity — verify] |
| 3 | Skill divergence — all 12 skills assessed | SKILL.md frontmatter read + Perplexity verification | [Perplexity + user confirmed] |
| 3 | SA absolute novelty (no grace period) | Perplexity | [Perplexity — verify] |
| 3 | SA s34 global appreciation test (not du Pont) | Perplexity | [Perplexity — verify] |
| 3 | SA fair dealing s12 (closed list, not open-ended) | Perplexity | [Perplexity — verify] |
| 3 | SA depository patent system (no substantive examination) | Perplexity | [Perplexity — verify] |
| 3 | CIPC as registrar (TM, patent, design) | Perplexity | [Perplexity — verify] |
| 5 | SA patent attorney vs US patent agent distinction | Model knowledge | [model knowledge — verify] |
| 5 | In re Queen's University is US-only doctrine | Model knowledge | [model knowledge — verify] |
| 7 | All 13 high-risk flags | Perplexity comprehensive risk research | [Perplexity — verify] |
| 7 | Anton Piller order requirements | Perplexity | [Perplexity — verify] |
| 7 | Compulsory licence under s56 | Perplexity | [Perplexity — verify] |
| 7 | Counterfeit Goods Act enforcement risks | Perplexity | [Perplexity — verify] |
| 7 | Copyright ownership s21/s22(3) formalities | Perplexity | [Perplexity — verify] |
| 8 | SA delict elements for passing off (reputation + misrepresentation + damage) | Perplexity | [Perplexity — verify] |

---

## Implementation Sequence

Following the same task structure as prior overlays:

1. Extend `copyright.yaml` (8 new sections) + extend `ecta.yaml` (1 new section)
2. New statute YAML files (4: trade-marks, patents, designs, counterfeit-goods)
3. Topic overlay markdown files (6 files)
4. Skill router (`jurisdictions/za/ip-legal/router.md`)
5. Practice profile template (`jurisdictions/za/ip-legal/practice-profile-template.md`)
6. Cold-start interview fork (add ZA branch to `ip-legal/skills/cold-start-interview/SKILL.md`)
7. Validation scripts (extend existing validators for ip-legal)
8. Scenario eval cases (18 cases in `jurisdictions/za/evals/ip-legal/`)
9. Final validation run
