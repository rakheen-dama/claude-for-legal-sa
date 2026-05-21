# SA-Specific Diligence — South African Framework

This overlay covers South African-specific due diligence categories, regulatory compliance requirements, contract law conventions, and post-close integration items that differ from US defaults. It is loaded by diligence-issue-extraction, material-contract-schedule, and integration-management when jurisdiction = ZA.

---

## 1. SA diligence request categories

The following table maps standard US due diligence categories to their South African equivalents. Skills loading this overlay must substitute the SA column when generating diligence request lists, checklists, or issue trackers.

| Category | US request | SA equivalent |
|---|---|---|
| **Corporate organization** | Certificate of good standing; bylaws; articles of incorporation; charter | CIPC company search (confirms "active" status); MOI (Memorandum of Incorporation); director register (CoR39 filings); share register; beneficial ownership declaration |
| **Contracts — general** | Material contracts; customer/supplier agreements | Material contracts; customer/supplier agreements; **B-BBEE compliance certificates** for counterparties; conventional penalty clauses; restraint of trade clauses |
| **Contracts — real property** | Title search; title insurance | Deeds Office search; zoning certificate; municipal clearance certificate; no title insurance equivalent in SA |
| **Employment** | WARN compliance; benefits plans; employment agreements; handbook | LRA s197 transfer analysis; BCEA conditions of employment; bargaining council agreements; employment equity plan and reports; skills development levies; COIDA registration |
| **Regulatory** | State permits; federal licences; environmental permits | CIPC compliance status; Competition Act (prior merger approvals and conditions); MPRDA (mining/prospecting rights); NEMA (environmental authorisations); FSCA/Prudential Authority (financial services); ICASA (telecoms); NLA/DALRRD (agriculture) |
| **Tax** | Federal and state tax returns; IRS compliance | SARS tax clearance certificate; income tax (IT14); VAT registration and returns; PAYE/UIF/SDL compliance; STC legacy (secondary tax on companies — pre-April 2012 dividends); withholding tax on dividends (post-April 2012); transfer pricing documentation |
| **IP** | USPTO registrations; patent portfolio | CIPC trademark registrations; CIPC patent registrations; CIPC design registrations; copyright (no registration system in SA — copyright vests automatically under Copyright Act 98 of 1978); domain name registrations (ZADNA / .za registry) |
| **Insurance** | Policy schedule; claims history | Policy schedule; claims history; short-term insurance (STIA); long-term insurance (LTIA); **no title insurance** — SA uses the Deeds Office registration system which provides state-guaranteed title |
| **Competition** | HSR/Hart-Scott-Rodino filings; antitrust compliance | Competition Act merger notifications; prior approval conditions still in force; restrictive practices (s4 horizontal, s5 vertical); abuse of dominance (s8, s9); exemptions |
| **Data protection** | State privacy laws; CCPA/CPRA | POPIA: Information Officer registration with Information Regulator; POPIA compliance framework; data processing agreements (operator agreements per s19–21); cross-border transfer safeguards (s72); direct marketing consent (s69) |
| **Exchange control** | N/A (no equivalent) | SARB approvals for cross-border structures; authorised dealer confirmations; loop structure analysis; inward/outward listed investment; thin capitalisation rules |

---

## 2. Regulatory compliance categories

### B-BBEE

| Check | Where to find it | Risk level |
|---|---|---|
| B-BBEE certificate validity | Target company; SANAS-accredited verification agency | **High** — expired certificate means unverified B-BBEE status; government contracts at risk |
| Scorecard breakdown by element | Verification agency report | **High** — ownership element changes trigger scorecard recalculation |
| Ownership element: direct vs indirect | Share register; shareholder agreements; trust deeds | **High** — indirect ownership requires flow-through calculation |
| Fronting indicators | Shareholder agreements; side letters; management agreements | **Critical** — fronting is a criminal offence (B-BBEE Act s13F) |
| Sector code applicability | Industry classification; sector charter | **Medium** — wrong sector code invalidates scorecard |

### POPIA

