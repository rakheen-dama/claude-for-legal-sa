# Fintech and Credit — South African Framework

This overlay covers the National Credit Act 34 of 2005 (NCA), Financial Intelligence Centre Act 38 of 2001 (FICA), and related financial sector regulation as it applies to product-legal workflows for fintech features. It is conditionally loaded by launch-review (fintech sector), feature-risk-assessment, and is-this-a-problem skills when jurisdiction = ZA and product touches fintech.

---

## 1. Is this credit? (NCA applicability)

The NCA has a broad definition of "credit agreement" that captures many product features not traditionally considered credit. A product feature constitutes credit if it involves:

- **Deferred payment** — the consumer receives goods or services now and pays later, including instalment sales (s1 "instalment agreement") and any arrangement where payment is deferred beyond the time of delivery.
- **Fees contingent on time** — any charge that accrues over time on an outstanding amount, including interest, service fees, and administration fees.
- **Lending** — any arrangement where money is advanced to the consumer, including personal loans, overdrafts, and revolving credit facilities.

### Common product features that may be credit

| Feature | Likely credit? | NCA provision | Notes |
|---|---|---|---|
| **BNPL (buy now, pay later)** | Yes — unless genuinely interest-free and fee-free with no penalty for late payment | Instalment agreement (s1) or credit facility (s1) | Many BNPL products charge late fees or service fees, bringing them within the NCA |
| **Salary advance / earned wage access** | Likely yes — if a fee or interest is charged | Credit facility or short-term credit (s1) | The fee structure determines classification |
| **Revolving credit / wallet with credit line** | Yes | Credit facility (s1) | Requires credit provider registration |
| **Subscription with deferred billing** | Generally no — if payment is for services to be rendered, not a loan | — | But if the consumer can consume services before payment is due with fees for late payment, reassess |
| **Invoice financing / merchant cash advance** | Depends on structure | May be credit agreement or excluded | Complex — requires specific legal analysis |
| **Lay-by** | No — CPA s62 governs lay-by, not NCA | CPA s62 | Consumer pays before receiving goods |

### Registration requirement (NCA s40)

No person may carry on the business of a credit provider unless registered with the National Credit Regulator (NCR). Operating as an unregistered credit provider is a criminal offence and renders agreements void.

---

## 2. Credit marketing obligations (NCA s74-76)

### Required disclosures in credit advertising

Any advertisement that includes specific credit terms must disclose:

- **Annual percentage rate (APR)** — the total cost of credit expressed as a percentage, calculated in accordance with NCA regulations.
- **All fees and charges** — initiation fees, monthly service fees, credit life insurance premiums, and any other charges.
- **Total cost of credit** — the total amount the consumer will pay over the full term of the agreement, including all interest, fees, and compulsory insurance.
- **Repayment terms** — instalment amount, frequency, and duration.

### Misleading credit advertising prohibition

NCA s76 prohibits advertising that is misleading or deceptive in respect of credit. Specific prohibitions:

- Advertising "0% interest" when fees, service charges, or compulsory insurance increase the effective cost of credit.
- Stating a monthly instalment without disclosing the total cost, APR, and term.
- Advertising credit availability without disclosing that the consumer must qualify through an affordability assessment.
- Using "pre-approved" language that implies guaranteed access to credit.

---

## 3. Reckless credit (NCA s80-81)

### Affordability assessment requirement

Before entering into a credit agreement, a credit provider must conduct a reasonable assessment of the consumer's:

1. **Financial means, prospects, and obligations** — current income, expenses, existing debt commitments, and expected future income.
2. **Understanding of the risks and costs** — the consumer must understand the nature, terms, and consequences of the agreement.
3. **Debt repayment history** — the credit provider must consult a credit bureau.

### Consequences of reckless credit

If a court or Tribunal finds that a credit agreement was granted recklessly (NCA s83):

