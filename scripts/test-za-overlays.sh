#!/usr/bin/env bash
# Run all ZA overlay validation checks.
# Usage: bash scripts/test-za-overlays.sh
# Exits 0 if all pass, 1 if any fail.

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
ROOT="$(dirname "$SCRIPT_DIR")"
ERRORS=0

echo "=== ZA Overlay Validation ==="
echo ""

echo "--- 1. Statute YAML schema ---"
if python3 "$SCRIPT_DIR/validate-za-statutes.py"; then
    echo "PASS: statute validation"
else
    echo "FAIL: statute validation"
    ERRORS=$((ERRORS + 1))
fi
echo ""

echo "--- 2. Router cross-references ---"
if python3 "$SCRIPT_DIR/validate-za-router.py"; then
    echo "PASS: router validation"
else
    echo "FAIL: router validation"
    ERRORS=$((ERRORS + 1))
fi
echo ""

echo "--- 3. Template completeness ---"
if python3 "$SCRIPT_DIR/validate-za-templates.py"; then
    echo "PASS: template validation"
else
    echo "FAIL: template validation"
    ERRORS=$((ERRORS + 1))
fi
echo ""

echo "--- 4. US concept leak check ---"
US_CONCEPTS='FMLA|FLSA|at.will employment|EEOC|NLRB|WARN Act|Cal-WARN|PAGA'
LEAKS=$(grep -rinE "$US_CONCEPTS" \
    "$ROOT/jurisdictions/za/employment-legal/topics/" \
    "$ROOT/jurisdictions/za/statutes/" \
    2>/dev/null || true)

# Filter out legitimate references in privilege caveat explanations
FILTERED=$(echo "$LEAKS" | grep -v "privilege" | grep -v "FRCP" | grep -v "^$" || true)

if [ -n "$FILTERED" ]; then
    echo "FAIL: US concepts found in ZA overlay files:"
    echo "$FILTERED"
    ERRORS=$((ERRORS + 1))
else
    echo "PASS: no US concept leaks"
fi
echo ""

echo "--- 5. Watchlist validation ---"
if python3 "$SCRIPT_DIR/validate-za-watchlist.py"; then
    echo "PASS: watchlist validation"
else
    echo "FAIL: watchlist validation"
    ERRORS=$((ERRORS + 1))
fi
echo ""

echo "--- 6. Retired-literal check ---"
# Maintained list of superseded literal values that must not appear in prose files.
# Format: one extended-regex pattern per entry (no trailing slash needed).
# Scope: jurisdictions/za/**/*.md and */skills/cold-start-interview/SKILL.md
# Excludes: docs/ planning records; jurisdictions/za/statutes/*.yaml (closed
#   historical entries legitimately contain old values).
# To add a retired literal in a later PR, append to RETIRED_LITERALS below.
RETIRED_LITERALS=(
    # PR 3 (employment refresh) — superseded BCEA earnings threshold and
    # minimum-wage literals. Prose must point at the YAML key, not the figure.
    "254371\.67"       # 2024 BCEA earnings threshold (per annum)
    "254,371\.67"      # same, comma-formatted
    "R27\.58"          # 2024 national minimum wage (per hour)
    "R13\.97"          # 2024 EPWP minimum wage (per hour)
    # PR 4 (commercial/corporate/litigation refresh) — superseded VAT rate and
    # pre-1-May-2026 merger thresholds/fees. Precise old figures live only in the
    # closed YAML entries (statutes/*.yaml, excluded from this scan); prose must
    # point at the YAML key. The bare "16%" VAT literal is intentionally NOT
    # listed (too many false positives, e.g. B-BBEE weightings); the withdrawn
    # 15.5% rate is the unique VAT tell.
    "15\.5%"           # abandoned 2025 VAT increase (never took effect)
    "R6\.6 ?b"         # pre-2026 large-merger combined threshold (R6.6bn/R6.6b)
    "R190 ?m"          # pre-2026 large-merger target threshold (R190m/R190 million)
    "R600 ?m"          # pre-2026 intermediate-merger combined threshold
    "R165 ?000|R165,000|R165k"   # pre-2026 intermediate-merger filing fee
    "R550 ?000|R550,000|R550k"   # pre-2026 large-merger filing fee
)

# Build the list of files to scan
SCAN_FILES=()
while IFS= read -r -d '' f; do
    SCAN_FILES+=("$f")
done < <(find "$ROOT/jurisdictions/za" -name "*.md" -not -path "*/statutes/*" -not -path "*/docs/*" -print0 2>/dev/null)
while IFS= read -r -d '' f; do
    SCAN_FILES+=("$f")
done < <(find "$ROOT" -maxdepth 4 -path "*/skills/cold-start-interview/SKILL.md" -print0 2>/dev/null)

if [ "${#RETIRED_LITERALS[@]}" -eq 0 ]; then
    echo "PASS: retired-literal list is empty (no literals to check)"
else
    RETIRED_PATTERN=$(printf '%s\n' "${RETIRED_LITERALS[@]}" | paste -sd '|' -)
    if [ "${#SCAN_FILES[@]}" -eq 0 ]; then
        echo "PASS: no prose files found to scan"
    else
        RETIRED_HITS=$(grep -rlE "$RETIRED_PATTERN" "${SCAN_FILES[@]}" 2>/dev/null || true)
        if [ -n "$RETIRED_HITS" ]; then
            echo "FAIL: retired literals found in prose files:"
            echo "$RETIRED_HITS"
            ERRORS=$((ERRORS + 1))
        else
            echo "PASS: no retired literals found"
        fi
    fi
fi
echo ""

echo "=== Results ==="
if [ "$ERRORS" -eq 0 ]; then
    echo "ALL CHECKS PASSED"
    exit 0
else
    echo "$ERRORS CHECK(S) FAILED"
    exit 1
fi
