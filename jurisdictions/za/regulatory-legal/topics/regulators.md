# Regulators — South African Framework

This overlay provides a comprehensive reference for South African regulatory bodies, their enabling statutes, the instruments they issue, and their consultation practices. It is loaded by reg-feed-watcher, comments, cold-start-interview, and gap-surfacer skills when jurisdiction = ZA.

---

## 1. Core 12 SA regulators

These regulators are active by default in the regulatory-legal plugin when jurisdiction = ZA. Every practice profile should specify which of these are relevant.

| # | Regulator | Abbreviation | Enabling statute | Instruments issued | Consultation process | Comment period norm | Website |
|---|---|---|---|---|---|---|---|
| 1 | SA Revenue Service | SARS | SA Revenue Service Act 34/1997 | Binding rulings (general, class, private), interpretation notes, practice notes, external guides | Draft tax legislation via National Treasury; SARS issues binding rulings without Gazette comment but publishes drafts on its website | 30–45 days (tax bills via Treasury) | sars.gov.za |
| 2 | Companies and Intellectual Property Commission | CIPC | Companies Act 71/2008 | Regulations, practice notes, compliance notices, beneficial ownership requirements | Gazette notice-and-comment for regulations; practice notes published on website | 30 days | cipc.co.za |
| 3 | Department of Employment and Labour | DEL | BCEA 75/1997, LRA 66/1995, EEA 55/1998, OHSA 85/1993 | Regulations, sectoral determinations, codes of good practice, ministerial determinations | Gazette notice-and-comment; NEDLAC engagement for major amendments | 30 days | labour.gov.za |
| 4 | Financial Sector Conduct Authority | FSCA | FSR Act 9/2017 | Conduct standards, joint standards (with PA), board notices, directives, exemptions | Multi-step: discussion paper → draft standard → final standard; Gazette notice-and-comment | 30–60 business days | fsca.co.za |
| 5 | Prudential Authority (SARB) | PA/SARB | SARB Act 90/1989, FSR Act 9/2017 | Prudential standards, directives, guidance notes, exchange control circulars | Multi-step for prudential standards; circulars published directly; joint standards with FSCA | 30–60 days | resbank.co.za |
| 6 | National Treasury | NT | PFMA 1/1999 | Draft tax bills, policy papers, draft regulations, budget proposals, borrowing framework | Gazette and website publication for comment; Budget Review process | 30–45 days | treasury.gov.za |
| 7 | National Credit Regulator | NCR | NCA 34/2005 | Regulations, guidelines, compliance notices, affordability assessment guidelines | Gazette notice-and-comment for regulations; guidelines via website | 30 days | ncr.org.za |
| 8 | B-BBEE Commission | B-BBEE Commission | B-BBEE Act 53/2003 | Codes of good practice, sector codes, investigation reports, compliance certificates | Extended Gazette notice-and-comment; sector code development with sector councils | Variable — 60+ days for major codes | bbbeecommission.co.za |
| 9 | SA Health Products Regulatory Authority | SAHPRA | Medicines and Related Substances Act 101/1965 | Regulations, schedules (scheduling of substances), guidelines, registration requirements | Gazette notice-and-comment for regulations and schedules; guidelines via website | 30–60 days | sahpra.org.za |
| 10 | National Consumer Commission | NCC | CPA 68/2008 | Regulations, industry codes, compliance notices, product safety recalls | Gazette notice-and-comment for regulations; industry code negotiation with industry bodies | 30 days | thencc.gov.za |
| 11 | Competition Commission | CompCom | Competition Act 89/1998 | Regulations, guidelines, exemptions, block exemption orders, market inquiry reports | Gazette notice-and-comment; public hearings for market inquiries | 30 business days | compcom.co.za |
| 12 | Information Regulator | IR | POPIA 4/2013, PAIA 2/2000 | Regulations, codes of conduct, guidance notes, enforcement notices | Gazette notice-and-comment; consultation with industry on codes of conduct | 30 days | inforegulator.org.za |

---

## 2. Sector-specific regulators

These regulators are not active by default. They are added to the user's watchlist when the cold-start-interview identifies relevant sector exposure. Users can also add them manually via the practice profile.

| Regulator | Abbreviation | Sector | Enabling statute | Key instruments |
|---|---|---|---|---|
| National Energy Regulator of SA | NERSA | Energy (electricity, piped gas, petroleum pipelines) | National Energy Regulator Act 40/2004 | Licence conditions, tariff determinations, rules, codes |
| Independent Communications Authority of SA | ICASA | Telecommunications, broadcasting, postal services | ICASA Act 13/2000 | Licence conditions, regulations, spectrum assignments |
| Council for Medical Schemes | CMS | Healthcare, medical schemes | Medical Schemes Act 131/1998 | Regulations, circulars, prescribed minimum benefits |
| Department of Mineral Resources and Energy | DMRE | Mining, petroleum | MPRDA 28/2002 | Mining Charter, regulations, directives |
| Department of Forestry, Fisheries and the Environment | DFFE | Environmental | NEMA 107/1998 | Environmental impact assessment regulations, species lists, waste management standards |
| Financial Intelligence Centre | FIC | AML/CFT (cross-sector) | FICA 38/2001 | Guidance notes, directives, exemptions, public compliance communications |

---

## 3. Industry bodies for joint regulatory comment submissions

When the comments skill prepares a regulatory submission, it should identify the relevant industry body and assess whether a consolidated submission is appropriate or whether the client should submit independently.

### Cross-cutting

| Body | Full name | Role |
|---|---|---|
| BUSA | Business Unity South Africa | Apex business body; NEDLAC business constituency representative; economy-wide regulatory submissions |
| BLSA | Business Leadership South Africa | Large-company CEO body; policy advocacy on business environment |

### Financial services

| Body | Full name | Role |
|---|---|---|
| BASA | Banking Association South Africa | Consolidated FSCA/PA/NCR submissions on banking regulation |
| ASISA | Association for Savings and Investment South Africa | Collective investment schemes, life insurance, retirement funds |
| SAIA | South African Insurance Association | Short-term insurance regulation |
| FIA | Financial Intermediaries Association | Financial advisers, intermediaries, FAIS-related regulation |

### Mining and resources

| Body | Full name | Role |
|---|---|---|
| Minerals Council SA | (formerly Chamber of Mines) | Mining Charter, MPRDA, mine health and safety, environmental regulation |

### Manufacturing and trade

| Body | Full name | Role |
|---|---|---|
| SACCI | SA Chamber of Commerce and Industry | Trade policy, regulatory environment, technical standards |

### Retail and consumer

| Body | Full name | Role |
|---|---|---|
| CGCSA | Consumer Goods Council of South Africa | Consumer protection regulation, product safety, food safety |

### Telecommunications and ICT

| Body | Full name | Role |
|---|---|---|
| ISPA | Internet Service Providers' Association | ICASA regulations, spectrum policy, internet governance |

### Professional bodies

| Body | Full name | Role |
|---|---|---|
| SAICA | SA Institute of Chartered Accountants | Tax, company law, financial reporting standards, audit regulation |
| SAIPA | SA Institute of Professional Accountants | Tax administration, SME accounting regulation |

### SMEs and chambers

| Body | Full name | Role |
|---|---|---|
| NSBC | National Small Business Chamber | SME-specific regulatory burden, compliance costs |
| NAFCOC | National African Federated Chamber of Commerce | Black business advocacy, B-BBEE, transformation policy |
| FABCOS | Foundation for African Business and Consumer Services | Informal sector and emerging business regulatory environment |
