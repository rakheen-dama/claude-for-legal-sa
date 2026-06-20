# Kazi-Grounded Legal Plugin (South Africa)

Brings your firm's own Claude into your live [Kazi](https://heykazi.com) data over a **read-only** MCP
connection. Your Claude reads your matters, unbilled time, trust ledger, and FICA/compliance state, and
**drafts** — monthly fee notes, §86 trust-reconciliation checks, FICA/KYC gap reviews, client-ready
matter briefs, new-matter triage. A lawyer reviews each draft and commits the result back into Kazi by
hand.

**Bring your own Claude — Kazi provides the grounded context.** Your firm's own Claude subscription pays
the token bill; Kazi just exposes your data over MCP, with per-user authorisation, POPIA egress consent,
and a full read audit trail.

> **Read-only, draft-only.** This plugin never writes to Kazi. Trust-ledger data (Legal Practice Act
> §86) is read-only and never altered. Every output is a draft for attorney review.

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

> A future **v2** adds gated write-back (Claude proposes → attorney approves in Kazi). The contract is
> reserved in [`docs/v2-write-back-contract.md`](docs/v2-write-back-contract.md); v1 is read-only.

## Prerequisites

1. **A Kazi tenant** with the MCP connector enabled (Kazi Settings → Integrations → MCP), and **POPIA
   data-egress consent granted**. Without consent the server returns no client data.
2. **A Claude client** that supports remote MCP over HTTP with OAuth: Claude Code, Claude Desktop, or
   claude.ai.
3. **Your tenant's MCP endpoint**, e.g. `https://yourfirm.heykazi.com/mcp`.

## Install & connect

1. Install this plugin from the `claude-for-legal` marketplace (`/plugin`).
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

Every output is a **draft for attorney review**, committed back in Kazi by hand. Nothing is written to
Kazi by the plugin.

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
- **Read audit trail.** Every MCP read is logged in Kazi, so the firm has a POPIA-defensible record of
  what AI touched which client data.
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
