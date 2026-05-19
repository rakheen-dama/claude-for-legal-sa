# ZA Overlay Expansion: regulatory-legal

**Date:** 2026-05-20
**Plugin:** regulatory-legal v1.0.2
**Target jurisdiction:** South Africa (ZA)
**Status:** Spec complete — ready for implementation planning

---

## Decision Summary

| # | Step | Decision | Source |
|---|---|---|---|
| 1 | Target | regulatory-legal — 9 skills, 6 in scope for v1 | user confirmed |
| 2 | Statutes | 7 existing (extend) + 7 new (PAJA, FSR, FICA, NEMA, OHSA, NCA, PRECCA) | Perplexity + user confirmed |
| 3 | Skill divergence | 4 HIGH (reg-feed-watcher, policy-diff, comments, cold-start-interview), 2 MEDIUM (gap-surfacer, policy-redraft), 3 LOW (gaps, customize, matter-workspace) | user confirmed |
| 4 | Topic overlays | 4 topics: regulatory-process, feed-sources, rule-status-verification, regulators | user confirmed |
| 5 | Practice profile | SA privilege framework, 3 new sections (regulatory landscape, consultation engagement posture, Gazette monitoring), SA-specific materiality examples, seed documents | Perplexity + user confirmed |
| 6 | Cold-start questions | 6 must-have + 4 nice-to-have, quick (2 min) and full (15 min) tracks | user confirmed |
| 7 | High-risk flags | 12 flags covering Gazette commencement trap, licence gaps, deadline misses, B-BBEE fronting, POPIA breach, comment periods, AML/CFT, competition thresholds, rule status, PAJA fairness, provincial divergence, industry body divergence | Perplexity + user confirmed |
| 8 | Validation | 20 eval cases across 6 skills, 5 domain-specific validation rules, expert review gate | user confirmed |

---

## 1. Statute Inventory

### Existing statutes — extend for regulatory-legal use

| Statute | File | Already covered | New sections for regulatory-legal |
|---|---|---|---|
| POPIA (Act 4 of 2013) | `popia.yaml` | 23 entries: consent, breach notification, fines, DPO duties | Information Regulator enforcement powers (s73-77), code of conduct process (s60-65) |
| CPA (Act 68 of 2008) | `cpa.yaml` | 6 entries: thresholds, cooling-off, fines | NCC complaint procedures (s71-73), product safety recalls (s60), industry codes (s82) |
| Competition Act (89 of 1998) | `competition.yaml` | 4 entries: prohibited practices, penalties | Merger notification thresholds (s11-13), Commission investigation powers (s49A-49D), leniency |
| ECTA (Act 25 of 2002) | `ecta.yaml` | 8 entries: e-signatures, contracts, takedowns | Cryptography registration (s29-30) |
| Cybercrimes Act (19 of 2020) | `cybercrimes.yaml` | 6 entries: offences, breach reporting, penalties | CSIRT reporting obligations (when s54 commences) |
| B-BBEE Act (53 of 2003) | `bbbee.yaml` | 6 entries: thresholds, procurement scoring, fronting | B-BBEE Commission investigation powers (s13F-13J), sector code process |
| PAIA (Act 2 of 2000) | `paia.yaml` | 4 entries: manual requirements, information officer | Internal appeal/review timelines (s74-77), Information Regulator complaint process |

### New statutes to create

| Statute | File | Key sections | Temporal/threshold values | Source |
|---|---|---|---|---|
| **PAJA (Promotion of Administrative Justice Act 3 of 2000)** | `paja.yaml` | s3 (procedurally fair admin action), s4 (admin action affecting public — notice-and-comment), s5 (written reasons), s6 (judicial review grounds), s7 (internal remedies) | 180-day judicial review limit (s7(1)) | [Perplexity — verify] |
| **FSR Act (Financial Sector Regulation Act 9 of 2017)** | `fsr.yaml` | s98-106 (PA standards-making), s107-115 (FSCA conduct standards), s126 (joint standards), s131-136 (consultation procedures for standards), s144 (transitional) | Comment periods for draft standards (typically 30-60 days per s133) | [Perplexity — verify] |
| **FICA (Financial Intelligence Centre Act 38 of 2001)** | `fica.yaml` | s21 (RMCP), s21A-21H (beneficial ownership), s28A (suspicious transactions), s29 (reporting), Schedule 1 (accountable institutions), s64 (administrative sanctions) | Cash transaction reporting threshold R24,999.99, administrative penalties | [Perplexity — verify] |
| **NEMA (National Environmental Management Act 107 of 1998)** | `nema.yaml` | s24 (EIA requirements), s28 (duty of care), s31A-31O (compliance notices, directives), Listing Notices 1-3 (GN R327-R325) | EIA comment period (30 days min per EIA regs), compliance notice response periods | [Perplexity — verify] |
| **OHSA (Occupational Health and Safety Act 85 of 1993)** | `ohsa.yaml` | s8 (general duties), s16 (CEO duty), s24 (incident reporting), s43 (administrative fines), Regulations (HCS, MHI, ERE, Construction) | Incident reporting: s24 "as soon as practicable" + written within 7 days; MHI thresholds | [Perplexity — verify] |
| **NCA (National Credit Act 34 of 2005)** | `nca.yaml` | s40-41 (credit provider registration), s60-65 (reckless credit), s86-88 (debt counselling), s150-151 (NCR enforcement), s171 (administrative fines) | Registration thresholds, reckless lending limits, interest rate caps (per NCR regulations) | [Perplexity — verify] |
| **PRECCA (Prevention and Combating of Corrupt Activities Act 12 of 2004)** | `precca.yaml` | s3-16 (corruption offences), s34 (reporting duty for persons in position of authority), s26 (penalties) | s34 reporting duty threshold: actual or suspected offence involving R100,000+ | [Perplexity — verify] |

