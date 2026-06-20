# PRD — Kazi-Grounded Skill Pack (`kazi-legal-za` plugin)

**Status:** Ready to build
**Date:** 2026-06-20
**Repo:** `claude-for-legal-sa` (this repo) — the build lands here, not in Kazi.
**Builds on:** Kazi Phase 78 (MCP server, shipped) + the 2026-06-14 MCP plugin strategy note
(`b2b-strawman/.claude/ideas/mcp-plugin-strategy-2026-06-14.md`).
**Pointer in Kazi:** none required — tracking lives here per founder decision (2026-06-20).

---

## 1. System context (what already exists)

Two assets exist today and are **severed** from each other:

**(a) The Kazi MCP server — shipped (Phase 78, PRs #1454–#1461).**
A per-tenant, per-user-authenticated remote MCP server, Spring AI 2.0 Streamable HTTP at `/mcp`
(default `http://localhost:8080/mcp`; prod behind the gateway). It exposes a **read-only** catalogue
of the firm's own live data, with auth, POPIA consent, and audit already built:

| Tools (read-only) | Resources |
|---|---|
| `list_matters` · `get_matter` · `get_matter_activity` | `kazi://matter` |
| `list_clients` · `get_client` | `kazi://client` |
| `get_unbilled_time` | `kazi://firm-profile` |
| `list_invoices` · `get_invoice` | |
| `get_trust_balance` · `list_trust_transactions` (§86-sensitive, read-only) | |
| `list_compliance_gaps` · `search_documents` · `get_document_url` | |
| `get_audit_events` · `kazi_ping` | |

- **Auth (ADR-303):** OAuth 2.0 protected-resource. The whole `/mcp` request traverses the JWT
  resource-server chain; the bearer token resolves tenant → member → capabilities exactly like an
  inbound API call. A user sees only what their Kazi role permits. RFC 9728 protected-resource
  metadata is advertised (`kazi.mcp.resource-url`).
- **Enablement + consent:** `POST /api/integrations/mcp/enable|revoke`, `GET /status`. Data egress to
  an LLM requires an explicit, append-only POPIA consent record (`mcp_egress_consents`,
  `GRANTED`/`REVOKED`). No consent → no egress.
- **Audit:** every tool call and session is logged (`mcp.*` / `ai.specialist.*`), giving the firm a
  POPIA-defensible trail of what AI touched which client data.

**(b) This repo — already a Claude Code plugin marketplace.**
`claude-for-legal-sa` is the fork of Anthropic's `claude-for-legal`: `.claude-plugin/marketplace.json`
lists 13 plugins (commercial, employment, litigation, …) with ~85 upstream skills. The SA layer adds
`jurisdictions/za/` (47 statute YAMLs + topic overlays), the `jurisdiction-expansion` skill, and
validator scripts under `scripts/`.

**The gap.** Every existing plugin's `.mcp.json` points at Slack / Google Drive — **none point at
Kazi.** The SA overlay is knowledge-as-data, not skills wired to live firm data. The MCP server has
**zero consumers**. This PRD builds the missing consumer: the "Phase C — skill pack + Claude-for-Legal
bridge" from the strategy note.

---

## 2. Objective

Ship **one new first-party plugin, `kazi-legal-za`**, in this marketplace. A SA law firm installs it
into their own Claude (Code / Desktop / claude.ai), points it at their Kazi tenant's `/mcp` endpoint,
and gets SA-legal-tuned skills **grounded in their live trust ledger, unbilled time, matter file, and
FICA state** — drafted by their own Claude, on their own token budget.

Positioning (unchanged): **"Bring your own Claude — Kazi provides the grounded context."**

**v1 posture: read-only intelligence.** Claude reads via MCP and *drafts*; a human reviews and commits
the result back into Kazi by hand. No write tools in v1. This sidesteps the §86 trust / Attorneys Act
write minefield and ships fast. The v2 write-back contract is specified (§9) but not built.

---

## 3. Constraints & assumptions

- **No Kazi backend changes.** This plugin is a pure consumer of the shipped MCP server. If a skill
  needs data the catalogue doesn't expose, that's a finding to raise against Kazi — not a reason to
  add backend code in this PRD's scope.
- **Reuse, don't fork.** Auth is the existing OAuth flow; do not invent a parallel token model.
  Every tool call is already tenant/capability-scoped server-side — the plugin trusts that, never
  re-implements authorization.
- **Marketplace conventions hold** (this repo's `CLAUDE.md`): one skill per `skills/<name>/SKILL.md`
  with a `description`; `.claude-plugin/plugin.json` mirrors the marketplace entry field-for-field;
  `claude plugin validate` must pass; skill names in prose must be canonical (real directory names).
- **SA-grounding is mandatory, not decorative.** Every drafting skill cites the relevant
  `jurisdictions/za` knowledge (see §6). Generic-legal output that ignores SA thresholds is a defect.
- **POPIA-first.** Skills assume egress consent is granted server-side; they surface (never bypass)
  the consent/enablement state and remind the user that client PII is flowing into their Claude
  context. Source-attribution guardrails (from `mcp-requirements-za.md`) apply unchanged.
- **Upstream-additive.** Don't modify upstream Anthropic plugins; `kazi-legal-za` is a sibling. The
  bridge (§7) is documentation + thin glue, not edits to the 13 existing plugins.

---

## 4. Plugin layout

```
kazi-legal-za/
  .claude-plugin/plugin.json     # name, version, description, author (b2mash)
  .mcp.json                      # the Kazi MCP server connection (see §8)
  CLAUDE.md                      # practice-profile template (firm name, tenant URL, house style)
  README.md                      # install + connect + first-run walkthrough
  skills/
    connect-kazi/SKILL.md        # one-time OAuth connect + consent check (onboarding)
    fee-note-run/SKILL.md        # monthly fee-note run
    trust-reconciliation/SKILL.md# §86 trust reconciliation check
    fica-gap-review/SKILL.md     # FICA/KYC gap review
    matter-brief/SKILL.md        # client-ready matter status brief
    intake-triage/SKILL.md       # new-matter triage against templates + conflicts
    kazi-bridge/SKILL.md         # how to run upstream legal skills against Kazi data (§7)
    customize/SKILL.md           # copies CLAUDE.md template to user config (marketplace convention)
  agents/                        # (optional) read-only sub-agents if a skill fans out
  data/                          # SA knowledge bundled/symlinked from jurisdictions/za (see §6)
  hooks/hooks.json               # stub (optional)
```

Plus repo-level additions:
- `scripts/` — `kazi-doctor`, `validate-kazi-skill-grounding.py` (see §8 tools/scripts).
- `.claude-plugin/marketplace.json` — register the new plugin (see §10).

---

## 5. The v1 skills

All skills are **read-only orchestrations** of the MCP catalogue. Each ends by producing a draft the
user reviews and commits back in Kazi by hand. Each skill's `SKILL.md` states: the MCP tools it calls,
the `jurisdictions/za` knowledge it cites, the output artefact, and an explicit "human commits this in
Kazi" handoff.

### 5.1 `connect-kazi` (onboarding)
- **Purpose:** one-time setup. Verify the `.mcp.json` endpoint, run the OAuth connect, confirm egress
  consent is `GRANTED` (calls `GET /api/integrations/mcp/status` guidance), `kazi_ping` to prove the
  link, and `get_firm-profile` to load house style.
- **Tools:** `kazi_ping`, `kazi://firm-profile`.
- **Output:** a "connected as <member>, role <…>, consent <state>" confirmation + what the role can/can't see.

### 5.2 `fee-note-run` (highest revenue proximity)
- **Purpose:** monthly fee-note run. Pull unbilled time across matters → draft LSSA-tariff-aware fee-note
  narratives, one per matter, grouped/totalled.
- **Tools:** `list_matters`, `get_unbilled_time`, `kazi://firm-profile` (billing house style).
- **SA knowledge:** LSSA / party-and-party vs attorney-and-client tariff; contingency fee cap; VAT.
- **Output:** draft fee-note narratives per matter; the user pastes/approves into Kazi's invoicing.

### 5.3 `trust-reconciliation` (high-trust differentiator)
- **Purpose:** §86 trust reconciliation check. Read trust balance + transactions, flag anomalies
  (negative balances, business/trust commingling indicators, stale unallocated funds).
- **Tools:** `get_trust_balance`, `list_trust_transactions`, `list_matters`.
- **SA knowledge:** Attorneys Act / LPA §86, Rule 54, §86(4) investment rules.
- **Output:** a read-only anomaly report. **Never writes.** Flags for the attorney to action in Kazi.

### 5.4 `fica-gap-review`
- **Purpose:** read a matter/client's compliance checklist, identify missing FICA/KYC docs, draft the
  client request letter.
- **Tools:** `list_compliance_gaps`, `get_client`, `get_matter`.
- **SA knowledge:** FICA CDD tiers (standard/enhanced/ongoing), acceptable docs (Smart ID, CIPC, trust
  deeds, CK forms), PEP / beneficial-ownership triggers (s21B, 25%), RMCP (s42).
- **Output:** gap list + a draft "please provide the following" client email.

### 5.5 `matter-brief`
- **Purpose:** synthesise activity feed + milestones + deadlines into a plain-language, client-ready
  status update.
- **Tools:** `get_matter`, `get_matter_activity`, `search_documents`.
- **Output:** a plain-language matter brief the attorney edits and sends.

### 5.6 `intake-triage`
- **Purpose:** analyse a new-matter description against practice-area templates and recent matters for
  conflicts; recommend matter type, governing statute, court routing, risk flags.
- **Tools:** `list_clients`, `list_matters` (conflict scan), `kazi://firm-profile`.
- **SA knowledge:** matter-type→statute map; Magistrate vs High Court routing; conflict classification
  (absolute vs consentable, former-client rules); prescription / CCMA 30-day / POPIA 72hr flags.
- **Output:** a triage memo. Conflict checks are advisory — the attorney confirms in Kazi.

---

## 6. SA statute knowledge bundling

Each drafting skill must reference the relevant `jurisdictions/za` knowledge so output is SA-grounded.

- **Mechanism (decide at architecture time):** prefer **referencing** `jurisdictions/za/...` by relative
  path from within each `SKILL.md` over copying, to avoid drift. If Claude Code plugin packaging can't
  resolve cross-plugin relative paths at install time, fall back to a build-time **symlink/copy into
  `kazi-legal-za/data/`** with a `scripts/` check that keeps it in sync (§8).
- **Mapping:**
  | Skill | Knowledge source |
  |---|---|
  | `fee-note-run` | LSSA tariff notes + practice-profile billing sections |
  | `trust-reconciliation` | Attorneys Act / LPA §86 + Rule 54 (statutes/overlays) |
  | `fica-gap-review` | `jurisdictions/za/statutes/fica*.yaml` + KYC overlay |
  | `intake-triage` | matter-type→statute map; `corporate-legal`/`commercial-legal` topic overlays |
- **Freshness:** skills carry no hard-coded thresholds beyond what the YAML provides; the
  statute-freshness validator (§8) warns when a cited YAML's `last_confirmed` is stale.

---

## 7. Claude-for-Legal bridge (`kazi-bridge` skill + doc)

The force multiplier: make the **85 upstream generic legal skills Kazi-aware** without editing them.

- A `kazi-bridge/SKILL.md` + a `docs/` note that explains: with the Kazi MCP server connected, any
  upstream skill (e.g. `commercial-legal:contract-review`, `litigation-legal:chronology`) can be run
  "against matter X in Kazi" — Claude pulls the matter file, documents, and parties via the Kazi tools,
  then runs the generic skill on that grounded context.
- Includes 2–3 worked examples ("run a contract review on the latest document in matter #1234").
- States the boundary clearly: upstream skills still draft only; commit-back is manual in Kazi.

---

## 8. Connection, tools & scripts

### 8.1 `.mcp.json`
- One `mcpServers` entry, `type: http`, `url` = the firm's Kazi `/mcp` endpoint (templated, default
  documented). Title/description name it "Kazi (your firm's data)".
- README documents the OAuth connect flow (ADR-303 protected-resource), how to find the tenant URL,
  and that egress consent must be granted in Kazi Settings first.

### 8.2 Tools / scripts (repo `scripts/`)
- **`kazi-doctor`** — connection check: resolves the endpoint, validates the OAuth/metadata handshake,
  calls `kazi_ping`, reports member/role/consent state, and prints the first failing hop on error.
- **`validate-kazi-skill-grounding.py`** — lint: every drafting skill references a real
  `jurisdictions/za` path and a live MCP tool name; fails CI on a dangling reference (mirrors the
  existing `lint-tool-scope.py` / `validate-za-*` family).
- **statute-freshness check** — extend an existing `validate-za-statutes.py` pass to warn on stale
  `last_confirmed` for any YAML a `kazi-legal-za` skill cites.
- **install/config helper** — scaffolds the user's `CLAUDE.md` (firm name, tenant URL, house style),
  reusing the `customize` skill convention.

---

## 9. v2 write-back contract (spec only — DO NOT BUILD)

Reserve the design so v2 isn't reinvented. v2 adds `propose_*` tools to the **Kazi** MCP server (not
this repo); this plugin would later call them. The contract:

