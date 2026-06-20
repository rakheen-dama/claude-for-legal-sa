---
name: kazi-bridge
description: >
  Run any upstream claude-for-legal skill against a matter's live data in Kazi.
  Pulls the matter, its parties, and its documents over the Kazi MCP server,
  then hands that grounded context to a generic legal skill (contract review,
  chronology, diligence, etc.) so it works on real firm data instead of pasted
  text. Read-only. Use when the user says "run [skill] on matter X in Kazi",
  "review the latest document on [matter]", or "use Kazi data for this".
argument-hint: "[upstream skill] on [matter name/id]   e.g. 'contract-review on matter Acme lease'"
---

# /kazi-bridge

Make the firm's other Claude legal skills Kazi-aware: ground a generic skill in a real matter's data.

## What this is

Anthropic's `claude-for-legal` plugins ship dozens of skills (contract review, chronology, diligence,
claim charts, …) that normally work on text you paste in. With the Kazi MCP server connected, this
bridge pulls a matter's real context from Kazi first, then runs the chosen skill on it — so the firm's
existing skills operate on live firm data, with the same per-user authorisation and audit as every other
Kazi read.

## Read-only, draft-only

Everything stays read-only: this bridge pulls context, the upstream skill drafts. Nothing is written back
to Kazi by either side. The attorney commits any result in Kazi by hand.

## Setup gate

Read `~/.claude/plugins/config/claude-for-legal/kazi-legal-za/CLAUDE.md`. If missing or `[PLACEHOLDER]`,
**stop** and say "Run `/kazi-legal-za:connect-kazi` first." The target upstream plugin (e.g.
`commercial-legal`) must also be installed.

## Workflow

**Step 1 — Parse the request** into `<upstream skill>` + `<matter>`. If the skill or matter is ambiguous,
ask.

**Step 2 — Pull the matter context** over MCP:
- `get_matter(<id>)` → name, type, parties, reference, status.
- `search_documents(projectId=<id>)` → the matter's documents; pick the relevant one(s) by `name`.
- `get_document_url(<documentId>)` → a presigned URL the upstream skill can read the document from.
- `get_matter_activity(<id>)` if the skill needs a timeline.

**Step 3 — Hand off to the upstream skill.** Invoke the named skill (e.g.
`/commercial-legal:nda-review`), passing the document(s) and matter context you just pulled as its input,
instead of asking the user to paste text. Preserve that skill's own guardrails and output format.

**Step 4 — Attribute and hand back.** Keep the upstream skill's source tags, and tag the Kazi-sourced
context as `[kazi MCP]`. Remind the user the result is a draft to commit in Kazi.

## Worked examples

- `contract-review on matter "Acme MSA"` → pull the latest agreement document on that matter, run
  `/commercial-legal:saas-msa-review` on it.
- `chronology on matter "Smith v Jones"` → pull the matter activity + documents, run the litigation
  chronology skill over them.
- `diligence on customer "TargetCo"` → list the customer's matters and documents, feed them to the
  corporate diligence skill.

## Boundaries

- **Read-only.** Neither this bridge nor the upstream skill writes to Kazi.
- **Never invent** matter data or document contents — pull them via the tools (`get_matter`,
  `search_documents`, `get_document_url`, `get_matter_activity`). If a tool errors or consent is missing,
  **stop and report**.
- The upstream skill's guardrails (source attribution, privilege, gating) apply unchanged. Every result
  is a draft the attorney commits in Kazi.