| Check | Where to find it | Risk level |
|---|---|---|
| Information Officer registration | Information Regulator register | **High** — failure to register is an offence |
| POPIA compliance framework | Internal policies; PAIA manual | **Medium** — assess maturity of compliance programme |
| Data processing agreements | Service contracts; outsourcing agreements | **High** — operator agreements required per s19–21 |
| Cross-border transfer safeguards | Contracts with foreign counterparties | **High** — s72 requires adequate safeguards for transborder information flows |
| Direct marketing consent records | CRM systems; marketing databases | **Medium** — s69 requires opt-in consent |

### NEMA (Environmental)

| Check | Where to find it | Risk level |
|---|---|---|
| Environmental authorisations (EAs) | Provincial environmental department; DFFE | **Critical** — operating without EA is a criminal offence |
| Waste management licences | DFFE; provincial department | **High** — required for listed waste management activities |
| Environmental compliance reports | Target company; consultants | **Medium** — indicates compliance track record |
| Water use licences | Department of Water and Sanitation | **High** — required for water use beyond Schedule 1 domestic use |
| Contaminated land | Environmental site assessments; NEMA s28 duty of care | **Critical** — successor liability for contamination |

### Competition Act

| Check | Where to find it | Risk level |
|---|---|---|
| Prior merger approvals | Competition Commission website; target records | **High** — conditions may still be in force and binding on successors |
| Conditions still in force | Approval orders; monitoring reports | **High** — breach of condition is a criminal offence |
| Restrictive practices exposure | Customer/supplier contracts; distribution agreements | **High** — cartel conduct (s4(1)(b)) carries administrative penalties up to 10% of annual turnover |
| Exemptions | Competition Commission records | **Medium** — exemptions have fixed terms and may have expired |

### Exchange control

| Check | Where to find it | Risk level |
|---|---|---|
| SARB approvals | Authorised dealer records; SARB correspondence | **High** — non-compliance renders transactions void |
| Loop structure analysis | Group structure chart; shareholding records | **Critical** — loop structures (SA residents indirectly holding SA assets through offshore entities) require SARB approval |
| Thin capitalisation | Loan agreements; intercompany funding | **Medium** — s31 transfer pricing rules apply to cross-border funding |

### Financial services

| Check | Where to find it | Risk level |
|---|---|---|
| Banks Act s37 — 15% threshold | Shareholding records | **Critical** — acquiring ≥15% of a bank requires Prudential Authority approval |
| FAIS licences | FSCA register | **High** — operating without licence is criminal offence |
| Insurance licences | Prudential Authority register | **High** — operating without licence is criminal offence |
| FSCA regulatory status | FSCA register; enforcement notices | **Medium** — check for pending investigations or sanctions |

---

## 3. B-BBEE due diligence

### Certificate validity

B-BBEE certificates are typically valid for **12 months** from the date of verification. Due diligence must confirm:

- Date of issue and expiry.
- Verification agency is SANAS-accredited or IRBA-approved.
- Certificate level corresponds to the target's self-assessment.

### Scorecard elements

The generic scorecard (Codes of Good Practice) comprises the following elements:

| Element | Weighting | Key diligence issue |
|---|---|---|
| Ownership | 25 points | Direct/indirect HDP ownership; flow-through; new entrants vs continuing |
| Management control | 23 points | Board and top management demographics |
| Skills development | 20 points | Training spend as % of payroll; learnerships |
| Enterprise and supplier development | 40 points (combined) | Procurement from QSEs/EMEs; enterprise development contributions |
| Socio-economic development | 12 points | CSI spend as % of NPAT |

### Fronting indicators

The B-BBEE Act s13F and the Codes of Good Practice identify the following fronting practices:

1. **Nominee arrangements** — BEE shareholder has no genuine participation in governance or economic benefits.
2. **Side agreements** — agreements that guarantee returns to the BEE shareholder while eliminating downside risk, or that give the non-BEE party a call option to reacquire the BEE shareholding.
3. **Excessive risk allocation** — BEE shareholder bears disproportionate risk relative to their shareholding.
4. **Lack of meaningful participation** — BEE shareholder has no board representation, no management involvement, and no real influence on business decisions.
5. **Token appointments** — senior management positions filled by HDP persons who have no real authority or decision-making power.

