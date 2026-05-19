# ZA IP-Legal Overlay Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build the South African overlay for the ip-legal plugin — extend 2 existing statute YAMLs, create 4 new statute YAMLs, 6 topic overlays, skill router, ZA practice profile template, cold-start interview fork, validation extensions, and 18 eval cases.

**Architecture:** Additive overlays in `jurisdictions/za/ip-legal/` — same pattern as employment-legal (phase 1), commercial-legal (phase 2), privacy-legal (phase 3), and litigation-legal (phase 4). No upstream skill modifications except cold-start-interview. See ADR-001 (`project/decisions/001-sa-overlay-architecture.md`).

**Spec:** `docs/superpowers/specs/2026-05-19-za-ip-legal-expansion.md` — read this before starting any task.

**Reference implementation:** `jurisdictions/za/litigation-legal/` (phase 4, most recent).

---

## File Map

### New files

| File | Responsibility |
|---|---|
| `jurisdictions/za/statutes/trade-marks.yaml` | Trade Marks Act 194 of 1993 — registrability, infringement, well-known marks, defences, duration |
| `jurisdictions/za/statutes/patents.yaml` | Patents Act 57 of 1978 — patentability, exclusions, infringement, compulsory licences |
| `jurisdictions/za/statutes/designs.yaml` | Designs Act 195 of 1993 — aesthetic vs functional, registrability, terms |
| `jurisdictions/za/statutes/counterfeit-goods.yaml` | Counterfeit Goods Act 37 of 1997 — search/seizure, criminal enforcement |
| `jurisdictions/za/ip-legal/router.md` | Maps 11 in-scope skills to topic + statute files |
| `jurisdictions/za/ip-legal/practice-profile-template.md` | ZA practice profile for SA IP practitioners |
| `jurisdictions/za/ip-legal/topics/trademarks.md` | SA s34 confusion test, CIPC searching, well-known marks, passing off |
| `jurisdictions/za/ip-legal/topics/patents.md` | SA patentability, absolute novelty, exclusions, infringement, compulsory licences |
| `jurisdictions/za/ip-legal/topics/copyright-and-fair-dealing.md` | SA copyright, fair dealing (s12), ECTA s77 takedowns |
| `jurisdictions/za/ip-legal/topics/ip-registration-and-renewal.md` | CIPC, TM/patent/design renewal, depository system |
| `jurisdictions/za/ip-legal/topics/ip-ownership-and-clauses.md` | SA employer ownership, assignment, moral rights |
| `jurisdictions/za/ip-legal/topics/ip-enforcement.md` | Interdicts, damages, Anton Piller, Counterfeit Goods Act |
| `jurisdictions/za/evals/ip-legal/clearance/case-01-well-known-foreign.yaml` | Eval: clearance with well-known foreign mark |
| `jurisdictions/za/evals/ip-legal/cease-desist/case-02-inbound-cd.yaml` | Eval: inbound C&D from SA rights holder |
| `jurisdictions/za/evals/ip-legal/infringement-triage/case-03-passing-off.yaml` | Eval: passing off — unregistered mark |
| `jurisdictions/za/evals/ip-legal/invention-intake/case-01-prior-disclosure.yaml` | Eval: invention disclosure after conference presentation |
| `jurisdictions/za/evals/ip-legal/fto-triage/case-02-software-method.yaml` | Eval: FTO — software patent |
| `jurisdictions/za/evals/ip-legal/fto-triage/case-03-compulsory-licence.yaml` | Eval: compulsory licence risk |
| `jurisdictions/za/evals/ip-legal/takedown/case-01-ecta-s77.yaml` | Eval: ECTA s77 takedown notice |
| `jurisdictions/za/evals/ip-legal/infringement-triage/case-02-fair-dealing.yaml` | Eval: fair dealing edge case |
| `jurisdictions/za/evals/ip-legal/oss-review/case-03-agpl-saas.yaml` | Eval: AGPL copyleft in SaaS |
| `jurisdictions/za/evals/ip-legal/portfolio/case-01-tm-renewal.yaml` | Eval: trademark renewal |
| `jurisdictions/za/evals/ip-legal/portfolio/case-02-design-dual-filing.yaml` | Eval: design category dual filing |
| `jurisdictions/za/evals/ip-legal/ip-clause-review/case-01-contractor-no-assignment.yaml` | Eval: contractor missing IP assignment |
| `jurisdictions/za/evals/ip-legal/ip-clause-review/case-02-trade-secret-nda.yaml` | Eval: trade secret NDA review |
| `jurisdictions/za/evals/ip-legal/cease-desist/case-01-counterfeit-raid.yaml` | Eval: counterfeit goods criminal enforcement |
| `jurisdictions/za/evals/ip-legal/infringement-triage/case-04-anton-piller.yaml` | Eval: Anton Piller order for trade secret |

### Modified files

| File | Change |
|---|---|
| `jurisdictions/za/statutes/copyright.yaml` | Add 8 new sections (categories, subsistence, duration, fair dealing, infringement, remedies, moral rights) |
| `jurisdictions/za/statutes/ecta.yaml` | Add 1 new section (s77 takedown) |
| `scripts/validate-za-router.py` | Add ip-legal to `PRACTICE_AREAS` list |
| `scripts/validate-za-templates.py` | Add ip-legal to `TEMPLATE_CONFIG` dict |
| `ip-legal/skills/cold-start-interview/SKILL.md` | Add ZA fork after Part 0 with 7 must-have questions |

---

## Task 1: Extend `copyright.yaml` with 8 new sections

**Files:**
- Modify: `jurisdictions/za/statutes/copyright.yaml`

- [ ] **Step 1: Read the existing file**

```bash
cat jurisdictions/za/statutes/copyright.yaml
```

Confirm the 3 existing sections (employer_ownership, assignment_must_be_in_writing, computer_generated_works).

- [ ] **Step 2: Append 8 new sections**

Add the following sections after the existing `computer_generated_works` entry:

```yaml
  categories_of_works:
    ref: "Copyright Act s2"
    value: 9
    unit: "categories"
    effective_from: null
    effective_until: null
    effect: "Copyright subsists in 9 categories of works: literary works (including computer programs, tables, compilations), musical works, artistic works (drawings, photographs, architecture), cinematograph films, sound recordings, broadcasts, programme-carrying signals, published editions, and computer programs."

  subsistence_conditions:
    ref: "Copyright Act s3-4"
    value: true
    effective_from: null
    effective_until: null
    effect: "Copyright subsists if the work is original and the author is a qualified person (SA citizen or resident, or first publication in SA or a Berne Convention country). No registration is required — copyright arises automatically on creation and fixation."
    note: "SA has no general copyright registration system (unlike the US Copyright Office). Copyright arises automatically. Some specific registers exist (e.g., cinematograph films)."

  duration_literary_musical_artistic:
    ref: "Copyright Act s3(2)(a)"
    value: 50
    unit: "years after death of author"
    effective_from: null
    effective_until: null
    effect: "Copyright in literary, musical, and artistic works subsists for the life of the author plus 50 years from the end of the year in which the author dies."
    note: "SA is life+50, not life+70 as in the US and EU. Some work categories have different terms (e.g., films and sound recordings: 50 years from first publication or making)."

  fair_dealing:
    ref: "Copyright Act s12"
    value: "closed list of permitted purposes"
    effective_from: null
    effective_until: null
    effect: "Fair dealing with a work is permitted for specific enumerated purposes: research or private study, personal or private use, criticism or review, reporting current events. This is a CLOSED LIST — not the open-ended US fair use test under 17 USC §107. Uses outside these purposes are infringing absent another statutory exception or a licence."
    note: "SA fair dealing is narrower than US fair use. There is no 'transformative use' doctrine. A use that might be defensible as fair use in the US may be infringing in SA."

  infringement_direct:
    ref: "Copyright Act s23(1)"
    value: true
    effective_from: null
    effective_until: null
    effect: "Copyright is infringed by any person who, without the authority of the owner, does or causes any other person to do any act which the owner has the exclusive right to do or to authorize."

  infringement_secondary:
    ref: "Copyright Act s23(2)-(3)"
    value: true
    effective_from: null
    effective_until: null
    effect: "Secondary infringement includes: importing, selling, distributing, or possessing for trade purposes an article which the person knows or ought reasonably to know is an infringing copy."

  remedies:
    ref: "Copyright Act s24"
    value: true
    effective_from: null
    effective_until: null
    effect: "Civil remedies for copyright infringement include: interdict (injunction), damages, reasonable royalty, delivery up of infringing copies, and an account of profits. Criminal penalties also apply for commercial infringement (s25-27)."

  moral_rights:
    ref: "Copyright Act s20"
    value: true
    effective_from: null
    effective_until: null
    effect: "The author of a work has the right to claim authorship (paternity) and to object to any distortion, mutilation, or other modification of the work that would be prejudicial to the author's honour or reputation (integrity). Moral rights cannot be assigned, only waived by consent."
```

- [ ] **Step 3: Run validation**

```bash
python3 scripts/validate-za-statutes.py
```

Expected: PASS — copyright.yaml validates with 11 sections (3 existing + 8 new).

- [ ] **Step 4: Commit**

```bash
git add jurisdictions/za/statutes/copyright.yaml
git commit -m "feat(za): extend copyright.yaml with 8 IP-specific sections"
```

---

## Task 2: Extend `ecta.yaml` with takedown section

**Files:**
- Modify: `jurisdictions/za/statutes/ecta.yaml`

- [ ] **Step 1: Read the existing file and append**

Add the following section after the existing `schedule_1_exclusions` entry:

```yaml
  takedown_notice:
    ref: "ECTA s77"
    value: true
    effective_from: "2002-08-30"
    effective_until: null
    effect: "A complainant may send a takedown notice to a service provider's designated agent requesting removal of infringing content. The notice must include: full contact details, description and location of the infringing material, statement of ownership or authority, and signature. Service providers that comply with takedown requests benefit from limitations on liability (safe harbour). There is no statutory counter-notice procedure — unlike the US DMCA, there is no mandatory 'put back' mechanism."
    note: "ECTA takedowns are not limited to copyright — they can apply to any unlawful content. The absence of a counter-notice regime means ISPs often over-comply (quick removal) to preserve safe harbour. Practice varies between ISPs."
```

- [ ] **Step 2: Run validation and commit**

```bash
python3 scripts/validate-za-statutes.py
git add jurisdictions/za/statutes/ecta.yaml
git commit -m "feat(za): add ECTA s77 takedown section"
```

---

## Task 3: Create IP statute files — trade-marks and patents

**Files:**
- Create: `jurisdictions/za/statutes/trade-marks.yaml`
- Create: `jurisdictions/za/statutes/patents.yaml`

- [ ] **Step 1: Create `trade-marks.yaml`**

```yaml
statute: "Trade Marks Act 194 of 1993"
authority: "Companies and Intellectual Property Commission (CIPC)"
last_confirmed: "2025-05-01"
source_url: "https://www.gov.za/documents/trade-marks-act"

sections:
  registrability:
    ref: "Trade Marks Act s9"
    value: "capable of distinguishing"
    effective_from: null
    effective_until: null
    effect: "A mark is registrable as a trade mark if it is capable of distinguishing the goods or services of one person from those of another. The mark must be inherently distinctive or have acquired distinctiveness through use."

  unregistrable_marks:
    ref: "Trade Marks Act s10"
    value: true
    effective_from: null
    effective_until: null
    effect: "Marks that shall not be registered include: marks devoid of distinctive character (s10(1)), descriptive or generic marks (s10(2)), marks where the applicant has no bona fide claim to proprietorship (s10(3)), marks confusingly similar to earlier marks (s10(12), s10(14)), marks contrary to law or morality (s10(10)), and marks that would cause deception (s10(11))."

  well_known_marks_registered:
    ref: "Trade Marks Act s11"
    value: true
    effective_from: null
    effective_until: null
    effect: "A well-known trade mark as defined in the Paris Convention is entitled to protection in South Africa even if not registered. The Registrar must refuse to register a mark that conflicts with a well-known mark."

  infringement_identical:
    ref: "Trade Marks Act s34(1)(a)"
    value: true
    effective_from: null
    effective_until: null
    effect: "A registered trade mark is infringed by the unauthorized use, in the course of trade, of an identical or confusingly similar mark in relation to identical or similar goods or services, where such use is likely to cause deception or confusion."

  infringement_similar:
    ref: "Trade Marks Act s34(1)(b)"
    value: true
    effective_from: null
    effective_until: null
    effect: "A registered trade mark is infringed by the use of a similar mark on goods or services so similar to those covered by the registration that use is likely to cause deception or confusion."

  infringement_dilution:
    ref: "Trade Marks Act s34(1)(c)"
    value: true
    effective_from: null
    effective_until: null
    effect: "A well-known registered trade mark is infringed by the use of a similar mark on any goods or services (even dissimilar) where such use is likely to take unfair advantage of, or be detrimental to, the distinctive character or repute of the registered mark. No need to show confusion."

  well_known_unregistered:
    ref: "Trade Marks Act s35"
    value: true
    effective_from: null
    effective_until: null
    effect: "A mark entitled to protection under the Paris Convention as a well-known trade mark is protected even if unregistered in South Africa and even if the owner has no local business, provided the mark is well known in the relevant sector of the SA public. Allows infringement actions and opposition/cancellation of conflicting marks."

  defences:
    ref: "Trade Marks Act s36"
    value: true
    effective_from: null
    effective_until: null
    effect: "Statutory defences to infringement include: honest use of one's own name or the name of a predecessor in business (bona fide use of name), use of indications of kind, quality, or geographical origin (descriptive use), and use of the trade mark to indicate the intended purpose of goods or services (e.g., spare parts, compatible products)."

  duration_and_renewal:
    ref: "Trade Marks Act s37"
    value: 10
    unit: "years"
    effective_from: null
    effective_until: null
    effect: "A trade mark registration is valid for 10 years from the filing date and may be renewed indefinitely for further 10-year periods. Renewal can be filed from 6 months before expiry. A 6-month grace period with penalty fee applies after expiry."

  confusion_test:
    ref: "Trade Marks Act s34 (case law)"
    value: "global appreciation"
    effective_from: null
    effective_until: null
    effect: "SA courts apply a global appreciation test for likelihood of confusion, considering: visual, aural, and conceptual similarity of marks as wholes; comparison of goods/services; the average consumer with imperfect recollection; distinctiveness and strength of the earlier mark; and overall impression. This is NOT the US multi-factor test (du Pont, Polaroid, Sleekcraft)."
    note: "SA confusion analysis draws on UK/EU case law. Factors are similar in substance to US tests but less formally enumerated — more 'global and impressionistic' than factor-by-factor."
```

