# Regulatory Feed Sources — South African Framework

This overlay covers the available data sources for monitoring South African regulatory developments, including free and paid feeds, regulator-specific publication channels, and the feed-check workflow. It is loaded by reg-feed-watcher and cold-start-interview skills when jurisdiction = ZA.

---

## 1. SA feed architecture

South Africa does not have:

- A structured JSON API for the Government Gazette (contrast: US Federal Register API)
- A centralised comment submission portal with tracking (contrast: US Regulations.gov)
- A free structured case law database with API access (contrast: US CourtListener)

Monitoring SA regulatory developments therefore requires assembling feeds from multiple sources with different structures, update frequencies, and access models.

---

## 2. Tier 1 — free feeds (always active)

### Open Gazettes (opengazettes.org.za)

A civil society project providing free searchable access to 20,000+ Government Gazette issues.

| Feature | Detail |
|---|---|
| Atom feed | Recently added gazettes (last 100 entries) — use for real-time monitoring |
| JSON index | Metadata for all gazettes (date, number, type, URL) in JSON lines format — use for historical search |
| Coverage | National and provincial gazettes |
| Lag | Typically 1–3 days after GPW publication |
| Documentation | opengazettes.org.za/about.html |

Primary monitoring source. The Atom feed is the backbone of the reg-feed-watcher workflow.

### gov.za documents and notices

The official government portal lists documents and notices at gov.za/documents/notices.

| Feature | Detail |
|---|---|
| Structure | HTML listing; no structured API |
| Coverage | National government documents, notices, speeches |
| Lag | Variable; some documents appear before the Gazette |
| Reliability | Intermittent — not all Gazette items appear here |

Useful as a supplementary source but not reliable as a primary feed.

### Direct regulator RSS and email

Most major regulators publish updates on their websites. Availability varies:

- Some offer email subscription or newsletter sign-up (FSCA, SARS, Information Regulator)
- Some publish RSS feeds (rare and often unmaintained)
- Most publish a "latest news" or "media statements" page that can be scraped

These are essential for catching non-Gazette publications: guidance notes, practice notes, media statements, FAQs, and interpretation notes that never appear in the Gazette but shape compliance obligations.

---

## 3. Tier 2 — structured and paid feeds

### Laws.Africa Content API

Structured legislation in Akoma Ntoso XML and HTML format.

| Feature | Detail |
|---|---|
| Content | Legislation, regulations, by-laws — consolidated and point-in-time |
| Format | Akoma Ntoso XML, HTML, PDF |
| Metadata | Citation graphs, amendment tracking, publication dates, commencement status |
| Access | Free tier for non-commercial use; commercial subscriptions available |
| Documentation | laws.africa/api/detail |

Primary source for verifying current consolidated text and amendment history.

### Sabinet

Comprehensive South African legal database (paid subscription).

| Feature | Detail |
|---|---|
| Content | Gazette archive, legislation, case law, legal journals |
| Coverage | Extensive historical archive dating back decades |
| Access | Institutional or commercial subscription |

Gold standard for historical research and comprehensive Gazette archive searching.

---

## 4. Regulator feed mapping (core 12)

| # | Regulator | Website | RSS/feed available | Email subscription | Gazette notice pattern |
|---|---|---|---|---|---|
| 1 | SARS | sars.gov.za | No | Yes — mailing list | Binding rulings, interpretation notes via website; tax law amendments via National Treasury Gazette |
| 2 | CIPC | cipc.co.za | No | Yes — newsletter | Practice notes and compliance notices via website; regulations via Gazette |
| 3 | DEL | labour.gov.za | No | No | Sectoral determinations and regulations via Gazette; codes of good practice via Gazette |
| 4 | FSCA | fsca.co.za | No | Yes — regulatory updates | Conduct standards, joint standards, board notices via Gazette; guidance via website |
| 5 | PA/SARB | resbank.co.za | No | Yes — subscription service | Prudential standards and directives via Gazette; exchange control circulars via website |
| 6 | National Treasury | treasury.gov.za | No | Yes — mailing list | Draft tax bills, policy papers via website and Gazette; budget documents via website |
| 7 | NCR | ncr.org.za | No | No | Regulations and guidelines via Gazette; compliance notices via website |
| 8 | B-BBEE Commission | bbbeecommission.co.za | No | No | Codes of good practice via Gazette; sector codes via Gazette; reports via website |
| 9 | SAHPRA | sahpra.org.za | No | Yes — newsletter | Regulations and schedules via Gazette; guidelines and notices via website |
| 10 | NCC | thencc.gov.za | No | No | Regulations and industry codes via Gazette; compliance notices via website |
| 11 | Competition Commission | compcom.co.za | No | Yes — media releases | Regulations and guidelines via Gazette; exemptions via Gazette; media statements via website |
| 12 | Information Regulator | inforegulator.org.za | No | Yes — newsletter | Regulations and codes of conduct via Gazette; guidance notes via website |

---

## 5. Feed-check workflow

The reg-feed-watcher skill executes the following workflow on each check cycle:

### Step 1 — Pull gazette feed

Pull the Open Gazettes Atom feed for entries since the last check timestamp. Parse each entry for gazette number, date, and title.

### Step 2 — Keyword and regulator filter

Match each new gazette entry against the user's watchlist:

- Regulator name matches (e.g., "Financial Sector Conduct Authority", "FSCA")
- Statute references (e.g., "Financial Sector Regulation Act", "NCA")
- Topic keywords from the user's practice profile (e.g., "conduct standard", "B-BBEE", "data protection")

### Step 3 — Pull per-regulator feeds

For each regulator on the user's watchlist, check the regulator's website for non-Gazette publications:

- Guidance notes, practice notes, interpretation notes
- Media statements announcing regulatory intentions
- Draft documents published for comment on the regulator's website (not all are gazetted)

### Step 4 — De-duplicate

The same document may appear in the Gazette and on the regulator's website. De-duplicate by matching on:

- Gazette number and notice number
- Document title similarity
- Publication date proximity

### Step 5 — Classify by materiality

Apply the user's materiality threshold from the practice profile:

| Tier | Criteria | Action |
|---|---|---|
| 🔴 High | New binding instrument in user's practice areas; comment deadline within 14 days | Immediate alert |
| 🟡 Medium | Draft instrument for comment; guidance note in adjacent area; comment deadline > 14 days | Include in next digest |
| 🟢 Low | Informational notice; media statement; item outside core practice areas | Weekly summary only |

### Step 6 — Produce digest

Generate a digest grouped by materiality tier, with:

- Document title and gazette reference (if applicable)
- Regulator and enabling statute
- Comment deadline (if applicable)
- Brief summary of the instrument's subject matter
- Link to source document
