---
name: fee-note-run
description: >
  Draft fee notes from a firm's unbilled time in Kazi. Reads unbilled-time
  totals and matter context over the Kazi MCP server and drafts a per-matter
  fee-note narrative in the firm's house style, with VAT and South African
  contingency-fee caps applied. Read-only: a human reviews each draft and
  finalises the fee note inside Kazi. Use when the user says "fee note",
  "fee notes", "monthly billing run", "bill matter X", "draft a fee note for
  [client/matter]", or "what's unbilled".
argument-hint: "[client name/id | matter name/id | 'all' — defaults to a full unbilled run]"
---

# /fee-note-run

Turn the firm's unbilled time in Kazi into draft fee-note narratives.

## Read-only, draft-only

This skill **reads** unbilled time + matter context over MCP and **drafts**. It never writes to Kazi.
Every fee note it produces is a draft for attorney review — the lawyer reviews, itemises, and finalises
the fee note **inside Kazi**, then sends it. Do not present a draft as issued or final.

## Setup gate

Read `~/.claude/plugins/config/claude-for-legal/kazi-legal-za/CLAUDE.md`. If it is missing or still
contains `[PLACEHOLDER]`, **stop** and say: "Run `/kazi-legal-za:connect-kazi` first — this skill needs
your Kazi connection and house style." The only skill that runs without setup is `connect-kazi`.

## What the data supports — and its limits

`get_unbilled_time` returns **aggregates, not line items**:

- **No matter id** → org-wide: a list of clients with unbilled time — `{customerName, amountMinor, currency}` per client.
- **With a matter (project) id** → that matter only: `{totalAmountMinor, currency, entryCount}`.

So this skill drafts **matter-level** fee-note narratives and totals. It **cannot itemise individual
time entries** — that detail is not exposed over MCP. State this in the draft and tell the user to
itemise in Kazi. **Money is in minor units (cents): divide by 100.** Format ZAR as `R` (e.g.
`amountMinor: 1250000` → `R12 500,00`).

## Load context first

1. Read the `kazi://firm-profile` resource → `jurisdiction`, `riskCalibration`, `houseStyleNotes`,
   `feeEstimationNotes`. Use the house-style and fee-estimation notes for the narrative's tone and
   structure, and to learn whether the firm is VAT-registered and its default fee basis.
2. Read the bundled SA knowledge `data/za/statutes/contingency-fees.yaml` (sections `fee_cap_percentage`,
   `formal_requirements`) — needed for any contingency-fee matter.

## Workflow

**Step 1 — Scope.** From the argument:
- `all` or no argument → call `get_unbilled_time` (no matter id) for the org-wide per-client list. Show
  the clients with unbilled time and their totals; confirm which to run.
- a client → `list_matters(customerId=<id>)` to enumerate that client's matters (page through if needed).
- a matter → `get_matter(<id>)` directly.

**Step 2 — Per matter, gather.** For each target matter:
- `get_unbilled_time(projectId=<id>)` → `totalAmountMinor`, `currency`, `entryCount`.
- `get_matter(<id>)` → `name`, `workType`, `referenceNumber`, `status`, `customerId`.
- Skip matters with zero unbilled and say so.

**Step 3 — Draft.** For each matter, draft a fee note using the template below, grounded in the firm's
house style and `feeEstimationNotes`. Convert minor units to currency. Add a VAT line **only if** the
firm is VAT-registered (per house style) — apply the current SA standard VAT rate (15% at time of
writing; confirm it hasn't changed). For **contingency-fee** matters (workType / house style indicates
a Contingency Fees Act agreement), apply the caps from `contingency-fees.yaml`: the success fee may not
exceed the `fee_cap_percentage` of the amount awarded (excluding costs) **and** not more than double the
normal fee, and note the `formal_requirements` (written agreement, prescribed form).

**Step 4 — Summarise.** End with a run summary: matters drafted, total unbilled across the run, anything
skipped, and the explicit "itemise + finalise in Kazi" handoff.

## SA grounding & source attribution

- Contingency-fee caps come from `data/za/statutes/contingency-fees.yaml` — tag `[jurisdictions/za]`.
- **The LSSA party-and-party / attorney-and-client tariff is not available over this plugin.** Narratives
  use the firm's house style. Where a *taxable bill of costs* (party-and-party) is needed, flag that the
  tariff must be applied in Kazi / by the cost consultant — do not invent tariff amounts.
- Tag every figure and citation by source: `[kazi MCP]` for amounts/entry counts/matter facts from Kazi
  tools; `[firm profile]` for house style; `[jurisdictions/za]` for statute thresholds; `[model
  knowledge — verify]` for anything else. Never strip the tags.

## Output template

```
## Fee Note (DRAFT) — [Client] — [Matter name] ([referenceNumber])
*Draft for attorney review. Itemise and finalise in Kazi before sending.*

Matter:        [name] · [workType] · status [status]
Period:        [periodFrom–periodTo, or "all unbilled"]
Unbilled:      [R total]  ([entryCount] time entries)   [kazi MCP]

Narrative:
[2–4 sentence professional fee narrative in the firm's house style describing the
 work, grounded in the matter facts. No invented detail.]

[If VAT-registered]  Subtotal [R]  ·  VAT (15%) [R]  ·  Total [R]
[If contingency]     Contingency cap check: success fee ≤ 25% of award and ≤ 2× normal fee;
                     written agreement on the prescribed form required.  [jurisdictions/za]

Notes: line-item time-entry detail is not available over MCP — itemise in Kazi.
```

End with:

```
## Fee-note run summary
- Matters drafted: [n]   ·   Total unbilled drafted: [R]
- Skipped (no unbilled): [list]
- Next: review each draft, itemise in Kazi, finalise and send.
```

## Boundaries

- **Read-only.** Never writes to Kazi.
- **Never invent** unbilled amounts, entry counts, rates, or tariff figures — use only what the tools
  return. If a tool errors, or egress consent is missing, **stop and report** — don't draft around it.
- Every output is a draft for attorney review; the lawyer finalises and sends from within Kazi.