- [ ] **Step 2: Create `patents.yaml`**

```yaml
statute: "Patents Act 57 of 1978"
authority: "Companies and Intellectual Property Commission (CIPC)"
last_confirmed: "2025-05-01"
source_url: "https://www.gov.za/documents/patents-act-20-apr-1978-0000"

sections:
  patentability:
    ref: "Patents Act s25(1)"
    value: "new, inventive step, capable of industrial application"
    effective_from: null
    effective_until: null
    effect: "An invention is patentable if it is new (novel), involves an inventive step (non-obvious), and is capable of being used or applied in trade, industry, or agriculture (industrial applicability)."

  absolute_novelty:
    ref: "Patents Act s25(1) read with s25(5)-(6)"
    value: "worldwide, no grace period"
    effective_from: null
    effective_until: null
    effect: "SA applies absolute worldwide novelty. Any prior disclosure anywhere in the world before the priority date is prior art. There is NO general 12-month grace period like the US (35 USC §102(a)(1)). Very limited exceptions exist (officially recognised exhibitions, unlawful third-party disclosure) but should not be relied upon."
    note: "This is the single most important difference from US patent practice. Public disclosure before filing — conference presentations, demos, website launches, investor decks, academic publications, product samples — will almost certainly destroy novelty."

  exclusions_as_such:
    ref: "Patents Act s25(2)-(3)"
    value: "excluded only as such"
    effective_from: null
    effective_until: null
    effect: "The following are not deemed inventions: discoveries, scientific theories, mathematical methods, literary/dramatic/musical/artistic works, schemes for mental acts or doing business, computer programs, and presentation of information. However, s25(3) provides these are excluded ONLY 'to the extent that the application relates to that thing as such.' Claims directed to technical implementations can still be patentable."
    note: "Similar to EPC/European approach. Software and business methods are excluded 'as such' but computer-implemented inventions with a technical character/effect can be patentable. Drafting must emphasise technical features and effects."

  methods_of_treatment:
    ref: "Patents Act s25(4)(a)"
    value: "excluded"
    effective_from: null
    effective_until: null
    effect: "Methods of treatment of the human or animal body by surgery, therapy, or diagnosis are not patentable. However, products (e.g., pharmaceutical compounds, medical devices) for use in such methods CAN be patented."
    note: "This differs from US law, where methods of treatment ARE patentable."

  patent_term:
    ref: "Patents Act s45-46"
    value: 20
    unit: "years from filing date"
    effective_from: null
    effective_until: null
    effect: "A patent is valid for 20 years from the filing date, subject to payment of annual renewal fees (annuities). The first annuity is due on the third anniversary of the filing date, and annually thereafter."

  compulsory_licences:
    ref: "Patents Act s56"
    value: true
    effective_from: null
    effective_until: null
    effect: "The Commissioner of Patents may grant a compulsory licence where the patentee abuses patent rights, including: failure to work the invention in SA on a scale adequate to meet demand on reasonable terms, refusal to grant licences on reasonable terms leading to anti-competitive effects, or unreasonable pricing. Also used in public health contexts consistent with TRIPS flexibilities."

  infringement:
    ref: "Patents Act s65-66"
    value: true
    effective_from: null
    effective_until: null
    effect: "Patent infringement includes: for product patents — making, using, exercising, disposing of, offering to dispose of, importing, or stocking the patented product; for process patents — using the patented process and dealing in products obtained directly by that process. SA does not have the same developed doctrine of indirect/contributory infringement as the US."

  remedies:
    ref: "Patents Act s67"
    value: true
    effective_from: null
    effective_until: null
    effect: "Remedies for patent infringement include: interdict, damages (compensatory only — no treble/enhanced damages), reasonable royalty, and delivery up. The Commissioner of Patents (a High Court judge sitting in that capacity) hears patent matters."

  declaration_of_non_infringement:
    ref: "Patents Act s68"
    value: true
    effective_from: null
    effective_until: null
    effect: "Any person may apply to the Commissioner for a declaration that a process or article does not infringe a patent. The applicant must first request and be refused or not receive a written acknowledgement from the patentee."

  depository_system:
    ref: "Patents Act (administrative practice)"
    value: "formal examination only"
    effective_from: null
    effective_until: null
    effect: "SA operates a depository patent system. Patent applications undergo formal examination only (completeness, formalities, classification) — NOT substantive examination for novelty, inventive step, or industrial applicability. A granted SA patent may therefore be invalid. Validity is tested in litigation or revocation proceedings before the Commissioner of Patents."
    note: "Registration does NOT equal validity. Prior-art screening before relying on a patent is essential. In transactions, check the prosecution file and assess validity risk."
```

- [ ] **Step 3: Run validation and commit**

```bash
python3 scripts/validate-za-statutes.py
git add jurisdictions/za/statutes/trade-marks.yaml jurisdictions/za/statutes/patents.yaml
git commit -m "feat(za): add trade-marks and patents statute files"
```

---

## Task 4: Create designs and counterfeit-goods statute files

**Files:**
- Create: `jurisdictions/za/statutes/designs.yaml`
- Create: `jurisdictions/za/statutes/counterfeit-goods.yaml`

- [ ] **Step 1: Create `designs.yaml`**

```yaml
statute: "Designs Act 195 of 1993"
authority: "Companies and Intellectual Property Commission (CIPC)"
last_confirmed: "2025-05-01"
source_url: "https://www.gov.za/documents/designs-act"

sections:
  aesthetic_design:
    ref: "Designs Act s1"
    value: "appearance judged by the eye"
    effective_from: null
    effective_until: null
    effect: "An aesthetic design is any design applied to an article primarily for aesthetic appeal — features judged solely by the eye, irrespective of the article's function. Registered under Part A of the register."

  functional_design:
    ref: "Designs Act s1"
    value: "features necessitated by function"
    effective_from: null
    effective_until: null
    effect: "A functional design has features necessitated by the function that the article is to perform. Registered under Part F of the register."

  registrability_aesthetic:
    ref: "Designs Act s14 (aesthetic)"
    value: "new and original"
    effective_from: null
    effective_until: null
    effect: "An aesthetic design is registrable if it is new and original. The design must not have been published or used in SA before the filing date."

  registrability_functional:
    ref: "Designs Act s14 (functional)"
    value: "new and not commonplace"
    effective_from: null
    effective_until: null
    effect: "A functional design is registrable if it is new and not commonplace in the art. The threshold for functional designs is lower than for aesthetic designs (not commonplace vs original)."

  term_aesthetic:
    ref: "Designs Act s27 (aesthetic)"
    value: 15
    unit: "years from filing date"
    effective_from: null
    effective_until: null
    effect: "An aesthetic design registration is valid for up to 15 years from the filing date, subject to periodic renewal."

  term_functional:
    ref: "Designs Act s27 (functional)"
    value: 10
    unit: "years from filing date"
    effective_from: null
    effective_until: null
    effect: "A functional design registration is valid for up to 10 years from the filing date, subject to periodic renewal."

  infringement:
    ref: "Designs Act s20-21"
    value: true
    effective_from: null
    effective_until: null
    effect: "The registered proprietor has the exclusive right to use the design. Infringement occurs when any person, without authority, uses the registered design for commercial purposes. Remedies include interdict, damages, reasonable royalty, and delivery up."
```

- [ ] **Step 2: Create `counterfeit-goods.yaml`**

