# AI Features Acceptance Test Plan — Kazi app + `kazi-legal-za` plugin + `claude-for-legal-sa`

A single execution plan for a Claude agent to exercise **all three AI surfaces** of the legal demo:

1. **Kazi in-product AI (BYOAK)** — the firm's own Anthropic key drives 5 server-side skills, with
   attorney sign-off gates, cost metering, and audit. (Claude *inside* Kazi.)
2. **`kazi-legal-za` plugin** — the firm's Claude, connected over MCP, runs 7 read-only/draft-only
   skills against live Kazi data. (Claude *calling* Kazi.)
3. **`claude-for-legal-sa`** — the upstream legal skills + the ZA jurisdiction overlay, including the
   bridge that runs upstream skills against Kazi data.

> **Discipline (from CLAUDE.md):** **PASS means observed** — every test records evidence (UI
> screenshot, API response, a `*.audit` event id, a DB/MCP read, or a draft artefact). Inferring PASS
> from "looks right" is forbidden. Mark `DEFERRED` (not PASS) anything you couldn't run.

---

## Prerequisites (given)

- ✅ A **demo-seeded `legal-za` tenant** (e.g. `demo-legal-za-complete`): 5 clients incl. a TRUST
  client (Dlamini Property Trust), 6 matters, unbilled time, a §86 trust account with **one creditor
  in debit (−R3 000)**, a FICA checklist with pending items, and a populated firm profile.
- ✅ A **BYOAK Anthropic key** configured in Kazi (Settings → Integrations → AI).
- ✅ An **authenticated `kazi-legal-za` plugin** in the agent's Claude client (MCP connected, egress
  consent GRANTED).
- A Kazi **member with `owner`/`admin` role** for the tenant (needs capabilities `AI_EXECUTE`,
  `AI_REVIEW`, `AI_MANAGE`, `TEAM_OVERSIGHT`, `AI_ASSISTANT_USE`).

## How the agent operates — two access modes

- **Kazi app** (for in-product AI + app features): drive the web app at `/org/<slug>/...` as the
  logged-in member (browser automation), or call the API with that member's bearer token. UI routes
  and API endpoints are given for each test — use whichever the agent can drive.
- **Claude-with-plugin** (for plugin + upstream skills): invoke `/kazi-legal-za:*` and upstream
  `/<plugin>:*` skills in the agent's own Claude session; the MCP tools read the tenant's live data.

Record the tenant **slug** and these ids up front (from the seed): one **matter id**, the **Dlamini
Property Trust client id**, the **trust-account id**, and a client with **open FICA items**.

---

## Phase 0 — Preconditions (run first; a failure here blocks the relevant phase)

| # | Step | PASS |
|---|---|---|
| **0.1** | Plugin: run `/kazi-legal-za:connect-kazi`. | "Connected … consent GRANTED"; `kazi_ping` + `list_clients` return live data. |
| **0.2** | BYOAK: Settings → Integrations → **AI** card. Confirm provider is a real Anthropic provider (not `noop`); click **Test connection** (`POST /api/integrations/AI/test`). | Test returns **success**. `GET /api/integrations` shows AI `enabled:true` + a `keySuffix`. |
| **0.3** | Firm profile: Settings → AI (`GET /api/ai/profile`). | practice areas + house-style + fee notes populated (not empty defaults). |
| **0.4** | Cost baseline: `GET /api/ai/cost-summary`. | Returns `currentMonthSpentCents`, `monthlyBudgetCents`, `invocationCount` — record the baseline. |
| **0.5** | **Upload sample documents** (the seed has none, and two skills need them): upload a sample **commercial agreement** to a matter, and a sample **ID/FICA doc** to the Dlamini Property Trust client (matter/customer → Documents → Upload). | Both documents show `UPLOADED`; record their document ids. |

---

## Phase 1 — Kazi in-product AI (BYOAK)

These call the firm's Anthropic key, meter cost, and (mostly) create an **attorney-approval gate**.
Each test: **invoke → assert output → check gate → approve/reject → verify effect + audit + cost**.

### 1.1 FICA verification (creates a gate)
1. On the Dlamini Property Trust client, trigger **FICA verification** (`POST /api/ai/skills/fica-verification {customerId}`).
2. **Assert output:** `overallAssessment` (COMPLETE/INCOMPLETE/NEEDS_REVIEW), `riskLevel`, `checklistReview[]`, `missingDocuments[]`, `recommendedActions[]`. SA-grounded (references FICA CDD / s21B for a TRUST client).
3. **Gate:** response `gates[]` includes a `MARK_KYC_COMPLETE` gate (PENDING, expires ~72h). Find it at **`/org/<slug>/ai/reviews`** (`GET /api/ai/gates?status=PENDING`).
4. **Approve** it (`POST /api/ai/gates/{id}/approve`) → **verify the checklist items are now marked complete** in the client's FICA checklist.
5. **Audit:** Settings → Audit log shows `ai.specialist.invoked` then `ai.specialist.approved` with your member as actor.
6. **Cost:** `GET /api/ai/cost-summary` — `currentMonthSpentCents` and `invocationCount` increased vs the 0.4 baseline.

