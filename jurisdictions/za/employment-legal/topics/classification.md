# Classification — BCEA s213, Control Test, Deemed Employees

South African overlay for worker classification skills. Covers the statutory definition of employee, the presumption of employment, the common law dominant impression test, deemed employees under TES/labour broker provisions, and a practical classification review checklist.

---

## Statutory definition of employee

### BCEA s213 / LRA s213

Both the Basic Conditions of Employment Act 75 of 1997 (s213) and the Labour Relations Act 66 of 1995 (s213) define "employee" as:

> (a) any person, excluding an independent contractor, who works for another person or for the State and who receives, or is entitled to receive, any remuneration; and
>
> (b) any other person who in any manner assists in carrying on or conducting the business of an employer.

The definition explicitly **excludes independent contractors**. The question in disputed cases is whether a person is truly an independent contractor or is in substance an employee regardless of the label the parties have used. South African law applies the **substance over form** principle — the label in the contract does not determine the true nature of the relationship.

---

## Presumption of employment (LRA s200A / BCEA s83A)

### Applicability

The presumption applies to persons earning **below the BCEA earnings threshold** (read `jurisdictions/za/statutes/bcea.yaml` → `earnings_threshold` for the current figure). Persons earning above the threshold are not excluded from being employees; the presumption simply does not assist them, and the common law test applies directly.

### The seven factors

A person who works for or renders services to another person is **presumed to be an employee** if any one or more of the following factors are present, regardless of the form of the contract:

| Factor | Indicator of employment |
|---|---|
| **(a)** Manner of work is subject to the control or direction of the other person | The principal dictates how, when, and where the work is done |
| **(b)** Hours of work are subject to the control or direction of the other person | The principal sets the schedule |
| **(c)** Forms part of the organisation of the other person | The worker is integrated into the business, not running a separate enterprise |
| **(d)** Has worked for the other person for an average of at least 40 hours per month over the last 3 months | Sustained, regular engagement — not ad hoc |
| **(e)** Economically dependent on the other person | The worker relies on the principal for the majority of income |
| **(f)** Provided with tools of trade or work equipment by the other person | The principal supplies what is needed to do the work |
| **(g)** Only works for or renders services to one person | Exclusivity — not operating an independent business serving multiple clients |

### Burden of proof

Once any one factor is established, the **burden shifts to the employer** to prove that the person is not an employee. The employer must rebut the presumption on a balance of probabilities.

---

## Common law dominant impression test

### Multi-factor analysis

For persons earning above the BCEA threshold, or where the statutory presumption is rebutted, the common law test applies. The leading authority is *SABC v McKenzie* (1999) 1 BLLR 1 (LAC), which endorsed the **dominant impression** approach — no single factor is decisive; the court assesses the totality of the relationship.

| Factor | Employee signal | Independent contractor signal |
|---|---|---|
| **Control** — does the principal control how the work is done, not just the result? | Principal directs methods, sequence, and manner of work | Worker determines own methods; principal specifies outcome only |
| **Integration** — is the worker part of the organisation? | Worker is part of the business structure, has a role title, attends meetings, reports to a manager | Worker operates separately, has own business identity |
| **Economic dependence** — is the worker dependent on a single principal? | Single source of income, no other clients | Multiple clients, bears own business risk |
| **Tools and equipment** — who provides them? | Principal provides tools, equipment, software, workspace | Worker provides own tools and equipment |
| **Profit and loss risk** — can the worker profit or lose beyond the fee? | Fixed salary, no risk of loss | Can make or lose money on the engagement |
| **Right to delegate** — can the worker send a substitute? | Must perform personally | Can delegate or subcontract |
| **Exclusivity** — does the worker serve only one principal? | Exclusive engagement | Serves multiple clients |
| **Tax and benefits** — how is the worker treated for tax and benefits? | PAYE deducted, UIF contributions, benefits provided | Worker invoices, handles own tax (provisional taxpayer), no employer benefits |

### Substance over form

The courts have repeatedly confirmed that the label the parties attach to the relationship is not determinative. In *Denel (Pty) Ltd v Gerber* (2005) 9 BLLR 849 (LAC), the Labour Appeal Court held that the court must examine the reality of the relationship, not the contractual label. A contract describing the person as an "independent contractor" does not prevent a finding of employment if the substance of the arrangement indicates otherwise.

---

## Deemed employees — TES / labour broker provisions (LRA s198A)