```yaml
statute: "Counterfeit Goods Act 37 of 1997"
authority: "Department of Trade, Industry and Competition"
last_confirmed: "2025-05-01"
source_url: "https://www.gov.za/documents/counterfeit-goods-act"

sections:
  counterfeit_definition:
    ref: "Counterfeit Goods Act s1"
    value: true
    effective_from: "1998-01-01"
    effective_until: null
    effect: "Counterfeit goods are goods bearing, without authorization, a trade mark identical or substantially similar to a registered trade mark, or goods that are copies of copyright-protected works made without the owner's consent."

  search_and_seizure:
    ref: "Counterfeit Goods Act s4-6"
    value: true
    effective_from: "1998-01-01"
    effective_until: null
    effect: "Inspectors (appointed under the Act), SAPS, and customs officials may search premises and seize suspected counterfeit goods. Search warrants may be obtained ex parte. Rights holders may lay complaints initiating enforcement action."

  criminal_offences:
    ref: "Counterfeit Goods Act s2-3"
    value: true
    effective_from: "1998-01-01"
    effective_until: null
    effect: "It is a criminal offence to manufacture, produce, package, sell, offer for sale, distribute, or possess for trade purposes goods that the person knows or reasonably suspects are counterfeit. Penalties include fines and imprisonment."

  civil_enforcement_complement:
    ref: "Counterfeit Goods Act (practice)"
    value: true
    effective_from: "1998-01-01"
    effective_until: null
    effect: "Rights holders commonly combine Counterfeit Goods Act criminal enforcement (raids, seizures, prosecution) with civil proceedings (interdicts, damages, delivery up) under the Trade Marks Act or Copyright Act. The criminal route provides supply-chain disruption; the civil route provides compensation."
```

- [ ] **Step 3: Run validation and commit**

```bash
python3 scripts/validate-za-statutes.py
git add jurisdictions/za/statutes/designs.yaml jurisdictions/za/statutes/counterfeit-goods.yaml
git commit -m "feat(za): add designs and counterfeit-goods statute files"
```

---

## Task 5: Create directory structure and router

**Files:**
- Create: `jurisdictions/za/ip-legal/topics/` (directory)
- Create: `jurisdictions/za/ip-legal/router.md`

- [ ] **Step 1: Create directory structure**

```bash
mkdir -p jurisdictions/za/ip-legal/topics
```

- [ ] **Step 2: Create `router.md`**

Write `jurisdictions/za/ip-legal/router.md`:

````markdown
# Skill Router — South African IP Law Overlay

When jurisdiction = ZA, skills load the topic overlays and statute files listed below.

Topic files resolve to: `jurisdictions/za/ip-legal/topics/{name}.md`
Statute files resolve to: `jurisdictions/za/statutes/{name}.yaml`

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
````

- [ ] **Step 3: Commit**

```bash
git add jurisdictions/za/ip-legal/
git commit -m "feat(za): add ip-legal directory structure and router"
```

---

## Task 6: Topic overlay — trademarks.md

**Files:**
- Create: `jurisdictions/za/ip-legal/topics/trademarks.md`

- [ ] **Step 1: Write the topic overlay**

