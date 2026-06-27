---
name: correspondence-digest
description: >
  Read filed correspondence back across a matter (or client) and surface what
  needs the lawyer's attention — inbound that's gone unanswered, matters gone
  quiet, and deadlines implied by the email bodies. Reads correspondence over
  the Kazi MCP server and can propose follow-up tasks for the attorney to
  approve **inside Kazi**. Reasons over what was *filed* in Kazi (e.g. via
  /file-email), not the live mailbox. Use when the user says "correspondence
  digest", "what needs a reply on [matter]", "anything gone quiet", "summarise
  the emails on [matter]", or "what deadlines are in the correspondence".
argument-hint: "[matter name/id (default) | client name/id | how many days back to scan]"
---

# /correspondence-digest

Summarise the correspondence already filed in Kazi for a matter (or client) and surface what needs the
lawyer's attention — unanswered inbound, matters gone quiet, and deadlines stated in the email bodies.

## Honest scope — this reads what was *filed*, not your inbox

This skill reasons over correspondence **filed in Kazi** (for example by `/kazi-legal-za:file-email`).
It is **not a live inbox monitor** — it sees Kazi's correspondence records, not the raw mailbox, and
Kazi has no mail integration by design (bring your own Claude). Say so if the user expects it to catch
something they never filed.

## Reads + one gated proposal

- `list_correspondence` and `get_correspondence` are **reads**, under the same POPIA data-egress consent
  as the other read skills. Reading a body pulls client PII into your Claude context — the same posture
  as `get_matter`/`get_client`.
- `propose_task` is the **only write**, and it only creates a **PENDING approval gate**. Say "**proposed
  a task — approve it in Kazi to create it**," never "created a task" or "set a deadline."
- **Trust is never touched.**

## Setup gate

Read `~/.claude/plugins/config/claude-for-legal/kazi-legal-za/CLAUDE.md`. If it is missing or still
contains `[PLACEHOLDER]`, **stop** and say: "Run `/kazi-legal-za:connect-kazi` first — this skill needs
your Kazi connection and house style."

Proposing a task additionally needs **MCP write enablement + consent** in Kazi. Reading the digest does
not — but if `propose_task` returns a not-enabled error, surface "Enable MCP **write** + consent in Kazi
Settings → Integrations → MCP" and still deliver the read-only digest. If a *read* tool returns a
consent error, stop and point the user to the same settings — don't work around it.

## What the tools support — and their limits

- `list_correspondence(matterId | customerId, page?, size?)` → a page of metadata rows
  `{id, subject, fromAddress, receivedAt, attachmentCount, direction}` (`direction` is `INBOUND` or
  `OUTBOUND`) plus `{page, size, total, truncated}`. **`size` is capped at 50**; page through when
  `truncated` is true. **List rows do not include `messageId` or the body** — fetch the record for those.
- `get_correspondence(id)` → the full record **with body** (`bodyText`, `bodyHtml`) plus `customerId`,
  `projectId`, `toAddresses`, `ccAddresses`, `sentAt`, `threadKey`, `messageId`, `attachmentCount`,
  `filedAt`, `direction`. Deadlines and obligations live in the **body**, so fetch it for anything you
  reason over. **`projectId` is the matter id** — use it as the `projectId` for `propose_task`
  (it may be null if the email was filed against a client only).
- `propose_task(projectId, correspondenceId, …)` → `{gateId, status: "PENDING", duplicate, message}`.
  `correspondenceId` is **required** — you already hold it from the list/get, so anchor each proposal on
  the correspondence that implied it.

## Load context first

Read `~/.claude/plugins/config/claude-for-legal/kazi-legal-za/CLAUDE.md` for house style and the firm's
active matters/conventions. For deadline sanity-checking you may consult the bundled SA knowledge
`data/za/statutes/prescription.yaml` (section `general_debt_prescription`) — **advisory only**.

## Workflow

**Step 1 — Scope.** From the argument pick the unit (default **per-matter**): a `matterId` →
`list_correspondence(matterId=…)`; a client → `list_correspondence(customerId=…)`. Default the look-back
to ~30 days unless the user gives a window. Page through (respect `size ≤ 50` and `truncated`); say so if
you stop early.

**Step 2 — Read the bodies worth reasoning over.** For recent inbound, and anything whose subject hints
at an obligation/date, call `get_correspondence(id)` to get the body, `threadKey`, and timestamps. Don't
fetch every record blindly on a busy matter — prioritise inbound and recent items, and note what you
skipped.

**Step 3 — Build the digest.** Classify into three buckets:
- **Needs a reply** — an `INBOUND` item with **no later `OUTBOUND`** in the same `threadKey` (or, if
  `threadKey` is absent, no later outbound to that correspondent on the matter).
- **Gone quiet** — an active matter with **no correspondence in N days** (use the look-back window).
- **Deadline spotted** — a **date-bearing obligation extracted from a body** ("respond by…", "file
  by…", "pay within…"). Sanity-check the date against `prescription.yaml` / court-deadline awareness
  **advisorily**; never assert a statutory deadline as fact.

**Step 4 — Optionally propose follow-ups.** For a clear, dated obligation, offer to
`propose_task(projectId, correspondenceId=<the item that implied it>, title, dueDate?)` — take
`projectId` from that correspondence's `get_correspondence` record (its matter id), and `dueDate` is
`yyyy-MM-dd`. It creates a **PENDING gate**: "Proposed a task — approve it in Kazi to create it." On
`duplicate: true`, say "a matching proposal is already pending." Only propose when the user wants
follow-ups created; otherwise just list the spotted deadlines. **If the correspondence has no
`projectId`** (filed against a client only), don't propose — list the deadline and ask which matter to
attach it to.

When a body references "the attached…", you may locate it via `search_documents` / `get_document_url`
(existing read tools) to confirm what's being referred to — but don't re-file anything here.

## SA grounding & source attribution

- Spotted deadlines are **advisory**, tagged `[jurisdictions/za]` when sanity-checked against
  `data/za/statutes/prescription.yaml`, else `[model knowledge — verify]`. The authoritative deadline is
  the attorney's, set on approving the task in Kazi.
- Tag facts by source: `[kazi MCP]` for correspondence records, ids, and counts; `[firm profile]` for
  house style; `[jurisdictions/za]` for statute thresholds; `[model knowledge — verify]` for anything
  inferred from a body. Never strip the tags.

## Output template

```
## Correspondence digest — [Matter name | Client]   ([window], [N] items scanned)   [kazi MCP]

### Needs a reply  ([k])
- #[id] · [fromAddress] · [receivedAt] — "[subject]"
  [one-line why: inbound, no later outbound in thread]

### Gone quiet  ([k])
- [Matter / correspondent] — last correspondence [date] ([days] days ago)

### Deadlines spotted  ([k])
- #[id] — "[obligation]" → suggested due [yyyy-MM-dd]   [jurisdictions/za | model knowledge — verify]
  [→ PROPOSED task, gate #[gateId] — approve in Kazi]   (only if proposed)

Scope note: reasons over correspondence FILED in Kazi, not the live mailbox.
[Skipped: [what you didn't fetch], paging [truncated?].]
```

Optionally, a cross-matter "my inbox today" roll-up is a **fast-follow** once per-matter paging is
proven; v1 defaults to per-matter.

## Boundaries

- **Never overstate the gate.** "Proposed — approve in Kazi" for `propose_task`; never "created."
- **Filed, not live.** Be explicit that the digest only sees what's in Kazi.
- **Trust is never touched.**
- **Never invent** correspondence, dates, or a "gone quiet" state — derive everything from the tool
  results. If a read tool errors or consent is missing, stop and report.