- A write tool (`propose_fee_note`, `propose_kyc_complete`, …) **does not mutate state** — it creates an
  `AiExecutionGate` (PENDING) exactly as the in-product skills do.
- The attorney approves/rejects **inside Kazi** (existing `AiExecutionGateController` + UI), never in
  Claude.
- Audit records "AI-suggested (via MCP) → attorney-approved" with actor + timestamp.
- Liability surface stays identical to the in-product path; v2 is "expose existing gate creation over
  MCP," not new safety machinery.

This PRD ships **reads only**. v2 is a separate `/ideate` when its turn comes.

---

## 10. Marketplace registration

- Add a `kazi-legal-za` entry to `.claude-plugin/marketplace.json` with `source: "./kazi-legal-za"`,
  `author: { name: "b2mash" }` (NOT Anthropic — this is the first-party Kazi plugin), description
  10–2000 chars. Respect invariant I1 (curated order — ask before re-sorting) and I8 (source dir must
  contain `.claude-plugin/plugin.json`).
- `plugin.json` `name`/`description`/`author` mirror the marketplace entry field-for-field.

---

## 11. Out of scope

- **Any Kazi backend change.** Pure consumer.
- **Any write-back tool / mutation.** v1 is read-only (§9 is spec-only).
- **New external MCP data connectors** (SAFLII / CCMA / Gazette / LexisNexis) — already deferred in
  `mcp-requirements-za.md`. This plugin connects to **Kazi**, not to legal-research sources.