- The agreement may be declared void from inception.
- The consumer's obligations may be suspended.
- The credit provider loses the right to enforce the agreement, including recovering the capital advanced.
- The credit provider may be ordered to refund amounts already paid by the consumer.

### Impact on BNPL and fintech

Products that extend credit without conducting affordability assessments face severe consequences. The "it's not really credit" argument is not a defence if the product functionally meets the NCA definition. NCR enforcement actions against online lenders and micro-credit providers have increased since 2024.

---

## 4. FICA obligations

### Accountable institutions (Schedule 1)

The following entities are accountable institutions under FICA and must comply with KYC/CDD requirements:

- Banks and mutual banks.
- Financial services providers (authorised under FAIS).
- Persons who carry on the business of dealing in foreign exchange.
- Persons who carry on the business of lending money or providing credit.
- Persons who carry on the business of a money remitter.

If a fintech product involves any of these activities, the operating entity is likely an accountable institution.

### KYC and customer due diligence (CDD)

Accountable institutions must:

1. **Verify identity** before establishing a business relationship — acceptable identification (SA ID, passport, or temporary residence permit).
2. **Verify address** — utility bill, bank statement, or other proof of residential address (not older than 3 months).
3. **Screen against sanctions lists** — UN, SARB Targeted Financial Sanctions list.
4. **Ongoing monitoring** — transaction monitoring for suspicious or unusual activity.
5. **Record-keeping** — maintain records of identity verification and transactions for at least 5 years.

### Suspicious transaction reporting

Accountable institutions must file suspicious transaction reports (STRs) with the Financial Intelligence Centre:

- **Section 29** — cash transactions above the prescribed threshold (currently R24 999.99).
- **Section 29** — suspicious or unusual transactions regardless of amount.
- Failure to report is a criminal offence.

### Product onboarding design implications

Fintech product onboarding flows must integrate FICA requirements:

- Identity verification step before account activation (for accountable institutions).
- Address verification step or risk-based approach to ongoing verification.
- Sanctions screening at onboarding and periodically.
- Transaction monitoring capabilities from launch.

---

## 5. Stored value and payment systems

### Banks Act 94/1990 — deposit-taking

The Banks Act prohibits any person from accepting deposits from the public unless registered as a bank. A stored-value product (wallet, prepaid account) may constitute deposit-taking if:

- Funds are accepted from users and held in an account controlled by the product provider.
- Users can store value for future use (not immediately applied to a specific purchase).
- The product provider has an obligation to return funds on demand.

SARB has issued guidance on e-money and stored-value products. Products that meet the deposit-taking definition require either a banking licence or operation through a registered bank partner.

### National Payment System Act 78/1998 (NPS Act)

The NPS Act regulates payment systems and settlement systems. A fintech product that facilitates the transfer of funds between parties may be operating a payment system requiring:

- Designation by SARB as a payment system operator, or
- Operation under an existing designated payment system (e.g., BankservAfrica, Visa, Mastercard), or
- Exemption from SARB.

### When does a wallet need a banking licence?

| Feature | Likely regulated? | Applicable regime |
|---|---|---|
| Wallet with stored funds, withdraw on demand | Yes — deposit-taking | Banks Act — banking licence or bank partner |
| Prepaid voucher for specific merchant | Less likely — limited purpose | May be exempt; assess on facts |
| Pass-through payment (funds not held) | Payment system, not deposit-taking | NPS Act — payment system designation or exemption |
| Crypto wallet (custody of crypto assets) | Emerging regulation | FSCA declaration of crypto as financial product (2022); FAIS licensing |

---

## 6. High-risk flag checklist

| Flag | Why high-risk | What to check |
|---|---|---|
| **NCA credit marketing violations (fintech)** | Agreements declared void. BNPL may be regulated credit without registration. | Product functionally credit? Registered credit provider? APR/fees/total cost displayed? Pre-agreement disclosures? Affordability assessment? |