Read the spec Section 3 (Topic Overlay Map, entry #1) for content requirements. Write `jurisdictions/za/ip-legal/topics/trademarks.md` covering:

- SA s34 confusion test (global appreciation — visual, aural, conceptual similarity of marks as wholes; average consumer with imperfect recollection; distinctiveness/strength of earlier mark)
- Key difference from US: no codified multi-factor test (du Pont, Polaroid, Sleekcraft). SA is "global and impressionistic."
- CIPC searching and examination (10-12 months, formal + substantive, Nice classification)
- Clearance beyond the register: well-known marks (s35), common-law passing off, company names (CIPC), domains (.co.za via ZADNA), market reputation
- Well-known marks (s35, Paris Convention) — unregistered foreign marks can block SA use
- Passing off (common-law delict: reputation + misrepresentation + damage)
- Defences (s36: own name, descriptive use, intended purpose)
- First-to-file system
- What NOT to replicate from US practice table (du Pont, Polaroid, Sleekcraft, TTAB, Lanham Act)

- [ ] **Step 2: Commit**

```bash
git add jurisdictions/za/ip-legal/topics/trademarks.md
git commit -m "feat(za): add trademarks topic overlay"
```

---

## Task 7: Topic overlay — patents.md

**Files:**
- Create: `jurisdictions/za/ip-legal/topics/patents.md`

- [ ] **Step 1: Write the topic overlay**

Read spec Section 3 entry #2. Cover:

- SA patentability (s25): new, inventive step, industrial applicability
- **Absolute novelty** (no grace period) — the #1 difference from US practice. Any prior disclosure destroys novelty.
- s25(2)-(3) exclusions with "as such" qualification: discoveries, scientific theories, mathematical methods, business methods, computer programs, presentation of information — excluded ONLY "as such." Technical implementations can be patentable.
- Software/business method patents: European-style technical effect test. Claims must emphasise technical features.
- Methods of treatment: excluded in SA (unlike US). Products for treatment CAN be patented.
- Infringement (s65-66): product patents (making, using, importing) and process patents. No developed doctrine of indirect/contributory infringement.
- Purposive claim construction (not Markman hearing — claim interpretation at trial)
- Compulsory licences (s56): failure to work, anti-competitive refusal to license, public health
- No treble/enhanced damages
- Depository system: formal examination only, validity tested in litigation
- Commissioner of Patents as forum
- What NOT to replicate from US practice table (35 USC §101, Alice/Mayo, doctrine of equivalents, Markman, treble damages, 1-year grace period, Hatch-Waxman)

- [ ] **Step 2: Commit**

```bash
git add jurisdictions/za/ip-legal/topics/patents.md
git commit -m "feat(za): add patents topic overlay"
```

---

## Task 8: Topic overlay — copyright-and-fair-dealing.md

**Files:**
- Create: `jurisdictions/za/ip-legal/topics/copyright-and-fair-dealing.md`

- [ ] **Step 1: Write the topic overlay**

Read spec Section 3 entry #3. Cover:

- SA Copyright Act categories (s2): 9 categories including computer programs
- Subsistence (s3-4): original + qualified person. No registration required (automatic).
- Fair dealing (s12): CLOSED LIST of permitted purposes — research/private study, criticism/review, reporting current events. NOT open-ended US fair use. No "transformative use" doctrine.
- ECTA s77 notice-and-takedown: requirements (full details, precise URL, ownership statement, signature), no statutory counter-notice, ISP safe harbour, ISP over-compliance tendency
- Key difference from US: no DMCA §512. No designated agent registry. No perjury gate. No mandatory put-back.
- Duration: life+50 (not life+70)
- Infringement (s23): direct and secondary
- Remedies (s24): interdict, damages, reasonable royalty, delivery up, account of profits, criminal penalties (s25-27)
- Moral rights (s20): paternity and integrity, cannot assign only waive
- What NOT to replicate from US practice table (DMCA §512, §107 fair use, transformative use, Lenz v Universal, work made for hire, life+70)

- [ ] **Step 2: Commit**

```bash
git add jurisdictions/za/ip-legal/topics/copyright-and-fair-dealing.md
git commit -m "feat(za): add copyright-and-fair-dealing topic overlay"
```

---

## Task 9: Topic overlay — ip-registration-and-renewal.md

**Files:**
- Create: `jurisdictions/za/ip-legal/topics/ip-registration-and-renewal.md`

- [ ] **Step 1: Write the topic overlay**

Read spec Section 3 entry #4. Cover:

- CIPC as registrar (TM, patent, design). No copyright registry.
- TM renewal: 10 years from filing, 6-month pre-expiry filing window, 6-month grace with penalty, indefinitely renewable, non-use cancellation after 5 years
- Patent maintenance: annual annuities from year 3 to year 20, grace period with surcharge, lapse on non-payment
- Design renewal: aesthetic 15yr, functional 10yr, periodic renewals
- Depository patent system: formal examination only, no substantive examination, validity in litigation
- CIPC examination timeline: TM ~10-12 months, significant backlog
- Nice classification for TM
- No §8 declarations (US TM maintenance)
- No USPTO TSDR equivalent
- SA-specific renewal deadlines table
- What NOT to replicate from US practice table (§8 declarations, §8/§9 affidavit, USPTO TSDR, US design patent 35 USC §171)

- [ ] **Step 2: Commit**

```bash
git add jurisdictions/za/ip-legal/topics/ip-registration-and-renewal.md
git commit -m "feat(za): add ip-registration-and-renewal topic overlay"
```

---

## Task 10: Topic overlay — ip-ownership-and-clauses.md

**Files:**
- Create: `jurisdictions/za/ip-legal/topics/ip-ownership-and-clauses.md`

- [ ] **Step 1: Write the topic overlay**

Read spec Section 3 entry #5. Cover:

- SA employer ownership (Copyright Act s21(1)(d)): employer owns copyright in works made in the course of employment, subject to contrary agreement. Different from US work-for-hire doctrine.
- Key difference: US work-for-hire has specific categories (17 USC §101); SA employer ownership applies broadly to "contract of service" relationships
- Independent contractors: SA does NOT automatically vest ownership in the commissioner. Written assignment (s22(3)) is required.
- Assignment formalities: must be in writing, signed by assignor/licensor (s22(3))
- Moral rights (s20): cannot assign, only waive. Include moral rights consent in contracts.
- Background vs foreground IP in SA contracts: define clearly
- IP from Publicly Financed R&D Act 51 of 2008: publicly funded research IP vests in the institution, not the funder. Relevant for university/research collaborations.
- Restraint of trade: SA common law — enforceable only if reasonable and necessary to protect a legitimate interest
- Trade secrets: no dedicated statute. Protection via common-law confidentiality, contract, delict/unlawful competition. Operational controls essential.
- What NOT to replicate from US practice table (work made for hire 17 USC §101, DTSA, inevitable disclosure doctrine)

- [ ] **Step 2: Commit**

```bash
git add jurisdictions/za/ip-legal/topics/ip-ownership-and-clauses.md
git commit -m "feat(za): add ip-ownership-and-clauses topic overlay"
```

---

## Task 11: Topic overlay — ip-enforcement.md

**Files:**
- Create: `jurisdictions/za/ip-legal/topics/ip-enforcement.md`

- [ ] **Step 1: Write the topic overlay**

Read spec Section 3 entry #6. Cover:

- Interdicts (interim and final): primary enforcement tool. Requirements: clear right (or prima facie for interim), infringement/threat, no adequate alternative remedy. SA term is "interdict" not "injunction."
- Damages: compensatory only. No treble/punitive damages. Lost profits, price erosion.
- Reasonable royalty: hypothetical licence fee
- Account of profits: disgorgement of infringer's profits
- Delivery up/destruction of infringing goods
- Anton Piller orders: ex parte search and seizure for evidence preservation. Requirements: strong prima facie case, serious potential damage, clear evidence respondent has relevant material, real risk of destruction. Supervising attorney required.
- Counterfeit Goods Act 37 of 1997: criminal enforcement via raids, seizure, prosecution. Combine with civil proceedings for full enforcement strategy.
- Commissioner of Patents: patent forum (High Court judge sitting in that capacity)
- Costs: loser-pays default (party-and-party scale)
- Forum: High Court for TM/copyright/design; Commissioner of Patents for patent
- What NOT to replicate from US practice table (treble damages, ITC exclusion orders, Section 337, TRO under DTSA, customs seizure 19 USC)

- [ ] **Step 2: Commit**

```bash
git add jurisdictions/za/ip-legal/topics/ip-enforcement.md
git commit -m "feat(za): add ip-enforcement topic overlay"
```

---

## Task 12: Practice profile template

**Files:**
- Create: `jurisdictions/za/ip-legal/practice-profile-template.md`

- [ ] **Step 1: Write the practice profile template**

Read the US template (`ip-legal/CLAUDE.md`) for structure and the spec Section 4 for all replacement decisions. Follow the litigation-legal practice profile template (`jurisdictions/za/litigation-legal/practice-profile-template.md`) for the SA configuration block pattern.

Key SA-specific adaptations:
- Configuration comment block: adapt path to ip-legal, add ZA overlay router instruction
- Work-product header: SA privilege formulation. Drop patent agent privilege section entirely.
- Who's using this: "Patent attorney" (not "Registered patent agent"). Drop In re Queen's University.
- Available integrations: SAFLII/Juta instead of CourtListener/Descrybe. Add CIPC online services.
- Source tags: SAFLII/Juta/CIPC instead of Westlaw/CourtListener/USPTO
- IP practice profile — Registered in: CIPC (TM/patent/design), Madrid, PCT, ARIPO
- Outside counsel roster: patent attorneys + advocates for Commissioner/High Court
- IP portfolio: SA-specific deadlines (TM 10yr, patent annual annuities, design aesthetic 15yr/functional 10yr). No §8 declarations.
- Brand protection: SA + regional watch jurisdictions
- Enforcement posture: drop TTAB. CIPC opposition + High Court. Interdict not injunction. Add Counterfeit Goods Act raid. Replace DMCA takedown with ECTA s77.
- New sections: SA IP registration landscape, SA patentability notes, SA trademark framework, SA copyright and takedowns, SA enforcement landscape
- Seed documents: 8 SA-specific (TM portfolio, patent portfolio, design registrations, C&D template, OSS policy, IP assignment template, brand guidelines, ECTA s77 template)

Ensure no US-forbidden terms outside privilege caveat (no USPTO, no DMCA §512, no Lanham Act, no 35 USC, no §8 declarations, no TTAB, no du Pont, no Bluebook).

- [ ] **Step 2: Commit**

```bash
git add jurisdictions/za/ip-legal/practice-profile-template.md
git commit -m "feat(za): add ip-legal ZA practice profile template"
```

---

## Task 13: Cold-start interview fork

**Files:**
- Modify: `ip-legal/skills/cold-start-interview/SKILL.md`

- [ ] **Step 1: Read existing cold-start interview**

```bash
cat ip-legal/skills/cold-start-interview/SKILL.md
```

Locate the end of Part 0 (role, integrations). The ZA fork goes after Part 0, following the same pattern as `litigation-legal/skills/cold-start-interview/SKILL.md`.

- [ ] **Step 2: Add the ZA fork**

Insert after Part 0:

```markdown
---

## Jurisdiction fork

After Part 0, check the company profile's primary jurisdiction:
- Read `~/.claude/plugins/config/claude-for-legal/company-profile.md`
- Check the `jurisdiction` or `Primary jurisdiction` field

**If PRIMARY JURISDICTION = "South Africa" (or "ZA" or matches SA):** fork to the SA interview path below.
**Otherwise:** continue with the standard interview.

---

## SA Interview Path — IP Practice

*This path runs instead of the US-specific interview when jurisdiction = ZA.*

### Part 1: SA IP Footprint (3-5 minutes)

**Q1: IP types** — "Which IP types does your SA practice cover?"
- Options: Trademark, Patent, Design, Copyright, Trade secret, Open source, All
- Multiple select allowed
- Writes to: `## IP practice profile — Practice area mix`

**Q2: SA registrations** — "Do you hold SA registrations at CIPC? If yes, can you provide or upload your trademark, patent, and design registration numbers?"
- Free text or file upload
- Writes to: `## IP portfolio`

**Q3: Absolute novelty** — "Important: SA requires absolute novelty for patents — there is no 1-year grace period like the US. Any public disclosure before filing destroys novelty. Is your team aware of this requirement?"
- Options: Yes — we have processes for this, No — we need to implement disclosure controls, Not sure
- Writes to: `## SA patentability notes`

**Q4: Outside counsel** — "Do you use patent attorneys registered with CIPC, or do you also brief advocates for Commissioner of Patents proceedings?"
- Options: Patent attorneys only, Patent attorneys + advocates, Varies by matter
- Writes to: `## IP practice profile — Outside counsel roster`

**Q5: Enforcement posture** — "For enforcement in the SA market, do you use the Counterfeit Goods Act (criminal raids) in addition to civil interdicts?"
- Options: Civil only (interdicts, damages), Civil + criminal (Counterfeit Goods Act), Criminal-led (raids first), Depends on the matter
- Writes to: `## Enforcement posture`

**Q6: Takedowns** — "For online copyright infringement, do you file ECTA s77 takedown notices, or do you rely on platform-specific (DMCA-style) processes?"
- Options: ECTA s77 notices, Platform-specific (DMCA/DSA), Both depending on where hosted, Haven't needed to yet
- Writes to: `## SA copyright and takedowns`

**Q7: Currency** — "What currency do you use for IP budgets, enforcement thresholds, and settlement authority?"
- Options: ZAR, USD, EUR, Other
- Writes to: `## Enforcement posture — approval matrix`

### Part 2: Build the configuration

- Use ZA practice profile template from `jurisdictions/za/ip-legal/practice-profile-template.md`
- Populate sections from interview answers
- Write to `~/.claude/plugins/config/claude-for-legal/ip-legal/CLAUDE.md`
- Include the overlay loading instruction: "After loading context, read `jurisdictions/za/ip-legal/router.md` and load the listed overlays for this skill."
```

- [ ] **Step 3: Commit**

```bash
git add ip-legal/skills/cold-start-interview/SKILL.md
git commit -m "feat(za): add ZA fork to ip-legal cold-start interview"
```

---

## Task 14: Extend validation scripts

**Files:**
- Modify: `scripts/validate-za-router.py`
- Modify: `scripts/validate-za-templates.py`

- [ ] **Step 1: Add ip-legal to router validator**

In `scripts/validate-za-router.py`, find the `PRACTICE_AREAS` list and add `"ip-legal"`:

```python
PRACTICE_AREAS = [
    "employment-legal",
    "commercial-legal",
    "privacy-legal",
    "litigation-legal",
    "ip-legal",  # Phase 5
]
```

- [ ] **Step 2: Add ip-legal to template validator**

In `scripts/validate-za-templates.py`, find the `TEMPLATE_CONFIG` dict and add before the closing `}`:

```python
"ip-legal": {
    "path": ROOT / "jurisdictions" / "za" / "ip-legal" / "practice-profile-template.md",
    "required_sections": [
        "IP Practice Profile",
        "Company profile",
        "Who's using this",
        "Outputs",
        "IP practice profile",
        "IP portfolio",
        "Brand protection",
        "Enforcement posture",
        "SA IP registration landscape",
        "SA patentability notes",
        "SA enforcement landscape",
    ],
    "sa_required_terms": [
        "CIPC",
        "Trade Marks Act",
        "Patents Act",
        "Designs Act",
        "Copyright Act",
        "ECTA",
        "interdict",
        "legal practitioner",
        "patent attorney",
        "fair dealing",
        "absolute novelty",
    ],
    "us_forbidden": [
        (r"\bUSPTO\b", "USPTO"),
        (r"\bLanham Act\b", "Lanham Act"),
        (r"\bDMCA\b", "DMCA"),
        (r"\b35 USC\b", "35 USC"),
        (r"\bTTAB\b", "TTAB"),
        (r"\bdu Pont\b", "du Pont"),
        (r"\bPolaroid\b", "Polaroid"),
        (r"\bSleekcraft\b", "Sleekcraft"),
        (r"\b§8 declaration\b", "§8 declaration"),
        (r"\bBluebook\b", "Bluebook"),
    ],
},
```

- [ ] **Step 3: Run both validators**

```bash
python3 scripts/validate-za-router.py && python3 scripts/validate-za-templates.py
```

Expected: PASS — all topic/statute references resolve, template has required sections and terms, no forbidden terms.

- [ ] **Step 4: Commit**

```bash
git add scripts/validate-za-router.py scripts/validate-za-templates.py
git commit -m "feat(za): extend validators for ip-legal overlay"
```

---

## Task 15: Eval cases — trademarks, patents, copyright (9 cases)

**Files:**
- Create: 9 eval case YAML files in `jurisdictions/za/evals/ip-legal/`

- [ ] **Step 1: Create eval directories**

```bash
mkdir -p jurisdictions/za/evals/ip-legal/{clearance,cease-desist,infringement-triage,invention-intake,fto-triage,takedown,oss-review}
```

- [ ] **Step 2: Write trademark eval cases**

Write `jurisdictions/za/evals/ip-legal/clearance/case-01-well-known-foreign.yaml`:

```yaml
name: "Clearance with well-known foreign mark"
skill: clearance
input: |
  Client wants to launch "AURORA" for cosmetics in South Africa. A search of
  the CIPC register shows no identical or similar marks in class 3. However,
  Aurora is a well-known international cosmetics brand with significant online
  presence and SA consumer awareness.

