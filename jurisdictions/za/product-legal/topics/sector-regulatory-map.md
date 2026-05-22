# Sector Regulatory Map — South African Framework

This overlay maps product verticals to South African regulatory regimes, replacing the US-centric sector overlay hints table. It is loaded by launch-review (sector hints), feature-risk-assessment (regulatory landscape), and is-this-a-problem skills when jurisdiction = ZA.

---

## Sector overlay table

| Sector | SA regulatory regimes | Key statutes | Regulator(s) |
|---|---|---|---|
| **Children / minors** | Child protection, content classification, data protection | Children's Act 38/2005, POPIA s34-35, Films & Publications Act 65/1996, Protection from Harassment Act 17/2011 | FPB, Information Regulator |
| **Gaming / gamification** | Gambling regulation, lottery prohibition, consumer protection | National Gambling Act 7/2004, Lotteries Act 57/1997, CPA s36 | NGB, provincial gambling boards |
| **Financial / fintech** | Credit regulation, anti-money laundering, financial advice, banking, payments | NCA 34/2005, FICA 38/2001, FAIS 37/2002, Banks Act 94/1990, NPS Act 78/1998 | FSCA, SARB, NCR |
| **Health / health-tech** | Medicines regulation, health professions, data protection | Medicines and Related Substances Act 101/1965, NHA 61/2003, Health Professions Act 56/1974 | SAHPRA, HPCSA |
| **Consumer / retail / marketing** | Consumer protection, advertising, e-commerce, trade marks | CPA s29-41, ARB Code of Advertising Practice, ECTA 25/2002, Merchandise Marks Act 17/1941, Lotteries Act 57/1997 | NCC, ARB, Consumer Tribunal |
| **Content / UGC** | Content classification, cybercrime, electronic takedown | Films & Publications Act 65/1996, Cybercrimes Act 19/2020, ECTA s77 (takedown) | FPB, ICASA |
| **Telecom / OTT** | Electronic communications licensing, spectrum, content | Electronic Communications Act 36/2005, ICASA regulations | ICASA |
| **Insurance / insurtech** | Insurance regulation, financial advice, data protection | Insurance Act 18/2017, FAIS 37/2002, POPIA | FSCA (Prudential Authority) |
| **Education / ed-tech** | Higher education regulation, children's data, qualifications | Higher Education Act 101/1997, NQF Act 67/2008, Children's Act 38/2005, POPIA s34-35 | DHET, CHE, SAQA, Information Regulator |
| **Property / proptech** | Estate agency regulation, consumer protection | Estate Agency Affairs Act 112/1976, CPA, FICA | EAAB, NCC |

### How to use this table

1. During launch review, identify the product's sector(s) from the left column.
2. Each sector maps to specific statutes and regulators that must be assessed.
3. Products spanning multiple sectors (e.g., a fintech product targeting children) require assessment against all applicable rows.
4. If no sector match, the Consumer / retail / marketing row applies as the baseline for any product sold to SA consumers.

### Cross-cutting statutes

Regardless of sector, the following statutes apply to virtually all products sold to SA consumers:

| Statute | Applicability | Regulator |
|---|---|---|
| **CPA** | All consumer-facing products (natural persons + juristic persons below R2m) | NCC, Consumer Tribunal |
| **POPIA** | Any product collecting or processing personal information | Information Regulator |
| **ECTA** | Any product sold via electronic transaction (website, app, online signup) | — (enforced via criminal law + CPA overlap) |
| **Competition Act** | Any product in a market — relevant when market power, mergers, or exclusionary conduct arise | Competition Commission |

These cross-cutting statutes are assessed in every launch review. The sector overlay table adds sector-specific requirements on top of this baseline.

---

## SA regulator reference

### National Consumer Commission (NCC)

Enforces the Consumer Protection Act. Receives consumer complaints, investigates non-compliance, and issues compliance notices. Refers matters to the Consumer Tribunal for adjudication and fines. Active enforcement posture since 2024 — 62+ compliance notices issued in 2025-26. Product counsel typically engages the NCC through formal written representations in response to complaints or compliance notices.

### Information Regulator (IR)

Enforces POPIA and PAIA. Issues enforcement notices, conducts investigations, and imposes administrative fines up to R10 million. Increasingly active since POPIA enforcement began in July 2021. High-profile actions against Blouberg Municipality (R500k), Lancet Laboratories (R100k), and investigations into WhatsApp/Meta data transfers. Product counsel engages through breach notification (POPIA s22), prior authorisation applications (s57), and formal responses to assessment notices.

