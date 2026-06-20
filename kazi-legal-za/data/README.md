# `data/` — bundled, shipped-with-the-plugin reference data

Everything here ships **inside** the plugin so it is present after install. (Repo-root
directories like `jurisdictions/za/` do **not** ship inside a plugin — this is a documented
marketplace gap, so the knowledge a skill needs must live here.)

| Path | What | Edit? |
|---|---|---|
| `mcp-catalogue.json` | The Kazi MCP read catalogue (tools + resources) the skills may call. Mirrors the Phase 78 backend. | By hand, when the backend catalogue changes. |
| `za/statutes/*.yaml` | **Generated.** Copies of the `jurisdictions/za` statute files cited in `../knowledge-map.yaml`. | **No — generated.** Run `scripts/sync-kazi-knowledge.py`. |

## Regenerating the bundled statutes

The source of truth is `jurisdictions/za/statutes/`. To refresh the bundle after editing a
statute or changing `knowledge-map.yaml`:

```bash
python3 scripts/sync-kazi-knowledge.py            # copy cited files in
python3 scripts/sync-kazi-knowledge.py --check    # CI: fail if bundle is out of sync
python3 scripts/validate-kazi-skill-grounding.py  # verify all references resolve
```

The linter fails if `za/statutes/` drifts from source, so the bundle can never silently go stale
relative to the overlay.
