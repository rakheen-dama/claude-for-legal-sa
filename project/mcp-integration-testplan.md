# MCP Integration Testplan — `kazi-legal-za` ↔ Kazi MCP server

**What this tests:** the live Claude–Kazi integration — a Claude client connecting to the Kazi `/mcp`
server over OAuth and the `kazi-legal-za` skills running against real seeded data.

**What this is NOT:** a `/qa-cycle-kc` run. That harness drives the Kazi **browser UI** (Playwright on
`:3000`); the MCP integration has no UI — Claude *is* the client, calling JSON-RPC tools over HTTP. This
plan targets that surface instead.

**Three layers, run in order** — a failure at a lower layer blocks the ones above:
1. **Transport & auth** — OAuth → member-scoped tool calls, consent gating, audit.
2. **Tool correctness** — each of the 15 tools returns its documented shape against seeded data.
3. **Skill behaviour** — the 7 skills orchestrate tools into correct, guardrail-respecting drafts.

> **"PASS means observed."** Record evidence for every test (tool output, a Kazi audit id, or a
> screenshot). Inferring PASS from "looks right" is not PASS.

---

## Prerequisites (once, in order)

- [ ] **P1 — Stack up.** `bash compose/scripts/dev-up.sh` then `bash compose/scripts/svc.sh start backend gateway frontend`. Confirm `svc.sh status` shows backend `:8080`, gateway `:8443`, frontend `:3000`, Keycloak `:8180` healthy. Backend must include PR #1465 (RFC 9728 metadata fix) — restart if it predates 2026-06-19.
- [ ] **P2 — Seed a legal tenant.** Use (or provision) a **legal-vertical** tenant; the demo seeders (`backend/.../demo/seed/LegalDemoDataSeeder`) populate matters, clients, time entries, a trust account, and compliance checklists. Log into `:3000` as the tenant's Keycloak user and **confirm in the UI** that there are: ≥2 matters, ≥1 client (one a company/trust for beneficial-ownership), unbilled time, a trust account with transactions, and a client with open FICA gaps. **Record the ids** you'll need: one matter id, one client id, the trust-account id.
- [ ] **P3 — Enable MCP + consent.** Settings → Integrations → MCP → **Enable** (POPIA consent). Or API: `POST /api/integrations/mcp/enable` body `{"consentVersion":"popia-egress-v1"}` (member JWT). Verify `GET /api/integrations/mcp/status` shows enabled + consented.
- [ ] **P4 — Install the plugin.** Install `kazi-legal-za` into your Claude client (Claude Code: `/plugin`; or local marketplace). Set `KAZI_MCP_URL=http://localhost:8080/mcp`.
- [ ] **P5 — Doctor.** Run `python3 "$CLAUDE_PLUGIN_ROOT/scripts/kazi-doctor.py"` → **PASS** (metadata advertises the Keycloak auth server; `/mcp` returns 401 unauth). This proves the unauthenticated hops before you sign in.
- [ ] **P6 — Connect (interactive OAuth).** In the Claude client, add/authorise the **kazi** MCP server → complete the **Keycloak login + consent** in the browser as the test user. This is the one human step.

---

## Layer 1 — Transport & auth

| # | Step | Expected | PASS criteria |
|---|---|---|---|
| **T1.1** | Call `kazi_ping`. | Returns ok; identifies the signed-in member. | Ping succeeds and names the test member/role. |
| **T1.2** | Run `/kazi-legal-za:connect-kazi`. | "Connected to <firm> as <member> (<role>). Consent: GRANTED." | Member/role/consent match the test user. |
| **T1.3** | As a **limited-role** user, call `list_matters`; compare to an owner/admin's result. | Limited user sees **only** permitted matters. | Result is a strict subset; no leakage of matters the role can't access. (Needs 2 Keycloak users.) |
| **T1.4** | `POST /api/integrations/mcp/revoke`, then call any tool; then re-enable (P3) and retry. | Revoked → `notEnabled` error; re-granted → data. | Data flows **only** with consent granted. |
| **T1.5** | After T1.1–T1.4, inspect the Kazi audit log (DB `audit_*` / audit API) for `mcp.*` reads. | Each tool call logged with actor = member, tenant scoped. | Reads are recorded (POPIA egress trail). |

---

## Layer 2 — Tool correctness

For each: call the tool, assert the **shape**, and reconcile **values** against what P2 showed in the UI.
Money fields are **minor units** (÷100; ZAR → `R`). Lists are paginated (≤50).