**PASS:** output is structured + SA-grounded; gate created; approval applied the action; both audit events present; cost incremented.

### 1.2 Matter intake
1. Trigger **matter intake** with a free-text matter (`POST /api/ai/skills/matter-intake {customerId, description}`), e.g. *"Debt claim, R180 000, against Naidoo & Partners Developers."*
2. **Assert:** `matterClassification`, `templateRecommendation`, `requiredDocuments[]`, `feeEstimate` (tariff basis, ZAR range), `conflictScreening.status` — and it should flag **Naidoo as a POTENTIAL_CONFLICT** (existing client), plus `riskFlags[]` (e.g. prescription).

**PASS:** classification + fee estimate + conflict detection present and correct for the seeded data.

### 1.3 Contract review (uses the 0.5 document)
1. On the matter with the uploaded agreement, trigger **contract review** (`POST /api/ai/skills/contract-review {documentId, projectId}`).
2. **Assert:** `documentClassification`, `findings[]` (each with `severity`, `clauseReference`, `statutoryReference`), `missingProtections[]`, `overallRiskAssessment`. Findings cite SA statutes where relevant.

**PASS:** real findings tied to the document's clauses, SA-aware.

### 1.4 Drafting
1. Trigger **drafting** for a project + a template (`POST /api/ai/skills/drafting {templateId, projectId}`). (Use a seeded `project_template`; if none, pick any template available in the tenant.)
2. **Assert:** `variableFills[]` (with `source`/`confidence`), `narrativeSections[]`, `clauseRecommendations[]`, `warnings[]`.

**PASS:** variables filled from real matter/firm context; house style reflected.

### 1.5 Compliance audit (org-level)
1. Trigger **compliance audit** (`POST /api/ai/skills/compliance-audit {}`) — org-wide, no input.
2. **Assert:** `overallGrade` (A–F), `categoryScores`, `findings[]` (with `regulatoryBasis`), `recommendations[]`. Should surface the **trust debit** and **pending FICA** items as findings.

**PASS:** grade + findings reflect the seeded compliance gaps.

### 1.6 Gate lifecycle — approve / reject / expire
1. From the gates above, **reject** one (`POST /api/ai/gates/{id}/reject {notes}`) → verify the proposed action did **NOT** apply; audit `ai.specialist.rejected`.
2. Confirm a PENDING gate's `expiresAt` is ~72h out (don't wait — just verify the field). Note the `ai.specialist.expired` path as DEFERRED unless time permits.

**PASS:** reject leaves state unchanged + logs; expiry window correct.

### 1.7 Cost metering + budget enforcement
1. Set a **low monthly budget** below current spend: Settings → AI → `PUT /api/ai/profile {monthlyBudgetCents: <below spend>}`.
2. Invoke any skill again → expect **HTTP 403** "Monthly AI spend … has reached the budget".
3. Raise the budget back (or unlimited) → skill runs again.

**PASS:** budget cap blocks with 403; raising it unblocks. Cost summary math (`remaining = budget − spent`) is correct.

### 1.8 Audit completeness
`GET /api/audit-events?eventType=ai.specialist.*` (or Settings → Audit log, filter `ai.specialist`).
**PASS:** every Phase-1 invocation/approval/rejection appears with actor + timestamp + execution metadata.

### 1.9 Assistant / specialist (Phase 70)
1. `GET /api/assistant/specialists` → list available specialists. On a matter/customer page, use the **Specialist Launcher** button (or `POST /api/assistant/specialists/{id}/sessions`).
2. If driving the API: `POST /api/assistant/chat` (SSE stream) with a context ref; if the specialist proposes a tool call, `POST /api/assistant/chat/confirm {toolCallId, approved}`.
3. Automation queue: `/org/<slug>/settings/automations/ai-queue` (`GET /api/assistant/invocations?status=PENDING_APPROVAL`) → approve/reject one.

**PASS:** a specialist session streams a grounded response; tool-use requires confirmation; queue approve/reject works. *(Note: there is no standalone chat page — access is via launcher buttons / API; record this.)*

### 1.10 BYOAK negative path
1. Toggle the AI integration **off** (`PATCH /api/integrations/AI/toggle {enabled:false}`) or delete the key.
2. Invoke a skill → expect a **clear error** (not a 500/stack trace).
3. Re-enable for the rest of the run.

**PASS:** missing/disabled key fails gracefully with an actionable message.

---

## Phase 2 — `kazi-legal-za` plugin (MCP, read-only & draft-only)

Run in the agent's Claude session. (Full detail in `project/mcp-integration-testplan.md` Layer 3.)

