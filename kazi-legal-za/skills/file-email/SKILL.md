---
name: file-email
description: >
  File an inbound email into the right Kazi matter without copy-paste — and
  optionally propose the follow-up it implies. Resolves the sender to a client
  + matters over the Kazi MCP server, files the email as correspondence
  (idempotent), uploads attachments as stamped documents, and can propose a
  task for the attorney to approve **inside Kazi**. Provider-neutral: paste or
  forward any email (Gmail, Outlook, anything), no mail integration required.
  Use when the user says "file this email", "file into Kazi", "log this
  correspondence", "save this email to matter X", or forwards/pastes an email.
argument-hint: "[paste/forward the email; optionally a client/matter hint or reference number]"
---

# /file-email

File an email the lawyer's Claude can already see into the correct Kazi matter, then optionally propose
the follow-up it implies — so the attorney approves it in Kazi.

## Tier-1 writes + one gated proposal — what actually happens

This skill **writes** to Kazi, but in a tightly bounded way. Be precise in every message about which
kind of action you took:

- `file_correspondence` and `attach_document` are **real, immediate, audited writes** — once they
  return, the email/attachment **is filed**. Say "**filed**."
- `propose_task` does **not** create a task. It creates a **PENDING approval gate**. The task only
  exists once the attorney approves it **inside Kazi**. Say "**proposed a task — approve it in Kazi to
  create it**." Never say "created a task" or "set a deadline."
- **Trust is never touched.** This skill never proposes or files anything against the trust ledger.

## Setup gate

Read `~/.claude/plugins/config/claude-for-legal/kazi-legal-za/CLAUDE.md`. If it is missing or still
contains `[PLACEHOLDER]`, **stop** and say: "Run `/kazi-legal-za:connect-kazi` first — this skill needs
your Kazi connection and house style."

Writing additionally needs **MCP write enablement + consent** in Kazi (a stricter posture than the
read-only skills). If a tool returns a not-enabled / not-consented error, **stop** and say: "Enable MCP
**write** + data-egress consent in Kazi Settings → Integrations → MCP" — do not present it as a raw
error and do not try to work around it.

**POPIA note:** filing moves the email (and its client PII) *into* Kazi — the lower-risk direction — but
it is still an audited write. Remind the user once that the email content is flowing through their Claude
context on its way in.

## What the tools support — and their limits

- `resolve_matter_by_email(email, subjectHint?, reference?)` → `{customer | null, matters[]}`. The
  server does **no fuzzy matching** — `subjectHint`/`reference` are hints for *your* disambiguation only.
  Kazi never auto-files on a guess; you pass an explicit `matterId`/`customerId`.
- `file_correspondence(matterId | customerId, …, messageId)` → `{correspondenceId, idempotent}`.
  **Idempotent on `messageId`** (a DB-unique key). Re-filing the same `messageId` returns the existing
  id with `idempotent: true` — that is **success ("already filed")**, not an error.
- `attach_document` is a **two-phase presigned upload**, not a single call (see Step 5). It needs the
  attachment's **raw bytes as a local file**.
- `propose_task(projectId, correspondenceId, …)` → `{gateId, status: "PENDING", duplicate, message}`.
  `correspondenceId` is **required** — you can only propose a task off a filed correspondence. There is
  **no MCP endpoint to approve** a gate; approval happens only in Kazi.

## Load context first

Read `~/.claude/plugins/config/claude-for-legal/kazi-legal-za/CLAUDE.md` for the firm's house style and
jurisdiction. For a proposed task with a date, you may consult the bundled SA knowledge
`data/za/statutes/prescription.yaml` (section `general_debt_prescription`) — **advisory only**, to help
phrase a proposed task's title/date. The lawyer confirms the real deadline in Kazi; no statutory
deadline is committed by this skill.

## Workflow

**Step 1 — Read the email.** The v1 floor is a **single email the user pastes or forwards** (any
provider). Extract: `fromAddress`, `toAddresses`, `ccAddresses`, `subject`, body (`bodyText` and
`bodyHtml` if available), `sentAt` / `receivedAt`, the `threadKey` (provider thread/conversation id if
present), and the RFC-822 **`Message-ID`** header if present.

**Step 2 — Resolve the matter.** Call `resolve_matter_by_email(fromAddress, subjectHint=subject,
reference=<any ref no. you spotted>)`.
- **Exactly one matter** → confirm it with the lawyer, then proceed.
- **No customer / no matters** → ask the lawyer: file against the client only (pass `customerId` if the
  customer resolved), or stop because this sender isn't a known client. **Never invent a matter.**
- **Multiple matters** → show the candidates and **ask which one** (or "file against the client only").

