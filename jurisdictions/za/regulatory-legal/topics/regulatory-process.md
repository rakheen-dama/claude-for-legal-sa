# Regulatory Process — South African Framework

This overlay covers the South African rulemaking and public participation framework under the Promotion of Administrative Justice Act 3 of 2000 (PAJA), the Government Gazette system, and parliamentary processes. It is loaded by reg-feed-watcher, comments, and cold-start-interview skills when jurisdiction = ZA.

---

## 1. SA rulemaking framework

### Government Gazette as central publication channel

All binding legal instruments in South Africa are published in the Government Gazette, which is the sole official publication channel for:

- Acts of Parliament (after presidential assent)
- Regulations (subordinate legislation made under enabling Acts)
- Government notices and general notices
- Determinations and directives issued by regulators
- Exemptions and proclamations
- Provincial gazettes (published separately by each province)

The Government Printing Works (GPW) publishes the Gazette. It is available at gov.za and gpwonline.co.za. Gazette numbers are sequential and serve as the canonical citation reference.

### How regulations are made

The typical lifecycle of a regulation under an enabling Act:

1. **Drafting** — the responsible department or regulator drafts the regulation under the authority of the enabling Act.
2. **Internal approval** — Cabinet approval (for national department regulations) or board/committee approval (for regulator instruments).
3. **Draft publication** — the draft regulation is published in the Government Gazette for public comment, specifying the comment period and submission details.
4. **Comment period** — interested parties submit written comments to the publishing authority.
5. **Consideration** — the authority considers comments and may revise the draft.
6. **Final publication** — the final regulation is published in the Government Gazette, with or without amendments from the comment process.

---

## 2. PAJA public participation requirements

### s3 — procedurally fair administrative action (individuals)

Where administrative action materially and adversely affects the rights or legitimate expectations of a person, PAJA s3 requires:

- **s3(2)(a):** adequate notice of the nature and purpose of the proposed action
- **s3(2)(b)(i):** a reasonable opportunity to make representations
- **s3(2)(b)(ii):** a clear statement of the administrative action taken
- **s3(2)(b)(iii):** adequate notice of any right of review or internal appeal
- **s3(2)(b)(iv):** adequate notice of the right to request written reasons under PAJA s5

### s4 — administrative action affecting the public

Where administrative action materially and adversely affects the rights of the public, the administrator must decide whether to hold a public inquiry, give notice for written comments, or follow another appropriate procedure. PAJA s4(1) provides five options:

| Option | Mechanism |
|---|---|
| s4(1)(a) | Publication of notice with reasonable comment period — notice-and-comment |
| s4(1)(b) | Public inquiry conducted by a presiding official |
| s4(1)(c) | Formalised notice-and-comment procedure with specific procedural rules |
| s4(1)(d) | Advisory committee including representatives of affected persons |
| s4(1)(e) | Any combination of the above |

The administrator must select one or more of these procedures. The choice is itself subject to judicial review if unreasonable.

### "Reasonable period" standard

PAJA does not prescribe a fixed comment period. The standard is "reasonable" — determined by the complexity of the matter, the number of persons affected, and the impact of the proposed action. Courts assess reasonableness on a case-by-case basis.

---

## 3. Typical comment periods

| Type | Typical period | Examples |
|---|---|---|
| Standard regulations | 30 days | Most department regulations |
| Complex/technical instruments | 45–60 days | FSCA conduct standards, ICASA spectrum allocation |
| Urgent/minor amendments | 14–21 days | Emergency measures, technical corrections |
| Major reforms | Up to 90 days | Financial sector overhauls, COFI Bill consultations |

These are norms, not statutory requirements. The publishing authority sets the comment period in the Gazette notice and may extend it on request or shorten it with justification.

---

## 4. Multi-step rulemaking

Major regulatory reforms frequently follow a multi-step consultation process:

1. **Discussion paper / policy paper** — sets out the policy problem and proposed approach; invites broad input.
2. **Draft regulation / exposure draft** — specific legal text published for targeted comment.
3. **Revised draft** (optional) — where material changes are made after the first round.
4. **Final regulation** — published in the Gazette as binding law.

This pattern is common for FSCA conduct standards, NERSA licence conditions, major National Treasury reforms, and B-BBEE codes of good practice. Each step has its own Gazette notice and comment period.

---

## 5. Comment submission mechanics

- There is no centralised comment submission portal equivalent in SA. Each regulator manages its own process.
- The Gazette notice specifies: the contact person, email address, physical address for postal submissions, and the deadline.
- Comments are typically submitted by email or post directly to the publishing regulator.
- Some regulators (FSCA, ICASA, Information Regulator) have developed online submission portals, but these are regulator-specific.
- Format requirements vary — some regulators request comments in a prescribed template; others accept free-form submissions.
- Industry bodies (BUSA, BASA, ASISA) frequently coordinate consolidated submissions on behalf of their members.

---

## 6. NEDLAC process

The National Economic Development and Labour Council (NEDLAC) is a statutory body established under the National Economic Development and Labour Council Act 35 of 1994. Major socio-economic legislation must be considered by NEDLAC before it is introduced in Parliament.

### Constituencies

| Constituency | Representatives |
|---|---|
| Government | Relevant national departments |
| Business | BUSA (Business Unity South Africa) |
| Labour | COSATU, FEDUSA, NACTU |
| Community | Community constituency organisations |

### Process

- The responsible department tables the draft legislation or policy at NEDLAC.
- Constituencies negotiate and attempt to reach consensus on the content.
- NEDLAC issues a report recording areas of agreement and disagreement.
- The report accompanies the Bill when it is introduced in Parliament.
- NEDLAC engagement is separate from and additional to Gazette comment periods.

---

## 7. Parliamentary process

Parliamentary scrutiny of legislation is distinct from executive rulemaking:

- **Bills** are gazetted separately from regulations and published in the Government Gazette with a separate numbering sequence.
- **Parliamentary committee hearings** — the relevant portfolio committee invites written submissions and holds public hearings on Bills.
- **NCOP process** — Bills affecting provinces require consideration by the National Council of Provinces (NCOP) under Constitution s76.
- Regulations made under an enabling Act generally do not require parliamentary approval unless the enabling Act specifically requires that they be "tabled" in Parliament.

---

## 8. Gazette commencement rules

### Default rule

A regulation comes into force on the date of its publication in the Government Gazette unless the regulation itself specifies otherwise.

### Variations

| Mechanism | How it works |
|---|---|
| Specified future date | The regulation states "this regulation comes into operation on [date]" |
| Proclamation | The enabling Act or regulation states it comes into force "on a date determined by the President/Minister by proclamation in the Gazette" — requires a separate commencement notice |
| Phased commencement | Different sections come into force on different dates, specified in the commencement notice or the regulation itself |

### The commencement trap

**WARNING:** Regulations are enforceable from their commencement date, not from the date you become aware of them. If you are not actively monitoring the Gazette, a regulation can be in force before you know it exists. This is especially dangerous for:

- Regulations published with immediate commencement (same day as Gazette publication)
- Proclamations bringing long-dormant Acts or provisions into force
- Phased commencement notices adding new provisions to an already partially commenced Act

The reg-feed-watcher skill addresses this risk by monitoring the Gazette feed continuously against the user's watchlist.
