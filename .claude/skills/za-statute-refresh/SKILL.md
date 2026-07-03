---
name: za-statute-refresh
description: >
  Maintainer workflow for refreshing South African statute YAML files, prose overlays,
  and the pending-legislation watchlist. Use when asked to "refresh statutes",
  "statute refresh", "are the ZA values current", "update thresholds", or
  "check staleness".
---

# /za-statute-refresh

Maintainer workflow for keeping `jurisdictions/za/` statute data, prose overlays, and
the watchlist current. Run on a feature branch before raising a PR.

## Step 1 — Report: identify stale files and overdue watchlist items

```bash
python3 scripts/validate-za-statutes.py --strict-staleness
```

The script prints:
- `OK: …` — within the staleness window
- `WARN: …` — stale (demoted to `FAIL:` when `--strict-staleness` is passed)

Staleness windows by `volatility` field:
- `annual` → 12 months (366 days)
- `statutory` → 18 months (548 days)
- `stable` or absent → 36 months (1096 days)

List all stale files grouped by volatility bucket. Then open
`jurisdictions/za/watchlist.yaml` and list any items whose `last_checked` is more
than 90 days ago — those need a status check in Step 5.

## Step 2 — Research: verify values against authoritative sources

For each stale statute file:

1. Read its `authority` and `source_url` fields.
2. Query Perplexity (`mcp__perplexity__perplexity_search` or
   `mcp__perplexity__perplexity_research`) scoped to that authority and URL:
   > "Current [section name] under [statute name], South Africa — confirm figure,
   > effective date, and Government Notice / Gazette reference"
3. Accept a value change **only** with a Government Gazette notice number, GN
   reference, or a direct authority-site URL. **Always distinguish draft/bill figures
   from gazetted finals before writing a value.**

   **Lesson from this repo:** When competition-act merger thresholds were refreshed,
   a draft target figure (R175m) differed from the gazetted final (R200m — per
   GN 7029 GG 54020). The gazetted value shipped; the draft figure was discarded.
   Never accept a Perplexity-sourced draft value as confirmed.

4. Tag every proposed value:
   - `[Gazette — confirmed]` — GN reference verified against the Government Gazette.
   - `[Perplexity — verify]` — figure found but the specific GN could not be
     confirmed; requires expert review before the value is considered authoritative.

Do not apply any change that cannot be sourced to a Gazette ref or authority URL.

## Step 3 — Apply: append-only temporal edits

For each confirmed value change, edit the statute YAML. **Never overwrite a live entry.**

Rules:
- Set `effective_until` on the old entry to the day **before** the new value's
  `effective_from`.
- Add a `_YYYY` successor key (e.g., `earnings_threshold_2025`):
  - `effective_until: null`
  - Updated Gazette ref in `ref`
  - Confidence tag in `note`
- Bump the file's `last_confirmed` date **only** for entries confirmed with a Gazette ref.
- Add `volatility` at the top level if the field is missing.

Illustrative example (close + append):

```yaml
  earnings_threshold:                       # Closed — superseded; retained for temporal queries
    ref: "BCEA s6(3), GN Rxxxx GG xxxxx"
    value: 250000.00
    currency: ZAR
    unit: per_annum
    effective_from: "2024-03-01"
    effective_until: "2025-02-28"           # Day before successor takes effect
    effect: "Employees above threshold excluded from ss9-16, 17(2), 18(3)."
    note: "Superseded by earnings_threshold_2025. Retained for temporal queries."

  earnings_threshold_2025:                  # _YYYY successor key — open entry
    ref: "BCEA s6(3), GN Rxxxx GG xxxxx [Gazette — confirmed]"
    value: 260000.00
    currency: ZAR
    unit: per_annum
    effective_from: "2025-03-01"
    effective_until: null
    effect: "Current threshold. Employees above this excluded from ss9-16, 17(2), 18(3)."
    gazette_date: "2025-02-28"
    note: "Confirmed against GN Rxxxx GG xxxxx."
```

## Step 4 — Prose sweep: retire stale literals

Scan prose files for values that are now superseded. The scope matches the
retired-literal check in `scripts/test-za-overlays.sh`:

```bash
# Prose files in scope
find jurisdictions/za -name "*.md" -not -path "*/statutes/*" -not -path "*/docs/*"
find . -maxdepth 4 -path "*/skills/cold-start-interview/SKILL.md"
```

For each retired numeric value, percentage, or threshold:

1. Grep the prose files for the old figure.
2. Replace prose references with a pointer to the YAML key (e.g.,
   "see `bcea.yaml → earnings_threshold_YYYY` for the current value") or remove.
3. Append the old literal as an extended-regex pattern to `RETIRED_LITERALS` in
   `scripts/test-za-overlays.sh`, following the precision convention already
   documented there (escape `.` and `,`; use ` ?` for optional spacing around units).

Also check `jurisdictions/za/evals/**/*.yaml`: if any eval's `expected_statutes` or
`must_not_contain` list pins a stale figure, update it to match the current YAML key.

## Step 5 — Watchlist pass: update status and promote enacted items

For each item in `jurisdictions/za/watchlist.yaml`:

1. Update `last_checked` to today's date.
2. Research current status via Perplexity if `last_checked` was more than 90 days ago.
3. If a bill or consultation has progressed, update the `status` field.
4. If an item is **enacted and commenced** (proclamation date confirmed in the
   Gazette — not just assented to): promote it into the relevant statute YAML using
   the close+append pattern (Step 3), then set the watchlist `status` to
   `"Enacted — promoted to {statute}.yaml (effective YYYY-MM-DD)"`.
   Do not delete the item; leave it as a closed record.

## Step 6 — Exit gate: validate and produce the reviewer summary

```bash
bash scripts/test-za-overlays.sh
```

All six checks must pass: statute schema, router cross-references, template
completeness, US-concept leak check, watchlist validation, and retired-literal check.

**Do not declare the refresh done without a reviewer-facing change summary.** Format
per `jurisdictions/za/REVIEWER-GUIDE.md`. For each value changed:

```
## Statute changes

| File | Key | Change | Ref | Confidence |
|------|-----|--------|-----|------------|
| `bcea.yaml` | `earnings_threshold_2025` | closed 250000.00; opened 260000.00 | GN Rxxxx GG xxxxx | [Gazette — confirmed] |
| `prescribed-rate-of-interest.yaml` | `prescribed_rate_YYYY_MM` | rate: N.NN% p.a. | statutory formula | [Perplexity — verify] |

## Watchlist changes

| Item | Old status | New status |
|------|-----------|------------|
| … | … | … |

## Prose changes

- `{file}.md`: removed reference to old value; replaced with YAML key pointer.
- `scripts/test-za-overlays.sh`: appended retired literal pattern to RETIRED_LITERALS.
```

Post this summary to the PR description. The skill is not complete until
`test-za-overlays.sh` passes and the reviewer summary is written.
