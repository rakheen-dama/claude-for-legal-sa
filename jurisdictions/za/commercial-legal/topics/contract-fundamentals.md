# Contract Fundamentals — South African Framework

This overlay covers the foundational principles of South African commercial contract law, electronic formation, Consumer Protection Act applicability, exchange control, and VAT on imported services. It is loaded by vendor-agreement-review, saas-msa-review, and nda-review skills when jurisdiction = ZA.

---

## 1. SA common law of contract

South African contract law derives from Roman-Dutch law, not English common law. Several foundational principles diverge from US contract law:

### No consideration doctrine

SA law does not require consideration for contract formation. A contract is valid if there is:

1. **Consensus ad idem** — genuine meeting of minds between the parties.
2. **Capacity** — both parties have legal capacity to contract.
3. **Legality** — the object of the contract must be lawful.
4. **Possibility** — performance must be possible.
5. **Formalities** — where required by statute (e.g., alienation of land, suretyship).

The concept of causa (the lawful purpose underlying the agreement) replaces consideration. A gratuitous promise seriously intended and accepted is enforceable.

### Specific performance as primary remedy

SA law treats specific performance — a court order compelling the defaulting party to perform its obligations — as the **primary** remedy for breach of contract. This is the opposite of the US position where damages are the default remedy and specific performance is exceptional.

A party seeking specific performance need not prove that damages are inadequate. The court has discretion to refuse specific performance only where it would be inequitable or where performance has become impossible.

**Practical consequence:** liability caps in SA contracts are less protective than in US contracts because a court can order the breaching party to perform in full regardless of any monetary cap.

### Exceptio non adimpleti contractus

A party is entitled to withhold its own performance if the other party has not performed or tendered performance. This defence applies to reciprocal obligations without the need for a notice of breach. It is automatically available where obligations are interdependent.

### Pacta sunt servanda

Agreements must be kept. The Constitutional Court in **Beadica 231 CC v Trustees for the time being of Oregon Trust** (2020) reaffirmed that pacta sunt servanda is a constitutional value, subject only to public policy limitations. Courts will not lightly set aside freely concluded agreements.

---

## 2. Shifren principle — non-variation clauses

The Supreme Court of Appeal established in **SA Sentrale Ko-op Graanmaatskappy Bpk v Shifren** (1964) that a non-variation clause (requiring all amendments to be in writing) is strictly enforced in SA law. The key rules:

1. **Oral amendments are void** — if the contract contains a properly drafted non-variation clause, no oral or informal agreement can vary the contract's terms.
2. **Self-entrenchment required** — the clause must entrench itself: it must state that the non-variation clause itself can only be amended in writing. Without self-entrenchment, the parties could orally agree to waive the non-variation clause.
3. **Course of conduct irrelevant** — unlike US law, a course of conduct cannot override a written non-variation clause.

### High-risk flag: Missing or defective non-variation clause

| Check | What to look for |
|---|---|
| Non-variation clause present | Contract contains a clause requiring all amendments to be in writing, signed by both parties |
| Self-entrenching | The clause explicitly states that it cannot itself be waived or varied except in writing |
| History of oral variations | Evidence that parties have been varying terms informally (emails, phone calls) without written amendments |

**Why this matters:** Without a Shifren clause, oral agreements or conduct can modify the written contract, creating uncertainty about the actual terms in force. A clause that fails to entrench itself is equally ineffective.

---

## 3. ECTA — electronic formation and e-signatures

The Electronic Communications and Transactions Act 25 of 2002 (ECTA) governs electronic contract formation:

### Legal recognition (ECTA s11-s13)

- **Data messages** have legal recognition (s11). Information is not without legal force solely because it is in electronic form.
- **Writing requirement** satisfied by a data message that is accessible for subsequent reference (s12).
- **Electronic signatures** — two tiers:
  - **Standard electronic signature** (s13(1)) — any data attached to or associated with a data message, intended as a signature. Includes typed names, email signatures, click-wrap acceptances.
  - **Advanced electronic signature** (s13(3)) — accredited by the South African Accreditation Authority. Required only for transactions listed in ECTA Schedule 2.

### Schedule 1 and 2 exclusions

Certain transactions are excluded from electronic formation:

- **Schedule 1** — agreements excluded from ECTA entirely: wills, bills of exchange, alienation of immovable property.
- **Schedule 2** — agreements requiring advanced electronic signatures: long-term insurance, alienation of real rights in immovable property.

For most commercial contracts (vendor agreements, SaaS MSAs, NDAs), standard electronic signatures suffice.

### Automated transactions (ECTA s20)

An agreement formed by automated systems (e.g., online ordering) is valid. A party interacting with an automated system has the right to withdraw from the transaction if the system did not provide an opportunity to review, correct, and confirm the transaction.

---

## 4. Consumer Protection Act applicability

The Consumer Protection Act 68 of 2008 (CPA) applies to specific transactions. Determining applicability is a threshold question in every contract review.

### Applicability threshold

The CPA applies when:

1. The supplier supplied goods or services **in the ordinary course of business**.
2. The transaction involves a **consumer** — defined as:
   - A natural person, OR
   - A juristic person whose **annual turnover or asset value at the time of the transaction** falls below the threshold determined by the Minister (currently **R2 million**).

**Critical rule:** Section 5(2)(b) exempts transactions between juristic persons where neither party falls below the R2m threshold. Most B2B transactions between established companies fall outside the CPA.

### CPA s14 — fixed-term agreements

Where the CPA applies, s14 imposes strict requirements on fixed-term agreements:

1. **Maximum initial term** — 24 months (s14(2)(a)).
2. **Consumer's right to cancel** — the consumer may cancel with **20 business days' notice** (s14(2)(b)(i)(bb)), subject to a reasonable cancellation penalty.
3. **Expiry notice** — the supplier must notify the consumer **40 to 80 business days** before the expiry date (s14(2)(d)).
4. **Continuation after expiry** — if the consumer does not cancel, the agreement continues on a **month-to-month basis** on the same terms (s14(2)(e)).

**Section 14 does NOT apply between two juristic persons above the R2m threshold.** This is a common misapplication.

### CPA s48 — unfair contract terms

Where the CPA applies, s48 prohibits terms that are:

- Unfair, unreasonable, or unjust
- Excessively one-sided in favour of the supplier
- So adverse to the consumer as to be inequitable

### CPA s22 — plain language

Consumer agreements must be in plain and understandable language. The test (s22(2)) considers the likely audience, including their literacy level and knowledge.

### CPA Regulation 44(3) — unfair terms list

Regulation 44(3) provides a non-exhaustive list of presumptively unfair terms, including:

- Terms allowing the supplier to unilaterally vary material terms
- Terms requiring the consumer to waive rights under the CPA
- Terms that limit the consumer's right to seek legal recourse
- Terms imposing excessive penalties or forfeiture

### CPA s51 — prohibited terms

Section 51 renders void any term that:

- Purports to limit or exempt the supplier from liability for **gross negligence** (s51(1)(c)(i))
- Requires the consumer to assume risk for loss caused by gross negligence
- Imposes an obligation on the consumer to indemnify the supplier for loss caused by the supplier's own fault

### High-risk flag: CPA-covered agreement with non-compliant terms

| Check | What to look for |
|---|---|
| CPA applicability assessed | Counterparty is a natural person or juristic person below R2m turnover/assets |
| Fixed term compliant | Term does not exceed 24 months; 20 business days' cancellation right included |
| Plain language | Agreement written in plain, understandable language per s22 |
| No prohibited exclusions | No exclusion of supplier's liability for gross negligence (void under s51) |
| Unfair terms screened | Terms assessed against s48 fairness standard and Regulation 44(3) list |
| Expiry notice mechanics | Supplier must give 40-80 business days' notice before expiry |

**Why this matters:** Non-compliant terms in CPA-covered agreements are void or voidable. The National Consumer Commission can issue compliance notices and refer matters to the National Consumer Tribunal, which can impose administrative fines.

### High-risk flag: Auto-renewal without proper notice mechanics

| Check | What to look for |
|---|---|
| CPA-covered transaction | If yes, s14 notice requirements apply — 40-80 business days' pre-expiry notice mandatory |
| Calendar-based cancel-by deadline | Non-CPA agreements should include a specific deadline for cancellation notice |
| Renewal term reasonable | Auto-renewal term should not exceed the original term without justification |
| Silent renewal hostile | SA courts increasingly hostile to silent auto-renewals; explicit opt-in preferred |

**Why this matters:** CPA-covered agreements with defective renewal mechanics are unenforceable as to the renewal term. Even for non-CPA agreements, Johannesburg High Court trial dates are extending to 2027, making dispute prevention through clear cancellation mechanics critical.

---

## 5. Commercial bribery

Commercial bribery is a ground for rescission of a contract in SA law. The Prevention and Combating of Corrupt Activities Act 12 of 2004 criminalises gratification intended to influence a party's conduct in relation to a transaction. A contract procured through bribery is voidable at the instance of the innocent party.

---

## 6. Exchange control

South Africa maintains exchange control regulations under the Currency and Exchanges Act 9 of 1933, administered by the South African Reserve Bank (SARB) Financial Surveillance Department.

### Key requirements for cross-border commercial contracts

1. **Authorised Dealer routing** — all cross-border payments must be processed through an Authorised Dealer (commercial bank with exchange control authority). Payments cannot bypass the banking system.
2. **Arm's length pricing** — related-party cross-border fees (management fees, royalties, licence fees, technical services fees) must be demonstrably arm's length. SARB may disallow payments deemed excessive.
3. **Advance payment limits** — advance payments to non-residents are subject to limits and may require SARB approval depending on the amount and nature.
4. **Foreign currency exposure** — contracts denominated in foreign currency are permissible, but payment must flow through Authorised Dealer channels.
5. **Circular 13/2024** — liberalised certain routine payments (subscriptions, SaaS licence fees) by increasing thresholds and simplifying Authorised Dealer processes. Payments below the threshold no longer require detailed supporting documentation beyond the invoice.