- **Editing the 13 upstream plugins.** The bridge is additive glue + docs only.
- **Self-serve hosting of the Kazi MCP server.** Hosting is a Kazi-side decision (strategy note risk #2).

---

## 12. Validation / acceptance (v1 is "done" when)

1. `claude plugin validate .claude-plugin/marketplace.json` and `claude plugin validate kazi-legal-za`
   both pass; existing repo validators stay green.
2. `kazi-doctor` connects to a running Kazi MCP server, completes the OAuth handshake, and reports
   member/role/consent.
3. Each of the 6 skills, run against a seeded Kazi tenant, calls its declared MCP tools and produces its
   declared artefact — **observed end-to-end** (Claude → MCP tool call → Kazi audit log entry → draft
   output), not inferred. (Mirrors Kazi's "PASS means observed" bar.)
4. `validate-kazi-skill-grounding.py` passes — no skill references a dead `jurisdictions/za` path or a
   non-existent MCP tool.
5. The `kazi-bridge` worked examples run an upstream skill against live Kazi matter data successfully.
6. README walkthrough takes a fresh user from install → connect → first fee-note draft.

---

## 13. Suggested build sequence (epics → slices)

Achievable in ~7 epics. One concern per slice; each verified before the next.

1. **E1 — Plugin skeleton + connection.** `plugin.json`, `.mcp.json`, `CLAUDE.md` template, README
   stub, `connect-kazi` skill, marketplace registration, `kazi-doctor`. *Verify: validate passes,
   doctor connects, ping works.*
2. **E2 — SA knowledge bundling + grounding linter.** Reference/symlink mechanism (§6),
   `validate-kazi-skill-grounding.py`. *Verify: linter green on a sample skill.*
3. **E3 — `fee-note-run`.** Highest revenue proximity; exercises `list_matters` + `get_unbilled_time` +
   firm-profile + LSSA grounding.
4. **E4 — `trust-reconciliation`.** §86 read-only anomaly report.
5. **E5 — `fica-gap-review`.** Compliance-gap → client-request draft.
6. **E6 — `matter-brief` + `intake-triage`.** Activity synthesis + conflict/triage memo.
7. **E7 — `kazi-bridge` + README walkthrough + v2 contract doc.** Bridge skill, worked examples, the
   `docs/` v2 write-back contract (§9), end-to-end README.

---

## 14. Open decisions for architecture/build

- **Knowledge reference vs copy** (§6) — resolve based on how Claude Code resolves cross-plugin paths
  at install time. Default: reference; fall back to synced symlink.
- **`agents/` sub-agents** — only if a skill genuinely needs to fan out (e.g. fee-note across many
  matters). Default: none in v1; keep skills flat.
- **Endpoint templating in `.mcp.json`** — how the firm injects their tenant URL (env var vs
  `customize`-written value). Decide in E1.
- **Hosting/auth UX** — the OAuth connect from Claude Desktop vs Claude Code may differ; document both
  paths in README, surface the difference in `connect-kazi`.
