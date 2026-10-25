---
type: glossary
status: written
level: 90
section: Glossary
depth: 101
summary: "Skipping whole folders of a table because the query's filter shows they cannot contain matching rows."
related:
  - "[[Partitions]]"
  - "[[Data Skipping]]"
  - "[[Liquid Clustering]]"
  - "[[Z-Ordering]]"
  - "[[Query Performance and Caching]]"
  - "[[Catalyst Optimizer]]"
aliases:
  - "partition elimination"
  - "dynamic partition pruning"
  - "DPP"
last_verified: 2026-10-25
tags:
  - glossary
  - flashcards
---

# Partition Pruning

> [!eli5] Summary
> Partition pruning is skipping parts of a table that cannot contain the rows a query asks for. Reading less data makes the query faster.

**In data work:** When a table is split into [[Partitions|partitions]] by a column (often date), each partition is stored separately, usually as a folder such as `order_date=2026-10-01/`. If a [[Query|query]] filters on that column, the engine reads only the matching partitions and prunes the rest, which cuts the data scanned and the time taken. Dynamic partition pruning, added in Spark 3.0, does this even when the filter comes from a joined table. Pruning only helps if queries filter on the partition column, and partitioning by a column with too many values creates lots of tiny files.

**In Databricks:** Delta tables in Databricks support partitioning and prune partitions automatically through the [[Catalyst Optimizer]]. Databricks now recommends [[Liquid Clustering]] for most new tables instead of manual partitioning; it relies on file-level statistics and [[Data Skipping|data skipping]], which achieves a similar effect without fixed folders. Databricks' guidance: do not partition tables under 1 TB, consider liquid clustering for 1 to 100 TB, and only partition by a column if each partition will hold at least 1 GB. Dynamic partition pruning is on by default.

Seen in: [[Partitions]], [[Data Skipping]], [[Liquid Clustering]]

## Recall

Partition Pruning::Reading only the partitions that can match a query's filter and skipping the rest, which cuts data scanned.

> [!sources]- Sources (last verified: 2026-10-25)
> - [When to partition tables on Databricks (AWS)](https://docs.databricks.com/aws/en/tables/partitions)
> - [When to partition tables (Azure Databricks)](https://learn.microsoft.com/en-us/azure/databricks/tables/partitions)
> - [Introducing Spark 3.0 in Databricks Runtime 7.0 (Databricks blog)](https://www.databricks.com/blog/2020/06/18/introducing-apache-spark-3-0-now-available-in-databricks-runtime-7-0.html)
> - [Comprehensive Guide to Optimize Data Workloads](https://www.databricks.com/discover/pages/optimize-data-workloads-guide)