### Competition Commission (CC)

Enforces the Competition Act. Investigates anti-competitive conduct, mergers, and abuse of dominance. Relevant to product counsel for: comparative advertising by dominant firms (s8(1)(d)), exclusive dealing arrangements, bundling practices, and digital platform market inquiries. The Commission has conducted digital platform market inquiries and may impose remedial action. Engagement is typically through merger notification or response to complaint referrals.

### Advertising Regulatory Board (ARB)

Self-regulatory body administering the Code of Advertising Practice. Not a statutory regulator — membership is voluntary but industry-wide adherence is the norm. Handles complaints about advertising content, substantiation, comparative claims, and decency. Rulings require ad withdrawal and non-publication. Media owners generally enforce ARB rulings by refusing to carry non-compliant advertisements. Product counsel engages by filing responses to complaints or seeking pre-clearance on sensitive claims.

### Independent Communications Authority of SA (ICASA)

Regulates electronic communications, broadcasting, and postal services. Relevant for telecom/OTT products, broadcasting licences, spectrum allocation, and electronic communications service licensing. Enforcement through licence conditions and regulations. Product counsel engages through licence applications and compliance with regulations.

### South African Health Products Regulatory Authority (SAHPRA)

Regulates medicines, medical devices, and health products. Relevant for health-tech products that may constitute medical devices or make health claims. SAHPRA registration is mandatory before marketing a medicine or medical device. Health claims on non-medical products may trigger Medicines Act obligations. Product counsel engages through registration applications and regulatory classification assessments.

### Financial Sector Conduct Authority (FSCA) and South African Reserve Bank (SARB)

FSCA regulates market conduct of financial institutions, financial advice (FAIS), and insurance. SARB regulates banking, payment systems (NPS Act), and prudential oversight. Relevant for fintech products: payment processing, stored-value products, credit, insurance, and financial advice. Product counsel engages through licence applications, exemption requests, and compliance with conduct standards.

### National Gambling Board (NGB) and Provincial Gambling Boards

NGB oversees national gambling policy; provincial boards issue licences and regulate gambling within each province. Online gambling remains prohibited in South Africa (National Gambling Act). Relevant for gamification features, loot boxes, and prize mechanics that may constitute gambling. Product counsel engages through regulatory classification assessments and, if applicable, provincial licence applications.

### Film and Publication Board (FPB)

Classifies content (films, games, publications) and regulates online content distribution under the Films & Publications Act, including the 2019 online content amendments. Relevant for platforms hosting user-generated content, content distribution services, and any product directed at children. Registration requirements for online content distributors. Product counsel engages through content classification applications and platform registration.

### National Credit Regulator (NCR)

Regulates credit providers, credit bureaus, and debt counsellors under the NCA. Relevant for any fintech product that extends credit (including BNPL, salary advances, revolving credit). Registration as a credit provider is mandatory before offering credit. NCR conducts compliance inspections and investigates consumer complaints about credit marketing and reckless lending. Product counsel engages through registration applications, compliance reports, and responses to NCR investigations.

---

## Enforcement posture summary

Current regulatory enforcement intensity varies by regulator. This table helps prioritise compliance effort:

| Regulator | Current enforcement posture | Trend | Priority actions |
|---|---|---|---|
| **NCC** | Active — 62+ compliance notices 2025-26 | Increasing | T&C review against CPA s48-52; marketing claims audit |
| **Information Regulator** | Active — high-profile fines, investigations | Increasing | POPIA compliance programme; breach notification procedure |
| **Competition Commission** | Selective — focused on digital platform inquiries | Stable | Monitor market inquiry outcomes; merger notification |
| **ARB** | Responsive — complaint-driven | Stable | Pre-publication substantiation file; comparative claims review |
| **FSCA** | Active — fintech licensing focus | Increasing | Licensing assessment for financial product features |
| **SAHPRA** | Selective — registration-driven | Stable | Health claims review; medical device classification |
| **NGB / provincial boards** | Low for digital — but online gambling prohibition strict | Stable | Gamification feature classification |
| **FPB** | Increasing — online content amendments taking effect | Increasing | Content classification; platform registration assessment |
| **ICASA** | Selective — licence-driven | Stable | OTT/telecom licence assessment |
| **NCR** | Active — micro-lender and BNPL focus | Increasing | Credit product classification; registration |