---

## 2. Skill Divergence Matrix

| Skill | Description | Divergence | In scope v1 | Reasoning |
|---|---|---|---|---|
| `reg-feed-watcher` | Pull feeds, filter, produce digest | **HIGH** | **Y** | Federal Register API, US agency slugs, NPRMs, CourtListener. SA needs Government Gazette, Open Gazettes, Laws.Africa, SA regulator feeds. |
| `policy-diff` | Diff reg change against policy library | **HIGH** | **Y** | Federal Register docket for rule-status verification. SA uses Gazette proclamation checks, PAJA s6 judicial review. |
| `comments` | Track comment periods, log decisions | **HIGH** | **Y** | Built around NPRM comment periods. SA has Gazette notice-and-comment, PAJA s4, regulator-specific consultation. |
| `cold-start-interview` | Onboarding, build watchlist, configure | **HIGH** | **Y** | US regulators, Federal Register API slugs, Thomson Reuters. SA needs different regulator list, Open Gazettes, Laws.Africa. |
| `gap-surfacer` | Track gaps, route to owners, notify | **MEDIUM** | **Y** | NPRM references in gap types. Maps to SA Gazette consultation but terminology needs overlay. |
| `policy-redraft` | Produce marked-up policy redraft | **MEDIUM** | **Y** | Rule-status check inherits US Federal Register references. Core workflow portable. |
| `gaps` | View, close, risk-accept gaps | LOW | N | Thin wrapper. Jurisdiction-neutral. |
| `customize` | Edit practice profile sections | LOW | N | Jurisdiction-neutral infrastructure. |
| `matter-workspace` | Per-matter isolation | LOW | N | Jurisdiction-neutral infrastructure. |

---

## 3. Topic Overlay Map

All topic files live in `jurisdictions/za/regulatory-legal/topics/`.

### 3.1 `regulatory-process.md`

**Skills served:** reg-feed-watcher, comments, cold-start-interview

**Content:**

- SA rulemaking framework — replaces APA/NPRM/Federal Register framework
- Government Gazette as publication channel: Acts, regulations, notices, determinations, directives
- Government Printing Works (GPW) publication process
- PAJA s3 (procedurally fair admin action for individuals)
- PAJA s4 (admin action affecting the public — notice-and-comment):
  - s4(1)(a): publication of notice with reasonable comment period
  - s4(1)(b): public inquiry with presiding official
  - s4(1)(c): notice-and-comment procedure (formalised)
  - s4(1)(d): advisory committee
  - s4(1)(e): combination
  - "Reasonable period" standard (no hard-coded minimum — fact-specific)
- Typical comment periods by regulator type:
  - Standard: 30 days
  - Complex/technical: 45-60 days (FSCA conduct standards, ICASA spectrum)
  - Urgent/minor: 14-21 days
  - Major reforms: up to 90 days
- Multi-step rulemaking: discussion paper → draft → final (common for FSCA, NERSA)
- Comment submission mechanics: email/post to publishing regulator (no Regulations.gov equivalent)
- NEDLAC process for major socio-economic legislation
- Parliamentary committee submissions and public hearings
- Gazette commencement rules: in force on publication date OR specified future date OR by proclamation

### 3.2 `feed-sources.md`

**Skills served:** reg-feed-watcher, cold-start-interview

**Content:**

- SA feed architecture — replaces Federal Register API + CourtListener
- **Tier 1 — Free feeds (always active):**
  - Open Gazettes (opengazettes.org.za):
    - Atom feed: recently added gazettes (last 100)
    - JSON index: metadata for all gazettes (date, number, type, URL)
    - Search by keyword, date range, Gazette type
  - Direct regulator RSS/email subscriptions (per-regulator URLs)
  - gov.za Documents/Notices interface
- **Tier 2 — Structured/paid feeds:**
  - Laws.Africa Content API:
    - Akoma Ntoso XML/HTML for Acts, regulations, notices
    - Citation graphs, amendment tracking
    - Free for non-commercial; commercial subscriptions available
  - Sabinet (SA legal database — paid)
- **No SA equivalent of:** Federal Register API (per-agency structured JSON), Regulations.gov (centralised comment portal), CourtListener (free case law API)
- Regulator-to-feed mapping table (for each of the core 12 regulators):
  - Website URL for consultations/publications
  - RSS feed URL (if available)
  - Email subscription mechanism
  - Gazette notice format and typical keywords
