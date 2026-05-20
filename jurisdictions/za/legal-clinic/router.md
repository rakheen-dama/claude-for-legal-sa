# Legal-Clinic — South African Skill Router

Maps each skill to the topic overlays and statute files it should load when jurisdiction = ZA.

Topic files resolve to `jurisdictions/za/legal-clinic/topics/{name}.md`.
Statute files resolve to `jurisdictions/za/statutes/{name}.yaml`.

```yaml
cold-start-interview:
  topics: [clinic-regulatory-framework, supervision-and-ethics, clinic-client-access]
  statutes: [lpa, lpc-rules, legal-aid-sa]

build-guide:
  topics: [clinic-regulatory-framework, supervision-and-ethics]
  statutes: [lpa, lpc-rules]

ramp:
  topics: [clinic-regulatory-framework, supervision-and-ethics, sa-court-system, sa-legal-research, clinic-client-access]
  statutes: [lpa, lpc-rules]

client-intake:
  topics: [clinic-practice-areas, clinic-client-access]
  statutes: [dva, maintenance, childrens-act, small-claims, cpa, nca, popia]

draft:
  topics: [clinic-practice-areas, sa-court-system, sa-procedural-rules]
  statutes: [dva, maintenance, childrens-act, criminal-procedure, magistrates-courts, state-liability]

deadlines:
  topics: [sa-procedural-rules, sa-court-system]
  statutes: [prescription, dva, magistrates-courts, state-liability]

research-start:
  topics: [sa-legal-research, sa-court-system]
  statutes: []

memo:
  topics: [sa-legal-research, clinic-practice-areas]
  statutes: [dva, maintenance, childrens-act]

status:
  topics: [sa-court-system, sa-procedural-rules]
  statutes: [magistrates-courts]

supervisor-review-queue:
  topics: [clinic-regulatory-framework, supervision-and-ethics]
  statutes: [lpa, lpc-rules]
```
