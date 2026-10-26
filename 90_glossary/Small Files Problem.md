---
type: glossary
status: written
level: 90
section: Glossary
depth: 101
summary: "The slowdown caused when a table consists of many tiny files, because opening and tracking each file costs more than reading its data."
related:
  - "[[OPTIMIZE and VACUUM]]"
  - "[[Predictive Optimization]]"
  - "[[Liquid Clustering]]"
  - "[[Structured Streaming]]"
  - "[[HDFS]]"
  - "[[Partitions]]"
aliases:
  - "small file problem"
  - "too many small files"
  - "auto compaction"
  - "optimized writes"
last_verified: 2026-10-26
tags:
  - glossary
  - flashcards
---

# Small Files Problem

> [!eli5] Summary
> A table split into thousands of tiny files is slow to read, because the system spends more time opening files than reading data. The fix is to combine them into fewer, larger files.

**In data work:** Each file has a fixed overhead: a metadata entry, an open request to storage, and a footer to read. With millions of small files, that overhead dominates. In [[HDFS]], small files also exhausted the NameNode's memory. In object storage, they mean more requests and slower query planning. Common causes are frequent small appends, streaming micro-batches, and over-partitioning by a high-cardinality column. A shop that appends each sale as its own file creates the problem within weeks.

**In Databricks:** Delta tables offer several fixes.
- **Optimized writes:** Shuffle data during a write so fewer, larger files are produced.
- **Auto compaction:** After a write commits, combine small files within partitions on the same cluster. For Unity Catalog managed tables, Databricks recommends the `auto` setting. Both features are always on for `MERGE`, `UPDATE`, and `DELETE`.
- **`OPTIMIZE`:** Rewrite small files into larger ones (see [[OPTIMIZE and VACUUM]]). Databricks recommends scheduled `OPTIMIZE` for tables over 1 TB, because auto compaction and optimized writes do not fully replace it.
- **[[Predictive Optimization|Predictive optimization]]:** Runs `OPTIMIZE` automatically on Unity Catalog managed tables using serverless compute.
- **Layout:** Avoid over-partitioning; use [[Liquid Clustering|liquid clustering]] instead.

Seen in: [[OPTIMIZE and VACUUM]], [[HDFS]], [[Query Performance and Caching]]

## Recall

Small files problem::Performance loss when a table has many tiny files, because per-file overhead outweighs the data read.
Which Delta features reduce small files automatically during writes?::Optimized writes and auto compaction.

> [!sources]- Sources (last verified: 2026-10-26)
> - [Control data file size (AWS)](https://docs.databricks.com/aws/en/tables/tune-file-size)
> - [Control data file size (Azure Databricks)](https://learn.microsoft.com/en-us/azure/databricks/tables/tune-file-size)
> - [Optimize data file layout (AWS)](https://docs.databricks.com/aws/en/delta/optimize)
> - [Best practices for performance efficiency (AWS)](https://docs.databricks.com/aws/en/lakehouse-architecture/performance-efficiency/best-practices)