- Feed check workflow:
  1. Pull Open Gazettes Atom feed for new entries since last check
  2. Filter by keyword/regulator against watchlist
  3. Pull per-regulator RSS/email for non-Gazette publications (guidance notes, media statements)
  4. De-duplicate across sources
  5. Classify by materiality threshold
  6. Produce digest

### 3.3 `rule-status-verification.md`

**Skills served:** policy-diff, policy-redraft, gap-surfacer

**Content:**

- SA rule-status verification — replaces Federal Register docket / stays / injunctions / vacatur
- **How SA regulations come into force:**
  - On date of publication in Government Gazette (default)
  - On future date specified in the regulation
  - By separate proclamation in the Gazette (common for Acts of Parliament)
  - Some provisions commence at different dates (phased commencement)
- **How SA regulations can be invalidated or suspended:**
  - PAJA s6 judicial review — grounds:
    - s6(2)(a): administrator not authorised by empowering provision
    - s6(2)(b): material error of law
    - s6(2)(c): procedurally unfair
    - s6(2)(d): materially influenced by error of fact
    - s6(2)(e): not rationally connected to purpose
    - s6(2)(f): unconstitutional or unlawful
    - s6(2)(h): unreasonable
    - s6(2)(i): otherwise unconstitutional or unlawful
  - s7(1): 180-day time limit for judicial review from date of internal remedies or date person was informed
  - s7(2): must exhaust internal remedies before approaching court (unless court exempts)
  - Constitutional Court: can declare legislation/regulation constitutionally invalid (s172 Constitution)
  - Regulator withdrawal: regulator can withdraw/amend its own regulations via new Gazette notice
  - Interim interdicts: court can grant interim relief suspending a regulation pending review
- **Red flags that a regulation may not be in force (SA version):**
  - Commencement date not yet reached (check for proclamation)
  - Known PAJA s6 review proceedings
  - Constitutional Court challenge pending or decided
  - Regulator has published amendment/withdrawal notice
  - Regulation is >12 months old with no confirmation of current status
  - Regulation was gazetted but enabling Act not yet commenced
- **Verification steps (SA):**
  1. Check Laws.Africa or Sabinet for current consolidated text
  2. Search Open Gazettes for amendment/withdrawal notices
  3. Web search for PAJA review or Constitutional Court challenge
  4. Check regulator website for current status
  5. If cannot verify: emit `⚠️ RULE STATUS UNVERIFIED` banner with SA-specific framing

### 3.4 `regulators.md`

**Skills served:** reg-feed-watcher, comments, cold-start-interview, gap-surfacer

**Content — core 12 SA regulators:**

| # | Regulator | Enabling statute | Instruments | Comment period norm | Website |
|---|---|---|---|---|---|
| 1 | **SARS** (SA Revenue Service) | SA Revenue Service Act 34/1997 | Binding rulings, interpretation notes, practice notes, regulations | Via National Treasury draft tax bills (30-45 days) | sars.gov.za |
| 2 | **CIPC** (Companies & IP Commission) | Companies Act 71/2008 | Regulations, practice notes, compliance notices, beneficial ownership requirements | 30 days typical | cipc.co.za |
| 3 | **DEL** (Dept of Employment & Labour) | BCEA, LRA, EEA, OHSA | Regulations, sectoral determinations, codes of good practice, OHS standards | 30 days typical | labour.gov.za |
| 4 | **FSCA** (Financial Sector Conduct Authority) | FSR Act 9/2017 | Conduct standards, joint standards, board notices, directives, guidance notices | 30-60 business days | fsca.co.za |
| 5 | **PA/SARB** (Prudential Authority / Reserve Bank) | SARB Act 90/1989, FSR Act | Prudential standards, directives, guidance notes, exchange control circulars | 30-60 days | resbank.co.za |
| 6 | **National Treasury** | PFMA 1/1999 | Draft tax bills, policy papers, draft regulations, COFI Bill | 30-45 days | treasury.gov.za |
| 7 | **NCR** (National Credit Regulator) | NCA 34/2005 | Regulations, guidelines, compliance notices, registration conditions | 30 days | ncr.org.za |
| 8 | **B-BBEE Commission** | B-BBEE Act 53/2003 | Codes of good practice, sector codes, investigation reports, practice guides | Variable (major code revisions: 60+ days) | bbbeecommission.co.za |
| 9 | **SAHPRA** (Health Products Regulatory Authority) | Medicines Act 101/1965 | Regulations, schedules, guidelines, licensing conditions | 30-60 days | sahpra.org.za |
| 10 | **NCC** (National Consumer Commission) | CPA 68/2008 | Regulations, industry codes, compliance notices, recall notices | 30 days | thencc.gov.za |
| 11 | **Competition Commission** | Competition Act 89/1998 | Regulations, guidelines, exemption decisions, market inquiry terms of reference | 30 business days | compcom.co.za |
| 12 | **Information Regulator** | POPIA 4/2013, PAIA 2/2000 | Regulations, codes of conduct, guidance notes, enforcement notices | 30 days | inforegulator.org.za |

