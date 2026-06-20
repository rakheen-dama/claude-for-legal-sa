<!--
CONFIGURATION LOCATION

User-specific configuration for this plugin lives at a version-independent path that survives plugin updates:

  ~/.claude/plugins/config/claude-for-legal/kazi-legal-za/CLAUDE.md

Rules for every skill, command, and agent in this plugin:
1. READ configuration from that path. Not from this file.
2. If that file does not exist or still contains [PLACEHOLDER] markers, STOP before doing substantive
   work. Say: "This plugin needs setup before it can give you useful output. Run
   /kazi-legal-za:connect-kazi — it connects to your firm's Kazi tenant, confirms data-egress consent,
   and learns your house style. Without it, outputs will be generic and may not match how your practice
   actually works." Do NOT proceed with placeholder or default configuration. The only skill that runs
   without setup is /kazi-legal-za:connect-kazi itself.
3. Setup and connect-kazi WRITE to that path, creating parent directories as needed.
4. On first run after a plugin update, if a populated CLAUDE.md exists at the old cache path
   (~/.claude/plugins/cache/claude-for-legal/kazi-legal-za/<version>/CLAUDE.md for any version)
   but not at the config path, copy it forward to the config path before proceeding.
5. This file (the one you are reading) is the TEMPLATE. It ships with the plugin and shows the
   structure the config should have. It is replaced on every plugin update. Never write user data here.

**Shared company profile.** Company-level facts (firm name, where you practise, key people) live in
`~/.claude/plugins/config/claude-for-legal/company-profile.md` — one level above this file, shared by
all plugins. Read it before this plugin's practice profile. If it doesn't exist, connect-kazi creates it.
-->

# Kazi Practice Profile
*Written by /kazi-legal-za:connect-kazi. Until then, this is a template — if you see
`[PLACEHOLDER]`, run `/kazi-legal-za:connect-kazi`.*

---

## Read-only, draft-only — the core boundary

This plugin **reads** your firm's live Kazi data over MCP and **drafts**. It never writes to Kazi.
Every output — fee note, trust-recon report, FICA request, matter brief, triage memo — is a draft for
attorney review. **A human reviews it and commits the result back into Kazi by hand.** Trust-ledger
data (Legal Practice Act §86) is read-only and must never be altered by anything this plugin produces.

## The Kazi connection

- **Tenant MCP endpoint:** [PLACEHOLDER — e.g. https://yourfirm.heykazi.com/mcp] *(set `KAZI_MCP_URL`
  to this value; see README)*
- **Authorization server (Keycloak):** [PLACEHOLDER — discovered automatically via
  /.well-known/oauth-protected-resource; record it after first connect]
- **Signed in as:** [PLACEHOLDER — member name + Kazi role, e.g. "Alice Mokoena / Attorney"]
- **Your role sees:** [PLACEHOLDER — the matters/clients your Kazi capabilities permit. The MCP server
  enforces this server-side; you only see what your role allows.]
- **Data-egress consent (POPIA):** [PLACEHOLDER — GRANTED / NOT GRANTED. Enable in Kazi Settings →
  Integrations → MCP before any client data flows into Claude.]

## Firm house style

*Loaded from the `kazi://firm-profile` resource by connect-kazi; edit here to override.*

- **Fee-note style:** [PLACEHOLDER — narrative vs itemised; LSSA / party-and-party vs
  attorney-and-client default; VAT number; rounding convention]
- **Trust account:** [PLACEHOLDER — bank, account reference convention, §86(4) investment practice]
- **FICA posture:** [PLACEHOLDER — standard CDD by default; matters/clients that trigger enhanced DD]
- **Practice areas:** [PLACEHOLDER — from firm-profile; drives matter-type → statute mapping]
- **Matter-brief tone:** [PLACEHOLDER — plain-language register for client-facing updates]

## Available integrations

*Updated by /kazi-legal-za:connect-kazi --check-integrations. Only ✓ if an MCP tool call actually
succeeded this session.*

- Kazi MCP server: [PLACEHOLDER — ✓ / ⚪ not yet confirmed]

## SA legal grounding

Skills cite South African statute knowledge from the `claude-for-legal-sa` overlay
(`jurisdictions/za/...`). Drafts must reflect SA thresholds and procedure — generic-legal output that
ignores SA law is a defect, not a stylistic choice.
