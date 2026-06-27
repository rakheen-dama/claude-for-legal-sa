# Kazi-Grounded Legal Plugin (South Africa)

Brings your firm's own Claude into your live [Kazi](https://heykazi.com) data over MCP. Your Claude
reads your matters, unbilled time, trust ledger, and FICA/compliance state, and **drafts** — monthly
fee notes, §86 trust-reconciliation checks, FICA/KYC gap reviews, client-ready matter briefs,
new-matter triage. It also **files correspondence**: file an email into the right matter and surface
what needs a reply. A lawyer reviews each draft and commits the result back into Kazi.

**Bring your own Claude — Kazi provides the grounded context.** Your firm's own Claude subscription pays
the token bill; Kazi just exposes your data over MCP, with per-user authorisation, POPIA egress consent,
and a full audit trail.

> **Mostly read + draft, with bounded correspondence write-back.** The fee-note / trust / FICA / brief /
> triage skills never write to Kazi — every output is a draft for attorney review. Two correspondence
> skills do write: `file-email` files an email (and its attachments) into a matter, and both
> correspondence skills may **propose** a follow-up task — a PENDING gate the attorney approves **inside
> Kazi**, never created by Claude. **Trust-ledger data (Legal Practice Act §86) stays strictly
> read-only** and is never altered or proposed against.

## What's in v1

| Skill | Does | Status |
|---|---|---|
| `/kazi-legal-za:connect-kazi` | Connect, confirm consent, load house style, write config | ✅ |
| `/kazi-legal-za:fee-note-run` | Draft fee notes from unbilled time (house style + contingency caps) | ✅ |
| `/kazi-legal-za:fica-gap-review` | Identify missing FICA/KYC docs, draft the client request | ✅ |
| `/kazi-legal-za:matter-brief` | Plain-language, client-ready matter status update | ✅ |
| `/kazi-legal-za:intake-triage` | Triage a new matter — conflicts, forum, governing law, deadlines | ✅ |
| `/kazi-legal-za:trust-reconciliation` | §86 trust-account **anomaly screen** (read-only) | ✅ ⚠️ statute refs pending attorney sign-off |
| `/kazi-legal-za:kazi-bridge` | Run upstream `claude-for-legal` skills against Kazi data | ✅ |
| `/kazi-legal-za:file-email` | File an email into the right matter (+ attachments); optionally propose a follow-up task | ✅ ✍️ writes (needs MCP write enabled) |
| `/kazi-legal-za:correspondence-digest` | Read filed correspondence back — what needs a reply, gone quiet, deadlines | ✅ ✍️ gated propose only |

> **Write-back is live, and bounded.** `file-email` / `correspondence-digest` consume Kazi's gated
> correspondence write tools: filing is a direct audited write; tasks are only ever **proposed**
> (PENDING gate → attorney approves in Kazi). The original design is in
> [`docs/v2-write-back-contract.md`](docs/v2-write-back-contract.md) (Kazi shipped `propose_task`, not
> the other `propose_*` tools that doc sketched). Trust write-back is deliberately excluded.

## Prerequisites

1. **A Kazi tenant** with the MCP connector enabled (Kazi Settings → Integrations → MCP), and **POPIA
   data-egress consent granted**. Without consent the server returns no client data.
2. **A Claude client** that supports remote MCP over HTTP with OAuth: Claude Code, Claude Desktop, or
   claude.ai.
3. **Your tenant's MCP endpoint**, e.g. `https://yourfirm.heykazi.com/mcp`.
4. **For the correspondence skills only:** **MCP write enabled** for your member (Kazi Settings →
   Integrations → MCP) — a stricter posture than read-only, under the same POPIA consent. The read-and-
   draft skills don't need it. Filing attachments via `file-email` also needs a client that can perform
   an HTTP upload (Claude Code, via `curl`) and the attachment as a local file; on the bare paste path
   the email body files fine and you attach documents in Kazi.

## Install & connect