### Related-party transactions

Where the counterparty is a connected person (group company, common shareholder, common director):

- Transfer pricing documentation must support the arm's length nature of the fee
- The Authorised Dealer may request the transfer pricing study before processing payment
- SARB Financial Surveillance retains the right to query any payment and request supporting documentation

### High-risk flag: Foreign governing law + exchange control blind spot

| Check | What to look for |
|---|---|
| Non-SA counterparty | Vendor or service provider is a foreign entity |
| Foreign currency payment | Contract requires payment in USD, EUR, GBP, or other non-ZAR currency |
| Exchange control acknowledged | Contract or payment terms acknowledge Authorised Dealer routing requirement |
| Arm's length for related parties | If connected persons, transfer pricing documentation supports the fee level |
| Circular 13/2024 threshold | Whether the payment falls within liberalised thresholds or requires additional documentation |

**Why this matters:** Non-compliance with exchange control regulations can result in SARB refusing to authorise the payment, penalties, and in serious cases criminal prosecution. Contracts that ignore exchange control create a performance risk — the SA party may be unable to lawfully make the payment.

---

## 7. VAT on electronic services

The Value-Added Tax Act 89 of 1991 imposes VAT on electronic services supplied by foreign suppliers to SA recipients.

### Current rate

The standard VAT rate is **15%** (VAT Act s7(1); see `statutes/vat.yaml` → `standard_rate_2018`). It has been 15% since 1 April 2018.

> **Historical note — the abandoned 2025 increase.** The 2025 Budget announced two staged VAT increases above 15% (effective May 2025 and April 2026). Both were **abandoned before taking effect**: the increase was withdrawn following a Western Cape High Court settlement order (April 2025) and National Treasury's reversal statement of 24 April 2025. VAT never rose above 15%. Do not apply any rate above 15% — confirm the current rate against the latest SARS notice. The specific announced (and withdrawn) rates are recorded in `statutes/vat.yaml` → `standard_rate_2018` note.

### Registration threshold

A foreign supplier of electronic services must register for SA VAT if the value of electronic services supplied to SA recipients exceeds **R1 million** in any consecutive 12-month period (VAT Act s23(1A); Electronic Services Regulations GN 429 GG 42316; see `statutes/vat.yaml` → `electronic_services_registration_threshold`).

### B2B exclusion

A foreign supplier is excluded from the obligation to register and charge SA VAT if the supplier supplies electronic services **solely** to SA recipients that are registered VAT vendors. This is the B2B exclusion.

**Critical limitation:** The B2B exclusion applies only if **every** SA recipient is a registered VAT vendor. If the foreign supplier has even one non-registered SA customer, the exclusion fails for all SA supplies.

### Reverse charge mechanism

Where the foreign supplier is not registered for SA VAT and the SA recipient is a registered VAT vendor, the SA recipient must self-assess and account for VAT on the imported services under the reverse charge mechanism. The SA recipient claims the input tax deduction in the same period (net zero effect for fully taxable supplies).

### Practical impact on SaaS and service contracts

- Foreign SaaS vendors supplying to SA above R1m must register and charge SA VAT
- SA companies purchasing imported electronic services from unregistered foreign vendors must account for reverse charge VAT
- Contract pricing should specify whether fees are VAT-inclusive or VAT-exclusive, and which party bears the SA VAT cost
- Automatic price escalation clauses should be drafted to absorb any future VAT rate change (the rate is a policy variable and has been the subject of announced-then-abandoned increases), rather than hardcoding a specific rate

### High-risk flag: VAT on imported services misconfigured

| Check | What to look for |
|---|---|
| Foreign vendor identified | Vendor is a non-SA entity supplying electronic services |
| SA VAT registration status | Is the foreign vendor registered for SA VAT? If not, reverse charge applies |
| B2B exclusion validity | Does the vendor supply solely to SA VAT-registered vendors? One non-registered customer invalidates the exclusion |
| Correct rate applied | Rate matches the current standard rate of 15% (confirm against the latest SARS notice; the announced 2025/2026 increases were abandoned) |
| Pricing clause addresses VAT | Contract specifies VAT treatment, which party bears VAT cost, and adjusts for rate changes |

**Why this matters:** Incorrect VAT treatment on imported services results in under-declaration by the SA recipient (reverse charge obligation) or double taxation. SARS actively audits cross-border electronic services VAT, and penalties for non-compliance include interest, understatement penalties (up to 200% for intentional non-disclosure), and potential criminal prosecution.

---

## 8. Must-not-contain reference

When jurisdiction = ZA, contract review skills must not use the following US terms:

| US term | SA replacement |
|---|---|
| "consideration" (as formation requirement) | causa / no equivalent requirement |
| "UCC" (Uniform Commercial Code) | SA common law of contract + CPA |
| "Statute of Frauds" | SA formality requirements (specific statutes) |
| "parol evidence rule" (US formulation) | SA integration clause + Shifren principle |
| "blue pencil doctrine" | SA severability |
| "preliminary injunction" | interdict |
