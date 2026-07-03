# Demands and Settlement — South African Framework

This overlay covers SA letters of demand, mora, without-prejudice rules, and settlement communication. Loaded by demand-draft, demand-intake, and demand-received when jurisdiction = ZA.

---

## 1. Letter of demand (interpellatio)

In SA law, a letter of demand is not just a strategic tool — it can be a **legal prerequisite** to completing a cause of action.

### When a demand is required

- **Mora ex persona (default by demand):** Where the contract does not specify a fixed due date for performance, the debtor must be placed in mora by a demand (interpellatio). Without the demand, the cause of action may be incomplete and summons premature.
- **Mora ex re (automatic default):** Where the contract sets a fixed due date and time is of the essence, default occurs automatically on non-performance. No demand is required, but one is still good practice.

### Legal consequences of a demand

1. **Places debtor in mora** — completes the cause of action (if mora ex persona)
2. **Starts running of interest** as damages for late performance (mora interest). Where no contractual rate applies, mora and judgment interest run at the statutory prescribed rate (repo + 3.5%; currently 10.25% p.a. from 1 March 2026) — see `statutes/prescribed-rate-of-interest.yaml` for the current rate and the historical rate path for interest that began running earlier
3. **Evidence of notice** — demonstrates the creditor attempted amicable resolution
4. **Prescription awareness** — the demand date is relevant to prescription analysis (though the demand itself does not interrupt prescription — only service of process does under s15)

### Formal requirements

No rigid statutory form for most demands, but best practice:

| Element | Required content |
|---|---|
| Parties | Creditor and debtor clearly identified (names, addresses, contract reference) |
| Cause of action | Concise description of the legal basis, obligation, relevant dates and amounts |
| Demand | Clear demand for specific performance or payment, with a time period to comply (typically 7-14 days) |
| Consequences | That legal proceedings will or may be instituted without further notice |
| Costs | Demand for costs of the letter (recoverable on taxation in many cases) |
| Banking details | For payment demands |

### Special statutory requirements

- **Organs of state:** Institution of Legal Proceedings Against Organs of State Act — 6-month written notice with prescribed content before suing (s3)
- **National Credit Act:** Specific notice requirements before debt enforcement
- **Consumer Protection Act:** Notice requirements for certain consumer disputes

---

## 2. Without-prejudice communications

### SA common-law rule

Communications genuinely aimed at settlement are privileged from being tendered in evidence to prove admissions. This is a **common-law rule**, not a statutory rule like US FRE 408.

### Key principles

| Principle | SA position |
|---|---|
| Source | Common law (confirmed in Civil Proceedings Evidence Act s21) |
| Label | "Without prejudice" label creates a **rebuttable presumption** of settlement intent, but is not decisive — court examines purpose and context |
| Scope | Covers communications genuinely aimed at settlement — not communications that merely carry the label |
| Waiver | Can be waived by agreement; may be waived impliedly by conduct |
| Exceptions | Without-prejudice communications may be used to prove that a settlement was concluded, or on the issue of costs |

### Open vs without-prejudice

| Type | Effect | When to use |
|---|---|---|
| **Open letter** | Admissible in evidence. Admissions and positions stated can be used against the writer in court. | When you want the court to see the demand (e.g., to prove notice, mora, refusal to pay) |
| **Without prejudice** | Privileged from admission into evidence to prove admissions. | When making a settlement offer or inviting compromise — protects admissions made in the course of negotiation |
| **Without prejudice save as to costs** | Privileged on the merits, but may be disclosed on the issue of costs. | Calderbank-style offer: if the recipient rejects and achieves a worse result at trial, the court may penalise them on costs |

### Skill impact

- **demand-draft:** Toggle between open and without-prejudice marking. Default for pure payment demands: open (to prove mora and notice). Default for settlement offers: without prejudice.
- **demand-received:** Assess whether the incoming demand is open or WP. If WP, note that admissions cannot be used in evidence.
- **demand-intake:** Capture the intended marking and explain the consequences.

---

## 3. Prescription and demands

A letter of demand **does not interrupt prescription**. Only service of process interrupts prescription (Prescription Act s15).

However, demands are relevant to prescription analysis because:
- The demand date may establish when the creditor first knew about the claim (s12(3) knowledge)
- An acknowledgement of liability in response to a demand interrupts prescription (s14)
- The demand establishes the date the debtor was placed in mora, which may be relevant to when the cause of action was complete

**Critical point:** Do not rely on a demand letter to "stop the clock" on prescription. Only service of summons (or equivalent process) interrupts prescription.