expected_flags:
  - "well-known mark"
  - "passing off"
  - "s35"

must_not_contain:
  - "du Pont factors"
  - "Polaroid test"
  - "Sleekcraft"
  - "likelihood of confusion under Lanham Act"
  - "TTAB"

notes: |
  The CIPC register is clear but the well-known international brand creates a
  conflict risk under Trade Marks Act s35 (Paris Convention). The skill should
  flag that register-only clearance is insufficient and that SA protects
  well-known foreign marks even without local registration. Common-law passing
  off is also a risk if the foreign brand has SA reputation.
```

Write `jurisdictions/za/evals/ip-legal/cease-desist/case-02-inbound-cd.yaml`:

```yaml
name: "Inbound C&D from SA rights holder"
skill: cease-desist
input: |
  Our company received a cease-and-desist letter from a SA law firm alleging
  trademark infringement under Trade Marks Act s34(1)(a). They claim our mark
  is confusingly similar to their client's registered mark on identical goods.
  They demand we cease use within 14 days or they will apply for an interdict.

expected_flags:
  - "costs"
  - "s34"

must_not_contain:
  - "TTAB cancellation"
  - "Lanham Act §32"
  - "federal registration"
  - "US district court"

notes: |
  The skill should triage the C&D under SA law: assess s34(1)(a) using the
  global appreciation test (not US multi-factor), flag loser-pays costs
  exposure, note that the threat is an interdict (SA term, not injunction),
  and present response options (cease, negotiate, defend, counterclaim).
