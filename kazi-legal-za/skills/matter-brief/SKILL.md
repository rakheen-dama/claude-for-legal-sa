---
name: matter-brief
description: >
  Write a plain-language, client-ready status update for a matter, synthesised
  from its recent activity, key dates, and documents in Kazi. Reads over the
  Kazi MCP server and drafts; a human reviews and sends from Kazi. Use when the
  user says "matter update", "status brief", "where are we on [matter]",
  "client update", or "brief me on [matter]".
argument-hint: "[matter name/id]"
---

# /matter-brief

Turn a matter's recent activity into a clear, client-ready status update.

## Read-only, draft-only

Reads the matter, its activity, and its documents over MCP and **drafts** a brief. Never writes to Kazi.
The attorney reviews, edits, and sends it from Kazi. The brief is a draft, not a sent communication.

## Setup gate

Read `~/.claude/plugins/config/claude-for-legal/kazi-legal-za/CLAUDE.md`. If missing or `[PLACEHOLDER]`,
**stop** and say "Run `/kazi-legal-za:connect-kazi` first."

## Workflow

**Step 1 — Resolve the matter.** From the argument, `get_matter(<id>)` → `name`, `workType`, `status`,
`referenceNumber`, `dueDate`, `customerId`, `description`.

**Step 2 — Read recent activity.** `get_matter_activity(<projectId>)` → a feed of
`{occurredAt, action, message, actor, entityType, entityName}`. Read the most recent items (page if
needed) to understand what has actually happened and when. Use `occurredAt` for the timeline.

**Step 3 — Note key documents.** `search_documents(projectId=<id>)` → recent `{name, contentType,
createdAt}`. Mention notable recent documents by name; do not summarise contents you haven't read.

**Step 4 — Synthesise.** Write a short, plain-language brief a client (not a lawyer) can understand:
what's happened recently, what it means, what's next, and any date the client should know (`dueDate`).
Translate internal/legal shorthand into plain English. Keep it factual — only what the activity and
matter data support; never imply progress or outcomes that aren't in the feed.

## Source attribution

Tag facts: `[kazi MCP]` for matter facts, activity, and document names; `[model knowledge — verify]` for
any legal framing you add. Never overstate status. If activity is sparse, say "limited recent activity
recorded" rather than inventing progress.

## Output template

```
## Matter update (DRAFT) — [Client] — [Matter name]
*Draft for attorney review. Edit and send from Kazi.*

Reference: [referenceNumber] · Status: [status] · Next key date: [dueDate or "none recorded"]

**Where things stand**
[2–4 plain-language sentences synthesising recent activity.]   [kazi MCP]

**Recent activity**
- [date] — [plain-language line from the activity feed]   [kazi MCP]
- ...

**Recent documents**
- [name] ([date])   [kazi MCP]

**What's next**
[1–2 sentences — only what the data supports.]
```

## Boundaries

- **Read-only.** Never writes to Kazi.
- **Never invent** activity, progress, outcomes, or document contents — use only what the tools return.
  If a tool errors or consent is missing, **stop and report**.
- Every brief is a draft for attorney review, sent from within Kazi.
