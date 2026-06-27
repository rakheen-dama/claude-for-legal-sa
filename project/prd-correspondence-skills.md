# PRD — Correspondence Skills for `kazi-legal-za` (write-back loop + read-back digest)

**Status:** Ready to build (one dependency — see §3)
**Date:** 2026-06-27
**Repo:** `claude-for-legal-sa` (this repo) — the build lands here, not in Kazi.
**Builds on:** the shipped `kazi-legal-za` v1 plugin (PRs #1–#7, read-only) + Kazi **Phase 81**
(gated MCP write-back, shipped) + Kazi **Phase 82** (correspondence read-back over MCP — the one
backend dependency, see §3).
**Pointer in Kazi:** `b2b-strawman/requirements/claude-code-prompt-phase82.md` (the read-tool slice
this PRD consumes).

---

## 1. System context (what already exists)

`kazi-legal-za` v1 shipped 7 **read-only, draft-only** skills (`connect-kazi`, `fee-note-run`,
`fica-gap-review`, `matter-brief`, `intake-triage`, `trust-reconciliation`, `kazi-bridge`). Every skill
reads the firm's live Kazi data over MCP, drafts an artefact, and hands off "a human commits this in
Kazi by hand." **Nothing in the plugin writes to Kazi.**

Kazi **Phase 81 changed that on the server side.** The MCP server now exposes — live — a tiered set of
**write** tools, built precisely so a firm's own Claude can file email into Kazi without copy-paste:

| Phase 81 MCP tool | Tier | What it does |
|---|---|---|
| `resolve_matter_by_email(email, …)` | read | Returns candidate `{client, matters[]}` for a sender address. Kazi never auto-files on a guess — Claude disambiguates and passes an explicit `matterId`/`customerId`. |
| `file_correspondence(matterId\|customerId, headers, body, messageId, …)` | **Tier-1 write** | Records an inbound email against a matter/client. Idempotent on `messageId`. Direct, audited, ungated. |
| `attach_document(correspondenceId, …)` | **Tier-1 write** | Files an email attachment as a stamped `Document` linked to the correspondence + matter. Direct, audited. |
| `propose_task(matterId, title, dueDate, correspondenceId, …)` | **Tier-2 gated write** | Creates an `AiExecutionGate(PENDING)` — does **not** create the task. An attorney approves/rejects **inside Kazi**; on approval the task is created. |

All four ride the existing Phase 78 pipeline: per-user OAuth, tenant/member/capability resolution,
enablement + POPIA consent, per-call audit (`mcp.write.*` for writes). Tier-2 safety is enforced
**server-side** — there is no direct path for a Tier-2 action, so Claude cannot bypass the gate.

**The gap (consumer side).** The plugin has **zero skills that use any of this.** The whole point of
Phase 81 — a lawyer's Claude files email and proposes follow-ups — has no consumer skill. And there is
no skill that reads filed correspondence *back* to reason over it. This PRD builds both.

---

## 2. Objective

Add **two new skills** to the `kazi-legal-za` plugin that complete the BYOC correspondence loop:

1. **`file-email`** — the lighthouse. From an email the lawyer's Claude can already see (a mail
   connector, *or* a pasted/forwarded message), file it into the right Kazi matter: resolve → file →
   attach documents → optionally propose a follow-up task for in-Kazi approval.
2. **`correspondence-digest`** — read filed correspondence back across a matter (or the firm) and
   surface "what needs a reply, what's gone quiet, what implies a deadline," proposing follow-ups via
   the same gated `propose_task`.

Positioning unchanged: **"Bring your own Claude — Kazi provides the grounded context."** The new wrinkle
is that the loop now *closes*: Claude proposes, the attorney approves in Kazi, Kazi acts — with the
liability surface identical to the in-product AI path.

**Posture: Tier-1 writes + exactly one gated action (`propose_task`).** No skill mutates trust, money,
or client-visible state directly. Tasks are *proposed*, never created from Claude. This is the v2
write-back contract (`kazi-legal-za/docs/v2-write-back-contract.md`) finally being consumed — but note
that contract is **partly superseded**: Phase 81 built `propose_task`, **not** the four `propose_fee_note`/
`propose_kyc_request`/`propose_matter_update`/`propose_intake_decision` tools the contract sketched.
Those tools do not exist; this PRD does not pretend they do.

---

## 3. The one dependency — Kazi Phase 82 (read-back tools)

`file-email` needs **no new Kazi backend** — all four tools it uses shipped in Phase 81. It can be built
and shipped today.

`correspondence-digest` needs to **read filed correspondence back**, which Phase 81 did **not** expose
over MCP (the only correspondence read surface is the in-app REST tab). Kazi **Phase 82** adds the two
read tools it grounds on:

| Phase 82 MCP tool | Returns |
|---|---|
| `list_correspondence(matterId\|customerId, page)` | Metadata rows: `id`, `subject`, `fromAddress`, `receivedAt`, `attachmentCount`, `direction` (+ possibly `messageId`). |
| `get_correspondence(id)` | A single record **with body** (`bodyText`/`bodyHtml`) + headers (to/cc, `sentAt`, `threadKey`, `messageId`, `attachmentCount`). |

Body read-back rides the **existing** read-egress consent (same posture as `get_matter`/`get_client`) —
it is **provider-neutral** (works regardless of the firm's mail host, and for archived mail). Reading
the body is what makes the digest useful: deadlines and obligations live in the body, not the subject.

**Build order:** `file-email` first (zero dependency, closes the live-OAuth GA gate). `correspondence-digest`
lands after Phase 82 ships the read tools — until then it is blocked and the grounding linter should
report `list_correspondence`/`get_correspondence` as not-yet-in-catalogue.

---

## 4. Constraints & assumptions

- **Provider-neutral — NOT a Gmail feature.** The Kazi write tools take **structured input**; they do
  not care where the email came from. The mail source is whatever the firm's Claude can see:
  - **With a mail connector (Gmail today, Outlook/MS via MCP later):** bulk inbox triage ("file my
    unfiled client emails").
  - **Without any connector:** the lawyer **pastes or forwards** the email into Claude → still works,
    any provider, zero integration.
  Skill copy and the README **must not assume Gmail.** Gmail unlocks the *automated bulk* mode; the
  paste/forward path is the floor and keeps the addressable market open (much of SA SME legal is on
  Microsoft 365).
- **No Kazi backend changes in this repo.** Pure consumer. `file-email` consumes Phase 81 tools;
  `correspondence-digest` consumes Phase 82 tools. If a skill needs data the catalogue doesn't expose,
  that's a finding to raise against Kazi (it became Phase 82), not backend code here.
- **The gate is sacred.** `propose_task` creates a PENDING gate; the skill must **state plainly** that
  nothing happens until the attorney approves *in Kazi*, and must never imply the task was created. No
  skill ever calls an approval endpoint (there is none over MCP).
- **Trust stays out of every write path** (unchanged hard line from the v1 contract). No correspondence
  or task proposal touches trust. `file-email`/`correspondence-digest` never propose a trust action.
- **Tight `propose_task` reach.** Only these two new skills use `propose_task`. Do **not** retrofit it
  into `fee-note-run`/`fica-gap-review`/`matter-brief`/`intake-triage`/`trust-reconciliation` — they
  stay read-only/draft-only. One coherent correspondence story; no scope bleed.
- **Idempotency is the user's safety net.** `file_correspondence` is idempotent on `messageId`; the
  skill should pass a stable `messageId` (the RFC-822 Message-ID when available) so re-running a triage
  never double-files. Surface "already filed" rather than erroring.
- **POPIA-first.** Filing *moves data into* Kazi (lower-risk direction) but is still audited as a write;
  the digest *reads bodies out* under egress consent. Skills surface (never bypass) the
  enablement/consent state and remind the user that client PII is flowing through their Claude context.
- **Marketplace conventions hold** (repo `CLAUDE.md`): one skill per `skills/<name>/SKILL.md` with a
  `description`; `plugin.json` mirrors the marketplace entry; `claude plugin validate` passes; skill
  names in prose are canonical real directory names; grounding linter stays green.

---

## 5. The two new skills

### 5.1 `file-email` (the lighthouse — ships first, no dependency)
- **Purpose:** file an inbound email into the right Kazi matter without copy-paste, and optionally
  propose the follow-up it implies.
- **Flow:**
  1. Read the email — from a connector (bulk) or a pasted/forwarded message (any provider).
  2. `resolve_matter_by_email(senderAddress, subjectHint?)` → candidate client + matters. If
     zero/many, **ask the lawyer** which matter (or confirm "no matter — file against the client only").
     Never guess.
  3. `file_correspondence(matterId|customerId, from/to/cc/subject/body/timestamps, messageId)` →
     returns the correspondence id (or "already filed" on a `messageId` replay).
  4. For each attachment: `attach_document(correspondenceId, …)` → filed as a stamped `Document`.
  5. **Optionally** — if the email implies an action with a date ("respond by 15 July", "file answering
     affidavit by…") — `propose_task(matterId, title, dueDate, correspondenceId)` → a PENDING gate.
     Tell the lawyer: *"Proposed a task — approve it in Kazi to create it."* Do **not** claim it's done.
- **Tools:** `resolve_matter_by_email`, `file_correspondence`, `attach_document`, `propose_task`.
- **SA knowledge:** light — prescription / court-deadline awareness (`prescription.yaml`,
  `magistrates-courts.yaml`, `superior-courts.yaml`) only insofar as it helps phrase a *proposed* task's
  title/date; the lawyer confirms the deadline in Kazi. No statute output is committed.
- **Output:** a per-email summary — "filed as correspondence #…, N attachments, 1 task proposed (pending
  your approval in Kazi)." For bulk: a table of what was filed / skipped (already-filed) / needs
  disambiguation.

### 5.2 `correspondence-digest` (read-back — ships after Phase 82)
- **Purpose:** across a matter (or a set of matters), summarise recent filed correspondence and surface
  what needs the lawyer's attention — unanswered inbound, matters gone quiet, and **deadlines implied by
  the email bodies**.
- **Flow:**
  1. `list_correspondence(matterId|customerId, page)` → recent correspondence metadata.
  2. For items worth reasoning over, `get_correspondence(id)` → the body, to extract obligations /
     deadlines / "who owes whom a response."
  3. Produce the digest: needs-a-reply (inbound with no later outbound), gone-quiet (no correspondence
     in N days on an active matter), deadline-spotted (date-bearing obligations from the body).
  4. **Optionally** propose follow-ups for the deadlines it spots via `propose_task(…)` — PENDING gates,
     approved in Kazi. Same "nothing happens until you approve" framing as `file-email`.
- **Tools:** `list_correspondence`, `get_correspondence`, `propose_task`. May pull attached documents via
  the existing `search_documents`/`get_document_url` when a body references "the attached…".
- **SA knowledge:** prescription / court-deadline overlays for sanity-checking spotted dates (advisory).
- **Output:** a matter (or cross-matter) correspondence digest; any deadlines optionally turned into
  *proposed* tasks the attorney approves in Kazi.
- **Honest scope:** the digest reasons over what was **filed** (via `file-email`). It is not a live
  inbox monitor — it sees Kazi correspondence, not the raw mailbox. State this in the skill.

---

## 6. SA knowledge bundling

Both skills carry only **light** SA grounding (court-deadline / prescription awareness for phrasing
proposed task dates) — they are workflow skills, not statute-drafting skills like `trust-reconciliation`.
Follow the existing `knowledge-map.yaml` + `scripts/sync-kazi-knowledge.py` mechanism: declare each
skill's `mcp` tools and any `za_knowledge` refs; the grounding linter
(`scripts/validate-kazi-skill-grounding.py`) enforces that every tool name resolves in
`data/mcp-catalogue.json` and every statute ref resolves + is bundled.

- **Add the Phase 81/82 tool names to `data/mcp-catalogue.json`** so the linter can resolve them:
  `resolve_matter_by_email`, `file_correspondence`, `attach_document`, `propose_task` (81),
  `list_correspondence`, `get_correspondence` (82). Until Phase 82 ships, mark the latter two so the
  linter reports `correspondence-digest` as blocked rather than dangling.
- `knowledge-map.yaml` entries:
  ```yaml
  file-email:
    status: built          # ships first
    mcp: [resolve_matter_by_email, file_correspondence, attach_document, propose_task]
    za_knowledge:
      - prescription.yaml#general_debt_prescription   # advisory, for proposed-task dates
  correspondence-digest:
    status: blocked         # until Phase 82 read tools land
    mcp: [list_correspondence, get_correspondence, propose_task]
    za_knowledge:
      - prescription.yaml#general_debt_prescription
    knowledge_gaps:
      - "Depends on Kazi Phase 82 (list_correspondence / get_correspondence). Blocked until those tools are in data/mcp-catalogue.json."
  ```

---

## 7. The gate UX (write-back framing — applies to both skills)

The single most important behaviour: **never overstate what happened.**

- `file_correspondence` / `attach_document` are real, immediate writes — say "filed."
- `propose_task` is a **proposal** — say "proposed a task; approve it in Kazi to create it," and link/name
  the gate review surface. Never "created a task," never "set a deadline."
- If enablement/consent is off, the tool returns a not-enabled error — surface it as "MCP write isn't
  enabled / consent isn't granted in Kazi Settings," not a raw error.
- Re-running a triage is safe (idempotent on `messageId`) — present "already filed" as success, not
  failure.

This mirrors the in-product AI gate semantics and the `docs/v2-write-back-contract.md` requirements
(no mutation in the tool, approval only in Kazi, same auth as reads, audited, idempotent).

---

## 8. Marketplace / packaging

- No new plugin — both skills are added **inside the existing `kazi-legal-za` plugin**
  (`kazi-legal-za/skills/file-email/`, `kazi-legal-za/skills/correspondence-digest/`).
- Bump `kazi-legal-za/.claude-plugin/plugin.json` version; update its `description` to mention email
  filing + correspondence digest. The marketplace entry mirrors it field-for-field.
- README + `connect-kazi` get a short addition: write tools require **MCP write enablement + consent**
  in Kazi Settings (a stricter posture than read-only); `connect-kazi` should report write-capability
  state too.

---

## 9. Out of scope

- **Any Kazi backend change in this repo.** `file-email` consumes Phase 81; `correspondence-digest`
  consumes Phase 82 (specified separately in `b2b-strawman/requirements/claude-code-prompt-phase82.md`).
- **`propose_*` beyond `propose_task`.** `propose_fee_note`/`propose_kyc_request`/etc. from the old v2
  contract are **not built** in Kazi — no skill may call them. Retrofitting `propose_task` into the
  other five skills is also out (tight reach, §4).
- **Any trust write/proposal.** Hard line.
- **Outbound / "send email from Kazi"**, thread reconstruction, new-party/contact creation, bulk
  multi-matter auto-filing without disambiguation — all deferred (these were Phase 81 v2 too).
- **A live inbox monitor / background poll.** The digest reads *filed* correspondence; it does not watch
  the mailbox. (Kazi has no mail integration by design — BYOC.)
- **Re-hydrating bodies from Gmail.** Rejected at ideation (would make the digest provider-locked); the
  digest reads bodies from Kazi via Phase 82.

---

## 10. Validation / acceptance ("done" when)

1. `claude plugin validate kazi-legal-za` passes; existing repo validators + grounding linter stay green.
2. **`file-email`, run against a seeded Kazi tenant, observed end-to-end:** a pasted/forwarded email →
   `resolve_matter_by_email` → `file_correspondence` → `attach_document` → `propose_task` → a PENDING
   gate visible in Kazi; the Kazi **audit log** shows the `mcp.write.*` entries. Re-running the same
   email is a no-op ("already filed"). **Observed, not inferred** (Kazi's "PASS means observed" bar).
3. The proposed task, **approved in Kazi**, creates the task linked to the correspondence — proving the
   full Claude→propose→approve→execute loop. This also discharges the standing **live-OAuth GA gate** for
   the pack (a real client round-trip from a Claude client).
4. **`correspondence-digest`** (after Phase 82): run against the same tenant → `list_correspondence` +
   `get_correspondence` → a digest that correctly flags an unanswered inbound and a body-stated deadline;
   optionally proposes a task (PENDING). Observed end-to-end.
5. `validate-kazi-skill-grounding.py` passes — both skills' tool names resolve in the catalogue (and the
   linter correctly reports `correspondence-digest` as blocked until Phase 82 lands).
6. README walkthrough takes a fresh user from install → enable MCP **write** + consent in Kazi → file a
   first email → approve the proposed task in Kazi.

---

## 11. Suggested build sequence (epics → slices)

1. **E1 — `file-email` skill.** The full Phase 81 loop, provider-neutral (connector + paste/forward).
   Catalogue + `knowledge-map.yaml` entries for the four Phase 81 tools. README + `connect-kazi`
   write-enablement addition. *Verify: validate + grounding linter green; observed end-to-end against a
   seeded tenant incl. a real gate approval (item 2 + 3).*
2. **E2 — Catalogue + linter prep for read-back.** Add `list_correspondence`/`get_correspondence` to the
   catalogue marked blocked-until-Phase-82; `knowledge-map.yaml` `correspondence-digest: blocked`.
   *Verify: linter reports the skill blocked, not dangling.*
3. **E3 — `correspondence-digest` skill** (gated on Kazi Phase 82 shipping). Read-back + deadline
   surfacing + optional `propose_task`. Flip its status to `built`. *Verify: observed end-to-end (item 4).*
4. **E4 — version bump + marketplace + README walkthrough.** Plugin version, description, full
   install→enable→file→approve walkthrough.

---

## 12. Open decisions for build

- **`file-email` bulk vs single.** Default to single-email (paste/forward) as the floor; add a
  connector-driven bulk mode as an explicit sub-flow with a per-email disambiguation table. Decide
  whether bulk ships in E1 or as a fast-follow.
- **`messageId` source on the paste path.** A pasted email may lack a clean RFC-822 Message-ID; decide
  the fallback stable key (hash of from+subject+sentAt?) so idempotency still holds — and document it.
- **Digest scope unit.** Per-matter (default) vs cross-matter "my inbox today." Start per-matter; a
  cross-matter roll-up is a fast-follow once `list_correspondence` paging is proven.
- **Does `list_correspondence` expose `messageId`?** Nice-to-have for the digest to cross-check against
  what `file-email` filed — flagged as an open question in the Phase 82 spec; if it ships, use it.