**Step 3 — Derive a stable `messageId`** (the idempotency key, required by `file_correspondence`):
- If the email has an RFC-822 `Message-ID`, use it verbatim.
- Otherwise (a paste often lacks one), derive a deterministic fallback:
  `mcp-paste-<first 16 hex chars of sha256("<fromAddress>|<subject>|<sentAt ISO>")>`.
  This guarantees that re-filing the *same* pasted email is idempotent. State the derived key to the
  user so a later re-run is predictable.

**Step 4 — File the correspondence.** Call
`file_correspondence(matterId | customerId, fromAddress, toAddresses, ccAddresses, subject, bodyText,
bodyHtml, sentAt, receivedAt, threadKey, messageId)`.
- On `idempotent: true` → tell the user **"already filed"** (success) and reuse the returned
  `correspondenceId`; do not re-upload attachments unless they're missing.

**Step 5 — Attachments (two-phase upload).** For each attachment whose **raw bytes are reachable as a
local file** (a connector saved it to disk, or the user gives you a path):
1. `attach_document(phase="INITIATE", correspondenceId, fileName, contentType?, size)` →
   `{documentId, presignedUrl, expiresInSeconds}`. `size` **must equal the real byte count** of the
   file; `contentType` is optional — omit it and let the server infer if you can't determine the MIME
   type.
2. **PUT the bytes** to the presigned URL — in Claude Code:
   ```bash
   curl -sS -X PUT --upload-file "<localPath>" -H "Content-Type: <contentType>" "<presignedUrl>"
   ```
3. `attach_document(phase="CONFIRM", correspondenceId, documentId)` →
   `{documentId, status: "UPLOADED", correspondenceId}`. CONFIRM is idempotent.

**Environment caveat — state it plainly when it bites:** the upload needs a client that can perform an
HTTP PUT (e.g. Claude Code with `curl`) **and** a local file. On the bare paste path (no attachment
bytes), or in a client without shell/file access, **do not fake it** — file the body, record that N
attachments exist, and tell the user to attach them in Kazi. Count these as **skipped**, not failed.

**Step 6 — Optionally propose a follow-up.** Only if the email implies a dated action ("respond by
15 July", "file answering affidavit by…", "pay by month-end"):
- `propose_task(projectId=<matterId>, correspondenceId, title, description?, dueDate?)` — `dueDate` is
  `yyyy-MM-dd`. Phrase the title/date from the email; use `prescription.yaml` only advisorily for sanity.
- Returns a **PENDING gate**. Tell the lawyer: **"Proposed a task — approve it in Kazi to create it."**
- On `duplicate: true` → say "a matching proposal is already pending in Kazi" (the open-gate dedupe
  caught it); do not propose again.
- If the matter didn't resolve (client-only filing) there is no `projectId` → **don't** propose a task;
  note the implied action in the summary for the lawyer to handle.

## SA grounding & source attribution

- Any deadline language in a *proposed* task is **advisory** and tagged `[jurisdictions/za]` when it
  leans on `data/za/statutes/prescription.yaml`, or `[model knowledge — verify]` otherwise. The
  authoritative deadline is the attorney's, set when they approve the task in Kazi.
- Tag facts by source: `[kazi MCP]` for resolve/file/attach/propose results and ids; `[firm profile]`
  for house style; `[jurisdictions/za]` for statute thresholds; `[model knowledge — verify]` for
  anything inferred from the email body. Never strip the tags.

## Output template

```
## Filed — [Client] — [Matter name]   [kazi MCP]

Correspondence: #[correspondenceId]   ([already filed — idempotent] | [newly filed])
From:           [fromAddress] · [sentAt]
Subject:        [subject]
Attachments:    [N uploaded] · [M skipped — no bytes reachable; attach in Kazi]
Follow-up:      [1 task PROPOSED — pending your approval in Kazi (gate #[gateId])]
                [or: "none proposed"] · [or: "duplicate — a proposal is already pending"]
messageId:      [the RFC-822 id, or the derived mcp-paste-… key]
```

## Bulk mode (fast-follow — not in v1)

When a mail **connector** is present (Gmail today; Outlook/MS via MCP later), a bulk sub-flow can triage
an inbox: resolve each unfiled email, file the unambiguous ones, and present a per-email
**disambiguation table** for the rest (file / skip-already-filed / needs-a-matter). This is **not built
yet** — v1 files one pasted/forwarded email at a time. Don't imply bulk filing is available.

## Boundaries

- **Never overstate the gate.** "Filed" only for `file_correspondence`/`attach_document`; "proposed —
  approve in Kazi" for `propose_task`. Never "created a task" or "set a deadline."
- **Idempotent re-runs are success.** `idempotent: true` / `duplicate: true` are "already done," not
  failures.
- **Trust is never touched** — no correspondence or task proposal goes near the trust ledger.
- **Never invent** a matter, a client, a deadline, or attachment bytes. If resolution is ambiguous,
  ask. If consent/enablement is off, stop and report.
