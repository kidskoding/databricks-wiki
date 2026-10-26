---
type: glossary
status: written
level: 90
section: Glossary
depth: 101
summary: "Recovery point objective is how much data loss you can tolerate; recovery time objective is how long you can be down. Both drive disaster recovery design."
related:
  - "[[Disaster Recovery]]"
  - "[[Point-in-Time Recovery]]"
  - "[[Replication]]"
  - "[[SLA]]"
  - "[[Region]]"
  - "[[Time Travel]]"
aliases:
  - "RPO"
  - "RTO"
  - "recovery point objective"
  - "recovery time objective"
last_verified: 2026-10-26
tags:
  - glossary
  - flashcards
---

# RPO and RTO

> [!eli5] Summary
> RPO answers "how much recent data can we afford to lose?" RTO answers "how long can we afford to be down?" Together they decide how much to spend on backup and recovery.

**In data work:**
- **Recovery point objective (RPO):** The maximum acceptable age of the data you recover to. An RPO of one hour means losing up to the last hour of changes is acceptable, so copies must be made at least hourly.
- **Recovery time objective (RTO):** The maximum acceptable time to restore service after an outage.

Lower values cost more: near-zero RPO needs continuous [[Replication|replication]], and near-zero RTO needs standby systems ready in another [[Region|region]]. Set targets per workload, not per company. A bakery's online ordering database might need an RPO of minutes, while its monthly sales dashboard can tolerate an RPO of a day and an RTO of a week.

**In Databricks:** The [[Disaster Recovery|disaster recovery]] guidance asks you to define RPO and RTO for each workload before choosing a strategy.
- **Data:** Delta tables can be copied to a secondary region with deep clone, and [[Time Travel|time travel]] or [[Point-in-Time Recovery|point-in-time restore]] covers logical mistakes within one region.
- **Code and configuration:** Keeping jobs, notebooks, and infrastructure in [[Git]], [[Declarative Automation Bundles]], and the [[Terraform Provider]] shortens RTO, because a second workspace can be rebuilt from code.
- **Managed option:** Databricks also documents a managed disaster recovery capability; check its current release status before planning around it.

Seen in: [[Disaster Recovery]], [[Point-in-Time Recovery]], [[SLA]]

## Recall

RPO::Recovery point objective: the maximum acceptable data loss, measured as time.
RTO::Recovery time objective: the maximum acceptable time to restore service.

> [!sources]- Sources (last verified: 2026-10-26)
> - [Disaster recovery (AWS)](https://docs.databricks.com/aws/en/admin/disaster-recovery)
> - [Disaster recovery (Azure)](https://learn.microsoft.com/en-us/azure/databricks/admin/disaster-recovery)
> - [Phase 10: Design high availability and disaster recovery (AWS)](https://docs.databricks.com/aws/en/lakehouse-architecture/deployment-guide/ha-dr)
> - [Managed disaster recovery (AWS)](https://docs.databricks.com/aws/en/admin/managed-disaster-recovery)
> - [Delta Clones Simplify Disaster Recovery (Databricks blog)](https://www.databricks.com/blog/2021/04/20/attack-of-the-delta-clones-against-disaster-recovery-availability-complexity.html)