| # | Tool (args) | Expected shape | PASS |
|---|---|---|---|
| **T2.1** | `list_matters` | `[{id,name,status,customerId,dueDate,createdAt}]` | shape + page/size work; count matches UI |
| **T2.2** | `get_matter(id)` | `{id,name,description,status,priority,workType,referenceNumber,customerId,dueDate,createdAt,updatedAt,projectRole}` | fields populated; values match UI |
| **T2.3** | `list_clients`, `get_client(id)` | list `{id,name,type,lifecycleStatus}`; detail adds `contacts[{name,email,phone}]`, `linkedMatters[]` | contacts + linked matters correct |
| **T2.4** | `get_unbilled_time` (no id; then `projectId`) | no id → `[{customerName,amountMinor,currency}]`; with id → `{totalAmountMinor,currency,entryCount}` | minor units; totals reconcile with UI |
| **T2.5** | `list_invoices`, `get_invoice(id)` | invoice list + detail | shape + values |
| **T2.6** | `get_trust_balance(trustAccountId[,customerId])` | `{trustAccountId,customerId,balanceMinor,currency}` | account total + per-creditor balances correct |
| **T2.7** | `list_trust_transactions(customerId,trustAccountId)` | `[{id,date,type,amountMinor,currency,reference,status}]` | transactions match UI/ledger |
| **T2.8** | `list_compliance_gaps(customerId)` | `{customerId,ficaStatus,items[{name,status,required}],truncated}` | checklist matches the client's FICA state |
| **T2.9** | `search_documents(...)`, `get_document_url(id)` | docs `{id,name,scope,contentType,sizeBytes,projectId,customerId,createdAt}`; url = presigned link | doc list correct; URL fetches the file |
| **T2.10** | `get_matter_activity(projectId)` | `[{occurredAt,entityType,entityId,entityName,action,message,actor}]` | activity matches the matter timeline |
| **T2.11** | `get_audit_events(...)` | audit event items | returns recent events |

---

## Layer 3 — Skill behaviour

Run each skill against the seeded ids from P2. Assert the **output** and the **guardrails**.

| # | Skill | Run | PASS criteria (output + guardrails) |
|---|---|---|---|
| **T3.1** | `fee-note-run` | `/kazi-legal-za:fee-note-run` (all, then one client) | Per-matter draft; amounts = `get_unbilled_time ÷100`; house style applied; VAT/contingency handled; states "itemise in Kazi"; **no invented line items**; source tags present; **nothing written to Kazi** (verify state unchanged). |
| **T3.2** | `fica-gap-review` | `/kazi-legal-za:fica-gap-review "<client>"` | Lists the **required-but-unsatisfied** items from the checklist; entity/trust client triggers **beneficial-ownership (s21B)**; drafts a request to the client contact; **never asserts "FICA-compliant"**; honours `truncated`. |
| **T3.3** | `matter-brief` | `/kazi-legal-za:matter-brief "<matter>"` | Plain-language brief reflecting **only** real activity; key date from `dueDate`; **no invented progress/outcomes**. |
| **T3.4** | `intake-triage` | `/kazi-legal-za:intake-triage "<new matter desc naming an existing party>"` | Surfaces the existing party as a **possible** conflict (never "no conflict"/"cleared"); forum/quantum cite the bundled thresholds; prescription + fee-cap flagged; never accepts/declines the matter. |
| **T3.5** | `trust-reconciliation` | `/kazi-legal-za:trust-reconciliation <trust-account-id>` | Flags any **debit balance → Rule 54.14.9**; shows the **PENDING-attorney-confirmation caveat** + `[jurisdictions/za — pending]` tag; states it is **not** a Rule 54.15.1 reconciliation; **never writes / moves money**. |
| **T3.6** | `kazi-bridge` | `/kazi-legal-za:kazi-bridge "contract-review on matter <matter>"` | Pulls the document via `search_documents` + `get_document_url`, runs the upstream `commercial-legal` skill on it; upstream guardrails preserved; result is a draft. (Needs `commercial-legal` installed.) |
| **T3.7** | `connect-kazi --check-integrations` | re-probe only | Updates `## Available integrations` to ✓ **only** after a real tool call succeeded; consent line current. |

### Cross-cutting guardrail checks (every L3 test)
- [ ] **Read-only:** after each skill, confirm **no** Kazi state changed (compare before/after).
- [ ] **Source attribution:** `[kazi MCP]` / `[jurisdictions/za]` / `[firm profile]` / `[model knowledge — verify]` tags present and not stripped.
- [ ] **No fabrication:** every figure/item traces to a tool result.
- [ ] **Trust caveat:** T3.5 visibly carries the pending-attorney-confirmation caveat.

---

## Results recording

| Test | Expected | Observed | PASS/FAIL | Evidence (output / audit id / screenshot) |
|---|---|---|---|---|
| T1.1 | | | | |
| … | | | | |

## Exit criteria

- [ ] **All Layer 1 + Layer 2 PASS** — transport, auth scoping, consent gating, and the 15 tools proven against seeded data.
- [ ] **All Layer 3 PASS**, or every FAIL triaged (skill bug vs tool bug vs data) with a follow-up.
- [ ] **Audit log shows the reads** (POPIA trail) — Layer 1 T1.5.
- [ ] Evidence captured per test ("PASS means observed").

## Notes & known gates

- **`trust-reconciliation` (T3.5)** verifies *behaviour and the caveat*, **not** legal accuracy — the §86/Rule 54 statute sections are still **pending attorney sign-off** (`project/trust-accounting-attorney-review.md`).
- The **OAuth login (P6)** is the one unavoidable human step.
- Layer 2 can also be smoke-tested with a scripted bearer token (if the `docteams` realm allows direct-access grants), but Layer 3 needs the skills running in a real Claude client.
- Re-run `kazi-doctor` (P5) first whenever something looks wrong — it isolates transport/metadata problems from skill/tool problems.
