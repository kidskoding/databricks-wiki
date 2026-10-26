---
type: glossary
status: written
level: 90
section: Glossary
depth: 101
summary: "Moving a query's filter conditions down to the storage or source system so that less data is read."
related:
  - "[[Data Skipping]]"
  - "[[Partition Pruning]]"
  - "[[Apache Parquet]]"
  - "[[Catalyst Optimizer]]"
  - "[[Lakehouse Federation]]"
  - "[[Liquid Clustering]]"
aliases:
  - "filter pushdown"
  - "pushdown"
  - "projection pushdown"
last_verified: 2026-10-26
tags:
  - glossary
  - flashcards
---

# Predicate Pushdown

> [!eli5] Summary
> Predicate pushdown means applying a query's filters as early as possible, close to where the data is stored, so the engine never reads rows it would throw away.

**In data work:** A predicate is a condition such as `WHERE order_date = '2026-10-01'`. Without pushdown, the engine reads every row and then filters. With pushdown, the optimizer sends the condition down to the reader or the source database. Columnar files such as [[Apache Parquet]] keep minimum and maximum values per row group, so a reader can skip whole blocks that cannot match. Projection pushdown does the same for columns: only the columns the query uses are read. A query for one store's sales in one week then reads a small fraction of a multi-year table.

**In Databricks:** The [[Catalyst Optimizer|Catalyst optimizer]] pushes filters into every scan.
- **Delta and Iceberg tables:** Per-file minimum and maximum values, null counts, and row counts let Databricks skip files ([[Data Skipping|data skipping]]). Statistics are collected on the first 32 columns by default; change this with `delta.dataSkippingNumIndexedCols` or `delta.dataSkippingStatsColumns`.
- **Layout:** Pushdown works best when similar values sit in the same files, which [[Liquid Clustering|liquid clustering]] arranges.
- **Parquet v2:** Available in Databricks Runtime 18.1 and above, it adds page-level statistics for finer pruning inside files.
- **[[Lakehouse Federation]]:** Filters, projections, and other operators are pushed to the remote database where supported.
- **Limits:** [[Row Filters and Column Masks|Row filters and column masks]] can prevent some pushdown.

Seen in: [[Data Skipping]], [[Partition Pruning]], [[Apache Parquet]]

## Recall

Predicate pushdown::Sending a query's filter conditions to the storage layer or source system so that non-matching data is never read.
On how many columns does Delta collect statistics by default?::The first 32 columns.

> [!sources]- Sources (last verified: 2026-10-26)
> - [Data skipping (AWS)](https://docs.databricks.com/aws/en/tables/data-skipping)
> - [Data skipping (Azure Databricks)](https://learn.microsoft.com/en-us/azure/databricks/tables/data-skipping)
> - [Parquet v2 (AWS)](https://docs.databricks.com/aws/en/tables/features/parquet-v2)
> - [Performance considerations for row filter and column mask policies (GCP)](https://docs.databricks.com/gcp/en/data-governance/unity-catalog/abac/performance)
> - [Run federated queries on PostgreSQL (AWS)](https://docs.databricks.com/aws/en/query-federation/postgresql)
