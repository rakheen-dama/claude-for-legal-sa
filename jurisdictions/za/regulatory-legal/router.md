# Skill Router — South African Regulatory Law Overlay

When jurisdiction = ZA, skills load the topic overlays and statute files listed below.

Topic files resolve to: `jurisdictions/za/regulatory-legal/topics/{name}.md`
Statute files resolve to: `jurisdictions/za/statutes/{name}.yaml`

```yaml
reg-feed-watcher:
  topics: [regulatory-process, feed-sources, regulators]
  statutes: [paja, fsr]

policy-diff:
  topics: [rule-status-verification, regulators]
  statutes: [paja]

comments:
  topics: [regulatory-process, regulators]
  statutes: [paja, fsr]

gap-surfacer:
  topics: [rule-status-verification, regulators]
  statutes: [paja]

policy-redraft:
  topics: [rule-status-verification]
  statutes: [paja]

cold-start-interview:
  topics: [regulatory-process, feed-sources, regulators]
  statutes: [paja, fsr, fica, nema, ohsa, nca, precca, popia, cpa, competition, ecta, cybercrimes, bbbee, paia]
```