```

Write `jurisdictions/za/evals/ip-legal/infringement-triage/case-03-passing-off.yaml`:

```yaml
name: "Passing off claim — unregistered mark"
skill: infringement-triage
input: |
  A competitor has been using a confusingly similar trading name for their
  coffee shop chain in Johannesburg for 5 years. They have no trademark
  registration. Our client has used their name for 8 years and wants to
  assert rights.

expected_flags:
  - "passing off"
  - "reputation"

must_not_contain:
  - "Lanham Act §43(a)"
  - "federal unfair competition"
  - "state unfair competition statute"
  - "TTAB"

notes: |
  SA passing off is a common-law delict (not statutory). The skill should
  assess: (1) reputation/goodwill in SA (8 years of use), (2) misrepresentation
  by the competitor (confusingly similar name), (3) damage or likelihood of
  damage. Remedies: interdict and damages.
```

- [ ] **Step 3: Write patent eval cases**

Write `jurisdictions/za/evals/ip-legal/invention-intake/case-01-prior-disclosure.yaml`:

```yaml
name: "Invention disclosure — prior conference presentation"
skill: invention-intake
input: |
  An engineer at our Johannesburg office presented the invention at an
  industry conference 3 months ago. The presentation included technical
  details of the invention. No patent application has been filed. The
  engineer now wants to file a patent in South Africa.

expected_flags:
  - "absolute novelty"
  - "bar date"
  - "prior disclosure"

must_not_contain:
  - "one-year grace period"
  - "§102(a)(1)"
  - "inventor's own disclosure exception"
  - "35 USC"

notes: |
  SA requires absolute novelty. The conference presentation 3 months ago
  is a public disclosure that almost certainly destroys novelty. There is
  NO 1-year grace period. The skill must flag this as a critical issue and
  advise that SA patent rights are likely lost. Foreign filing options may
  also be compromised.
```

Write `jurisdictions/za/evals/ip-legal/fto-triage/case-02-software-method.yaml`:

```yaml
name: "FTO triage — software payment method"
skill: fto-triage
input: |
  Our fintech startup wants to launch a new payment processing method in
  South Africa. A competitor holds a SA patent (granted under the depository
  system) on a related software-implemented payment method. We need to
  assess freedom to operate.

expected_flags:
  - "depository patent"
  - "validity"

must_not_contain:
  - "Alice/Mayo test"
  - "35 USC §101"
  - "abstract idea"
  - "CAFC"
  - "doctrine of equivalents"
  - "willfulness"
  - "treble damages"

notes: |
  The skill should flag that SA patents are granted without substantive
  examination (depository system) — the competitor's patent may be invalid.
  For software patents, SA uses the "as such" exclusion (s25(2)-(3)) with
  a European-style technical effect test. Infringement analysis uses
  purposive claim construction (no Markman hearing). No treble damages.
```

Write `jurisdictions/za/evals/ip-legal/fto-triage/case-03-compulsory-licence.yaml`:

```yaml
name: "Compulsory licence risk — pharma patent"
skill: fto-triage
input: |
  A foreign pharmaceutical company holds a SA patent for a critical
  medication but only imports the finished product — no local manufacture.
  A SA generic manufacturer is threatening to apply for a compulsory
  licence under Patents Act s56 on grounds of failure to work the patent
  in South Africa.

expected_flags:
  - "compulsory licence"
  - "s56"

must_not_contain:
  - "Hatch-Waxman"
  - "ANDA"
  - "Paragraph IV certification"
  - "FDA Orange Book"

notes: |
  The skill should assess the compulsory licence risk under s56: failure
  to work the patent in SA on a scale adequate to meet demand. Import-only
  may constitute failure to work. The patentee should document commercial
  rationale and consider local manufacturing or licensing strategies.
```

- [ ] **Step 4: Write copyright/takedown eval cases**

Write `jurisdictions/za/evals/ip-legal/takedown/case-01-ecta-s77.yaml`:

```yaml
name: "ECTA s77 takedown notice for copyright infringement"
skill: takedown
input: |
  Our client's copyrighted product photographs are being used without
  permission on a South African-hosted e-commerce website. The client
  wants to send a takedown notice to have the images removed.

expected_flags:
  - "ECTA"
  - "takedown"
  - "s77"

must_not_contain:
  - "DMCA §512(c)(3)"
  - "designated DMCA agent"
  - "§512(f)"
  - "Lenz v Universal"
  - "counter-notice"
  - "17 USC"

notes: |
  SA uses ECTA Chapter XI s77, not DMCA §512. The skill should draft the
  notice with all required elements: full contact details, precise URL,
  description of infringed right, statement of ownership, signature. Flag
  that there is no statutory counter-notice regime — ISPs tend to
  over-comply with removal.
```

Write `jurisdictions/za/evals/ip-legal/infringement-triage/case-02-fair-dealing.yaml`:

```yaml
name: "Fair dealing edge case — comparative review"
skill: infringement-triage
input: |
  A SA company wants to use excerpts from a competitor's technical manual
  in a comparative product review published on their commercial website.
  They claim this is fair use.

expected_flags:
  - "fair dealing"
  - "s12"

must_not_contain:
  - "fair use four-factor test"
  - "transformative use"
  - "§107"
  - "Campbell v Acuff-Rose"

notes: |
  SA has fair dealing (s12), not fair use. The permitted purposes are a
  closed list: research/private study, criticism/review, news reporting.
  "Criticism or review" may cover a comparative review, but it must be
  genuinely critical/analytical, not just commercial use of competitor
  content. The skill must NOT apply the US 4-factor fair use test.
```

Write `jurisdictions/za/evals/ip-legal/oss-review/case-03-agpl-saas.yaml`:

```yaml
name: "AGPL copyleft in SA SaaS context"
skill: oss-review
input: |
  Our SA SaaS company has discovered AGPL-licensed code in the backend of
  our payment processing service. We don't distribute binaries — the
  service is accessed over a network by SA customers.

expected_flags: []

must_not_contain:
  - "fair use defence to copyleft"
  - "§107 applies to licence obligations"

notes: |
  OSS licensing analysis is largely jurisdiction-neutral. AGPL's network
  interaction trigger applies regardless of jurisdiction. The skill should
  analyse the copyleft obligation (source code disclosure for network
  users) without invoking US fair use as a defence to licence terms. SA
  fair dealing (s12) would not provide a defence to copyleft obligations.
```

- [ ] **Step 5: Commit**

```bash
git add jurisdictions/za/evals/ip-legal/
git commit -m "feat(za): add 9 ip-legal eval cases (trademarks, patents, copyright)"
```

---

## Task 16: Eval cases — registration, clauses, enforcement (9 cases)

**Files:**
- Create: 9 remaining eval case YAML files

- [ ] **Step 1: Create remaining directories**

```bash
mkdir -p jurisdictions/za/evals/ip-legal/{portfolio,ip-clause-review}
```

- [ ] **Step 2: Write registration eval cases**

Write `jurisdictions/za/evals/ip-legal/portfolio/case-01-tm-renewal.yaml`:

```yaml
name: "SA trademark renewal approaching"
skill: portfolio
input: |
  Our SA trademark registration (CIPC) is expiring in 4 months. We need
  to confirm the renewal process, deadline, and fees.

