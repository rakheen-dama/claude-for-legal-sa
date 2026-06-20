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
| `/kazi-legal-za:connect-kazi` | Connect, confirm consent, load house style, write config | **shipped (E1)** |
| `/kazi-legal-za:fee-note-run` | Draft LSSA-tariff-aware fee notes from unbilled time | planned (E3) |
| `/kazi-legal-za:trust-reconciliation` | §86 trust-ledger anomaly report (read-only) | planned (E4) |
| `/kazi-legal-za:fica-gap-review` | Identify missing FICA/KYC docs, draft the client request | planned (E5) |
| `/kazi-legal-za:matter-brief` | Plain-language, client-ready matter status update | planned (E6) |
| `/kazi-legal-za:intake-triage` | Triage a new matter against templates + recent conflicts | planned (E6) |
| `/kazi-legal-za:kazi-bridge` | Run upstream `claude-for-legal` skills against Kazi data | planned (E7) |

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
