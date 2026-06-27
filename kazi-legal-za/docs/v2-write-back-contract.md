# v2 write-back contract — partly superseded by Kazi Phase 81

> **Status update.** This was the reserved spec for gated write-back. Kazi **Phase 81** then shipped a
> *correspondence* write-back slice, and `kazi-legal-za` now consumes it in two skills
> (`file-email`, `correspondence-digest`). What actually shipped differs from the sketch below — read
> this section first:
>
> - Kazi built exactly **one** gated proposal tool, **`propose_task`** (create a task from a filed
>   correspondence, via a PENDING `AiExecutionGate`). The four `propose_*` tools tabled below
>   (`propose_fee_note`, `propose_kyc_request`, `propose_matter_update`, `propose_intake_decision`)
>   **were not built and no skill calls them** — do not assume they exist.
> - Phase 81 also added **direct, ungated Tier-1 writes** for correspondence: `file_correspondence`
>   (idempotent on `messageId`) and `attach_document` (two-phase presigned upload), plus the read helper
>   `resolve_matter_by_email`. Phase 82 added correspondence **read-back** (`list_correspondence`,
>   `get_correspondence`).
> - `propose_task`'s reach is **deliberately limited** to the two correspondence skills. The other five
>   skills stay read-only/draft-only — do **not** retrofit `propose_task` (or any write) into them.
> - The principle below still holds exactly: a proposal creates a PENDING gate; approval happens only in
>   Kazi; trust is never a write/proposal target.
>
> The original spec is retained below for the design rationale and for the contract requirements, which
> the shipped tools satisfy.

---

The rest of this document is the original v2 reservation. Claude drafts, a human commits the result back
into Kazi by hand. It reserved the design for gated write-back so it wasn't reinvented when its turn
came — that turn became Phase 81 (correspondence only, as noted above).

## Principle: a write does not mutate state — it proposes

A v2 write tool **never** changes Kazi data directly. It creates an `AiExecutionGate` in `PENDING` state —
exactly as Kazi's in-product AI skills already do. The attorney approves or rejects the proposal **inside
Kazi** (the existing `AiExecutionGateController` + UI), never inside Claude. This keeps the liability
surface identical to the in-product path: v2 is "expose existing gate creation over MCP", not new safety
machinery.

```
Claude (kazi-legal-za skill)                Kazi backend                     Attorney (in Kazi)
  propose_fee_note(matter, draft)  ──▶  create AiExecutionGate(PENDING)  ──▶  approve / reject
                                         (no state mutation yet)               │
                                                                               ▼
                                                          on approve: Kazi applies the change,
                                                          audit: "AI-suggested (via MCP) → attorney-approved"
```

## Proposed v2 tools (Kazi backend — not this repo)

These are **Kazi MCP server** additions; the plugin would simply call them. Each maps a v1 read skill to
a gated proposal:

| v2 tool | From skill | Creates a PENDING gate to… |
|---|---|---|
| `propose_fee_note` | `fee-note-run` | draft-bill the matter's unbilled time (attorney finalises) |
| `propose_kyc_request` | `fica-gap-review` | record/send the FICA document request |
| `propose_matter_update` | `matter-brief` | post the status update to the client portal |
| `propose_intake_decision` | `intake-triage` | open the matter (after conflict clearance) |

**Deliberately excluded from any write path: trust.** Nothing in `trust-reconciliation` ever proposes a
trust mutation. Trust (LPA s86) stays strictly read-only — corrections happen in Kazi/accounting under
the trust-account practitioner's sign-off. This is a hard line, not a v2 backlog item.

## Contract requirements (when v2 is built)

1. **No mutation in the tool.** The tool returns the created gate's id + status `PENDING`; it must not be
   possible for a tool call alone to change client-visible state.
2. **Approval only in Kazi.** The approve/reject action is a Kazi UI/API action by an authenticated
   member with the right capability — never an MCP call, never Claude.
3. **Same auth as reads.** Write proposals resolve tenant → member → capability exactly like the read
   tools; a member who can't perform the action in Kazi can't propose it over MCP.
4. **Audit.** Every proposal and its disposition is logged ("AI-suggested (via MCP) → attorney-approved
   / rejected", with actor + timestamp), reusing the existing `ai.specialist.*` / `mcp.*` audit family.
5. **Consent.** Write proposals require the same (or a stricter) POPIA egress/enablement posture as reads.
6. **Idempotency / dedupe.** Re-running a skill must not create duplicate pending gates for the same
   proposed action.

## What stays unchanged from v1

- The plugin remains a thin client; all safety logic lives server-side in Kazi.
- Skills keep their read-only drafting behaviour; a v2 skill variant would add a final "propose to Kazi"
  step that calls a `propose_*` tool, after the human has reviewed the draft.
- Source attribution, the draft-only framing, and the "human decides in Kazi" handoff all carry over.

v2 is a separate ideation → architecture → build when its turn comes. Until then, this file is the
agreed shape so the read-only v1 doesn't foreclose it.
