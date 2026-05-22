# Skill Router — South African Product Law Overlay

When jurisdiction = ZA, skills load the topic overlays and statute files listed below.

Topic files resolve to: `jurisdictions/za/product-legal/topics/{name}.md`
Statute files resolve to: `jurisdictions/za/statutes/{name}.yaml`

```yaml
launch-review:
  topics: [consumer-protection, advertising-and-claims, e-commerce-and-digital, sector-regulatory-map]
  statutes: [cpa, ecta, popia, competition, lotteries, merchandise-marks]

marketing-claims-review:
  topics: [advertising-and-claims, e-commerce-and-digital]
  statutes: [cpa, ecta, lotteries, merchandise-marks, competition]

feature-risk-assessment:
  topics: [consumer-protection, sector-regulatory-map]
  statutes: [cpa, popia, ecta]

is-this-a-problem:
  topics: [consumer-protection, advertising-and-claims, sector-regulatory-map]
  statutes: [cpa, popia, ecta, competition]

cold-start-interview:
  topics: []
  statutes: [cpa, ecta, popia, nca, fica, competition]
```
