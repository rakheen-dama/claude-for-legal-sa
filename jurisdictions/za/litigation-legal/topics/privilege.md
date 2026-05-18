# Privilege — South African Framework

This overlay covers SA legal professional privilege, the dominant purpose test, in-house counsel capacity, and privilege in discovery. Loaded by privilege-log-review, legal-hold, and brief-section-drafter when jurisdiction = ZA.

---

## 1. SA legal professional privilege

SA privilege is primarily **common-law**, constitutionally reinforced (Constitution s14 privacy, s34 access to courts). There is no single codifying statute.

### Two branches

| Branch | Scope | Test |
|---|---|---|
| **Advice privilege** | Confidential communications between client and legal adviser for the purpose of obtaining or giving legal advice | (1) Communication between client and legal adviser, (2) made for the purpose of legal advice, (3) intended to be confidential |
| **Litigation privilege** | Communications and documents prepared for the dominant purpose of pending or contemplated litigation | (1) Litigation pending or reasonably contemplated, (2) communication/document prepared for the **dominant purpose** of that litigation, (3) confidential |

### No work-product doctrine

SA does not have a separate "work product" doctrine (US FRCP 26(b)(3)). What US law calls "attorney work product" falls under **litigation privilege** in SA, which uses the dominant purpose test. There is no distinction between "opinion work product" and "ordinary work product" and no "substantial need" exception.

---

## 2. In-house counsel — legal vs commercial capacity

This is the critical SA-specific issue. Privilege attaches to in-house counsel **only when acting in a legal advisory capacity**.

| Capacity | Privileged? | Example |
|---|---|---|
| **Legal** | Yes | Legal opinion on regulatory compliance, advice on litigation strategy, analysis of contractual obligations |
| **Commercial** | No | Business strategy memo, commercial negotiation notes, operational decision-making, marketing input |
| **Mixed** | Dominant purpose test | If dominant purpose was legal advice → privileged. If dominant purpose was commercial → not privileged. |

### Red flags for privilege loss

- In-house counsel copied on commercial emails "for information" — does not create privilege
- Report drafted by in-house counsel but circulated to non-legal stakeholders for business input — privilege may be waived
- In-house counsel attending meetings in a management (not legal) capacity — notes not privileged

### Practical guidance

- Clearly delineate legal advice from business advice in communications
- Mark legal advice as "Privileged and Confidential — Legal Advice"
- Limit circulation of legal advice to those who need it for the purpose of obtaining the advice
- When in-house counsel acts in both capacities, keep legal advice in separate communications from commercial input

---

## 3. Privilege in discovery (Rule 35)

### Discovery affidavit

When asserting privilege in discovery (Rule 35(2)), the discovery affidavit must:
- **List** the documents over which privilege is claimed (sufficient description to identify the document)
- **State the basis** of privilege (advice privilege, litigation privilege, without-prejudice)
- **Not disclose** the content of the privileged communication

### De facto privilege schedule

While there is no formal privilege log requirement (no FRCP 26(b)(5)(A) equivalent), complex matters commonly use a **privilege schedule** — a table listing:
- Document date
- Author / recipient
- Document type / description (without revealing content)
- Basis of privilege claimed

This is **best practice**, not a rule requirement. Courts may order a more detailed schedule if privilege claims are disputed.

### Challenging privilege claims

The opposing party may:
- Request further particulars of the privilege claim
- Apply to court for an order requiring a more detailed schedule
- Request **in camera inspection** — the court reviews the documents without disclosing them to the other party and rules on privilege

### Over-claiming privilege

Courts are sceptical of blanket privilege assertions. Over-claiming (asserting privilege over non-privileged documents) can result in:
- Costs orders
- Adverse findings on credibility
- Court-ordered disclosure of improperly claimed documents

---

## 4. Waiver of privilege

### Express waiver

Client may expressly waive privilege (privilege belongs to the client, not the lawyer).

### Implied waiver

| Scenario | Effect |
|---|---|
| **Partial disclosure** | Disclosing part of a privileged communication waives privilege over the remainder on the same subject matter. Selective disclosure is not permitted. |
| **Annexing to affidavit** | Annexing a privileged document to an affidavit filed in court waives privilege over that document. |
| **Circulation to third parties** | Circulating privileged advice to persons outside the attorney-client relationship (consultants, PR firms, funders) may waive privilege unless they are within the "necessary circle" for obtaining legal advice. |
| **Putting advice in issue** | If a party relies on legal advice as part of their case (e.g., "we acted on legal advice"), they waive privilege on that advice. |

### One-way door

Privilege waiver is **irreversible**. Once waived, the privilege cannot be reclaimed. This is why the practice profile defaults to over-marking (assert privilege and flag for review) rather than under-marking.

---

## 5. Without-prejudice privilege

Separate from legal professional privilege. Communications genuinely aimed at settlement are privileged from being tendered in evidence.

See `demands-and-settlement.md` for detailed coverage of without-prejudice rules.

---

## 6. What NOT to replicate from US practice

| US concept | SA status |
|---|---|
| Work product doctrine (FRCP 26(b)(3)) | No equivalent. Litigation privilege covers this ground via dominant purpose test. |
| Opinion vs ordinary work product | No distinction. All litigation privilege is assessed on dominant purpose. |
| Substantial need exception | No equivalent. Litigation privilege is not qualified in this way. |
| FRE 502 (waiver rules) | SA waiver follows common-law principles, not a statutory framework. |
| FRCP 26(b)(5)(A) privilege log | No mandatory privilege log. De facto privilege schedule is best practice. |
| Vaughn index | No equivalent. In camera inspection is the SA mechanism. |
| Crime-fraud exception | SA recognises that privilege does not extend to communications in furtherance of crime or fraud, but the doctrine is less developed than in US law. |