Fronting is a **criminal offence** carrying fines up to **10% of annual turnover** and/or imprisonment up to **10 years**.

### Government contract implications

- Government procurement requires minimum B-BBEE levels under the Preferential Procurement Policy Framework Act (PPPFA) and B-BBEE regulations.
- A drop in B-BBEE level may result in **loss of preferred supplier status**, inability to bid on new government contracts, or even **cancellation of existing contracts** if the contract terms require maintenance of a minimum B-BBEE level.
- The Competition Commission considers "greater spread of ownership" as a public interest factor in every merger assessment. A transaction that has a negative effect on HDP ownership may face conditions or prohibition.

---

## 4. SA contract law conventions

### Conventional penalties

The **Conventional Penalties Act 15 of 1962** governs penalty clauses in contracts.

- A conventional penalty clause (also known as a "penalty stipulation") is a clause providing for payment of a specified sum or for forfeiture of a specified benefit upon breach.
- Section 3 empowers the court to **reduce** a penalty if it is out of proportion to the prejudice suffered by the creditor. The court considers the actual loss suffered, not the theoretical maximum.
- **Diligence implication:** flag all conventional penalty clauses in material contracts and assess whether the penalty amounts are proportionate to likely breach scenarios. Disproportionate penalties may be unenforceable.

### Restraint of trade

Restraint of trade clauses are **enforceable** in South Africa, subject to a reasonableness test established in *Basson v Chilwan* 1993 (3) SA 742 (A):

| Factor | Test |
|---|---|
| 1. Protectable interest | Does the party seeking to enforce the restraint have a protectable interest (e.g., trade secrets, customer relationships, trade connections)? |
| 2. Reasonable necessity | Is the restraint reasonably necessary to protect that interest? |
| 3. Undue prejudice | Does the restraint prejudice the restrained party unduly, having regard to the scope, duration, and geographical area? |
| 4. Public interest | Is the restraint contrary to the public interest? |

The onus is on the party seeking to escape the restraint to show that it is unreasonable. Courts may partially enforce a restraint (reducing duration or area) rather than striking it down entirely.

**Diligence implication:** flag all restraint of trade clauses in employment contracts and commercial agreements. Assess enforceability against the *Basson v Chilwan* factors. Unreasonable restraints create risk if the target relies on them to protect its competitive position.

### Cession and delegation

South African law distinguishes between:

- **Cession** — transfer of rights (claims) under a contract. Generally does not require the consent of the debtor unless the contract contains an anti-cession clause. Anti-cession clauses are enforceable in SA.
- **Delegation** — transfer of obligations (duties) under a contract. Requires the **consent** of the creditor because the identity of the debtor is material to performance.

**Diligence implication:** review all material contracts for anti-cession clauses and consent-to-delegation requirements. In a share sale, no cession or delegation occurs (the contracting entity remains the same). In an asset sale, every contract must be analysed for cession/delegation mechanics.

### Mora (default)

- **Mora ex re** — the debtor is automatically in mora when a fixed due date passes without performance.
- **Mora ex persona** — where no fixed date is agreed, the creditor must demand performance; the debtor is in mora only after receiving the demand and failing to perform within a reasonable time.

**Diligence implication:** review outstanding debtor positions to determine whether debtors are in mora and whether interest on late payment is accruing.

### Breach and cancellation

- **Lex commissoria** clauses (cancellation on breach) are enforceable in SA.
- The party seeking to cancel must give **reasonable notice** of the breach and an opportunity to remedy (unless the contract provides otherwise or the breach is not capable of remedy).
- Cancellation is prospective (not retroactive) unless the contract provides otherwise.

**Diligence implication:** identify all contracts where the counterparty has a right to cancel on breach, and assess whether any existing breaches by the target could trigger cancellation.

---

## 5. SA materiality framing

### Statutory threshold

