---
name: connect-kazi
description: >
  Connect this plugin to your firm's Kazi tenant and confirm it's ready. Verifies the MCP endpoint,
  walks you through the OAuth sign-in, checks that POPIA data-egress consent is granted, proves the
  link with a ping, loads your firm's house style, and writes CLAUDE.md. Use on first run, when
  CLAUDE.md is missing or has placeholders, or when the user says "connect Kazi", "set up the Kazi
  plugin", "onboard me", or wants to re-check the connection.
argument-hint: "[--redo to re-run setup] [--check-integrations to re-probe the connection only]"
---

# /connect-kazi

This is the one skill that runs before setup is complete. Every other skill in this plugin reads the
config it writes. Goal: a clean, verified, consent-confirmed connection to the firm's live Kazi data,
and a populated practice profile.

## What "connected" means

Three things must all be true before any other skill should run:

1. **Endpoint reachable** — `KAZI_MCP_URL` is set and the Kazi MCP server answers.
2. **Signed in** — the user completed the OAuth authorization-code + PKCE flow against the firm's
   Keycloak (discovered automatically). The bearer token resolves to a Kazi member + role + capabilities
   server-side; the user sees only what their role permits.
3. **Consent granted** — POPIA data-egress consent is `GRANTED` in Kazi (Settings → Integrations → MCP).
   Without it the server refuses to return client data. This plugin never bypasses that.

## Steps

1. **Config check.** Look for `~/.claude/plugins/config/claude-for-legal/kazi-legal-za/CLAUDE.md`. If it
   is populated (no `[PLACEHOLDER]`) and `--redo` was not passed, confirm before overwriting.

2. **Endpoint.** Confirm `KAZI_MCP_URL` is set (the firm's `https://<tenant>.heykazi.com/mcp`). If not,
   tell the user how to set it (see README) and run the diagnostic:

   ```
   python3 "$CLAUDE_PLUGIN_ROOT/scripts/kazi-doctor.py"
   ```

   `kazi-doctor` is an *unauthenticated* probe — it proves the server is up, OAuth-protected, and
   advertising the right Keycloak authorization server. It does **not** sign you in (the client does
   that). Report the first failing hop verbatim if it fails; do not guess past it.

3. **Sign in.** Have the user connect the `kazi` MCP server in their Claude client (`/mcp` in Claude
   Code, or the connector UI in Claude Desktop / claude.ai). This runs the OAuth flow. Confirm by
   calling the **`kazi_ping`** tool — a successful ping means the token resolved to a member.

4. **Consent.** Remind the user that client PII will flow into their Claude context. Confirm POPIA
   data-egress consent is granted in Kazi. If a tool returns a consent error, stop and point them to
   Kazi Settings → Integrations → MCP — do not work around it.

5. **Load house style.** Read the `kazi://firm-profile` resource: practice areas, jurisdiction,
   fee-note/house style, FICA posture, trust-account conventions. These seed the practice profile.

6. **Migration.** If a populated CLAUDE.md (no `[PLACEHOLDER]`) exists at
   `~/.claude/plugins/cache/claude-for-legal/kazi-legal-za/*/CLAUDE.md` but not at the config path, copy
   it to the config path and show what was migrated.

7. **Write config.** Write `~/.claude/plugins/config/claude-for-legal/kazi-legal-za/CLAUDE.md` (create
   parent dirs as needed) from the template, filled with: tenant endpoint, authorization server,
   signed-in member + role, what the role can see, consent state, and the firm house style from step 5.
   Also create/update the shared `company-profile.md` one level up if firm-level facts were learned.

8. **Confirm.** Show a summary: "Connected to <tenant> as <member> (<role>). Consent: <state>. Your role
   can see <scope>." Then offer a first task — usually `/kazi-legal-za:fee-note-run` or
   `/kazi-legal-za:matter-brief`.

## `--check-integrations`

Re-probes the connection only (runs `kazi-doctor`, calls `kazi_ping`, re-reads `kazi://firm-profile`)
and updates `## Available integrations` and the consent line in the config CLAUDE.md. Does not re-onboard.

When probing: only report ✓ if an MCP tool call actually **succeeded** this session. A configured but
untested connection is ⚪ with a one-line how-to. Never report ✓ from the `.mcp.json` declaration alone —
that misleads the user into thinking data is flowing when it isn't.

```
/kazi-legal-za:connect-kazi
```

```
/kazi-legal-za:connect-kazi --check-integrations
```

## Boundaries

- Read-only. This skill (and every skill here) never writes to Kazi.
- Never fabricate a member, role, or consent state — read it from a live tool call or say it's unknown.
- If you can't reach the server or aren't signed in, say so plainly and stop. A broken connection is a
  report-up, not a thing to draft around.
