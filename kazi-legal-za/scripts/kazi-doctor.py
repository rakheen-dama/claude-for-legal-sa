#!/usr/bin/env python3
"""kazi-doctor — diagnose the connection from the kazi-legal-za plugin to a firm's Kazi MCP server.

This is an UNAUTHENTICATED probe. It proves the server is reachable, OAuth-protected, and advertising
the right authorization server (Keycloak) for MCP OAuth discovery (RFC 9728 / Kazi ADR-303). It does
NOT sign you in — the Claude client runs the authorization-code + PKCE flow. After this probe passes,
connect the `kazi` MCP server in your client and run /kazi-legal-za:connect-kazi.

Hops checked:
  1. KAZI_MCP_URL resolved        — the .mcp.json `url` (or env var it points at) is set.
  2. OAuth metadata reachable     — GET <host>/.well-known/oauth-protected-resource → 200 JSON
                                    with `authorization_servers` (the firm's Keycloak).
  3. /mcp endpoint protected      — POST <url> with no token → 401 (the server rejects unauth calls).

Exit code 0 = all hops passed; 1 = a hop failed (the first failing hop is reported); 2 = usage error.

Usage:
  python3 "$CLAUDE_PLUGIN_ROOT/scripts/kazi-doctor.py"          # auto-finds the plugin's .mcp.json
  python3 kazi-legal-za/scripts/kazi-doctor.py --url https://yourfirm.heykazi.com/mcp
"""

import argparse
import json
import os
import re
import sys
import urllib.error
import urllib.request
from urllib.parse import urlsplit, urlunsplit

TIMEOUT = 10
ENV_REF = re.compile(r"^\$\{([A-Z0-9_]+)\}$")

OK = "✓"   # ✓
BAD = "✗"  # ✗


def fail(hop, detail, hint):
    print(f"  {BAD} {hop}")
    print(f"      {detail}")
    if hint:
        print(f"      next: {hint}")
    print(f"\nkazi-doctor: FAILED at “{hop}”. Fix this hop and re-run.")
    sys.exit(1)


def ok(hop, detail=""):
    line = f"  {OK} {hop}"
    if detail:
        line += f" — {detail}"
    print(line)


def default_mcp_config():
    """The plugin's .mcp.json sits one level up from this script (kazi-legal-za/.mcp.json)."""
    return os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), ".mcp.json")


def resolve_url(args):
    if args.url:
        return args.url
    mcp_config = args.mcp_config or default_mcp_config()
    try:
        with open(mcp_config, encoding="utf-8") as f:
            cfg = json.load(f)
    except (OSError, json.JSONDecodeError) as e:
        print(f"kazi-doctor: cannot read {mcp_config}: {e}", file=sys.stderr)
        sys.exit(2)
    servers = cfg.get("mcpServers", {})
    entry = servers.get("kazi") or next(iter(servers.values()), None)
    if not entry:
        print(f"kazi-doctor: no mcpServers entry in {mcp_config}", file=sys.stderr)
        sys.exit(2)
    raw = entry.get("url", "")
    m = ENV_REF.match(raw.strip())
    if m:
        env_name = m.group(1)
        val = os.environ.get(env_name, "")
        if not val:
            fail(
                f"{env_name} resolved",
                f".mcp.json url is ${{{env_name}}} but the environment variable is not set.",
                f'export {env_name}="https://yourfirm.heykazi.com/mcp"',
            )
        return val
    return raw


def host_root(url):
    parts = urlsplit(url)
    if not parts.scheme or not parts.netloc:
        fail("URL well-formed", f"not a valid http(s) URL: {url!r}", "set KAZI_MCP_URL to your /mcp endpoint")
    return urlunsplit((parts.scheme, parts.netloc, "", "", ""))


def http(method, url, body=None):
    headers = {"Accept": "application/json"}
    data = None
    if body is not None:
        data = json.dumps(body).encode("utf-8")
        headers["Content-Type"] = "application/json"
    req = urllib.request.Request(url, data=data, headers=headers, method=method)
    try:
        with urllib.request.urlopen(req, timeout=TIMEOUT) as resp:
            return resp.status, resp.read()
    except urllib.error.HTTPError as e:
        return e.code, e.read()
    except (urllib.error.URLError, TimeoutError, OSError) as e:
        return None, str(e)


def main():
    ap = argparse.ArgumentParser(description="Diagnose the kazi-legal-za → Kazi MCP connection.")
    ap.add_argument("--mcp-config", help="path to the plugin's .mcp.json (default: sibling of this script)")
    ap.add_argument("--url", help="Kazi MCP endpoint, overrides --mcp-config")
    args = ap.parse_args()

    url = resolve_url(args)
    root = host_root(url)
    print(f"kazi-doctor: probing {url}\n")

    # Hop 1
    ok("KAZI_MCP_URL resolved", url)

    # Hop 2 — OAuth protected-resource metadata
    meta_url = root + "/.well-known/oauth-protected-resource"
    status, payload = http("GET", meta_url)
    if status is None:
        fail("OAuth metadata reachable", f"could not reach {meta_url}: {payload}",
             "check the URL and that your tenant is up")
    if status != 200:
        fail("OAuth metadata reachable",
             f"GET {meta_url} returned {status} (expected 200).",
             "confirm the endpoint ends in /mcp and the MCP connector is enabled in Kazi")
    try:
        meta = json.loads(payload)
    except json.JSONDecodeError:
        fail("OAuth metadata reachable", f"{meta_url} did not return JSON.", "is this really a Kazi MCP host?")
    auth_servers = meta.get("authorization_servers") or []
    if not auth_servers:
        fail("OAuth metadata advertises an authorization server",
             "metadata has no `authorization_servers` claim.",
             "the Kazi server must advertise its Keycloak issuer (ADR-303)")
    ok("OAuth metadata reachable", f"authorization server: {auth_servers[0]}")

    # Hop 3 — /mcp must reject unauthenticated calls
    init_body = {"jsonrpc": "2.0", "id": 1, "method": "initialize", "params": {}}
    status, _ = http("POST", url, body=init_body)
    if status is None:
        fail("/mcp endpoint reachable", f"could not POST to {url}.", "check the URL")
    if status == 401:
        ok("/mcp endpoint protected", "returns 401 to unauthenticated calls (correct)")
    elif status in (403,):
        ok("/mcp endpoint protected", f"returns {status} to unauthenticated calls")
    else:
        fail("/mcp endpoint protected",
             f"POST {url} returned {status} unauthenticated (expected 401).",
             "the endpoint should reject unauthenticated calls — re-check the URL")

    print("\nkazi-doctor: PASSED. The server is up and OAuth-protected.")
    print("Next: connect the `kazi` MCP server in your Claude client (sign in), then run")
    print("      /kazi-legal-za:connect-kazi")
    sys.exit(0)


if __name__ == "__main__":
    main()