**Sector-specific regulators (add via practice profile):**

| Regulator | Sector | Enabling statute |
|---|---|---|
| NERSA | Energy (electricity, gas, pipelines) | National Energy Regulator Act 40/2004 |
| ICASA | Telecoms, broadcasting, postal | ICASA Act 13/2000 |
| CMS (Council for Medical Schemes) | Healthcare / medical schemes | Medical Schemes Act 131/1998 |
| DMRE (Dept of Mineral Resources & Energy) | Mining, petroleum | MPRDA 28/2002 |
| DFFE (Dept of Forestry, Fisheries & Environment) | Environmental | NEMA 107/1998 |
| FIC (Financial Intelligence Centre) | AML/CFT (cross-sector) | FICA 38/2001 |

**Industry bodies for joint regulatory comment submissions:**

| Scope | Body | Role |
|---|---|---|
| Cross-cutting | **BUSA** (Business Unity South Africa) | Apex body; coordinates economy-wide submissions; represents business at NEDLAC |
| Financial services | **BASA** (Banking Association SA), **ASISA**, **SAIA**, **FIA** | Consolidated submissions on FSCA/PA/NCR standards |
| Mining/resources | **Minerals Council SA** | Mining Charter, MPRDA, environmental/safety regulation |
| Manufacturing | **SACCI**, sector-specific (NAAMSA, SAISI, etc.) | Technical standards, trade policy, industrial regulation |
| Retail/consumer | **CGCSA** (Consumer Goods Council) | Consumer protection, product safety, labelling |
| Telecoms/ICT | **ISPA** | ICASA regulations, spectrum, data protection |
| Professional | **SAICA**, **SAIPA** | Tax, company law, financial reporting |
| SMEs | **NSBC**, **NAFCOC**, **FABCOS** | SME-specific regulation, chambers of commerce |

---

## 4. Practice Profile Template Design

### Section replacement table

| US template section | Status | ZA replacement |
|---|---|---|
| Config location comment | REPLACE | Add `JURISDICTION OVERLAY` instruction pointing to `jurisdictions/za/regulatory-legal/router.md` |
| `# Regulatory Practice Profile` | REPLACE | `# Regulatory Practice Profile — South Africa` |
| `## Regulators we watch` | REPLACE | SA regulator table from core 12, categorized as "leading" vs "monitor" |
| `## Who's using this` | REPLACE | Role: `Admitted attorney or advocate under Legal Practice Act 28 of 2014 \| Non-lawyer with attorney access \| Non-lawyer without attorney access` |
| `## Available integrations` | REPLACE | Tier 1: Open Gazettes, SA regulator RSS/email. Tier 2: Laws.Africa API. Document storage + Slack unchanged. Drop Thomson Reuters. |
| `## Policy library` | KEEP | SA-specific example policies in placeholders |
| `## Materiality threshold` | REPLACE | SA examples (see below) |
| `## Gap response process` | KEEP | Jurisdiction-neutral |
| `## Feed configuration` | REPLACE | Open Gazettes Atom/JSON, Laws.Africa API, per-regulator RSS |
| `## Outputs` | REPLACE | SA legal professional privilege framework |
| `## Matter workspaces` | KEEP | Jurisdiction-neutral |
| All shared guardrails | KEEP | SA-specific examples where relevant |

### New SA-specific sections

**`## Regulatory landscape`**
- Which SA regulatory domains the user operates in
- Drives which statute files and regulators are active
- Selected during cold-start Q1

**`## Consultation engagement posture`**
- Whether org engages in regulatory consultations
- Through industry bodies, directly, or both
- Default stance on comment periods
- Industry body memberships
- Configured during cold-start Q4, Q5

**`## Government Gazette monitoring`**
- Check cadence (daily/weekly)
- Filter approach (by regulator, keyword, broad)
- Gazette types (national, provincial, extraordinary)
- Configured during cold-start Q3

### SA materiality threshold examples

**Always material (act immediately):**
- New regulation in Government Gazette with compliance deadline affecting your sector
- Regulator enforcement action against a company in your sector
- Draft regulation published for comment that directly affects your business model

**Review-worthy (assess and decide):**
- Draft regulation in a related sector
- Regulator guidance note or interpretation notice
- B-BBEE code amendment or sector code revision
- FICA/AML guideline update

**FYI (note, no action):**
- Regulator media statement or speech
- Industry body commentary on a regulatory trend
- Academic or legal commentary on regulatory developments

### Work-product header

- **Admitted attorney/advocate:** `PRIVILEGED & CONFIDENTIAL — PREPARED BY/AT THE DIRECTION OF LEGAL COUNSEL FOR THE PURPOSE OF PROVIDING LEGAL ADVICE`
- **Non-lawyer:** `CONFIDENTIAL — NOT LEGAL ADVICE — CONSULT AN ADMITTED ATTORNEY OR ADVOCATE BEFORE ACTING`

### Practice-specific privilege caveat