expected_flags:
  - "renewal"
  - "deadline"

must_not_contain:
  - "§8 declaration"
  - "§8 and §9 affidavit"
  - "USPTO TSDR"
  - "Section 8 maintenance"
  - "Section 9 renewal"

notes: |
  SA TM renewal: 10-year term, can file from 6 months before expiry,
  6-month grace period with penalty after expiry. Administrative process
  at CIPC — form plus fee, per class. No re-examination. The skill should
  NOT reference US §8 declarations or USPTO TSDR.
```

Write `jurisdictions/za/evals/ip-legal/portfolio/case-02-design-dual-filing.yaml`:

```yaml
name: "Design registration — aesthetic and functional dual filing"
skill: portfolio
input: |
  Our client has a new product with both aesthetic appeal (a distinctive
  curved shape) and functional features (ventilation slots that improve
  airflow). We need to register the design in South Africa.

expected_flags:
  - "design category"
  - "aesthetic"
  - "functional"
  - "dual filing"

must_not_contain:
  - "US design patent"
  - "35 USC §171"
  - "ornamental design"
  - "utility patent"

notes: |
  SA has two design categories: aesthetic (Part A, up to 15 years) and
  functional (Part F, up to 10 years). The skill should recommend dual
  filing (both Part A and Part F) to protect both the visual appeal and
  the functional features. Misclassification is a common pitfall.
```

- [ ] **Step 3: Write IP clause eval cases**

Write `jurisdictions/za/evals/ip-legal/ip-clause-review/case-01-contractor-no-assignment.yaml`:

```yaml
name: "Contractor agreement missing IP assignment"
skill: ip-clause-review
input: |
  Reviewing a software development agreement with an independent contractor
  in Cape Town. The contract covers development of a custom e-commerce
  platform. There is no IP assignment clause. Payment terms are specified
  but nothing about IP ownership.

expected_flags:
  - "assignment"
  - "ownership"
  - "s22(3)"
  - "moral rights"

must_not_contain:
  - "work made for hire"
  - "17 USC §101"
  - "work for hire categories"
  - "employer owns under US copyright"

notes: |
  Under SA law, payment does not equal ownership. The contractor (not the
  client) owns the copyright unless there is a written assignment (Copyright
  Act s22(3)). The skill must flag the missing assignment clause as critical
  and recommend: express written assignment, moral rights waiver (s20),
  and definition of background vs foreground IP.
```

Write `jurisdictions/za/evals/ip-legal/ip-clause-review/case-02-trade-secret-nda.yaml`:

```yaml
name: "Trade secret NDA review — SA common law"
skill: ip-clause-review
input: |
  Reviewing a mutual NDA for a potential joint venture partner. We need
  to assess whether it adequately protects our trade secrets under South
  African law. Our trade secrets include proprietary algorithms and
  customer data analytics methodologies.

expected_flags:
  - "trade secret"
  - "no statute"
  - "common law"

must_not_contain:
  - "DTSA"
  - "Defend Trade Secrets Act"
  - "18 USC §1836"
  - "inevitable disclosure doctrine"

notes: |
  SA has no dedicated trade secrets statute. Protection relies on
  common-law confidentiality, contract, and delict/unlawful competition.
  The skill should assess: (1) is confidential information clearly
  defined, (2) are obligations adequate (no disclosure, no use beyond
  purpose, return/destruction), (3) are remedies specified (interdict,
  damages), (4) operational controls recommended beyond the contract.
```

- [ ] **Step 4: Write enforcement eval cases**

Write `jurisdictions/za/evals/ip-legal/cease-desist/case-01-counterfeit-raid.yaml`:

```yaml
name: "Counterfeit goods — combined civil and criminal enforcement"
skill: cease-desist
input: |
  Large-scale counterfeiting of our client's trademarked clothing brand
  has been discovered at a market in Johannesburg. Multiple vendors are
  selling counterfeit goods bearing our client's registered trade mark.
  The client wants to take enforcement action using both civil and
  criminal channels.

expected_flags:
  - "counterfeit"
  - "raid"
  - "enforcement"

must_not_contain:
  - "customs seizure under 19 USC"
  - "ITC exclusion order"
  - "Section 337 investigation"
  - "CBP"

notes: |
  The skill should recommend a combined strategy: (1) Counterfeit Goods
  Act criminal enforcement — lay complaint, obtain search warrant, conduct
  raid with inspectors/SAPS, seize goods; (2) civil proceedings — apply
  for interdict under Trade Marks Act s34, claim damages, seek delivery up.
  Flag: need sufficient evidence before raid, proper warrant, chain of
  custody, and budget for follow-through.
```

Write `jurisdictions/za/evals/ip-legal/infringement-triage/case-04-anton-piller.yaml`:

```yaml
name: "Anton Piller order for trade secret preservation"
skill: infringement-triage
input: |
  A former senior developer left our SA company and joined a competitor.
  We believe they took proprietary source code and customer data. There
  is a risk they will destroy the evidence if we notify them of legal
  proceedings. We need to preserve the evidence.

expected_flags:
  - "trade secret"
  - "Anton Piller"
  - "evidence preservation"

must_not_contain:
  - "TRO under DTSA"
  - "ex parte seizure under 18 USC §1836"
  - "federal trade secret injunction"
  - "inevitable disclosure"

notes: |
  The skill should recommend an Anton Piller order (ex parte search and
  seizure) from the High Court. Requirements: (1) strong prima facie case
  of misappropriation, (2) serious potential damage, (3) clear evidence
  respondent has the material, (4) real risk of destruction. A supervising
  attorney is required. Also consider: urgent interdict to prevent further
  use, NDA/employment contract review for restraint clauses.
```

- [ ] **Step 5: Commit**

```bash
git add jurisdictions/za/evals/ip-legal/
git commit -m "feat(za): add 9 ip-legal eval cases (registration, clauses, enforcement)"
```

---

## Task 17: Final validation run

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
echo "=== Topic overlays ===" && ls jurisdictions/za/ip-legal/topics/*.md | wc -l
echo "=== Eval cases ===" && find jurisdictions/za/evals/ip-legal -name "*.yaml" | wc -l
echo "=== Router ===" && ls jurisdictions/za/ip-legal/router.md
echo "=== Practice profile ===" && ls jurisdictions/za/ip-legal/practice-profile-template.md
```

Expected:
- Statute files: 26 (22 existing + 4 new)
- Topic overlays: 6
- Eval cases: 18
- Router: exists
- Practice profile: exists

- [ ] **Step 3: Verify no US concepts leaked into ZA overlay files**

```bash
grep -rl "\bUSPTO\b\|\bLanham Act\b\|\bDMCA\b\|\b35 USC\b\|\bTTAB\b\|\bdu Pont\b\|\bPolaroid\b\|\bSleekcraft\b\|\bBluebook\b" jurisdictions/za/ip-legal/topics/ jurisdictions/za/ip-legal/practice-profile-template.md 2>/dev/null || echo "No US concepts found in overlay files — CLEAN"
```

Expected: Topic overlay files will contain US terms in "What NOT to replicate" tables (expected). Practice profile template should be clean.

- [ ] **Step 4: Final commit if any fixes were needed**

```bash
git status
# If clean: no commit needed
# If fixes: git add <files> && git commit -m "fix(za): address validation findings in ip-legal overlay"
```
