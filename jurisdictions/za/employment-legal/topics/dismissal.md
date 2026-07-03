# Dismissal — South African Framework

This overlay covers the full South African dismissal framework under the Labour Relations Act 66 of 1995 (LRA) and the Basic Conditions of Employment Act 75 of 1997 (BCEA). It is loaded by termination-review, policy-drafting, and handbook-updates skills when jurisdiction = ZA.

---

## 1. Statutory framework

South African law does not recognise the concept of termination without cause. Every dismissal must satisfy two independent requirements (LRA s188):

1. **Substantive fairness** — the employer must have a fair reason for dismissal, falling into one of three recognised categories:
   - Misconduct
   - Incapacity (poor performance, ill health, or injury)
   - Operational requirements (retrenchment)

2. **Procedural fairness** — the employer must follow a fair procedure before dismissing, with the specific procedure depending on the category of dismissal. The **2025 Code of Good Practice: Dismissal** provides detailed guidance.

> **Governing Code — temporal note.** The **Code of Good Practice: Dismissal** published in Government Gazette 53294 (GenN 3470, 4 September 2025) is the current Code. It repealed and replaced **both** the old Schedule 8 Code of Good Practice: Dismissal **and** the 1999 Code of Good Practice on Dismissal Based on Operational Requirements, consolidating misconduct, incapacity, poor performance, probation and operational-requirements dismissals into one instrument (see `jurisdictions/za/statutes/lra.yaml` → `dismissal_code`). Headline shifts from the old Code: it recognises **incompatibility** as an incapacity ground; permits **simpler, less rigid procedures for small employers** where basic fairness is observed; does **not** mandate a formal disciplinary hearing (the requirement is a reasonable opportunity to respond to the allegations); frames **probation** around performance *and* suitability; and accepts that a prior warning is not always required (e.g. for senior or highly skilled employees). **Historical carve-out:** a dismissal *effected before 4 September 2025* is assessed under the **old Schedule 8 Code** in force at the time — for those matters the Schedule 8 item references below still apply.

> **Verification caveat:** *The procedural detail below reflects the 2025 Code as reported in professional commentary — verify against the gazetted Code text (GenN 3470, GG 53294) before advising.*

### Consequences of unfair dismissal

| Type | Remedy | Maximum compensation |
|---|---|---|
| Substantively or procedurally unfair dismissal | Reinstatement, re-employment, or compensation | Up to 12 months' remuneration (LRA s194(1)) |
| Automatically unfair dismissal (LRA s187) | Reinstatement, re-employment, or compensation | Up to 24 months' remuneration (LRA s194(3)) |

The Labour Court or CCMA arbitrator determines the appropriate remedy. Reinstatement is the primary remedy; compensation is awarded when reinstatement is not practicable or the employment relationship has broken down.

---

## 2. Types of dismissal

### 2.1 Misconduct (2025 Code; formerly Schedule 8 Items 3–4)

#### Substantive fairness

All four elements must be established:

1. **Valid rule or standard** — a rule or standard existed in the workplace regulating conduct.
2. **Awareness** — the employee was aware, or could reasonably have been expected to be aware, of the rule or standard.
3. **Consistent application** — the rule or standard has been consistently applied across the workplace. Inconsistent treatment undermines the employer's case.
4. **Appropriate sanction** — dismissal is an appropriate sanction for the contravention, considering the gravity of the misconduct, the employee's circumstances (length of service, disciplinary record, personal circumstances), and any mitigating factors.

Progressive discipline is the norm under the 2025 Code (formerly Schedule 8 Item 3(4)). Dismissal for a first offence is appropriate only where the misconduct is so serious that it makes a continued employment relationship intolerable — typically involving dishonesty, gross insubordination, gross negligence, or conduct endangering safety. The 2025 Code confirms that a prior warning is not invariably required before dismissal (for example for senior or highly skilled employees who should need no warning).

#### Procedural fairness

The employer must follow a fair procedure before dismissing for misconduct (2025 Code; formerly Schedule 8 Item 4):