Regulatory compliance assessments and gap analyses are generally NOT privileged under SA law unless prepared at the specific direction of a legal practitioner for the dominant purpose of providing legal advice. Key principles [Perplexity — verify, citing *Mohamed v President of SA* 2001 (3) SA 893 (CC), *Ibex RSA Holdco v Tiso Blackstar*, *Trust Sentrum v Zevenburg*]:

- A compliance gap report prepared by a non-lawyer compliance officer for operational purposes is NOT privileged merely because a lawyer reviewed it or the document carries a "privileged" header.
- Privilege can attach where the report is created at the request of a legal practitioner for the dominant purpose of enabling legal advice (or for contemplated litigation).
- In-house counsel: privilege depends on whether they are acting in a legal capacity (providing legal advice) or a commercial/managerial capacity. Function, not job title, determines privilege. Courts scrutinize in-house claims more closely than external counsel.
- Litigation privilege: available for documents prepared for the dominant purpose of pending or reasonably contemplated regulatory enforcement defence (*Ibex RSA Holdco* — SCA adopted dominant purpose test).
- PAIA s46 public interest override: privilege can be overridden where evidence of substantial contravention of law or imminent serious threat to safety/environment.
- The `gap-surfacer` and `policy-diff` outputs should be treated as operational documents unless specifically commissioned as privileged legal work.

### Seed documents for cold-start

| Document | Priority | Why |
|---|---|---|
| Policy library (internal compliance policies) | Must-have | Core input for policy-diff and gap-surfacer |
| Existing regulatory register (if any) | Nice-to-have | Bootstraps watchlist and gap tracker |
| B-BBEE certificate/scorecard | Nice-to-have | Determines B-BBEE compliance obligations |
| POPIA compliance framework / privacy policy | Nice-to-have | Anchors data protection monitoring |
| Industry body membership details | Nice-to-have | Joint submission opportunity flagging |
| Recent regulatory correspondence / enforcement notices | Nice-to-have | Seeds gap tracker with known issues |

---

## 5. Cold-Start Interview Questions

The ZA fork inserts after Part 0 (role, practice setting, integrations already captured).

### Must-have (quick + full setup)

| # | Question | What it configures |
|---|---|---|
| Q1 | **Regulatory domains** — which SA regulatory areas to monitor? Multi-select from: financial services, consumer protection, data protection/POPIA, competition, environmental, H&S, tax & revenue, employment & labour, B-BBEE/transformation, telecoms/ICT, mining & resources, energy & electricity, healthcare/pharma | Statute files, regulator watchlist scope |
| Q2 | **Regulator watchlist confirmation** — auto-populated from Q1 domain mapping. Confirm each as "leading" or "monitor." Add/remove. | Regulators we watch table |
| Q3 | **Government Gazette monitoring** — check cadence (daily/weekly/both), filter approach (by regulator/keyword/broad) | Feed configuration |
| Q4 | **Consultation engagement posture** — actively file comments / through industry bodies / both / rarely / never. Default stance on comment periods. | Comments skill behaviour, comment-decision gap type |
| Q5 | **Industry body memberships** — which bodies coordinate regulatory submissions? (BUSA, sector-specific) | Joint submission flagging |
| Q6 | **SA materiality calibration** — confirm or adjust the 3-tier materiality threshold with SA examples | Materiality threshold |

### Nice-to-have (full setup only)

| # | Question | What it configures |
|---|---|---|
| Q7 | **Regulatory correspondence history** — current/recent inquiries, enforcement actions, inspections? | Seeds gap tracker |
| Q8 | **B-BBEE compliance posture** — level, sector code, verification agency, next verification date (only if B-BBEE selected in Q1) | B-BBEE monitoring |
| Q9 | **Feed source configuration** — Laws.Africa API access? Existing regulator email subscriptions? | Tier 1/2 feed setup |
| Q10 | **Provincial regulatory exposure** — operations in multiple provinces? (only if Environmental selected in Q1) | Provincial Gazette monitoring |

Quick setup (2 min): Q1, Q2, Q4 + defaults for rest.
Full setup (15 min): all 10 questions.

---

## 6. High-Risk Flag Table

12 flags for the SA regulatory compliance domain.

