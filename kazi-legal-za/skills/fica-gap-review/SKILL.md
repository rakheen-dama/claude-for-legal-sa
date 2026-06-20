---
name: fica-gap-review
description: >
  Review a client's FICA/KYC compliance state in Kazi, identify the missing or
  outstanding requirements, and draft the document-request to send the client.
  Reads the client's compliance checklist and profile over the Kazi MCP server
  and grounds the gaps in the Financial Intelligence Centre Act. Read-only: a
  human reviews and sends the request from Kazi, and a compliance officer makes
  the compliance call. Use when the user says "FICA", "KYC", "compliance gaps",
  "what's outstanding for [client]", "onboarding documents", or "draft a FICA
  request".
argument-hint: "[client name/id, or matter name/id]"
---

# /fica-gap-review

Find what's missing in a client's FICA/KYC file and draft the request to close it.

## Read-only, draft-only — and not a compliance determination

This skill **reads** the client's compliance checklist and profile over MCP and **drafts** a document
request. It never writes to Kazi. It **reports** checklist state and gaps — it does **not** decide that a
client is "FICA-compliant", "cleared", or "onboarded". That determination is the firm's compliance
officer / attorney call, made in Kazi. Never assert compliance; only report what the checklist shows.

## Setup gate

Read `~/.claude/plugins/config/claude-for-legal/kazi-legal-za/CLAUDE.md`. If it is missing or still
contains `[PLACEHOLDER]`, **stop** and say: "Run `/kazi-legal-za:connect-kazi` first." Only `connect-kazi`
runs without setup.

## Load context first

Read the bundled SA knowledge `data/za/statutes/fica.yaml` — sections `customer_due_diligence` (s21,
identity verification), `beneficial_ownership` (s21B, legal persons & trusts), `rmcp_requirement` (s42),
and `cash_threshold_reporting` (s28, the R25 000 cash trigger). Use these to explain *why* each gap
matters and *what* satisfies it.

## Workflow

**Step 1 — Resolve the client.** From the argument:
- a client → use it directly (resolve a name via `list_clients` if you only have a name).
- a matter → `get_matter(<id>)` → take its `customerId`.

**Step 2 — Read the client.** `get_client(<customerId>)` → `name`, `type` (the **client type drives the
FICA path**: a natural person needs identity + address verification; a **legal person or trust** also
triggers **beneficial-ownership** verification under s21B), `contacts` (the request recipient), and
`linkedMatters`.

**Step 3 — Read the checklist.** `list_compliance_gaps(<customerId>)` → `ficaStatus` and `items`
(`{name, status, required}`). The **gaps** are the items where `required` is true and `status` is not
satisfied. If `truncated` is true, say the list was capped and more may exist in Kazi.

**Step 4 — Map and explain.** For each gap, name the FICA requirement it addresses (CDD identity
verification, proof of residential address, beneficial ownership for entities/trusts, source of funds
where risk-rated) and what document satisfies it. Typical acceptable documents — confirm against the
firm's RMCP:
- **Natural person:** Smart ID / green ID book / passport; proof of residential address (≤3 months).
- **Company / CC:** CIPC registration (CoR14.3 / CK documents), directors'/members' IDs, beneficial
  owners (≥25% holding) per s21B.
- **Trust:** trust deed, Letters of Authority, trustee IDs, founder and beneficiary details (s21B).

**Step 5 — Draft the request.** Draft a short, professional document-request addressed to the client's
primary contact (from `get_client`), listing exactly the outstanding items, grouped by what's needed.
Keep it client-friendly. Do not threaten or assert legal consequences beyond noting FICA requires the
documents before the firm can proceed.

**Step 6 — Summarise.** End with a gap summary and the "review and send from Kazi" handoff.

## Source attribution

Tag every fact and citation: `[kazi MCP]` for the client profile, checklist items, and `ficaStatus`;
`[jurisdictions/za]` for FICA sections and thresholds (s21, s21B, s28, s42); `[firm profile]` for the
firm's RMCP/house rules; `[model knowledge — verify]` for anything else. Never strip the tags. If a
specific document's acceptability is uncertain, mark it `[model knowledge — verify]` and defer to the
firm's RMCP.

## Output template

```
## FICA / KYC gap review (DRAFT) — [Client] ([type])
*Reports checklist state — not a compliance determination. Review and send from Kazi.*

FICA status (Kazi):  [ficaStatus]   [kazi MCP]
Client type:         [natural person | company/CC | trust] → [CDD path]   [jurisdictions/za]

### Outstanding (required) items
- [item name] — needs: [document(s)] — [why: FICA s__]   [kazi MCP]/[jurisdictions/za]
- ...
[If truncated: "Checklist was capped — confirm the full list in Kazi."]

### Draft request to client
To: [contact name] <[email]>   [kazi MCP]
Subject: Documents required to proceed — [Client]

[Short professional body listing the outstanding documents, grouped clearly.]
```

End with:

```
## Summary
- Outstanding required items: [n]   ·   Beneficial-ownership applies: [yes/no]
- Next: review the request, then send it from Kazi. Compliance sign-off stays with the firm.
```

## Boundaries

- **Read-only.** Never writes to Kazi.
- **Never assert FICA compliance, clearance, or completeness** — report the checklist; the firm decides.
- **Never invent checklist items, statuses, or that a document was received** — use only what the tools
  return. If a tool errors or egress consent is missing, **stop and report**.
- Every output is a draft for attorney / compliance-officer review and is sent from within Kazi.