### Temporary Employment Services (TES) / labour brokers

A TES (commonly called a labour broker) is defined in LRA s198(1) as any person who, for reward, procures for or provides to a client other persons who perform work for the client, and who are remunerated by the TES.

### The three-month trigger (LRA s198A(3))

For employees earning **below the BCEA earnings threshold**:

- An employee placed by a TES with a client who performs work for that client for a period **exceeding three months** is **deemed to be the employee of the client** (not the TES) and is employed on an indefinite basis.
- The three-month period runs from the date the employee commences work for the client.

### Above-threshold workers

Workers earning **above the BCEA earnings threshold** are not covered by s198A. They remain employees of the TES.

### Consequences of deemed employment

| Consequence | Detail |
|---|---|
| **Client becomes employer** | The client is the deemed employer for purposes of the LRA and BCEA |
| **Joint and several liability** | The TES and the client are jointly and severally liable for contraventions of employment laws, collective agreements, and arbitration awards (LRA s198(4)) |
| **Equal treatment** | The deemed employee is entitled to conditions of employment that are on the whole not less favourable than those of directly employed employees performing the same or similar work (LRA s198A(5)) |
| **Unfair dismissal protection** | If the client terminates the placement, this may constitute a dismissal — the deemed employee has recourse to the CCMA |

### Justifiable reasons for fixed-term TES placement

Section 198B provides that a fixed-term contract (or TES placement) beyond three months is permissible only if there is a justifiable reason, including:

- Replacing a temporarily absent employee.
- A temporary increase in the volume of work.
- A student or recent graduate employed for work experience.
- A fixed project with a defined end.
- Seasonal work.
- A non-citizen with a work permit for a defined period.
- An official public works or similar public job creation scheme.
- A position funded by an external source for a limited period.

### TES compliance flags

| Flag | Risk | Action |
|---|---|---|
| TES worker placed for more than 3 months, earning below threshold | Deemed employment has triggered — client is the employer | Assess whether to formalise direct employment or ensure equal treatment |
| Client exercises day-to-day control over TES worker | Strengthens deemed employment, increases client liability | Review operational control arrangements |
| TES worker paid less than direct employees doing similar work | Contravention of s198A(5) equal treatment | Equalise conditions or justify the differential |
| No justifiable reason for fixed-term TES engagement beyond 3 months | Worker may claim indefinite employment | Document the justifiable reason per s198B |

---

## Classification review checklist

Apply the following steps in order to classify a worker in South Africa:

### Step 1: Earnings check

- What is the worker's annualised earnings?
- Is the worker above or below the current BCEA earnings threshold (read `jurisdictions/za/statutes/bcea.yaml` → `earnings_threshold` for the current figure)?

### Step 2: Statutory presumption (s200A)

*Applies only to below-threshold workers.*

- Does any one of the seven s200A factors apply?
- If yes: the worker is **presumed to be an employee**. Can the employer rebut the presumption?

### Step 3: Dominant impression test

*Applies to all workers, but is the primary test for above-threshold workers.*

- Apply the multi-factor table above.
- What is the dominant impression — employee or independent contractor?
- Is the substance of the relationship consistent with the contractual label?

### Step 4: TES / labour broker check

- Is a TES or labour broker involved in the arrangement?
- Has the worker been placed with the client for more than three months?
- Is the worker below the BCEA earnings threshold?
- If yes to all: deemed employment under s198A has likely triggered.

### Step 5: Substance over form

- Does the contractual label match the reality of the arrangement?
- Are there any indicators that the "independent contractor" label is being used to avoid statutory obligations?
- Would a CCMA commissioner, looking at the totality of the arrangement, conclude that this person is an employee?

### Classification summary table

| Classification | Tax treatment | Statutory protections | Key indicator |
|---|---|---|---|
| **Employee** | PAYE, UIF, SDL deducted by employer | Full LRA, BCEA, EEA, COIDA, UIA protections | Integrated into business, controlled by employer, economically dependent |
| **Independent contractor** | Worker handles own tax (provisional taxpayer), no UIF/SDL | Not covered by LRA, BCEA, EEA (unless misclassified) | Own business, multiple clients, controls own methods, bears profit/loss risk |
| **TES/labour broker employee** | TES deducts PAYE, UIF, SDL | Full protections; after 3 months (below threshold) deemed employed by client | Placed by TES, works for client, may trigger deemed employment |