| # | Flag | Severity | Why high-risk | What to check | Key statutes |
|---|---|---|---|---|---|
| 1 | **Gazette commencement trap** | 🔴 Blocking | Regulation in force on publication date — obligations enforceable before internal adjustment. No US equivalent. | Check effective date in Gazette notice. If commencement = publication and no transition period, flag immediately. | PAJA s4, enabling statute |
| 2 | **Licence/registration gap** | 🔴 Blocking | #1 enforcement trigger across FSCA, ICASA, NERSA, DEL. FSCA: >70% of investigations = unlicensed operations. | When new reg creates/changes licensing requirements, check current operations scope. Flag new business lines. | FSR Act, FAIS, ERA, ECTA |
| 3 | **Mandatory return/report deadline** | 🔴 Blocking | Most common, most avoidable trigger. SARS recurring monthly penalties. CIPC deregistration. FSCA licence withdrawal. | Central deadline calendar. Flag returns due within 30 days without confirmed submission. | Tax Administration Act, Companies Act, FSR Act |
| 4 | **B-BBEE fronting risk** | 🔴 Blocking | Criminal offence. Procurement blacklisting. NPA referral. SARS/CIPC collateral consequences. SA-specific, no US equivalent. | When B-BBEE codes change, check ownership/management structures. Flag scorecard-vs-reality misalignment. | B-BBEE Act s13F-13J |
| 5 | **POPIA breach notification failure** | 🟠 High | Information Regulator ramp-up: R10m per contravention. Notification "as soon as reasonably possible." Late notification is itself an offence. | When POPIA regs change breach notification requirements, flag against incident response procedures. | POPIA s22, 2025 regs |
| 6 | **Comment period closing without decision** | 🟠 High | Strategic risk: loss of influence, reduced PAJA challenge ability, implementation shocks. Courts may note absence of engagement. | Flag open comment periods on material drafts. Escalate undecided at 14 days and 3 days before deadline. | PAJA s4 |
| 7 | **AML/CFT compliance gap** | 🟠 High | FATF grey-listing drove continuous FICA reform. Schedule expansion bringing new entities into scope. Inadequate RMCP is primary trigger. | When FICA amendments change, check if entity newly in scope. Check RMCP currency. Flag new BO obligations. | FICA s21, s28A, s29, Schedule 1 |
| 8 | **Competition law threshold breach** | 🟠 High | Non-notification of notifiable mergers: penalties up to 10% annual turnover. "Creeping acquisitions" commonly missed. | When Competition Act thresholds change, flag against M&A pipeline and JV/partnership structures. | Competition Act s11-13 |
| 9 | **Regulation status unverified** | 🟡 Medium | Acting on lapsed rule wastes resources. Non-compliance against active rule creates exposure. | When gap >12 months old or rule under known challenge, verify before escalating. Check Gazette for withdrawal/court orders. | PAJA s6, s7 |
| 10 | **PAJA procedural fairness in own decisions** | 🟡 Medium | When business exercises public-law-like powers, PAJA may apply. Failure = decision set aside on review. | When reg changes affect company's own decision-making, check internal procedures comply with PAJA s3. | PAJA s3, s5 |
| 11 | **Provincial/sectoral regulatory divergence** | 🟡 Medium | Some regs are provincial or sectoral. National-only monitoring misses provincial Gazette publications. | If operations span provinces or fall under sectoral regimes, flag when monitoring covers only national Gazette. | NEMA, BCEA, MPRDA |
| 12 | **Industry body submission divergence** | 🟡 Medium | Industry body may concede points the user would not. Joint submission may conflict with firm interests. | When material draft detected AND industry body known to be filing, flag for user to review draft position. | — |

### Flag-to-statute cross-reference

| Flag | Primary statute sections |
|---|---|
| Gazette commencement trap | PAJA s4, Interpretation Act s13, enabling statute commencement provisions |
| Licence/registration gap | FSR Act s108-115 (FSCA), FAIS s7 (FSP), ERA s7 (generation), ECTA s29-30 (crypto) |
| Mandatory return deadline | Tax Administration Act s210-215, Companies Act s33, FSR Act s133 |
| B-BBEE fronting | B-BBEE Act s13F (fronting), s13G-13J (investigation/enforcement) |
| POPIA breach notification | POPIA s22 (notification), s107 (penalties), 2025 regs (eServices portal) |
| Comment period closing | PAJA s4(1)(a) (notice-and-comment), s4(1)(b) (public inquiry) |
| AML/CFT compliance gap | FICA s21 (RMCP), s21A-21H (BO), s28A (STRs), s64 (admin sanctions) |
| Competition threshold breach | Competition Act s11 (intermediate), s13 (large), s13A (small), s59 (penalties) |
| Regulation status unverified | PAJA s6 (judicial review grounds), s7 (180-day limit, internal remedies) |
| PAJA fairness in own decisions | PAJA s3 (individual fairness), s5 (written reasons) |
| Provincial/sectoral divergence | NEMA (provincial environmental), BCEA (sectoral determinations), MPRDA (mining charter) |
| Industry body divergence | No statutory basis — strategic/operational flag |

---

## 7. Eval Case Outlines

### 7.1 `reg-feed-watcher` — 4 cases

