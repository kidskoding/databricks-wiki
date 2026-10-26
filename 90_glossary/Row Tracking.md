---
type: glossary
status: written
level: 90
section: Glossary
depth: 101
summary: "A Delta Lake table feature that gives every row a stable ID and the version in which it last changed, so changes can be tracked row by row."
related:
  - "[[Delta Lake]]"
  - "[[Change Data Feed]]"
  - "[[Materialized Views]]"
  - "[[Deletion Vectors]]"
  - "[[Delta Transaction Log]]"
  - "[[Lakeflow Spark Declarative Pipelines]]"
aliases:
  - "row IDs"
  - "delta.enableRowTracking"
  - "row commit version"
last_verified: 2026-10-26
tags:
  - glossary
  - flashcards
---

# Row Tracking

> [!eli5] Summary
> Row tracking stamps each row in a table with a permanent ID and a record of when it last changed. Downstream systems can then process only the rows that changed.

**In data work:** Files in a lakehouse table are rewritten constantly by updates, merges, and compaction, so a row's physical position is not a stable identity. Without a stable identity, a downstream job cannot tell which rows changed and must recompute everything. Row tracking adds two pieces of metadata to every row: an ID that survives file rewrites, and the table version in which the row was last modified.

**In Databricks:** Row tracking is a Delta table feature, generally available since Databricks Runtime 14.0. Enable it with a table property:

```sql
ALTER TABLE shop.sales.orders
  SET TBLPROPERTIES ('delta.enableRowTracking' = 'true');
```

You can read the values through the hidden `_metadata.row_id` and `_metadata.row_commit_version` fields. Row tracking powers:
- **Incremental refresh of [[Materialized Views|materialized views]]:** Databricks recommends enabling row tracking, [[Deletion Vectors|deletion vectors]], and change data feed on source tables.
- **Automatic [[Change Data Feed|change data feed]]:** Computes row-level changes at query time from row tracking; generally available as of September 2026.

Automatic upgrades began enabling row tracking on existing tables in July 2026, and all Apache Iceberg v3 tables include it. Enabling it upgrades the table protocol, so older readers that do not support the feature cannot read the table. For a small team, row tracking mainly means cheaper incremental pipelines with no extra code.

Seen in: [[Change Data Feed]], [[Materialized Views]], [[Delta Lake]]

## Recall

Row tracking::A Delta table feature that assigns each row a stable ID and its last-modified commit version.
Which table property enables row tracking?::delta.enableRowTracking = true.

> [!sources]- Sources (last verified: 2026-10-26)
> - [Row tracking in Databricks (AWS)](https://docs.databricks.com/aws/en/tables/features/row-tracking)
> - [Delta Lake feature compatibility and protocols (AWS)](https://docs.databricks.com/aws/en/tables/features/feature-compatibility)
