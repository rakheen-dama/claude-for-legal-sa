# Rule Status Verification — South African Framework

This overlay covers how to verify whether a South African regulation is currently in force and the mechanisms by which regulations can be invalidated, suspended, or amended. It is loaded by policy-diff, policy-redraft, and gap-surfacer skills when jurisdiction = ZA.

---

## 1. How SA regulations come into force

### Default rule

A regulation comes into force on the date of its publication in the Government Gazette unless the regulation or its enabling Act specifies otherwise.

### Commencement mechanisms

| Mechanism | Description | Example |
|---|---|---|
| Date of publication | In force immediately upon Gazette publication — the default | Most departmental regulations |
| Specified future date | The regulation states a specific commencement date | "This regulation comes into operation on 1 April 2026" |
| Presidential/ministerial proclamation | A separate commencement notice must be published in the Gazette | Common for Acts of Parliament — e.g., POPIA was assented to in 2013 but most provisions commenced only on 1 July 2020 by proclamation |
| Phased commencement | Different provisions commence on different dates | FSR Act 9/2017 — different chapters commenced on different dates between 2018 and 2021 |

### Tabling requirement

Some enabling Acts require that regulations be "tabled" in Parliament before taking effect. If Parliament rejects the regulations within the prescribed period (typically 30 sitting days), they lapse. This is uncommon but applies to certain financial sector and taxation regulations.

---

## 2. How SA regulations can be invalidated or suspended

### 2.1 PAJA s6 judicial review

The Promotion of Administrative Justice Act 3 of 2000 (PAJA) provides the primary mechanism for challenging administrative action, including the making of regulations. A court may review and set aside administrative action on the following grounds:

| Ground | PAJA reference | Description |
|---|---|---|
| Lack of authority | s6(2)(a)(i) | The administrator was not authorised by the empowering provision to take the action |
| Material error of law | s6(2)(b) | The action was materially influenced by an error of law |
| Procedural unfairness | s6(2)(c) | The action was procedurally unfair — includes failure to follow PAJA s4 public participation requirements |
| Material error of fact | s6(2)(d) | The action was materially influenced by an error of fact |
| Not rationally connected | s6(2)(e)(iii) | The action is not rationally connected to the purpose of the empowering provision or the purpose for which it was purportedly taken |
| Unconstitutional or unlawful | s6(2)(f)(i) | The action itself contravenes a law or is not authorised by the empowering provision |
| Unreasonable | s6(2)(h) | So unreasonable that no reasonable person could have taken that action |
| Catch-all | s6(2)(i) | Otherwise unconstitutional or unlawful |

### 2.2 PAJA s7 constraints on judicial review

| Constraint | PAJA reference | Detail |
|---|---|---|
| Time limit | s7(1) | Proceedings for judicial review must be instituted within 180 days of the date the person became aware of the action and the reasons for it, or might reasonably have been expected to become aware |
| Internal remedies | s7(2) | A court or tribunal may not review an administrative action unless any internal remedy provided by the empowering legislation has been exhausted — unless the court exempts the person on grounds of exceptional circumstances |

### 2.3 Constitutional Court review

The Constitutional Court may declare legislation or subordinate legislation constitutionally invalid under Constitution s172. A declaration of constitutional invalidity:

- May be suspended to allow Parliament or the relevant authority time to cure the defect
- May apply prospectively only, or may include retrospective effect
- Is binding on all courts and organs of state

### 2.4 Regulator withdrawal or amendment

A regulator can withdraw or amend its own regulations by publishing a new notice in the Government Gazette. The amending or revoking notice must be published with the same formality as the original.

### 2.5 Interim interdicts

A court may grant interim relief under PAJA s8(2) or under its inherent jurisdiction, suspending the operation of a regulation pending the outcome of judicial review. Requirements for an interim interdict:

- Prima facie right
- Reasonable apprehension of irreparable harm
- Balance of convenience favours the applicant
- No alternative remedy

---

## 3. Red flags that a regulation may not be in force

The following indicators should trigger verification before relying on a regulation:

| # | Red flag | Why it matters |
|---|---|---|
| 1 | Commencement date not yet reached | The regulation may have been gazetted but awaits a proclamation or future date to come into effect |
| 2 | Known PAJA s6 review proceedings pending | A court may set aside the regulation, potentially with retrospective effect |
| 3 | Constitutional Court challenge pending or decided | The regulation may have been declared constitutionally invalid |
| 4 | Regulator has published amendment or withdrawal notice | The regulation may have been superseded by a later Gazette notice |
| 5 | Regulation is older than 12 months with no confirmation of current status | Stale regulations may have been amended, withdrawn, or overtaken by subsequent instruments |
| 6 | Enabling Act not yet commenced | If the parent Act is not in force, regulations made under it may lack legal authority |
| 7 | Phased commencement — partial force | Some provisions may be in force while others are not yet commenced |
| 8 | Tabling requirement not confirmed | If the enabling Act requires parliamentary tabling, the regulation may have lapsed |

---

## 4. Verification steps

When a skill needs to confirm whether a South African regulation is currently in force, it must follow these steps in order:

### Step 1 — Check consolidated text

Query Laws.Africa or Sabinet for the current consolidated text of the regulation. If the regulation has been amended or repealed, the consolidated text will reflect this.

### Step 2 — Search for amendment or withdrawal notices

Search the Open Gazettes archive for any amendment, withdrawal, or commencement notices referencing the regulation's gazette number or title.

### Step 3 — Search for judicial challenge

Conduct a web search for any PAJA s6 review proceedings or Constitutional Court challenge involving the regulation. Check the Constitutional Court and Supreme Court of Appeal websites for relevant judgments.

### Step 4 — Check regulator website

Visit the publishing regulator's website for current status information, errata, corrections, or superseding instruments.

### Step 5 — Emit banner if unverified

If the regulation's status cannot be positively confirmed through steps 1–4, the skill must emit the following banner:

> ⚠️ RULE STATUS UNVERIFIED — I could not confirm this rule is currently in force. SA regulations may be subject to PAJA s6 judicial review, Constitutional Court challenge, or regulator withdrawal. Do not treat any compliance date below as binding until you confirm the rule's status via the Government Gazette, Laws.Africa, or with outside counsel.

Every due date associated with an unverified regulation must be tagged: `[due date per published rule — status unverified]`

---

## 5. Downstream effects of unverified status

When a regulation's status is `status_verified: false`, downstream skills must adjust their behaviour:

| Skill | Adjustment |
|---|---|
| gap-surfacer | Must NOT classify as 🔴 Overdue — use 🟡 "Review needed" and route to `watch` bucket |
| policy-redraft | Must emit the ⚠️ RULE STATUS UNVERIFIED banner in the output |
| policy-diff | Must note the unverified status in the comparison header |
| reg-feed-watcher | Must flag the item for manual review in the next digest |

The purpose of this protocol is to prevent false urgency from driving compliance decisions based on regulations that may not be enforceable.
