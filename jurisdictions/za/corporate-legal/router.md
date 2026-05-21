# Skill Router — South African Corporate Law Overlay

When jurisdiction = ZA, skills load the topic overlays and statute files listed below.

Topic files resolve to: `jurisdictions/za/corporate-legal/topics/{name}.md`
Statute files resolve to: `jurisdictions/za/statutes/{name}.yaml`

```yaml
board-minutes:
  topics: [board-governance]
  statutes: [companies-act, companies-regulations]

closing-checklist:
  topics: [fundamental-transactions, takeover-regulation]
  statutes: [companies-act, companies-regulations, competition]

cold-start-interview:
  topics: []
  statutes: [companies-act, companies-regulations, competition, bbbee, close-corporations]

diligence-issue-extraction:
  topics: [fundamental-transactions, takeover-regulation, diligence-sa]
  statutes: [companies-act, competition, bbbee, popia]

entity-compliance:
  topics: [entity-compliance-cipc]
  statutes: [companies-act, close-corporations]

integration-management:
  topics: [fundamental-transactions, diligence-sa]
  statutes: [companies-act, competition, bbbee, lra]

material-contract-schedule:
  topics: [fundamental-transactions, diligence-sa]
  statutes: [companies-act, competition]

written-consent:
  topics: [board-governance]
  statutes: [companies-act, companies-regulations]
```
