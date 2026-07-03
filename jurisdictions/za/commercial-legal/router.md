# Skill Router — South African Commercial Contracts Overlay

When jurisdiction = ZA, skills load the topic overlays and statute files listed below.

Topic files resolve to: `jurisdictions/za/commercial-legal/topics/{name}.md`
Statute files resolve to: `jurisdictions/za/statutes/{name}.yaml`

```yaml
vendor-agreement-review:
  topics: [contract-fundamentals, liability-and-penalties, data-protection, competition-and-bbbee, confidentiality-and-restraint, dispute-resolution]
  statutes: [cpa, vat, ecta, popia, conventional-penalties, competition, bbbee, prescription, copyright]

saas-msa-review:
  topics: [contract-fundamentals, liability-and-penalties, data-protection, competition-and-bbbee, dispute-resolution]
  statutes: [cpa, vat, ecta, popia, conventional-penalties, competition, bbbee, prescription]

nda-review:
  topics: [contract-fundamentals, data-protection, confidentiality-and-restraint, dispute-resolution]
  statutes: [ecta, popia, prescription]

cold-start-interview:
  topics: []
  statutes: [cpa, vat, ecta, popia, conventional-penalties, competition, bbbee, prescription, copyright]

customize:
  topics: []
  statutes: []
```
