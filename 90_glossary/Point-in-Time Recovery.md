---
type: glossary
status: written
level: 90
section: Glossary
depth: 101
summary: "Restoring data to its exact state at a chosen moment in the past, usually to undo an accidental change or corruption."
related:
  - "[[Time Travel]]"
  - "[[Disaster Recovery]]"
  - "[[RPO and RTO]]"
  - "[[Lakebase]]"
  - "[[Delta Transaction Log]]"
  - "[[OPTIMIZE and VACUUM]]"
aliases:
  - "PITR"
  - "point-in-time restore"
  - "RESTORE TABLE"
last_verified: 2026-10-26
tags:
  - glossary
  - flashcards
---

# Point-in-Time Recovery

> [!eli5] Summary
> Point-in-time recovery rewinds data to how it looked at a specific moment, such as five minutes before someone deleted the wrong rows.

**In data work:** Backups taken once a night can only restore last night's state. Point-in-time recovery (PITR) keeps a continuous history, usually a log of every change plus periodic snapshots, so you can restore to any second inside a retention window. It protects against logical mistakes (a bad `DELETE`, a buggy job) that replication would copy faithfully. The retention window is a cost trade-off: longer windows keep more history in storage.

**In Databricks:** Two features provide PITR.
- **Delta tables:** Every commit creates a version, so you can query or restore a past state with [[Time Travel|time travel]]. `RESTORE` rolls a table back to a version or timestamp in one commit. The window is limited by `VACUUM`, which removes old files after 7 days by default (see [[OPTIMIZE and VACUUM]]).
- **[[Lakebase]]:** Point-in-time restore creates a new root branch at the chosen moment and leaves the original running. The restore window is 2 to 30 days (default 7); a longer window uses more storage.

```sql
-- Undo a bad update to the orders table
RESTORE TABLE shop.sales.orders TO TIMESTAMP AS OF '2026-10-26T09:00:00';
```

PITR is not [[Disaster Recovery|disaster recovery]]: it does not help if the region is unavailable. Use it with the targets in [[RPO and RTO]].

Seen in: [[Time Travel]], [[Lakebase]], [[Disaster Recovery]]

## Recall

Point-in-time recovery::Restoring data to its state at a chosen moment within a retention window.
Which SQL command rolls a Delta table back to an earlier version?::RESTORE TABLE ... TO VERSION AS OF or TO TIMESTAMP AS OF.
What is the Lakebase point-in-time restore window?::2 to 30 days, default 7.

> [!sources]- Sources (last verified: 2026-10-26)
> - [RESTORE (Databricks SQL reference, AWS)](https://docs.databricks.com/aws/en/sql/language-manual/delta-restore)
> - [Point-in-time restore (Lakebase, AWS)](https://docs.databricks.com/aws/en/oltp/projects/point-in-time-restore)
> - [Backup and restore methods (Lakebase, Azure Databricks)](https://learn.microsoft.com/en-us/azure/databricks/oltp/projects/backup-methods)