1. **Notify the employee** of the allegations in sufficient detail to allow a meaningful response.
2. **Allow reasonable time to prepare** a response to the allegations.
3. **Allow representation** — the employee is entitled to be assisted by a trade union representative or fellow employee.
4. **Give an opportunity to respond** — the employee must be given a genuine opportunity to state a case, call witnesses, and challenge evidence. **Under the 2025 Code a formal, court-like disciplinary hearing is not mandatory**: the essential requirement is a reasonable opportunity to respond to the allegations before a decision is taken, and the process may be less rigid for small employers provided basic fairness is observed.
5. **Communicate the decision** — the employer must communicate the decision in writing, with reasons.
6. **Inform of rights** — the employee must be informed of the right to refer the dispute to the CCMA or a bargaining council within 30 days (LRA s191).

The procedure need not be as formal as court proceedings, but must give the employee a fair opportunity to be heard.

### 2.2 Incapacity — poor performance (2025 Code; formerly Schedule 8 Items 8–9)

Poor performance dismissal requires the employer to demonstrate:

1. **Standard communicated** — the required performance standard was brought to the employee's attention and is objectively reasonable.
2. **Opportunity given** — the employee was given a fair opportunity to meet the standard.
3. **Evaluation, training, and counselling** — the employer evaluated the employee's performance, provided appropriate training or instruction, and counselled the employee regarding the shortfall.
4. **Reasonable period for improvement** — the employee was allowed a reasonable period to improve after being informed of the deficiency.

The purpose of the process is remedial, not punitive. If the employee fails to improve after being given a genuine opportunity, dismissal may be substantively fair.

#### Procedure

The procedure mirrors the misconduct hearing in general terms, but the focus is on establishing whether the employee was given a fair opportunity to improve, not on fault or blame. The hearing must address:

- The nature of the performance shortfall
- Whether the employee was aware of the required standard
- What support was provided
- Whether a reasonable period for improvement was given
- Whether dismissal is the appropriate step (as opposed to demotion or transfer)

### 2.3 Probation (2025 Code; formerly Schedule 8 Item 8)

Probation is **not** a free pass to dismiss without process. The 2025 Code (see `jurisdictions/za/statutes/lra.yaml` → `probation_2025`) frames probation around both **performance and suitability for employment** and requires:

1. **Purpose of probation** — probation is a trial period to allow the employer to assess whether the employee is suitable for the position, on both performance and broader suitability grounds.
2. **Evaluation** — the employer must evaluate the employee's performance during probation.
3. **Guidance and counselling** — the employer must provide reasonable guidance, instruction, training, and counselling to assist the employee in meeting the required standard.
4. **Consider extension** — before dismissing, the employer should consider extending the probationary period if there is a reasonable prospect that the employee will improve.

The procedure for dismissal during probation may be less formal than for a permanent employee, but it must still be fair. The employer must:
- Inform the employee of the performance shortfall
- Give the employee an opportunity to respond
- Consider alternatives to dismissal (extension, transfer)
- Communicate the decision

### 2.4 Incapacity — ill health or injury and incompatibility (2025 Code; formerly Schedule 8 Items 10–11)

The 2025 Code expressly recognises **incompatibility** — an employee's demonstrated inability to work in harmony with colleagues or within the workplace culture — as a further **incapacity** ground for dismissal, distinct from misconduct and requiring its own fair, remedial process.

Before dismissing for ill health or injury, the employer must:

1. **Establish the degree and duration** — investigate the degree of incapacity, the likely duration, and the possibility of recovery or treatment.
2. **Investigate alternative employment** — consider whether the employee can be accommodated in an alternative position or with adapted duties.
3. **Consider length of service** — the employee's length of service and the nature of the employment relationship are relevant factors.
4. **Consult the employee** — the employee must be given an opportunity to state a case and to be assisted by a representative.

Where the incapacity arises from an occupational injury or disease, the Compensation for Occupational Injuries and Diseases Act 130 of 1993 (COIDA) may apply, and the employee may be entitled to compensation irrespective of dismissal.

### 2.5 Operational requirements / retrenchment (LRA s189, s189A)

Dismissal for operational requirements (retrenchment) covers economic, technological, structural, or similar needs of the employer. The process is heavily regulated.

#### s189 consultation (all employers)

The employer must engage in a meaningful joint consensus-seeking process:

