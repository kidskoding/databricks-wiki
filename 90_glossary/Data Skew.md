---
type: glossary
status: written
level: 90
section: Glossary
depth: 101
summary: "An uneven distribution of data across partitions that leaves a few tasks with most of the work."
related:
  - "[[Partitions]]"
  - "[[Shuffles]]"
  - "[[Adaptive Query Execution]]"
  - "[[Spark UI]]"
  - "[[Jobs Stages and Tasks]]"
  - "[[Liquid Clustering]]"
aliases:
  - "skew"
  - "skewed data"
  - "hot key"
  - "skewed partition"
last_verified: 2026-10-25
tags:
  - glossary
  - flashcards
---

# Data Skew

> [!eli5] Summary
> Data skew happens when one part of a job has far more data than the others. The whole job waits for that one slow part to finish.

**In data work:** Spark processes [[Partitions|partitions]] in parallel. If one key has many more rows than others, the partition containing it is much larger, and its task runs long after the rest finish. Common causes are default or null keys (for example, all guest orders with `customer_id = 0`) and dominant customers, products, or dates. In the [[Spark UI]], skew appears as a stage where one task takes far longer than the median, often with [[Spill|spill]].

**In Databricks:** [[Adaptive Query Execution]] detects skewed partitions in shuffle-based joins (sort-merge and shuffle hash) from shuffle statistics and splits them into smaller subpartitions. It is enabled by default. A partition counts as skewed when it exceeds both a multiple of the median size (default factor 5) and an absolute size (default 256 MB). AQE does not handle skew in broadcast joins. For skew below the thresholds, lower them or salt the hot keys and aggregate in two stages.

Seen in: [[Partitions]], [[Shuffles]], [[Adaptive Query Execution]], [[Spark UI]]

## Recall

How does data skew appear in the Spark UI?::One or a few tasks in a stage take much longer than the median.
Which join types does AQE skew handling apply to?::Shuffle-based joins: sort-merge and shuffle hash joins.

> [!sources]- Sources (last verified: 2026-10-25)
> - [Adaptive query execution (AWS)](https://docs.databricks.com/aws/en/optimizations/aqe)
> - [Skew and spill (AWS)](https://docs.databricks.com/aws/en/optimizations/spark-ui-guide/long-spark-stage-page)
