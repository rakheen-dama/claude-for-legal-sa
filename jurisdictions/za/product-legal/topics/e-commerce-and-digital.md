# E-Commerce and Digital — South African Framework

This overlay covers the Electronic Communications and Transactions Act 25 of 2002 (ECTA) and its interaction with the CPA and POPIA for digital transactions. It is loaded by launch-review, marketing-claims-review, and is-this-a-problem skills when jurisdiction = ZA.

---

## 1. ECTA mandatory disclosures (s43)

Any person who offers goods or services for sale by way of an electronic transaction must make the following information available to consumers on their website or platform in a manner that is easily accessible:

| Disclosure | ECTA section | Detail |
|---|---|---|
| Full name and legal status | s43(1)(a) | Company name, registration number, whether (Pty) Ltd, CC, sole proprietor, etc. |
| Physical address | s43(1)(b) | Street address — not a PO Box |
| Telephone number | s43(1)(c) | Landline or mobile where the supplier can be contacted |
| Website and email address | s43(1)(d) | Must be current and monitored |
| Membership of self-regulatory or accreditation body | s43(1)(e) | E.g., DMASA, ARB, industry association |
| Code of conduct to which the supplier subscribes | s43(1)(f) | If any |
| In the case of a legal person: office-bearer responsible for the website | s43(1)(g) | Named individual |
| Physical address for receiving legal service of process | s43(1)(h) | Must accept physical service |
| Description of main characteristics of goods or services | s43(1)(i) | Sufficient to enable informed decision |
| Full price including transport, taxes, fees | s43(1)(j) | All-inclusive price — no hidden charges at checkout |
| Payment method | s43(1)(k) | Accepted payment methods |
| Terms of agreement, including cooling-off and return policies | s43(1)(l) | Must be available before transaction |
| Time within which goods will be dispatched or services rendered | s43(1)(m) | Must state delivery timeline |
| Complaint procedure | s43(1)(n) | How to lodge complaints |
| Security and privacy policy | s43(2) | How payment and personal data are secured |
| Return, exchange, and refund policy | s43(2) | Clear terms for returns |

### Criminal offence (s43(5))

Non-compliance with s43 disclosure requirements is a criminal offence. Beyond the criminal risk, failure to make required disclosures may undermine the enforceability of the terms and conditions of the online transaction, as the consumer may argue they did not have the information necessary to make an informed decision.

---

## 2. Transaction mechanics

### Review and correct (s43(2))

Before a consumer completes an electronic transaction, the supplier must provide an opportunity for the consumer to:

1. Review the entire transaction.
2. Correct any mistakes.
3. Withdraw from the transaction before final confirmation.

A single "Place Order" button without a review step may violate this requirement. Best practice: a summary page showing all items, pricing, terms, and delivery details with an explicit "Confirm" action.

### Cooling-off period (s44)

A consumer may cancel an electronic transaction without reason or penalty within 7 days of receiving the goods or concluding the service agreement. The supplier must refund all payments within 30 days of cancellation.

This right cannot be excluded by contract. It applies to all electronic transactions (not just direct marketing, distinguishing it from CPA s16).

### Performance within 30 days (s46)

Unless the parties have agreed otherwise, the supplier must execute the order within 30 days after the day on which the order was placed. If the supplier is unable to perform, the consumer must be notified and all payments refunded within 30 days.

### Refund obligations

Where a consumer exercises the cooling-off right or the supplier fails to perform within 30 days:

- The supplier must refund all amounts paid.
- Refund must be made within 30 days.
- The consumer bears only the direct cost of returning goods (unless the goods are defective or not as described).

---

## 3. Spam and unsolicited communications

Three overlapping frameworks regulate electronic direct marketing in South Africa:

### ECTA s45

- Unsolicited commercial communications must include an option to cancel subscription to the mailing list.
- Messages must contain the identity and physical address of the sender.
- A person who has opted out must not receive further communications.
- Non-compliance is an offence.

### POPIA s69

- Direct marketing by means of unsolicited electronic communications (including email, SMS, push notifications) is prohibited unless:
  - The data subject has given consent (opt-in), **or**
  - The data subject is an existing customer, the marketing relates to similar products or services, and the data subject has been given a reasonable opportunity to opt out at each communication.
- This "existing customer" exception is the SA equivalent of a soft opt-in.
- The data subject must be able to opt out at no cost and with no conditions.

### DMASA Code of Conduct

The Direct Marketing Association of Southern Africa administers a code of practice aligned with POPIA. Membership is voluntary but widely adopted. The DMASA Code adds operational standards for suppression list management, frequency caps, and consent record-keeping.

### Practical overlap

| Scenario | ECTA s45 | POPIA s69 | DMASA Code |
|---|---|---|---|
| New prospect, no prior relationship | Must include opt-out + address | Requires prior opt-in consent | Consent record required |
| Existing customer, similar product | Must include opt-out + address | Soft opt-in permitted; must offer opt-out | Suppression list check |
| Customer who opted out | Prohibited | Prohibited | Suppression list enforced |
| SMS/push notification (not email) | ECTA applies (electronic communication) | POPIA s69 applies (any electronic medium) | DMASA covers all direct marketing channels |

---

## 4. The triple-compliance problem

For any online business operating in South Africa, three statutes apply in parallel to digital transactions:

- **ECTA** — governs the electronic transaction mechanics, disclosures, and cooling-off.
- **CPA** — governs the consumer protection aspects: unfair terms, product quality, misleading marketing, plain language.
- **POPIA** — governs the collection, processing, and storage of personal information.

Compliance with one does not excuse non-compliance with the others. A common mistake is assuming that an ECTA-compliant checkout also satisfies CPA s49 (notice of adverse terms) or POPIA s18 (notification to data subject). Each has its own requirements.

### Practical compliance checklist

| Requirement | ECTA | CPA | POPIA |
|---|---|---|---|
| Disclosure of identity and contact details | s43(1)(a-h) | s22 (plain language) | s18(1)(a) (responsible party identity) |
| Full pricing disclosed before transaction | s43(1)(j) | s23 (right to information in plain language) | — |
| Terms and conditions available before transaction | s43(1)(l) | s49 (adverse terms conspicuously drawn to attention) | — |
| Right to cancel / cooling-off | s44 (7 days, e-commerce) | s16 (5 business days, direct marketing) | — |
| Privacy policy / data processing notice | s43(2) (security + privacy) | — | s18 (full data subject notification) |
| Complaint mechanism | s43(1)(n) | s69-71 (complaint resolution) | s74 (complaint to Information Regulator) |
| Consent for marketing | s45 (opt-out mechanism) | — | s69 (opt-in or existing customer exception) |
| Record-keeping | s16 (data messages) | s26 (sales records) | s14 (retention limitation) |

---

## 5. High-risk flag checklist

| Flag | Why high-risk | What to check |
|---|---|---|
| **ECTA e-commerce disclosure failures (s43-52)** | Criminal offence (s43(5)). Non-compliance undermines T&C enforceability. ECTA + CPA apply in parallel. | Physical address disclosed? Full pricing? Complaint procedure? Security/privacy disclosures? Review-and-correct step? Cooling-off honoured? 30-day performance? |