1. **Written notice** — issue a written notice to consulting parties (employees, trade unions, or workplace forums) of the contemplated dismissals.
2. **Disclose information** — the notice must disclose:
   - Reasons for the proposed dismissals
   - Alternatives considered and why they were rejected
   - Number of employees likely affected and job categories
   - Proposed selection criteria
   - Proposed timing of dismissals
   - Proposed severance pay
   - Any assistance the employer proposes (e.g., outplacement)
3. **Meaningful consultation** — the employer must allow the consulting party an opportunity to make representations about any of the disclosed matters, and must consider and respond to those representations. This is not a tick-box exercise — the consultation must be genuine and substantive.
4. **Selection criteria** — must be fair and objective. Last In, First Out (LIFO) is common and generally accepted, but not mandatory. Criteria may include length of service, skills, qualifications, and performance, but must not discriminate on prohibited grounds.
5. **Severance pay** — at least 1 week's remuneration for each completed year of continuous service (LRA s41(2)).

#### s189A large-scale retrenchments

Section 189A applies when the employer employs 50 or more employees **and** the number of employees to be dismissed meets the applicable threshold:

| Employer size (total employees) | Dismissal threshold |
|---|---|
| 50–200 | 10 or more employees |
| 201–300 | 20 or more employees |
| 301–400 | 30 or more employees |
| 401–500 | 40 or more employees |
| 501+ | 50 or more employees |

Additional requirements under s189A:

- **Facilitator** — either party may request the CCMA to appoint a facilitator to assist with the consultation process.
- **60-day minimum consultation** — the consultation period must be at least 60 days from the date the notice under s189(3) is given (unless the facilitator permits a shorter period).
- **Strike or lockout** — if the consultation fails, the employees may strike or the employer may lock out, subject to the dispute resolution provisions of the LRA.
- **Labour Court application** — employees may apply to the Labour Court to challenge the substantive or procedural fairness of the dismissal.

---

## 3. CCMA dispute resolution

### Referral

An employee who claims to have been unfairly dismissed must refer the dispute to the CCMA (or the relevant bargaining council, if one has jurisdiction) within **30 days** of the date of dismissal (LRA s191(1)).

Late referrals may be condoned if the employee shows good cause for the delay.

### Conciliation

The CCMA must attempt to resolve the dispute through conciliation within **30 days** of the referral (LRA s191(5)). The commissioner issues a certificate stating whether or not the dispute was resolved.

### After conciliation fails

If conciliation fails, the next step depends on the type of dispute:

| Dispute type | Forum | Timeframe |
|---|---|---|
| Misconduct or incapacity (below earnings threshold) | CCMA arbitration | Within 90 days of certificate |
| Automatically unfair dismissal (LRA s187) | Labour Court | Within 90 days of certificate |
| Operational requirements (LRA s189) | Labour Court | Within 90 days of certificate |
| Misconduct or incapacity (above earnings threshold) | Labour Court | Within 90 days of certificate |

### Con-arb

For dismissal disputes involving conduct or capacity of employees below the BCEA earnings threshold (read `jurisdictions/za/statutes/bcea.yaml` → `earnings_threshold` for the current figure), the CCMA may use **con-arb** — a combined conciliation-arbitration process where the matter proceeds directly to arbitration on the same day if conciliation fails (LRA s191(5A)).

---

## 4. High-risk termination flags

The following table identifies 11 high-risk indicators that should be assessed in every termination review. Any flag that triggers requires closer examination and may indicate exposure to an unfair dismissal finding.

