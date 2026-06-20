---
name: trust-reconciliation
description: >
  Screen a firm's trust account for anomalies against the Legal Practice Act
  s86 and LPC trust rules — debit (negative) balances, suspicious movements,
  and trust-position red flags — and produce a read-only report for the
  attorney. Reads trust balances and transactions over the Kazi MCP server.
  NEVER writes. Use when the user says "trust reconciliation", "trust account
  check", "s86", "trust anomalies", or "check the trust ledger".
argument-hint: "<trust-account-id> [client/customer id to scope to one trust creditor]"
---

# /trust-reconciliation

A read-only anomaly screen over the firm's trust account, framed by LPA s86 and the LPC trust rules.

## ⚠️ Knowledge caveat — read before relying on output

The South African trust-accounting knowledge this skill cites (LPA s84/s86/s87 and LPC Rules
54.14.8 / 54.14.9 / 54.15.1 / 54.10, in `data/za/statutes/lpa.yaml` and `lpc-rules.yaml`) was
**authored from web research and is PENDING ATTORNEY CONFIRMATION**. Until a legal practitioner has
signed off those sections, treat every statutory reference here as `[model knowledge — verify]` and do
**not** present the output as a compliance opinion.

## Read-only, NEVER writes — and not a full reconciliation

This skill **reads** trust balances and transactions and **flags anomalies**. It never writes to Kazi and
never moves money. It is an **anomaly screen**, **not** the formal LPC Rule 54.15.1 monthly trust
reconciliation: that requires comparing the full list of trust creditors against the trust **bank
statement**, which is not exposed over MCP. The formal reconciliation and any correction happen in Kazi
/ the firm's accounting system, signed off by the trust-account practitioner. Say this in the report.

## Setup gate

Read `~/.claude/plugins/config/claude-for-legal/kazi-legal-za/CLAUDE.md`. If missing or `[PLACEHOLDER]`,
**stop** and say "Run `/kazi-legal-za:connect-kazi` first."

## What the data supports

- `get_trust_balance(trustAccountId)` → `{balanceMinor, currency}` for the account (omit the customer for
  the account total; pass a `customerId` for one trust creditor's balance).
- `list_trust_transactions(customerId, trustAccountId)` → `{date, type, amountMinor, currency, reference,
  status}` per transaction.
- There is **no "list trust accounts" tool** — the user must supply the **trust-account id** (and a
  customer id to scope to one creditor). Money is **minor units** (÷100; ZAR → `R`).

## Load context first

Read `data/za/statutes/lpa.yaml` (`fidelity_fund_certificate`, `trust_banking_account`,
`trust_investment_client_instruction`) and `data/za/statutes/lpc-rules.yaml` (`trust_funds_sufficiency`,
`no_trust_debit`, `monthly_trust_reconciliation`) — the duties the anomalies map to.

## Workflow

**Step 1 — Account total.** `get_trust_balance(trustAccountId)` (no customer) → the account balance.

**Step 2 — Per-creditor balances.** For each customer in scope (from the argument, or iterate trust
creditors you can identify via `list_matters` / supplied ids), `get_trust_balance(trustAccountId,
customerId)`.

**Step 3 — Transactions.** `list_trust_transactions(customerId, trustAccountId)` (page as needed) → review
`type`, `amountMinor`, `status`, `reference`, `date`.

**Step 4 — Flag anomalies** that the data can actually show, each mapped to a rule:
- **Debit (negative) balance** on any trust creditor → **Rule 54.14.9** ("no account of any trust
  creditor in debit") — the strongest, most defensible flag.
- **Account total < sum of creditor balances you can see** → possible **Rule 54.14.8** sufficiency issue
  (note you can only see the creditors MCP exposed — not a full trust position).
- Stale `PENDING` transactions, unusually large or round movements, or references suggesting business/
  trust commingling → flag for the practitioner to investigate. Do not conclude wrongdoing.

**Step 5 — Report.** Read-only anomaly report + the explicit "formal reconciliation and any correction
happen in Kazi, signed off by the trust-account practitioner" handoff.

## Source attribution

`[kazi MCP]` for balances and transactions; `[jurisdictions/za — pending attorney confirmation]` for the
LPA/LPC duties; `[model knowledge — verify]` for anything else. Never strip the tags. Never state that the
trust account "balances" or "is compliant" — report only the anomalies found and not found.

## Output template

```
## Trust anomaly screen (DRAFT, read-only) — account [trustAccountId]
*Anomaly screen, NOT a Rule 54.15.1 reconciliation. Statutory refs PENDING ATTORNEY CONFIRMATION.
 Formal reconciliation and any correction happen in Kazi, signed off by the trust-account practitioner.*

Account balance: [R]   [kazi MCP]

### Flags
- 🔴 [creditor] — debit balance [R] → Rule 54.14.9 (no trust creditor in debit)   [kazi MCP]/[jurisdictions/za — pending]
- 🟠 [transaction/ref] — [why it's worth a look]   [kazi MCP]
- [or: "No debit balances detected among the creditors visible over MCP."]

### Not checked here (needs Kazi / accounting system)
- Full trust position vs trust bank statement (Rule 54.15.1)
- Fidelity Fund certificate currency (s84)
```

## Boundaries

- **Read-only. NEVER writes and NEVER moves money.** This is §86-sensitive.
- **Never invent** balances or transactions; use only what the tools return. Stop and report on tool
  error / missing consent.
- **Never present this as a compliance opinion or a completed reconciliation.** It is an anomaly screen
  for the trust-account practitioner, whose sign-off (and the pending statutory confirmation) is required.
