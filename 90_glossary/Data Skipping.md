---
type: glossary
status: written
level: 90
section: Glossary
depth: 101
summary: "Avoiding reads of files that cannot contain matching rows, using per-file column statistics such as minimum and maximum values."
related:
  - "[[Delta Lake]]"
  - "[[Delta Transaction Log]]"
  - "[[Liquid Clustering]]"
  - "[[Z-Ordering]]"
  - "[[Columnar Storage]]"
  - "[[Query Performance and Caching]]"
aliases:
  - "file skipping"
  - "file pruning"
  - "column statistics"
  - "dataSkippingNumIndexedCols"
last_verified: 2026-10-25
tags:
  - glossary
  - flashcards
---

# Data Skipping

> [!eli5] Summary
> Data skipping lets a query ignore files that cannot contain the data it is looking for, so it reads less and finishes faster.

**In data work:** A table format records statistics for each data file, such as the minimum and maximum value of each column. For a query such as `WHERE order_date = '2026-03-01'`, the engine checks these statistics and skips files whose ranges exclude that date. Skipping is most effective when related values are stored together in the same files.

**In Databricks:** [[Delta Lake]] collects file statistics automatically on write and records them in the [[Delta Transaction Log|transaction log]]. For Unity Catalog external tables, statistics are collected on the first 32 columns of the schema by default; for managed tables, predictive optimization can also collect statistics on frequently filtered columns beyond the first 32. The table properties `delta.dataSkippingNumIndexedCols` and `delta.dataSkippingStatsColumns` change the columns; run `ANALYZE TABLE ... COMPUTE DELTA STATISTICS` to recompute existing statistics. [[Liquid Clustering]] groups related rows into the same files and replaces partitioning and [[Z-Ordering]] for new tables.

Seen in: [[Delta Lake]], [[Liquid Clustering]], [[Z-Ordering]], [[Query Performance and Caching]]

## Recall

On how many columns does Delta collect statistics by default for an external table?::The first 32 columns of the schema.
Which table property names specific columns for statistics collection?::delta.dataSkippingStatsColumns.

> [!sources]- Sources (last verified: 2026-10-25)
> - [Data skipping (AWS)](https://docs.databricks.com/aws/en/tables/data-skipping)
> - [Use liquid clustering for tables (AWS)](https://docs.databricks.com/aws/en/tables/clustering)