| # | Flag | Why it's high-risk | Check |
|---|---|---|---|
| 1 | No opportunity to respond | Procedural unfairness — the 2025 Code requires a genuine opportunity to respond before dismissal for misconduct or incapacity (a formal hearing is not mandatory, but the employee must be heard) | Was the employee notified of the allegations and given adequate notice, time to prepare, the right to representation, and a real chance to respond? |
| 2 | Automatically unfair ground | LRA s187 — dismissal for a reason listed in s187 is automatically unfair and attracts up to 24 months' compensation | Is the dismissal connected to pregnancy, union activity, protected disclosure, exercise of a right under the LRA, or refusal to do a striker's work? |
| 3 | Discrimination / EEA-protected ground | LRA s187(1)(f) read with EEA — dismissal that constitutes unfair discrimination is automatically unfair | Is the dismissal connected to race, gender, sex, pregnancy, marital status, family responsibility, ethnic or social origin, colour, sexual orientation, age, disability, religion, HIV status, conscience, belief, political opinion, culture, language, birth, or any other EEA-listed ground? |
| 4 | Protected disclosure | Protected Disclosures Act 26 of 2000 — dismissal of an employee who made a protected disclosure is automatically unfair (LRA s187(1)(h)) | Has the employee made a protected disclosure to the employer, a legal adviser, a regulatory body, or the media in accordance with the Act? |
| 5 | Recent CCMA/union activity | LRA s187(1)(d) — dismissal for participating in lawful union activities or exercising rights under the LRA is automatically unfair | Has the employee recently referred a dispute to the CCMA, participated in union activity, acted as a shop steward, or participated in a lawful strike? |
| 6 | Operational requirements without s189 process | LRA s189 imposes mandatory consultation procedures; failure to follow them renders the dismissal procedurally unfair | Has the full s189 consultation process been followed? **Sub-check:** does the employer fall into s189A territory (50+ employees and above the applicable threshold)? |
| 7 | Probation without Code compliance | 2025 Code of Good Practice: Dismissal (probation item; formerly Schedule 8 Item 8) — probation does not remove the requirement for fair process | Is the employee on probation? Was evaluation, guidance, and counselling provided? Was extension of probation considered before dismissal? |
| 8 | Fixed-term — reasonable expectation | LRA s186(1)(b) — failure to renew a fixed-term contract where the employee had a reasonable expectation of renewal is treated as a dismissal | Is the employee on a fixed-term contract? Do prior renewals, employer conduct, or representations create a reasonable expectation of renewal? |
| 9 | Earnings below BCEA threshold | Employees below the BCEA earnings threshold (read `jurisdictions/za/statutes/bcea.yaml` → `earnings_threshold` for the current figure) receive full BCEA protections; adverse employment actions attract higher scrutiny | Does the employee earn below the threshold? Are full working-time protections (ordinary hours, overtime, meal intervals) being observed? |
| 10 | Thin documentation | The "why now?" problem — absence of a progressive discipline trail makes the employer's case difficult to sustain at the CCMA | Is there a progressive discipline record? Written warnings? Performance improvement plan? Was the employee given an opportunity to improve before dismissal? |
| 11 | Comparator problem / inconsistent discipline | Inconsistent application of disciplinary standards undermines the employer's substantive fairness case at the CCMA | Has another employee committed the same or similar misconduct and not been dismissed? Has the disciplinary code been applied consistently across the workforce? |

---

## 5. Notice periods

Minimum notice periods are prescribed by BCEA s37(1):

| Length of service | Minimum notice |
|---|---|
| 6 months or less | 1 week |
| More than 6 months but not more than 1 year | 2 weeks |
| More than 1 year | 4 weeks |

Additional rules:

- **Written notice** — notice of termination must be given in writing (BCEA s37(4)), except where the employee is illiterate and the notice is given by that employee.
- **Payment in lieu** — an employer may pay the employee in lieu of notice, equivalent to the remuneration the employee would have received during the notice period. The contract of employment may also provide for payment in lieu.
- **Contractual notice** — the contract may stipulate a longer notice period than the statutory minimum, and many senior employment contracts do. The contractual period applies if it exceeds the statutory minimum.
- **No notice for summary dismissal** — where the employee is guilty of conduct so serious that it would be unreasonable to require the employer to continue the employment relationship during the notice period, the employer may dismiss summarily. This does not remove the requirement for a fair hearing.

---

## 6. Severance pay

Severance pay is prescribed for **operational requirements dismissals only** (LRA s41(2)):

- **Amount:** at least 1 week's remuneration for each completed year of continuous service with the employer.
- **Forfeiture:** an employee who unreasonably refuses alternative employment offered by the employer or any other employer is not entitled to severance pay (LRA s41(4)).

Severance pay is **not** customarily payable for dismissals based on misconduct or incapacity. However, the contract of employment or a collective agreement may provide for additional payments.

### Tax treatment

Severance pay received on retrenchment qualifies for favourable tax treatment under the Income Tax Act. The first R500,000 (subject to a cumulative lifetime cap) is tax-free, with the balance taxed on a sliding scale. This applies only to retrenchment as defined in the Income Tax Act — not to resignation or dismissal for misconduct.
