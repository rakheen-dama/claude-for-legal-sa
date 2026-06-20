# Attorney review — trust-accounting statute sections (pending sign-off)

**Why this exists.** The trust-accounting knowledge that grounds
`/kazi-legal-za:trust-reconciliation` was **authored from web research on 2026-06-20**, not confirmed by
a legal practitioner. Until a South African attorney signs off, every statutory reference in that skill
is tagged `[jurisdictions/za — pending]` and the skill must not be used to produce a compliance opinion.
This checklist lets an attorney confirm each section against the primary source and clear the gate.

**Sections to review:** 6 in `jurisdictions/za/statutes/lpa.yaml`, 4 in `jurisdictions/za/statutes/lpc-rules.yaml`.
Each is also mirrored (synced copy) in `kazi-legal-za/data/za/statutes/` — confirm the **source** file;
re-running `python3 scripts/sync-kazi-knowledge.py` re-bundles after any edit.

**Primary sources used (verify against these or your preferred authority):**
- Legal Practice Act 28 of 2014 — `https://www.justice.gov.za/legislation/acts/2014-028.pdf`
- LPC Rules (GG 41781, 9 July 2018) and amendments — current consolidated version
- De Rebus, *"Determining a trust position"*; LSSA practice guidance

---

## How to use

For each row: read the authored `effect` in the YAML, compare to the source, then mark **✓ confirmed**,
**✎ correct** (note the fix), or **✗ wrong** (note what it should say). Initial + date each. When all
rows are cleared, do the **post-sign-off steps** at the bottom.

## A. `lpa.yaml` — Legal Practice Act 28 of 2014

| Section key | Ref | Claim to confirm | Verdict / correction | Init · date |
|---|---|---|---|---|
| `fidelity_fund_certificate` | s84(1) | A practitioner practising for own account / holding trust money must hold a Fidelity Fund certificate; **no fee recoverable** for work done without one. | | |
| `trust_banking_account` | s86(1) | Must keep a separate trust banking account at a bank (with which the Fidelity Fund has an arrangement); deposit all trust money; keep separate from business money. | | |
| `trust_interest_to_fund` | s86(2) | Interest on the s86(1) trust banking account vests in / is paid to the Fidelity Fund (less permitted bank charges). | | |
| `trust_investment_surplus` | s86(3) | Surplus trust money may be invested in a separate interest-bearing account; interest also vests in the Fund. | | |
| `trust_investment_client_instruction` | s86(4) | On a client's instruction, a separate "s86(4) account" may be opened; interest accrues to **the client**; replaces Attorneys Act s78(2A). | | |
| `trust_accounting_records` | s87 | Must keep proper accounting records of all trust money, per the Council's rules made under s87. | | |

## B. `lpc-rules.yaml` — LPC Rules

| Section key | Ref | Claim to confirm | Verdict / correction | Init · date |
|---|---|---|---|---|
| `trust_funds_sufficiency` | Rule 54.14.8 | Trust banking + trust investment + trust cash at any date ≥ total credit balances of trust creditors; a deficit is a contravention. | | |
| `no_trust_debit` | Rule 54.14.9 | No account of any trust creditor may be in debit. | | |
| `monthly_trust_reconciliation` | Rule 54.15.1 | Monthly: extract a list of trust creditors, total it, compare to the combined trust banking + investment + cash balances (the trust position). | | |
| `trust_records_retention` | Rule 54.10 | Trust accounting records updated monthly; retained ≥ 7 years after the last entry. | | |

## C. Watch-outs (where the author was least certain — check these first)

1. **s86 subsection boundaries.** The split between s86(2) (trust banking account interest → Fund) and
   s86(3) (investment of surplus → Fund) vs s86(4) (client-instruction account, interest → client).
   Confirm the subsection numbers map to the right duty.
2. **s84 fee consequence.** The exact wording/subsection for "not entitled to any fee without an FFC".
3. **Rule numbers.** 54.14.8 / 54.14.9 / 54.15.1 / 54.10 were taken from secondary sources — confirm
   against the **current consolidated** LPC Rules (they have been amended, e.g. Rule 54.14.16 in 2023).
4. **`effective_from: null`.** All trust sections use `null`. If you want temporal accuracy, the LPA
   trust provisions commenced ~1 March 2019 — supply the date to set `effective_from`.
5. **Not yet captured (gap, not error):** the **annual trust audit report within 6 months of financial
   year-end**. Omitted because the author could not pin the exact rule number. Add it if you want the
   skill to flag audit deadlines.

## D. Sign-off

> I have reviewed the sections above against the primary sources. The ✓-marked sections are accurate as
> at the date below; corrections are noted in-line.
>
> Attorney: ________________________  ·  LPC no.: ____________  ·  Date: ____________

## E. Post-sign-off steps (engineering)

Once an attorney has cleared the sections:

1. Apply any corrections to `jurisdictions/za/statutes/lpa.yaml` and `lpc-rules.yaml`.
2. Remove the `note: "Web-sourced 2026-06-20. Pending attorney confirmation."` line from each cleared
   section; set `last_confirmed:` on both files to the sign-off date.
3. Run `python3 scripts/sync-kazi-knowledge.py` to re-bundle into `kazi-legal-za/data/za/`.
4. In `kazi-legal-za/knowledge-map.yaml`, remove the `caveats:` block from `trust-reconciliation`.
5. In `kazi-legal-za/skills/trust-reconciliation/SKILL.md`, drop the "⚠️ Knowledge caveat" section and
   change the source tag from `[jurisdictions/za — pending]` to `[jurisdictions/za]`.
6. Run `python3 scripts/validate-kazi-skill-grounding.py` — the trust-reconciliation caveat warning
   should be gone; 0 errors.