**Case 1: Straightforward Gazette catch — new FSCA conduct standard**
- Input: Gazette notice publishing final FSCA conduct standard on retirement fund governance, effective 90 days from publication. User watchlist includes FSCA as "leading."
- Expected flags: Gazette commencement trap (flag #1). Materiality: "Always material."
- Expected statutes: FSR Act s107-115
- Must NOT contain: Federal Register, NPRM, CFR, SEC, FTC, any US agency

**Case 2: Comment period detection — draft POPIA code of conduct**
- Input: Gazette notice inviting 30-day comment on draft Information Regulator code of conduct for direct marketing.
- Expected flags: Comment period closing (flag #6). Create CMT entry in comment-tracker.
- Expected statutes: POPIA s60-65
- Must NOT contain: FTC, CAN-SPAM, CCPA, Regulations.gov

**Case 3: Below-threshold filter — regulator speech**
- Input: SARB Governor speech on monetary policy outlook. Materiality: "FYI."
- Expected flags: None escalated. Classified as FYI in digest.
- Must NOT contain: Material escalation, gap creation, any US reference

**Case 4: Multi-regulator — FICA amendment expanding scope**
- Input: Gazette publishing FICA Schedule 1 amendment adding crypto-asset service providers as accountable institutions. User is a fintech.
- Expected flags: AML/CFT compliance gap (flag #7), Licence/registration gap (flag #2). Materiality: "Always material."
- Expected statutes: FICA s21, Schedule 1, FSR Act
- Must NOT contain: BSA, FinCEN, SEC crypto guidance

### 7.2 `policy-diff` — 4 cases

**Case 1: Straightforward — POPIA regulation amendment**
- Input: New POPIA regulation strengthening breach notification (72-hour hard deadline via eServices portal). Existing policy says "as soon as reasonably possible."
- Expected flags: POPIA breach notification (flag #5). Gap type: "partial."
- Expected statutes: POPIA s22, 2025 regs
- Must NOT contain: GDPR 72-hour (POPIA requirement, not GDPR), HHS, HIPAA

**Case 2: Edge case — regulation with unverified status**
- Input: Regulation published 14 months ago with known PAJA s6 challenge.
- Expected flags: Regulation status unverified (flag #9). `⚠️ RULE STATUS UNVERIFIED` banner. `status_verified: false`.
- Expected statutes: PAJA s6, s7
- Must NOT contain: "Federal Register docket," "stays," "injunctions," "vacatur"

**Case 3: New policy needed — Competition Act threshold change**
- Input: Competition Commission publishes new merger notification thresholds. No competition compliance policy exists.
- Expected flags: Competition threshold breach (flag #8). Gap type: "new-policy."
- Expected statutes: Competition Act s11-13
- Must NOT contain: Hart-Scott-Rodino, FTC merger guidelines, DOJ

**Case 4: Below-threshold — B-BBEE code revision for EME**
- Input: Revised B-BBEE Codes changing skills development scoring. User is EME (turnover <R10m).
- Expected flags: None escalated. EME exempt from most requirements. Gap type: "none" or "watch."
- Expected statutes: B-BBEE Act, Codes of Good Practice
- Must NOT contain: Affirmative action (US), EEOC, Title VII

### 7.3 `comments` — 3 cases

**Case 1: Material comment period — FSCA draft conduct standard**
- Input: FSCA draft conduct standard on insurance product governance. 45-business-day comment period. User is insurer with FSCA "leading."
- Expected flags: Comment period closing (flag #6). Auto-create CMT entry. Notify decision owner.
- Expected statutes: FSR Act s107-115, s133
- Must NOT contain: NPRM, Regulations.gov, Federal Register docket

**Case 2: Industry body coordination — BUSA filing on Companies Act regs**
- Input: Draft Companies Act beneficial ownership regulations, 30-day comment. BUSA coordinating joint submission.
- Expected flags: Industry body divergence (flag #12). Surface dual-approach question.
- Expected statutes: Companies Act s56
- Must NOT contain: SEC disclosure, Dodd-Frank, US corporate governance

**Case 3: Non-lawyer consequential action gate**
- Input: Non-lawyer compliance officer wants to log "filing" decision and produce comment letter to NERSA.
- Expected flags: Consequential action gate fires. "Have you reviewed this with an attorney?"
- Must NOT contain: "State bar" (should reference "Legal Practice Council" or "Law Society of South Africa")

### 7.4 `gap-surfacer` — 3 cases

**Case 1: Overdue POPIA compliance gap**
- Input: GAP-005 for POPIA information officer registration, due 60 days ago, status_verified: true, open.
- Expected flags: 🔴 Overdue. Route to owner.
- Expected statutes: POPIA s55-56
- Must NOT contain: GDPR DPO, any EU reference

**Case 2: Unverified rule — no overdue classification**
- Input: GAP-008 with status_verified: false, due 30 days ago.
- Expected flags: 🟡 "Review needed" NOT 🔴 Overdue. Route to watch bucket.
- Expected statutes: PAJA s6
- Must NOT contain: "Federal Register docket," overdue escalation without verification caveat

**Case 3: Watch-to-active promotion**
- Input: Watch item for draft FICA amendment. Final regulation published in Gazette with 6-month deadline.
- Expected flags: Promote watch → full gap. New due date. status_verified: true. Trigger policy-diff.
- Expected statutes: FICA relevant sections
- Must NOT contain: Any US reference

### 7.5 `policy-redraft` — 3 cases

**Case 1: Straightforward — POPIA breach notification update**
- Input: GAP from policy-diff case 1. Existing policy: "as soon as reasonably possible." New: 72-hour via eServices.
- Expected output: Smallest edit. Add 72-hour timeline, eServices portal. Carry `[verify]` tags. Write to new file.
- Expected statutes: POPIA s22, 2025 regs
- Must NOT contain: GDPR, "data controller" (SA = "responsible party"), HHS

**Case 2: New competition compliance policy**
- Input: GAP from policy-diff case 3. No existing policy.
- Expected output: New competition compliance section. Merger thresholds, prohibited practices, leniency. Flag `[review]`.
- Expected statutes: Competition Act s4-5, s8-9, s11-13
- Must NOT contain: Sherman Act, Clayton Act, FTC Act, Hart-Scott-Rodino

**Case 3: Rule status unverified redraft**
- Input: GAP from policy-diff case 2. Regulation under PAJA s6 challenge.
- Expected output: `⚠️ RULE STATUS UNVERIFIED` banner. Redraft with caveat. Dates tagged `[due date per published rule — status unverified]`.
- Expected statutes: PAJA s6
- Must NOT contain: "Federal Register docket," US judicial review references

### 7.6 `cold-start-interview` (ZA fork) — 3 cases

**Case 1: In-house regulatory counsel, financial services**
- Input: Full setup. Admitted attorney. In-house. Insurance. ZA.
- Expected: ZA fork activates. SA regulators (FSCA, PA/SARB). Open Gazettes + Laws.Africa. SA materiality. SA privilege header. Industry body: ASISA/SAIA.
- Must NOT contain: Federal Register API, CourtListener, US agency slugs, Thomson Reuters, "state bar"

**Case 2: Non-lawyer compliance officer, manufacturing**
- Input: Quick setup. Non-lawyer with attorney access. Manufacturing. ZA.
- Expected: ZA fork. Quick runs Q1, Q2, Q4 with SA defaults. Non-lawyer output mode. SA header. Industry body: SACCI.
- Must NOT contain: Any US reference, "licensed attorney" (= "admitted attorney or advocate")

**Case 3: Multi-sector conglomerate**
- Input: Full setup. Multiple domains (financial services, mining, consumer, environmental). ZA.
- Expected: 8+ regulators. Provincial exposure question triggered. Multiple regulator RSS feeds. Cross-domain materiality. Multiple industry bodies.
- Must NOT contain: Any US reference

---

## 8. Domain-Specific Validation Rules

These apply across all eval cases and production outputs when jurisdiction = ZA:

1. **No US regulatory process concepts:** NPRM, Federal Register, CFR, APA (US), Regulations.gov, CourtListener, "notice-and-comment" (when referring to US APA-specific process)
2. **No US regulator references:** FTC, SEC, CFPB, DOL, HHS, FCC, EEOC, NLRB, EPA (US), OSHA (US — SA uses "OHSA")
3. **No US judicial concepts in rule-status verification:** "stays," "injunctions," "vacatur" — SA uses PAJA s6 judicial review, Constitutional Court invalidity
4. **No US privilege doctrine:** "attorney work product" (FRCP 26(b)(3)), "attorney-client privilege" — SA uses "legal professional privilege"
5. **Correct SA legal terminology:**
   - "responsible party" not "data controller" (POPIA vs GDPR)
   - "admitted attorney or advocate" not "licensed attorney"
   - "Legal Practice Council" not "state bar"
   - "Government Gazette" not "Federal Register"
   - "OHSA" not "OSHA"
   - "CCMA" not "NLRB"
   - "bargaining council" not "labor board"

---

## 9. Expert Review Gate

Before release, an SA regulatory compliance practitioner should review:

- [ ] Topic overlay content (regulatory-process.md, feed-sources.md, rule-status-verification.md, regulators.md) against current SA regulatory practice
- [ ] Statute YAML values against current Government Gazette publications
- [ ] High-risk flag table (12 flags) against current enforcement patterns
- [ ] Practice profile template for completeness and correctness
- [ ] Cold-start interview ZA fork for question accuracy and coverage
- [ ] Privilege framework against current SA case law position

This is a process gate, not an automated test.

---

## 10. Source Provenance Log

| Item | Source | Tag |
|---|---|---|
| SA regulatory landscape (statutes, regulators) | Perplexity search, 2026-05-20 | [Perplexity — verify] |
| Core 12 SA regulators ranking | Perplexity search, 2026-05-20 | [Perplexity — verify] |
| SA rulemaking process (Gazette, PAJA, comment periods) | Perplexity search, 2026-05-20 | [Perplexity — verify] |
| SA feed sources (Open Gazettes, Laws.Africa) | Perplexity search, 2026-05-20 | [Perplexity — verify] |
| SA privilege framework for compliance documents | Perplexity search, 2026-05-20 | [Perplexity — verify] |
| SA industry bodies for regulatory submissions | Perplexity search, 2026-05-20 | [Perplexity — verify] |
| SA regulatory enforcement patterns and penalties | Perplexity search, 2026-05-20 | [Perplexity — verify] |
| Existing statute YAML file coverage | Direct read of `jurisdictions/za/statutes/` files | [confirmed] |
| Plugin skills and SKILL.md content | Direct read of `regulatory-legal/skills/` | [confirmed] |
| Architecture decisions | Direct read of ADR-001 and ARCHITECTURE.md | [confirmed] |
| All design decisions (Steps 1-8) | User confirmed during interview | [user confirmed] |