---

## Multi-regulator escalation

A single product feature or marketing campaign may trigger oversight from multiple regulators simultaneously. This is not theoretical — it is the norm for digital products in South Africa.

### Why this is high-risk

- **Multiplicative exposure** — fines and remedial orders from each regulator stack independently. A misleading marketing campaign for a fintech product could face NCC action (CPA s29), IR investigation (POPIA breach), FSCA inquiry (FAIS compliance), and ARB complaint (advertising code).
- **Inconsistent timelines** — each regulator has its own investigation timeline and procedural requirements. Coordinating responses across multiple regulators requires a single internal coordination point.
- **No single-window mechanism** — SA does not have a unified regulator for digital products. Product counsel must independently assess applicability of each regulatory regime.

### Practical checklist

| Step | Action |
|---|---|
| 1 | Map the product against the sector overlay table — identify all applicable rows |
| 2 | For each applicable regulator, confirm: registration/licence status, current compliance, nominated contact person |
| 3 | Populate the escalation matrix in the practice profile with regulator-specific contacts and response protocols |
| 4 | Ensure a single internal coordination point for multi-regulator matters |
| 5 | When a complaint or investigation is received from one regulator, assess whether the same conduct triggers obligations to others |

### Common multi-regulator scenarios

| Scenario | Regulators triggered | Example |
|---|---|---|
| Fintech product with misleading marketing | NCC (CPA s29), FSCA (FAIS), NCR (NCA s76), ARB (advertising code) | BNPL product advertising "0% interest" without disclosing fees |
| Health-tech app collecting children's data | SAHPRA (health claims), IR (POPIA s34-35), FPB (children's content), NCC (CPA) | Wellness app for teens making health benefit claims |
| UGC platform with content monetisation | FPB (content classification), IR (POPIA), NCC (CPA unfair terms), Competition Commission (platform market power) | Video-sharing platform with in-app purchases and advertising revenue |
| E-commerce with promotional competition | NCC (CPA s36), NGB (gambling classification), IR (POPIA for entrant data), ARB (competition advertising) | "Spin-the-wheel" website promotion with prize draws |
| Insurance product sold online | FSCA (Insurance Act, FAIS), NCC (CPA unfair terms), IR (POPIA for policyholder data) | Online short-term insurance platform with automated underwriting |

### Response coordination protocol

When a complaint or investigation is received from one regulator:

1. **Identify the conduct** — what specific act, omission, or product feature is at issue?
2. **Map to all applicable regimes** — consult the sector overlay table above and the cross-cutting statutes table.
3. **Assess self-reporting obligations** — some regulators require proactive notification. For example, POPIA s22 requires breach notification to the Information Regulator regardless of whether the IR initiated the inquiry. FICA s29 requires suspicious transaction reporting regardless of NCC or FSCA involvement.
4. **Coordinate response timelines** — each regulator imposes different response deadlines. The NCC typically allows 20 business days for written representations. The IR may set shorter deadlines for breach notification. Map all deadlines and create a unified response calendar.
5. **Appoint a single coordination point** — one person (or team) must track all parallel regulatory processes and ensure consistency across responses. Contradictory representations to different regulators create severe credibility risk.
6. **Assess privilege implications** — legal advice prepared for one regulator response may not be privileged in proceedings before another regulator. Separate privileged legal analysis from factual submissions where possible.

### Penalty stacking

Penalties from different regulators are independent and cumulative:

| Regulator | Maximum penalty | Basis |
|---|---|---|
| NCC / Consumer Tribunal | R1m or 10% annual turnover | CPA s112 |
| Information Regulator | R10m or imprisonment up to 10 years | POPIA s107, s109 |
| Competition Commission / Tribunal | Up to 10% of annual turnover | Competition Act s59 |
| NCR | De-registration + agreement void | NCA s57, s89 |
| FSCA | Unlimited administrative penalties | Financial Sector Regulation Act s167 |
| Criminal prosecution | Fines + imprisonment | ECTA s43(5), Lotteries Act, Cybercrimes Act |

A single product launch that violates multiple regulatory frameworks can face cumulative penalties from each applicable regulator.

| Flag | Why high-risk | What to check |
|---|---|---|
| **Multi-regulator escalation** | Same conduct triggers multiple regulators simultaneously. Multiplicative exposure. | Assessed against all applicable regulators? Escalation matrix populated per regulator? Single coordination point? |