Companies Act s112 sets the statutory threshold for "all or the greater part" of assets or undertaking at **>50%** (gross assets fairly valued irrespective of liabilities, or undertaking fairly valued). This is the threshold above which shareholder approval by special resolution is required.

### Practice-area specific materiality

For due diligence purposes, "material contract" definitions in SA practice typically use one or more of the following criteria:

| Criterion | Example threshold | Rationale |
|---|---|---|
| ZAR value | >R5 million annual value | Absolute monetary materiality |
| Percentage of revenue | >5% of annual revenue | Relative size significance |
| Top-N customers/suppliers | Top 10 by revenue/spend | Concentration risk |
| Government contracts | All government contracts regardless of value | B-BBEE and procurement regulation exposure |
| B-BBEE-dependent contracts | Contracts requiring minimum B-BBEE level | Risk of loss if B-BBEE level drops |
| IP licences | All IP licences | Critical to business operations |
| Real property leases | All leases >3 years or >R500k annual rent | Operational continuity |
| Related-party transactions | All transactions with related parties (s1 definition) | Conflict of interest; s45 financial assistance |
| Loan agreements | All loan agreements >R1 million | Financing structure; change-of-control clauses |

### SA-specific materiality categories

Three categories of material assets are unique to SA and must be flagged in every corporate diligence exercise:

1. **B-BBEE-linked revenue** — contracts where the customer requires the target to maintain a minimum B-BBEE level. If the transaction causes a B-BBEE level drop, these contracts are at risk of cancellation or non-renewal.

2. **MPRDA-linked assets** — mining rights, prospecting rights, and reconnaissance permits under the Mineral and Petroleum Resources Development Act 28 of 2002. These rights often contain BEE shareholding conditions. Transfer of mining rights requires ministerial consent (MPRDA s11).

3. **CIPC-registered IP** — trademarks, patents, and designs registered with the CIPC. Assignment of registered IP requires CIPC recordal. Unrecorded assignments may not be enforceable against third parties.

---

## 6. Post-close integration (SA-specific items)

### CIPC CoR filings

| Filing | Form | Deadline | Consequence of non-filing |
|---|---|---|---|
| Director changes | CoR39 | Within **10 BD** of change | CIPC register reflects incorrect directors; third-party reliance risk |
| Registered address change | CoR21.1 | Within **10 BD** of change | Correspondence may not reach the company |
| MOI amendment (if needed) | CoR15.2 | Within **10 BD** of special resolution | Amendment not effective until filed |
| Name change (if applicable) | CoR44 | After special resolution and CIPC approval | Old name remains on register |

### B-BBEE re-scoring

A change in ownership triggers the need for re-verification of the B-BBEE scorecard:

1. **Ownership element recalculation** — new ownership structure must be verified against the Codes of Good Practice or applicable sector code.
2. **Management control** — if board composition changes, management control points may change.
3. **Timeline** — a new B-BBEE certificate should be obtained within **3 months** of closing to avoid a gap in verified status.
4. **Government contracts** — if the entity holds government contracts, notify the contracting authority of the ownership change and provide the updated B-BBEE certificate.

### IP recordals at CIPC

| IP type | Form/process | Effect of non-recordal |
|---|---|---|
| Trademark assignment | TM16 form filed at CIPC | Assignment not enforceable against third parties |
| Patent assignment | P7 form filed at CIPC | Assignment not enforceable against third parties |
| Design assignment | D5 form filed at CIPC | Assignment not enforceable against third parties |

### LRA s197 compliance

Post-close integration must respect the automatic transfer provisions:

- **Terms preserved** — all terms and conditions of employment that applied immediately before the transfer continue to apply.
- **12-month joint liability** — the transferor and transferee are jointly and severally liable for obligations arising before the transfer for a period of 12 months.
- **Collective agreements** — the transferee is bound by existing collective agreements and arbitration awards for their remaining term.
- **No dismissal by reason of transfer** — any dismissal motivated by the transfer is automatically unfair (s187(1)(g)).
- **Practical steps** — conduct employee verification, issue letters confirming transfer, update payroll systems, ensure pension/provident fund continuity.

