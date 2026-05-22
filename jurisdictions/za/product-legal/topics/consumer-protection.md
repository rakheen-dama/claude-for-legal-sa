# Consumer Protection — South African Framework

This overlay covers the Consumer Protection Act 68 of 2008 (CPA) as it applies to product-legal workflows — product quality, safety, strict liability, unfair contract terms, plain language, and cooling-off rights. It is loaded by launch-review, feature-risk-assessment, and is-this-a-problem skills when jurisdiction = ZA.

---

## 1. CPA applicability

The CPA applies broadly but not universally. Scope is set by s5:

- **Natural persons** — always covered, regardless of transaction value.
- **Juristic persons** — covered only if annual turnover or asset value is below the threshold set by the Minister (currently R2 million, published by Gazette — check `statutes/cpa.yaml` for current value).
- **B2B SaaS** — if the customer is a juristic person above R2m, the CPA does not apply to that transaction. However, the CPA may still apply to the end-users of that SaaS product if they are natural persons or small juristic persons interacting with the product.
- **Excluded transactions** — employment contracts, credit agreements governed by NCA (except CPA s60-61 for product liability), and transactions regulated by sector-specific legislation that provides equivalent consumer protection.

### Practical test for product counsel

1. Who is the contracting party — natural person or juristic person?
2. If juristic person, does it exceed the R2m threshold?
3. Even if the contract is excluded, do natural-person end-users interact with the product?
4. Is a sector-specific statute (NCA, FAIS, Medicines Act) the dominant regulatory framework?

---

## 2. Product quality and safety (CPA s55-58)

### Right to safe, good-quality goods (s55)

Every consumer has the right to receive goods that are reasonably suitable for their intended purpose, of good quality, in good working order, and free of defects. This applies to all goods, including digital products and software where they qualify as "goods" under the CPA.

### Implied warranty of quality (s56)

Every producer, importer, distributor, and retailer provides an implied warranty that goods comply with s55 for a minimum of 6 months after delivery. This warranty:

- Cannot be excluded or restricted by contract (s51).
- Runs in addition to any express warranty provided by the supplier.
- Entitles the consumer to return goods and choose between repair, replacement, or refund.

### Safety warnings and instructions (s58)

Producers and importers must provide adequate warnings and instructions in plain language (s22) regarding:

- Any reasonably foreseeable risk of harm associated with the product.
- Safe handling, use, storage, and disposal.

Failure to provide adequate warnings is relevant to both s58 compliance and s61 product liability.

### Product safety monitoring (s60)

Producers, importers, and distributors must monitor the safety of goods after supply. If a product presents a safety risk, they must:

1. Alert the public and trade of the risk.
2. Recall the product where necessary.
3. Refund consumers or replace the product.

For digital products, this translates to: monitoring for defects post-release, notifying users of known issues, and providing timely patches or remediation.

---

## 3. Strict product liability (CPA s61)

### No-fault liability regime

CPA s61 imposes strict liability for harm caused by defective goods, inadequate instructions, or failure to warn. Key features:

- **No fault required** — the claimant does not need to prove negligence. It is sufficient to show that the goods were defective, or that instructions or warnings were inadequate, and that this caused harm.
- **Joint and several liability** — the producer, importer, distributor, and retailer are all potentially liable. The claimant can pursue any or all members of the supply chain.
- **Cannot contract out** — s51 prohibits any term that purports to exclude or limit liability under s61. Indemnity clauses, liability caps, and limitation of liability provisions in T&Cs are void to the extent they conflict with s61.
- **Harm covered** — death, injury, illness, loss of or damage to property, and any economic loss resulting from harm to person or property.

### Application to digital products

The CPA's application to pure SaaS (where no physical goods are involved) remains untested in SA courts. However:

- Software embedded in physical products (IoT, smart devices, firmware) is covered as part of the goods.
- Software sold as a product (downloaded application, licensed software) likely qualifies as "goods" under the CPA's broad definition.
- Pure cloud services with no deliverable may fall outside s61 but remain subject to CPA s54 (services) and common law.

Product counsel should treat digital products as potentially within s61 scope until case law provides clarity.

---

## 4. Unfair contract terms (CPA s48-52)

### Prohibition on unfair terms (s48)

A supplier must not supply goods or services on terms that are unfair, unreasonable, or unjust. The NCC and Consumer Tribunal can declare such terms void.

### Notice requirements for adverse terms (s49)

Terms that limit the risk or liability of the supplier, or that constitute an assumption of risk by the consumer, must be drawn to the consumer's attention in a conspicuous manner and in plain language before the transaction.

