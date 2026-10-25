---
type: glossary
status: written
level: 90
section: Glossary
depth: 101
summary: "A Delta Lake technique that sorts related values into the same files so queries can skip more files."
related:
  - "[[Liquid Clustering]]"
  - "[[OPTIMIZE and VACUUM]]"
  - "[[Data Skipping]]"
  - "[[Partition Pruning]]"
  - "[[Delta Lake]]"
  - "[[Partitions]]"
aliases:
  - "Z-order"
  - "ZORDER"
  - "ZORDER BY"
  - "Z-order clustering"
  - "multi-dimensional clustering"
last_verified: 2026-10-25
tags:
  - glossary
  - flashcards
---

# Z-Ordering

> [!eli5] Summary
> Z-ordering is a way of arranging a table's data files so rows with similar values are stored together. Queries that filter on those values can skip most files.

**In data work:** Z-ordering (from the Z-order space-filling curve) rewrites a table's files so rows with similar values in several chosen columns are stored together. Each file then covers a narrow range of those values, so min and max statistics let the engine skip most files for a filter on any of the columns (see [[Data Skipping]]). It works best on columns that are often filtered and have many distinct values, such as `customer_id` or `event_date`. Its downsides: you must rerun it as new data arrives, and rewriting files takes compute.

**In Databricks:** In Delta Lake on Databricks you run `OPTIMIZE sales ZORDER BY (customer_id, sale_date)` (see [[OPTIMIZE and VACUUM]]). Databricks now recommends [[Liquid Clustering]] for new tables instead: it adapts clustering incrementally, lets you change the keys without rewriting the whole table, and replaces both Z-ordering and [[Partitions|partitioning]]. Liquid clustering and Z-ordering cannot be combined on one table.

Seen in: [[Liquid Clustering]], [[OPTIMIZE and VACUUM]], [[Data Skipping]]

## Recall

Z-Ordering::Rewriting Delta files so similar values across chosen columns sit together, improving data skipping; liquid clustering is now preferred for new tables.

> [!sources]- Sources (last verified: 2026-10-25)
> - [Use liquid clustering for tables (AWS)](https://docs.databricks.com/aws/en/tables/clustering)
> - [Use liquid clustering for tables (Azure Databricks)](https://learn.microsoft.com/en-us/azure/databricks/tables/clustering)
> - [Announcing General Availability of Liquid Clustering](https://www.databricks.com/blog/announcing-general-availability-liquid-clustering)
