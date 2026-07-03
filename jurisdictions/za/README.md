# SA Readiness Matrix

Status of the South African jurisdiction overlay across all plugins in this fork.

## Plugin Status

| Plugin | ZA Status | SA Coverage | Cold-Start ZA Fork |
|---|---|---|---|
| `commercial-legal` | Ready | CPA/VAT/exchange-control/POPIA operator clauses; B-BBEE competition; restraint of trade | Yes |
| `privacy-legal` | Ready | POPIA/PAIA/Information Regulator; data subject rights; operator agreements; cross-border transfers | Yes |
| `product-legal` | Ready | CPA/advertising standards; NCA fintech/credit; sector regulatory map (FSCA, SARB, ICASA) | Yes |
| `corporate-legal` | Ready | Companies Act/CIPC/B-BBEE; fundamental transactions; Takeover Regulation Panel; SA diligence | Yes |
| `employment-legal` | Ready | LRA/BCEA/EEA; CCMA dismissal procedure; hiring/probation; leave; disciplinary codes | Yes |
| `regulatory-legal` | Ready | Government Gazette; FSCA/SARB/ICASA/sector regulators; regulatory process; rule-status verification | Yes |
| `litigation-legal` | Ready | Magistrates'/High Court procedure; prescription; CCMA; SA courts structure; privilege; advocacy | Yes |
| `ip-legal` | Ready | CIPC trade mark and patent registry; copyright fair dealing; IP enforcement; ownership clauses | Yes |
| `legal-clinic` | Ready | LPC rules; Legal Aid SA; university law clinic framework; SA court system; SA legal research | Yes |
| `ai-governance-legal` | US defaults | No SA overlay — AI governance frameworks are largely US/EU-based; usable with manual SA calibration | No |
| `law-student` | US defaults | No SA overlay — MBE/bar prep is US-specific; SA LLB students can use Socratic drilling and outlining skills with manual jurisdiction context | No |
| `legal-builder-hub` | US defaults | No SA overlay — skill discovery and trust layer are jurisdiction-neutral; functions as-is | No |
| `kazi-legal-za` | Kazi-tenant-required | SA-native Kazi practice management integration (fee notes, trust reconciliation, FICA, correspondence) — requires a Kazi tenant | N/A |
| `cocounsel-legal` | Vendor–US | Thomson Reuters / Westlaw Deep Research; US research tooling only; not adapted for SA | N/A |

## What "Ready" Means

A plugin marked **Ready** has a full ZA overlay: a jurisdiction-specific router, topic overlay files grounded in SA statutes and procedure, a temporally-versioned statute YAML library, and a SA cold-start interview fork that writes a ZA practice profile. When `jurisdiction = ZA` is set in your company profile, skills load the overlay automatically — US defaults are replaced by SA statutory references, procedural steps, and risk flags. See [ARCHITECTURE.md](ARCHITECTURE.md) for the overlay mechanics.

## What "US defaults" Means

Plugins marked **US defaults** have no ZA overlay. They remain usable — the skills are jurisdiction-neutral enough that a practitioner can direct them with manual context — but they will not automatically substitute SA law for US defaults. Do not rely on jurisdiction-specific guidance from these plugins without reviewing and correcting the output.

## Statute Library

The ~50 YAML files in `statutes/` carry temporally-versioned threshold values (monetary limits, notice periods, rates) sourced from the Government Gazette. Files may carry a `volatility` field that sets the staleness window; absent `volatility` defaults to `stable` (36-month review window):

| Volatility | Window | Examples |
|---|---|---|
| `annual` | 12 months | BCEA earnings threshold, national minimum wage, sectoral determination rates |
| `statutory` | 18 months | Values that change only by Act amendment |
| `stable` (default) | 36 months | Original-statute constants unlikely to change |

Last verified: **2026-07-03** (employment/commercial volatile values confirmed against current Government Gazette).

To refresh stale statute values: run `/za-statute-refresh`. To check staleness without refreshing: `python3 scripts/validate-za-statutes.py`.

## Research Connectors (Deferred)

No live SA research connectors are included in this release. The CourtListener, Trellis, and Descrybe connectors in the upstream plugins are US-only and will not return SA case law.

SA connector requirements are documented in [project/mcp-requirements-za.md](../../project/mcp-requirements-za.md). Priority order:
1. **SAFLII** (saflii.org) — SA case law (Labour Court, LAC, Constitutional Court, CCMA awards)
2. **Department of Employment and Labour** (labour.gov.za) — Government Gazette, threshold updates
3. **CCMA** (ccma.org.za) — arbitration awards
4. **LexisNexis SA / Juta** — commercial annotated statutes (vendor plugin, equivalent to CoCounsel)

Until these connectors are available, statute values come from the YAML library and citations are tagged `[model knowledge — verify]`. Connect the research tool manually (paste a judgment, link a Gazette notice) and Claude will tag the source appropriately.