### Competition condition monitoring

If the Competition Commission imposed conditions on the merger approval, post-close integration must include:

- **Employment moratorium tracking** — conditions frequently require maintenance of employment levels for a specified period (typically 3–5 years).
- **B-BBEE condition compliance** — conditions may require maintenance or improvement of B-BBEE levels.
- **Reporting** — conditions typically require periodic reports to the Competition Commission.
- **Breach consequences** — breach of merger conditions may result in administrative penalties, variation of conditions, or revocation of the merger approval.

### Exchange control reporting

For transactions with a cross-border element:

- SARB reporting obligations for changes to cross-border group structures.
- Authorised dealer reporting for inward and outward investments.
- Compliance with loop structure regulations if the post-merger group includes SA residents holding SA assets through offshore entities.

---

## 7. US concepts that must not appear in SA outputs

Skills loading this overlay must suppress the following US legal concepts and substitute the SA equivalent. If there is no SA equivalent, the concept must be omitted entirely.

| US concept | SA equivalent or "no equivalent" |
|---|---|
| WARN Act (Worker Adjustment and Retraining Notification) | **No equivalent** — SA uses LRA s189/s189A for retrenchment consultation (60-day minimum for large-scale retrenchments) |
| COBRA (health insurance continuation) | **No equivalent** — SA medical schemes operate under the Medical Schemes Act 131 of 1998; no employer-continuation obligation |
| At-will employment | **No equivalent** — LRA requires a fair reason (misconduct, incapacity, or operational requirements) and a fair procedure for every dismissal |
| FLSA (Fair Labor Standards Act) | **BCEA** (Basic Conditions of Employment Act 75 of 1997) — minimum conditions of employment including working hours, overtime, leave, and minimum wage |
| FAR/DFARS (Federal Acquisition Regulation) | **No equivalent** — SA government procurement governed by PPPFA (Preferential Procurement Policy Framework Act 5 of 2000) and B-BBEE regulations |
| SBA set-aside | **No equivalent** — SA uses B-BBEE preferential procurement, QSE/EME recognition, and PPPFA preference points |
| CERCLA (Superfund) | **NEMA** (National Environmental Management Act 107 of 1998) — s28 duty of care and s24 environmental authorisations; no superfund equivalent |
| EPA (US Environmental Protection Agency) | **DFFE** (Department of Forestry, Fisheries and Environment) — and provincial environmental departments |
| State-specific rules | **Not applicable** — SA is a unitary state, not a federation; one set of national laws applies everywhere |
| Dollar-denominated thresholds | **Use ZAR** — all monetary thresholds must be expressed in South African Rand |
| DGCL / Delaware General Corporation Law | **Companies Act 71 of 2008** — single national statute; no state-level corporate law |
| Bylaws | **MOI** (Memorandum of Incorporation) — the sole governing document of a SA company |
| HSR / Hart-Scott-Rodino | **Competition Act 89 of 1998** — merger notification to the Competition Commission |
| SEC (Securities and Exchange Commission) | **JSE** (Johannesburg Stock Exchange) for listing regulation; **FSCA** (Financial Sector Conduct Authority) for market conduct and financial services regulation |
| UCC (Uniform Commercial Code) | **No equivalent** — SA uses common law of sale (influenced by Roman-Dutch law) supplemented by the Consumer Protection Act 68 of 2008 |
| Chapter 11 bankruptcy | **Business rescue** (Companies Act Chapter 6) — proceedings to rehabilitate financially distressed companies |
| Dodd-Frank | **No equivalent** — SA financial regulation uses a twin peaks model: Prudential Authority (prudential regulation) and FSCA (market conduct) |
| ERISA (Employee Retirement Income Security Act) | **Pension Funds Act 24 of 1956** — governs retirement funds; supplemented by the Financial Sector Regulation Act |
| OSHA (Occupational Safety and Health Act) | **OHS Act** (Occupational Health and Safety Act 85 of 1993) — and MHSA (Mine Health and Safety Act 29 of 1996) for mining operations |
