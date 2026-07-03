# Reviewer Guide — South African Legal Overlay

*For SA legal practitioners reviewing this system's South African content. No technical background required.*

---

## What is this system?

**Claude for Legal** is an AI assistant built by Anthropic for legal professionals. It works inside Claude (Anthropic's AI) as a set of **plugins** — one per practice area. Think of each plugin as a specialist colleague who knows your practice area's frameworks, checklists, and risk flags. A lawyer installs the plugin for their practice area, runs a short setup interview to teach it about their organisation, and then uses it day-to-day for reviews, drafting, triage, and tracking.

The system is not a chatbot that gives generic legal answers. It's a **structured assistant** that:
- Knows your organisation's playbook (escalation rules, risk appetite, review triggers)
- Runs checklists before concluding any review (so nothing gets missed)
- Cites its sources and flags when it's uncertain (every citation is tagged with where it came from)
- Produces draft work product for attorney review (it never files, sends, or acts on anything without a lawyer's sign-off)

**Every output is a draft for attorney review — not legal advice.** The system makes review faster; it does not replace it.

---

## The original system — built for US law

The base system has **12 practice-area plugins**, each with its own skills (specific tasks the assistant can do):

| Plugin | Practice area | Example tasks |
|---|---|---|
| **employment-legal** | Employment / labour law | Termination review, hiring review, worker classification, leave tracking, policy drafting, wage & hour Q&A |
| **commercial-legal** | Commercial contracts | Vendor agreement review, NDA triage, renewal tracking, SaaS MSA review, amendment tracing |
| **privacy-legal** | Privacy / data protection | DPA review, DSAR response, privacy impact assessments, regulatory gap analysis |
| **corporate-legal** | Corporate / M&A | Diligence review, disclosure schedules, board consents, entity compliance, closing checklists |
| **litigation-legal** | Litigation / disputes | Claim charts, chronologies, deposition prep, privilege logs, brief drafting |
| **product-legal** | Product counsel | Launch review, marketing claims checking, risk calibration |
| **regulatory-legal** | Regulatory compliance | Regulatory feed monitoring, policy diff, gap tracking |
| **ai-governance-legal** | AI governance | AI use-case triage, impact assessments, vendor AI review |
| **ip-legal** | Intellectual property | Trademark clearance, cease & desist, DMCA, OSS compliance |
| **employment-legal** | Employment law | Termination review, hiring review, worker classification |
| **law-student** | Legal education | Case briefing, Socratic drilling, bar prep, IRAC practice |
| **legal-clinic** | Legal clinics | Intake workflow, case assignment, deadline tracking |

All of these plugins were written with **US law** as the default — US statutes, US procedures, US risk flags, US terminology. When a plugin checks whether a termination is risky, it checks for FMLA retaliation, FLSA misclassification, and state-specific rules. When it reviews a contract, it thinks about UCC, Delaware law, and FRCP discovery rules.

**This is a problem for South African lawyers.** US defaults don't just fail to help — they actively mislead. At-will employment doesn't exist in SA. FMLA leave doesn't exist. The ABC test for worker classification doesn't apply. A South African lawyer following US-default guidance could face CCMA referrals, Labour Court claims, or regulatory penalties.

---

## What we've built — the South African layer

Instead of rewriting the entire system for SA, we've added a **South African overlay**. When a South African lawyer sets up a plugin, the system detects the SA jurisdiction and loads SA-specific content:

- **SA statutes** instead of US statutes (BCEA instead of FLSA, LRA instead of NLRA, POPIA instead of state privacy laws)
- **SA procedures** instead of US procedures (CCMA conciliation instead of EEOC charges, s189 consultation instead of WARN Act notice)
- **SA risk flags** instead of US risk flags (procedural fairness under the 2025 Code of Good Practice: Dismissal instead of at-will termination, dismissal-code compliance instead of FMLA interference)
- **SA privilege headers** instead of US headers ("legal professional privilege" instead of "attorney work product")

The US content stays intact underneath — it's not deleted or broken. The SA layer sits on top and activates when the user's jurisdiction is South Africa.

**Currently adapted for SA (9 practice areas — see [jurisdictions/za/README.md](README.md) for the full readiness matrix):**
- Employment law (complete — 7 skills adapted, 11 high-risk dismissal flags, 6 practice guides)
- Commercial law (complete — 5 skills adapted, 12 high-risk flags, 6 practice guides)
- Privacy / POPIA, Corporate, Litigation, IP, Product, Regulatory, Legal Clinic (each has a full ZA overlay: router, topic files, statute library, and ZA cold-start interview fork)

---

## How a lawyer actually uses this

Here's what the day-to-day experience looks like for an SA employment lawyer using the system:

**First-time setup (10 minutes):**
1. Install the employment-legal plugin
2. Run the setup interview — it asks about your organisation: BCEA earnings threshold coverage, bargaining council membership, designated employer status, CCMA vs. external consultant for disputes, whether your leave is at BCEA minimums or above
3. Upload your disciplinary code and standard employment contract — the system learns your actual framework
4. Done — your practice profile is saved and every skill reads from it

**Daily use — example: reviewing a proposed termination:**
1. The lawyer tells the system: "We want to dismiss an employee for misconduct. She's been with us 3 years, earns R180,000, no hearing has been held yet."
2. The system runs its **11 high-risk flag checklist** against the facts:
   - Flag 1 fires: **No opportunity to respond** — "The 2025 Code of Good Practice: Dismissal requires notice of allegations, time to prepare, the right to representation, and a genuine opportunity to respond before dismissal (a formal hearing is not mandatory)"
   - Flag 9 fires: **Earnings below BCEA threshold** — "This employee has full BCEA working-time and overtime protections; adverse changes face higher scrutiny"
3. The system produces a draft review memo with the flags, the applicable LRA sections, the CCMA referral risk, and a decision tree: "Hold the hearing first. Here's a checklist for procedural fairness."
4. The lawyer reviews, adjusts, and sends to HR

**The system never acts on its own.** It produces drafts, flags risks, and offers options. The lawyer decides.

**Other common tasks:**
- "Review this employment contract" → checks restraint of trade (Basson v Chilwan test), probation clause (2025 Code of Good Practice: Dismissal; formerly Schedule 8 Item 8), EEA obligations
- "Can we classify this person as a contractor?" → runs BCEA s213, s200A presumption, dominant impression test
- "Draft a disciplinary code" → produces a code aligned to the 2025 Code of Good Practice: Dismissal with the company's specific offence categories
- "How much annual leave does this employee have?" → calculates from BCEA s20 entitlements and the company's leave cycle

---

## What you're reviewing

**Your job as reviewer:** Check that the SA legal content is accurate, current, and complete. You don't need to understand the technology — just read the legal content in the files described below and flag anything that's wrong, outdated, or missing.

The SA layer is made up of files in the `jurisdictions/za/` directory. These files contain all the South African legal knowledge the system uses. If something is wrong in these files, the system will give wrong advice to every SA lawyer who uses it.

---

## How the SA layer is organised

Think of it like a law firm's knowledge management system with three layers:

### Layer 1: Statute reference files ("the law library")

**Where:** `jurisdictions/za/statutes/`

These are structured reference files — one per Act — that store **thresholds, deadlines, and key provisions** the system looks up when advising. Each entry has:

- **The section reference** (e.g., "BCEA s9(1)")
- **The value** (e.g., 45 hours per week)
- **When it took effect** and whether it's still current
- **A plain-English explanation** of what the provision does

**There are ~50 statute files** (full list: [`jurisdictions/za/statutes/`](statutes/)). The most frequently reviewed are:

| File | Act | What to check |
|---|---|---|
| `bcea.yaml` | Basic Conditions of Employment Act 75 of 1997 | Earnings threshold (see `earnings_threshold` — annual, verify against latest Gazette), hours, leave entitlements (note the Van Wyk interim parental-leave regime in `parental_leave_2025`), notice periods |
| `lra.yaml` | Labour Relations Act 66 of 1995 | Fair dismissal requirements, CCMA timelines (30-day referral, 30-day conciliation), compensation caps, retrenchment thresholds, severance |
| `eea.yaml` | Employment Equity Act 55 of 1998 | Designated employer threshold (50 employees — still correct after amendments?), protected grounds, EE reporting requirements |
| `sectoral-determinations.yaml` | Sectoral Determinations under BCEA s55 | National minimum wage (see `national_minimum_wage` — annual, verify against latest Gazette), sector-specific and EPWP rates |
| `cpa.yaml` | Consumer Protection Act 68 of 2008 | Juristic person threshold, fixed-term limits, cooling-off periods, penalties |
| `ecta.yaml` | Electronic Communications and Transactions Act 25 of 2002 | E-signature recognition, data message rules, contract formation |
| `popia.yaml` | Protection of Personal Information Act 4 of 2013 | Operator agreement requirements, breach notification (72 hours?), cross-border transfer rules, penalties |
| `conventional-penalties.yaml` | Conventional Penalties Act 15 of 1962 | Enforceability rules, cumulation bar, judicial reduction power |
| `competition.yaml` | Competition Act 89 of 1998 | Prohibited practices, restrictive horizontal/vertical agreements, penalties |
| `bbbee.yaml` | Broad-Based Black Economic Empowerment Act 53 of 2003 | Organs of state procurement requirements, EME/QSE thresholds, fronting prohibition |
| `prescription.yaml` | Prescription Act 68 of 1969 | Debt prescription periods (3 years for debts, 6 years for certain claims) |
| `copyright.yaml` | Copyright Act 98 of 1978 | Employer ownership rules, assignment requirements |

**What to look for:**
- Are the monetary thresholds current? (These change annually via Government Gazette)
- Are the section references correct? (e.g., does BCEA s9(1) actually say 45 hours?)
- Are the effective dates right?
- Is anything missing that a practitioner would expect to see?

**How to read these files:** Open them in any text editor. Ignore the formatting (the colons, dashes, and indentation are for the computer). Focus on the values, section references, and plain-English explanations.

---

### Layer 2: Practice guides ("the know-how")

**Where:** `jurisdictions/za/employment-legal/topics/` and `jurisdictions/za/commercial-legal/topics/`

These are **narrative guides** — the equivalent of a firm's internal know-how notes. Each file covers one legal topic and is shared across multiple tasks. They contain:

- The statutory framework (which Acts apply, key sections)
- Step-by-step procedures (e.g., how to run a s189 retrenchment consultation)
- Checklists (e.g., what to check before concluding a dismissal is fair)
- **High-risk flag tables** — the most important content for review

#### Employment law guides (6 files)

| File | Topic | Key content to review |
|---|---|---|
| `dismissal.md` | Termination / dismissal | **11 high-risk flags** (the checklist the system runs before concluding a dismissal review). LRA s188 framework, types of dismissal (misconduct, incapacity, operational requirements), CCMA process, notice periods, severance |
| `hiring.md` | Hiring and onboarding | Restraint of trade (Basson v Chilwan test), probation (2025 Code of Good Practice: Dismissal; formerly Schedule 8 Item 8), EEA obligations at hire (psychometric testing, medical/HIV testing restrictions), employment contract requirements (BCEA s29) |
| `classification.md` | Worker classification | BCEA s213 employee definition, s200A presumption of employment (7 factors), common law "dominant impression" test, deemed employees under s198A (TES/labour broker rules) |
| `leave-and-conditions.md` | Leave and working conditions | BCEA leave entitlements (annual, sick, family responsibility, maternity, parental), working time rules, overtime, Sunday/public holiday pay, notice periods, deductions |
| `policy-and-handbook.md` | Workplace policies | Disciplinary code requirements (2025 Code of Good Practice: Dismissal alignment), grievance procedure, sexual harassment policy (Code of Good Practice), other recommended policies |
| `investigation-privilege.md` | Investigations and privilege | SA legal professional privilege (narrower than US), in-house counsel distinction (legal adviser vs. management role), Protected Disclosures Act, POPIA considerations for investigations |

#### Commercial law guides (6 files)

| File | Topic | Key content to review |
|---|---|---|
| `contract-fundamentals.md` | SA contract law basics | Common law principles, Shifren clause, ECTA (electronic contracts), CPA (consumer protection), exchange control, VAT |
| `liability-and-penalties.md` | Liability, damages, penalties | Conventional Penalties Act (cumulation bar, judicial reduction), SA damages framework, Prescription Act |
| `data-protection.md` | POPIA in commercial contracts | Operator agreements (s21), cross-border transfers (s72), breach notification, Information Regulator enforcement |
| `competition-and-bbbee.md` | Competition Act and B-BBEE | Restrictive practices, B-BBEE procurement requirements, fronting prohibition |
| `confidentiality-and-restraint.md` | NDAs and restraint of trade | NDA enforceability in SA, restraint of trade doctrine (Basson v Chilwan), interdicts |
| `dispute-resolution.md` | Dispute resolution | SA governing law, AFSA arbitration, High Court divisions, prescription periods |

**What to look for:**
- Is the legal analysis correct? (e.g., does the Basson v Chilwan test have the right factors?)
- Are the procedures current? (e.g., has the CCMA process changed?)
- Are the high-risk flag tables complete? Would you add any flags?
- Is anything stated too absolutely that should have a caveat?
- Are the case law references correct? (e.g., is *Shifren* cited for the right principle?)

---

### Layer 3: High-risk flag tables ("the red flags")

These are embedded within the practice guides (Layer 2) and are **the most critical content for review**. They're the checklists the system runs before concluding any review.

#### Employment law: 11 dismissal flags (in `dismissal.md`)

| # | Flag | What the system checks |
|---|---|---|
| 1 | No hearing held | Was a disciplinary hearing held with proper notice, time to prepare, and right to representation? |
| 2 | Automatically unfair ground | Is the dismissal connected to pregnancy, union activity, protected disclosure, or exercise of rights? |
| 3 | Discrimination / EEA ground | Is there any connection to race, gender, disability, age, religion, HIV status, or other EEA grounds? |
| 4 | Protected disclosure | Has the employee made a whistleblowing disclosure? |
| 5 | Recent CCMA/union activity | Has the employee recently referred a dispute, participated in union activity, or been a shop steward? |
| 6 | Operational requirements without s189 | Has the consultation process been followed? Sub-check: does s189A (large-scale) apply? |
| 7 | Probation without Code compliance | Was evaluation, guidance, and counselling provided during probation? |
| 8 | Fixed-term — reasonable expectation | Has a reasonable expectation of renewal been created? |
| 9 | Earnings below BCEA threshold | Does the employee earn below the BCEA earnings threshold? (See `bcea.yaml` → `earnings_threshold` for the current figure; full BCEA protections apply below it) |
| 10 | Thin documentation | Is there a progressive discipline record? |
| 11 | Comparator / inconsistent discipline | Has the disciplinary code been applied consistently? |

#### Commercial law: 12 flags (distributed across topic files)

The commercial law flags cover: POPIA operator agreement gaps, cross-border data transfer without safeguards, CPA-covered counterparty issues, Conventional Penalties Act cumulation traps, B-BBEE procurement non-compliance, restraint of trade enforceability concerns, governing law / jurisdiction mismatches, exchange control exposure, prescription period risks, and competition law restrictive practice risks.

**What to look for:** Are these the right red flags? Would you add any? Would you remove any? Is the "what to check" column accurate?

---

### Layer 4: Practice profiles ("the firm's playbook")

**Where:** `jurisdictions/za/employment-legal/practice-profile-template.md` and `jurisdictions/za/commercial-legal/practice-profile-template.md`

These are **templates** that get filled in when a lawyer first sets up the system. They capture:

- The organisation's statutory baseline (earnings threshold coverage, sectoral determinations, bargaining council membership)
- Compliance posture (designated employer status, B-BBEE level, POPIA role)
- Dispute resolution preferences (CCMA vs. bargaining council, external consultants, recognised unions)
- Review triggers (when does legal see a termination? a contract? an NDA?)
- Escalation rules (who gets called when a high-risk flag fires?)
- The **privilege header** — what goes at the top of every document the system produces

**What to look for:**
- Does the privilege header use the correct SA formulation? (It should say "PRIVILEGED & CONFIDENTIAL — PREPARED BY/AT THE DIRECTION OF LEGAL COUNSEL FOR THE PURPOSE OF PROVIDING LEGAL ADVICE" for lawyers, not the US "ATTORNEY WORK PRODUCT" formulation)
- Does the template include the caveat about in-house counsel acting in a commercial vs. legal advisory capacity?
- Are the right questions being asked during setup? Would you add any?

---

## How to do your review

### Step 1: Start with the high-risk flag tables
These have the highest impact — they determine what the system flags as dangerous. Read the 11 employment flags in `dismissal.md` and the 12 commercial flags across the commercial topic files. Ask: would I flag these? Am I missing any?

### Step 2: Check the statute reference files
Open each `.yaml` file in `jurisdictions/za/statutes/`. Check that:
- Monetary values are current (especially the BCEA earnings threshold and minimum wage — these change annually)
- Section references are accurate
- The plain-English explanations are correct

### Step 3: Read the practice guides
Skim each topic file in the `topics/` directories. You don't need to read every word — focus on:
- Legal accuracy of the frameworks described
- Whether the procedures match current practice
- Whether the case law references are correct
- Whether anything important is missing

### Step 4: Check the privilege headers
In each `practice-profile-template.md`, read the "Outputs" section. Confirm the privilege header formulations are appropriate for SA law.

### Step 5: Flag issues
For anything that's wrong, outdated, or missing, note:
- **Which file** (e.g., `bcea.yaml`)
- **Which section** (e.g., `earnings_threshold`)
- **What's wrong** (e.g., "the earnings threshold was re-gazetted and the open entry no longer matches the current Gazette")
- **The correct information** with a source if possible

---

## What you can ignore

- File formatting (`.yaml`, `.md` extensions, indentation, colons) — that's for the computer
- The `evals/` directories — those are test scenarios for the development team
- `router.md` files — those are wiring instructions for the system
- `ARCHITECTURE.md` — that's a technical manual
- Anything under `scripts/`, `project/`, or `docs/` — technical infrastructure

**Focus on:** statute values, legal procedures, risk flags, privilege headers, and practice guides. That's where your expertise matters.

---

## Quick reference: where to find what

| "I want to check..." | Look in... |
|---|---|
| Whether a statutory threshold is current | `jurisdictions/za/statutes/{act-name}.yaml` |
| Whether a legal procedure is described correctly | `jurisdictions/za/{practice-area}/topics/{topic}.md` |
| Whether the right risk flags are being checked | The flag tables inside the topic files (especially `dismissal.md` for employment, and `contract-fundamentals.md` / `data-protection.md` for commercial) |
| Whether the privilege header is correct | `jurisdictions/za/{practice-area}/practice-profile-template.md` → "Outputs" section |
| Whether the setup questions are right | `jurisdictions/za/{practice-area}/practice-profile-template.md` → the `[PLACEHOLDER]` sections show what gets asked |

---

*Questions about this guide? Ask the development team. Questions about the law? That's why we need you.*
