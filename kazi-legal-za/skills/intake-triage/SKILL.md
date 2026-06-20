---
name: intake-triage
description: >
  Triage a new matter before it's opened: check the firm's existing clients and
  matters for conflicts, recommend the matter type and governing statute, the
  likely court / forum, and flag the deadlines that bite early (prescription,
  CCMA, POPIA). Reads existing clients/matters over the Kazi MCP server and
  drafts a triage memo. Use when the user says "new matter", "intake",
  "conflict check", "can we take this on", or "triage this".
argument-hint: "[describe the new matter / prospective client]"
---

# /intake-triage

A first-pass triage of a prospective matter — conflicts, forum, governing law, early deadlines.

## Read-only, draft-only — advisory, not a clearance

Reads the firm's existing clients and matters over MCP and **drafts** a triage memo. It never writes to
Kazi and it does **not** clear conflicts or accept the matter — the attorney confirms the conflict
position and the decision to act, in Kazi. The conflict scan here is a prompt for the attorney's check,
not a substitute for it.

## Setup gate

Read `~/.claude/plugins/config/claude-for-legal/kazi-legal-za/CLAUDE.md`. If missing or `[PLACEHOLDER]`,
**stop** and say "Run `/kazi-legal-za:connect-kazi` first."

## Load context first

- Read `kazi://firm-profile` → `jurisdiction`, practice areas, `riskCalibration` — to judge fit and tone.
- Read the bundled SA knowledge under `data/za/statutes/`: `magistrates-courts.yaml`
  (`district_court_monetary_jurisdiction`, `regional_court_monetary_jurisdiction`),
  `superior-courts.yaml` (`high_court_jurisdiction`), `prescription.yaml` (`general_debt_prescription`,
  `prescription_begins`), and `contingency-fees.yaml` (`fee_cap_percentage`) for fee-arrangement options.

## Workflow

**Step 1 — Conflict scan.** From the description, extract the prospective client name and any adverse
parties. Scan the firm's existing records:
- `list_clients` (page through) — does the prospective client, or an adverse party, already exist as a
  client? Match on name; flag near-matches for the attorney to verify.
- `list_matters` (optionally `customerId` for a matched client) — is there an existing or past matter
  that could create a conflict (acting against a current/former client)?
Report matches as **possible** conflicts for the attorney to confirm — never declare "no conflict".

**Step 2 — Characterise the matter.** From the description, identify the matter type / practice area and
the governing statute(s). Note whether it fits the firm's practice areas (firm profile).

**Step 3 — Forum & quantum.** Recommend the likely court / forum using the monetary-jurisdiction
thresholds (Magistrates' district vs regional vs High Court) from `magistrates-courts.yaml` /
`superior-courts.yaml`. If the claim value is unknown, say what threshold would decide it.

**Step 4 — Early-deadline flags.** Flag the deadlines that bite at intake — prescription period and when
it begins (`prescription.yaml`), and any matter-type-specific clocks (e.g. CCMA 30-day referral for
unfair dismissal, POPIA 72-hour breach notification) — so nothing is missed before the matter is opened.

**Step 5 — Fee arrangement.** Note viable fee options; if a contingency fee is contemplated, state the
Contingency Fees Act cap and formal-agreement requirement (`contingency-fees.yaml`).

## Source attribution

Tag everything: `[kazi MCP]` for existing client/matter matches; `[jurisdictions/za]` for jurisdiction
thresholds, prescription, and fee caps; `[firm profile]` for practice-area fit; `[model knowledge —
verify]` for matter characterisation and any deadline not drawn from the bundled statutes (e.g. CCMA /
POPIA clocks — verify the current period). Never strip the tags.

## Output template

```
## Intake triage (DRAFT) — [Prospective client]
*Advisory. The attorney confirms conflicts and the decision to act, in Kazi.*

**Possible conflicts** (confirm in Kazi)
- [matched client/matter] — [why it may conflict]   [kazi MCP]
- [or: "No matches found in existing clients/matters — attorney to confirm independently."]

**Matter type & governing law**: [type] — [statute(s)]   [jurisdictions/za]/[model knowledge — verify]
**Likely forum**: [Magistrates' district/regional | High Court] — [threshold reasoning]   [jurisdictions/za]
**Early deadlines**: prescription [period, when it begins]; [other clocks]   [jurisdictions/za]/[verify]
**Fee options**: [normal | contingency — cap 25% of award & ≤2× normal fee, written agreement]   [jurisdictions/za]
**Practice-area fit**: [fits / outside firm's areas]   [firm profile]
```

## Boundaries

- **Read-only.** Never writes to Kazi.
- **Never clear a conflict or declare "no conflict"** — report matches and absences; the attorney
  decides. Never accept or decline the matter.
- **Never invent** existing clients/matters or statutory thresholds — use only the tools and bundled
  statutes. Stop and report on tool error / missing consent.
- Advisory draft for attorney review; the decision and the conflict clearance happen in Kazi.