### Prohibited terms (s51)

The following terms are void to the extent indicated:

- Terms that exclude or limit liability for gross negligence.
- Terms that exclude or limit CPA rights (including s61 product liability).
- Terms requiring the consumer to assume risk for loss of or damage to goods in the supplier's control.
- Terms that waive the consumer's right to approach a court or tribunal.

### Common SaaS T&C pitfalls

| Pitfall | CPA provision | Risk |
|---|---|---|
| Overbroad liability exclusion ("in no event shall we be liable for any damages") | s51 — void | Entire clause may be struck; no fallback position |
| One-sided termination ("we may terminate at any time for any reason") | s48 — unfair | NCC complaint; term declared void |
| Unfair auto-renewal (renewal without clear notice and opt-out) | s14, s40(2) — right to cancel | Consumer may cancel at any time on 20 business days' notice |
| Hidden fee changes ("we may change pricing at our discretion") | s48, s49 — unfair + not conspicuous | Must give adequate notice; term may be void |
| Dense legalese violating s22 | s22 — plain language | Entire agreement enforceability at risk |
| Imported US/EU template without SA adaptation | s48-52 collectively | Multiple void provisions; no contractual protection where expected |

---

## 5. Plain language requirement (CPA s22)

Section 22 requires that any notice, document, or visual representation required under the CPA must be in plain language. A document is in plain language if an ordinary consumer of the class for which it is intended could be expected to understand it without undue effort.

### What it applies to

- Terms and conditions / terms of service.
- Privacy policies (also required by POPIA s18).
- Product disclosures and warranties.
- Marketing copy and promotional material.
- Notices required under s49 (adverse terms).
- Cancellation and refund notices.

### Practical standard

The CPA does not prescribe a specific readability formula, but the test is objective: would an ordinary consumer in the target market understand the document? Factors include vocabulary, sentence length, structure, layout, and use of headings and summaries.

---

## 6. Cooling-off rights

Two separate cooling-off regimes apply, depending on how the transaction was initiated:

### CPA s16 — direct marketing

- **Duration:** 5 business days from delivery of goods or conclusion of agreement.
- **Trigger:** Transaction resulted from direct marketing (phone, email, door-to-door, any unsolicited approach).
- **Effect:** Consumer may return goods without reason or penalty. Supplier must refund within 15 business days.

### ECTA s44 — e-commerce

- **Duration:** 7 days from date of delivery.
- **Trigger:** Any transaction concluded by electronic means (website purchase, app purchase, online signup).
- **Effect:** Consumer may cancel without reason or penalty. Supplier must refund within 30 days.

### When both apply

If a consumer receives a marketing email (direct marketing) containing a link to a website (e-commerce), both CPA s16 and ECTA s44 may apply. In practice, the consumer benefits from whichever period is more favourable. Product flows must accommodate both cooling-off periods.

---

## 7. NCC enforcement

### Complaint procedure (CPA s71)

1. Consumer lodges complaint with supplier's internal complaints mechanism.
2. If unresolved, consumer may approach an industry ombud, provincial consumer court, or the NCC directly.
3. NCC investigates and may issue a compliance notice (s100).
4. Non-compliance with a compliance notice is referred to the Consumer Tribunal.

### Penalties

- Consumer Tribunal may impose administrative fines up to R1 million or 10% of the supplier's annual turnover (s112), whichever is greater.
- The NCC has issued 62+ compliance notices in the 2025-26 period, reflecting increased enforcement activity.
- Common targets: unfair contract terms in T&Cs, misleading marketing claims, failure to honour cooling-off rights, and inadequate product safety monitoring.

---

## 8. High-risk flag checklist

| Flag | Why high-risk | What to check |
|---|---|---|
| **CPA strict product liability (s61)** | Strict no-fault liability. Cannot contract out (s51). Joint and several across supply chain. | Does product qualify as "goods"? Adequate warnings/instructions? Safety monitoring (s60) in place? Insurance clear for software liability? |
| **Unfair contract terms (s48-52)** | NCC can declare terms void. 62+ compliance notices issued 2025-26. US/EU template imports frequently violate CPA. | Overbroad liability exclusions? One-sided termination? Unfair auto-renewal? Hidden fee changes? Dense legalese violating s22? |
| **Product safety monitoring gap (s60)** | Delayed remediation + knowledge = aggravated liability. Class-style exposure for mass-market tech. | Safety monitoring process? Recall procedure? Post-sale notices reaching users? Upstream supplier obligations? |