1. Install this plugin from the `claude-for-legal-sa` marketplace (`/plugin`).
2. Point it at your tenant by setting the `KAZI_MCP_URL` environment variable to your MCP endpoint:

   ```bash
   export KAZI_MCP_URL="https://yourfirm.heykazi.com/mcp"
   ```

   Set it wherever your Claude client reads environment from (your shell profile for Claude Code, or the
   client's MCP settings for Desktop/claude.ai).
3. Run the connection diagnostic (no sign-in needed — it proves the server is up and OAuth-protected):

   ```bash
   python3 "$CLAUDE_PLUGIN_ROOT/scripts/kazi-doctor.py"
   ```

4. In your Claude client, connect the **kazi** MCP server (`/mcp` in Claude Code). This runs the OAuth
   sign-in (authorization-code + PKCE) against your firm's Keycloak — discovered automatically from the
   server's `/.well-known/oauth-protected-resource` metadata.
5. Finish setup:

   ```
   /kazi-legal-za:connect-kazi
   ```

   It confirms the ping, checks consent, loads your firm's house style, and writes your practice profile
   to `~/.claude/plugins/config/claude-for-legal/kazi-legal-za/CLAUDE.md` (survives plugin updates).

## First run — a walkthrough

Once connected, a typical first session:

1. **Confirm the link.** `/kazi-legal-za:connect-kazi` → "Connected to <firm> as <you> (<role>). Consent:
   GRANTED." If consent is not granted, enable it in Kazi Settings → Integrations → MCP first.
2. **Draft this month's fee notes.** `/kazi-legal-za:fee-note-run` → it lists clients with unbilled time,
   you pick some, and it drafts a fee note per matter in your house style. **Review, itemise, and
   finalise each one in Kazi** — the drafts are matter-level (line items live in Kazi).
3. **Close a compliance gap.** `/kazi-legal-za:fica-gap-review "Acme (Pty) Ltd"` → it reads the client's
   FICA checklist, lists what's outstanding, and drafts the document-request email. Send it from Kazi.
4. **Brief a client.** `/kazi-legal-za:matter-brief "Acme lease renewal"` → a plain-language status update
   from the matter's recent activity. Edit and send from Kazi.
5. **Triage a new enquiry.** `/kazi-legal-za:intake-triage "debt claim, R180k, against an existing
   client"` → possible conflicts, likely forum, prescription clock, fee options.
6. **Screen the trust account.** `/kazi-legal-za:trust-reconciliation <trust-account-id>` → a read-only
   anomaly screen (debit balances, odd movements). **Not** a formal reconciliation, and its statutory
   refs are pending attorney sign-off — see the skill's caveat.
7. **Use your other legal skills on Kazi data.** `/kazi-legal-za:kazi-bridge "contract-review on matter
   Acme MSA"` → pulls the document from Kazi and runs the upstream `commercial-legal` review on it.

### Close the correspondence loop (the write-back skills)

Enable **MCP write** for your member in Kazi Settings → Integrations → MCP first, then:

8. **File an email.** Forward or paste a client email and run `/kazi-legal-za:file-email`. It resolves
   the sender to a client + matter (asking you to disambiguate if needed), **files** it as
   correspondence, uploads any attachments, and — if the email implies a dated action — **proposes a
   task**. Re-running the same email is safe (it reports "already filed").
9. **Approve the follow-up in Kazi.** The proposed task is a **PENDING gate** — open it in Kazi and
   approve; only then is the task created and linked to the correspondence. Claude never creates it.
10. **Digest what's filed.** `/kazi-legal-za:correspondence-digest "Acme lease renewal"` → across the
    matter's filed correspondence: what's awaiting a reply, what's gone quiet, and deadlines stated in
    the bodies (optionally proposed as tasks, same approve-in-Kazi gate). It reads what's **filed** in
    Kazi, not your live mailbox.

The read-and-draft skills write nothing to Kazi — every output is a draft committed by hand. The
correspondence skills file directly (audited) but only ever **propose** tasks; you approve them in Kazi.
Trust is never written or proposed against.

### Claude Desktop / claude.ai vs Claude Code

The OAuth connect UX differs slightly: in **Claude Code** you add/authorise the server with `/mcp`; in
**Claude Desktop / claude.ai** you add it through the connectors UI. Either way the underlying flow is
the same RFC 9728 protected-resource discovery + authorization-code/PKCE. `connect-kazi` walks you
through whichever client you're in.

## How it stays safe

- **Per-user authorisation.** Your bearer token resolves to your Kazi member + role + capabilities
  server-side. You see only what your Kazi role lets you see — the plugin can't widen that.
- **POPIA consent.** Client data only flows after your firm grants egress consent in Kazi; revoking it
  is one click and the server stops returning data.
- **Read + write audit trail.** Every MCP read is logged in Kazi; every correspondence write
  (`mcp.write.*` — filed email, attached document, proposed task) is logged too, so the firm has a
  POPIA-defensible record of what AI touched — and proposed — for which client.
- **Writes are bounded and gated.** Only `file-email` / `correspondence-digest` write, only after MCP
  write is enabled. Filing is direct and audited; tasks are only **proposed** (a PENDING gate approved
  in Kazi). No skill writes to the trust ledger.
- **SA-grounded.** Drafts cite South African statute knowledge from the `claude-for-legal-sa` overlay
  (`jurisdictions/za/...`) — FICA, the Legal Practice Act, LSSA tariffs — not generic boilerplate.

## Troubleshooting

Run `python3 "$CLAUDE_PLUGIN_ROOT/scripts/kazi-doctor.py"`. It reports the first failing
hop:

- **`KAZI_MCP_URL` not set** → export it (step 2).
- **Endpoint unreachable** → check the URL and that your tenant is up.
- **No OAuth metadata** → the host answered but isn't advertising MCP OAuth discovery; confirm the
  endpoint ends in `/mcp` and the connector is enabled in Kazi.
- **`/mcp` not returning 401** → unexpected; the endpoint should reject unauthenticated calls. Re-check
  the URL.
- After the probe passes, sign in via your client and run `/kazi-legal-za:connect-kazi`.