| # | Skill | Run | PASS |
|---|---|---|---|
| 2.1 | `fee-note-run` | `/kazi-legal-za:fee-note-run` | per-matter drafts from unbilled time; house style applied; "itemise in Kazi" stated; no invented figures |
| 2.2 | `fica-gap-review` | `… "Dlamini Property Trust"` | lists pending FICA items + beneficial-ownership (TRUST); drafts client request; never asserts "compliant" |
| 2.3 | `matter-brief` | `… "<matter>"` | plain-language brief from real activity; no invented progress |
| 2.4 | `intake-triage` | `… "debt claim … Naidoo"` | flags Naidoo as **possible** conflict; forum/prescription/fee from bundled statutes |
| 2.5 | `trust-reconciliation` | `… <trust-account-id>` | flags the **−R3 000 debit** (Rule 54.14.9); shows the **pending-attorney-confirmation caveat**; never writes |
| 2.6 | `kazi-bridge` | see Phase 3.3 | — |

**Cross-cut PASS:** after Phase 2, confirm **no Kazi state changed** by the plugin (compare matter/trust/checklist before/after); every draft carries source tags (`[kazi MCP]`, `[jurisdictions/za]`).

---

## Phase 3 — `claude-for-legal-sa` upstream + SA overlay + bridge

| # | Step | PASS |
|---|---|---|
| 3.1 | Run an upstream skill standalone, e.g. `/commercial-legal:nda-review`, on a pasted NDA. | Produces a triage; respects its own guardrails (source tags, privilege). |
| 3.2 | Ask an SA-specific question that should hit the overlay (e.g. the FICA cash-reporting threshold, or LPA §86 trust duties). | Answer cites the `jurisdictions/za` knowledge (FICA s28 R25 000, LPA s86), not generic boilerplate. |
| 3.3 | **Bridge:** `/kazi-legal-za:kazi-bridge "contract-review on matter <Naidoo lease>"`. | Pulls the matter's document via MCP (`search_documents` + `get_document_url`) and runs the upstream `commercial-legal` review on it; upstream guardrails preserved; result is a draft. |

> Note: `trust-reconciliation` and any trust answer carry `[jurisdictions/za — pending]` — the §86/Rule 54
> statute text is **pending attorney sign-off** (`project/trust-accounting-attorney-review.md`). Verify
> the caveat is present; do **not** treat trust output as a compliance opinion.

---

## Phase 4 — Kazi app (non-AI) feature smoke

Exercise the underlying app on the demo tenant (so the AI's grounding data is real and editable):

| Area | Check |
|---|---|
| Matters | list/open a matter; create a new matter; edit status/due date |
| Clients | open Dlamini Property Trust; verify TRUST type + contacts; lifecycle transition |
| Time | log a time entry on a matter; confirm it appears as **unbilled** |
| Invoicing | open a draft invoice; (optionally) approve → sent → record payment |
| Trust | open the §86 account; view transactions; confirm the per-creditor balances incl. the Naidoo debit |
| Documents | the 0.5 uploads appear; download via presigned URL |
| Portal | generate a magic link for a client contact; load the portal read-model |
| Audit | Settings → Audit log shows the domain events from the above (created/updated) |

**PASS:** core CRUD + the trust/invoice/portal workflows function; data stays consistent with what the AI skills read.

---

## Phase 5 — Cross-cutting consistency (the payoff)

| # | Check | PASS |
|---|---|---|
| 5.1 | **Two FICA paths agree:** the in-product `fica-verification` skill (1.1) and the plugin `fica-gap-review` (2.2) identify the **same** outstanding items for the same client. | Gap sets match (modulo phrasing). |
| 5.2 | **Same firm profile grounds both:** the house-style/fee conventions set in the profile show up in both the in-product `drafting`/`contract-review` output **and** the plugin `fee-note-run` narratives. | Consistent tone/fee basis across both surfaces. |
| 5.3 | **Two-headed audit:** in-product AI logs `ai.specialist.*`; the plugin's MCP reads log `mcp.*`. Both visible in the audit log for the same tenant. | Both event families present, attributable to the actor. |
| 5.4 | **Write boundary:** in-product AI changes state only **after** a gate approval; the plugin **never** changes state. | Confirmed by before/after state + audit. |

---

## Results & exit

Record per test: `Test | Expected | Observed | PASS/FAIL/DEFERRED | Evidence`.

**Exit criteria:**
- [ ] Phase 0 all PASS (preconditions real).
- [ ] All 5 in-product skills invoked, each metered + audited; at least one gate approved (action applied) and one rejected (action not applied).
- [ ] Budget cap enforced (1.7) and BYOAK negative path graceful (1.10).
- [ ] All 7 plugin skills run; plugin write-boundary held (no state change).
- [ ] Bridge runs an upstream skill on live Kazi data (3.3).
- [ ] Cross-cutting 5.1–5.4 PASS.
- [ ] Every FAIL triaged (skill bug vs data vs config); every DEFERRED has a reason.

## Known gates / notes (not failures)
- **Trust statutes pending attorney sign-off** — `trust-reconciliation` + trust answers carry `[jurisdictions/za — pending]`; tests verify behaviour + the caveat, not legal accuracy.
- **No standalone assistant chat page** — Phase-70 chat is via launcher buttons / the SSE API; the queue page is the main UI.
- **Seed has no documents** — Phase 0.5 uploads are required before 1.3 (contract review) and document-dependent FICA review.
- **Agent auth** — in-product AI tests need the agent logged into the Kazi web app (or a member bearer token); the plugin tests use the already-authenticated MCP connection.
