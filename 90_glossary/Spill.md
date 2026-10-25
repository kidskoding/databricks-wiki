---
type: glossary
status: written
level: 90
section: Glossary
depth: 101
summary: "When Spark runs out of memory for a task and writes temporary data to disk, which slows the job."
related:
  - "[[Spark UI]]"
  - "[[Shuffles]]"
  - "[[Data Skew]]"
  - "[[Adaptive Query Execution]]"
  - "[[Driver and Executors]]"
  - "[[Query Performance and Caching]]"
aliases:
  - "disk spill"
  - "memory spill"
  - "spilling"
  - "spill to disk"
last_verified: 2026-10-25
tags:
  - glossary
  - flashcards
---

# Spill

> [!eli5] Summary
> Spill is when a processing task runs out of memory and temporarily writes data to disk. The job still finishes, but more slowly.

**In data work:** Operations like sorts, [[Join|joins]], and [[Aggregation|aggregations]] need memory to hold intermediate data. When a task's share of memory runs out, Spark writes (spills) part of it to local disk and reads it back later. Disk is far slower than memory, so heavy spill can turn a minute-long job into an hour-long one. Common causes are [[Data Skew|skewed]] partitions where one task gets far more data than the rest, too few shuffle partitions, or workers with too little memory. Spill is not an error; it is a performance warning.

**In Databricks:** The stage page of the [[Spark UI]] shows spill statistics; if none appear, the stage did not spill. Databricks' suggested fixes include auto-optimized shuffle partitions (`spark.sql.shuffle.partitions=auto`), holding less data in memory, and executors with more memory. [[Adaptive Query Execution]] also helps with skewed partitions. [[Shuffles]] explains where most spill comes from.

Seen in: [[Spark UI]], [[Shuffles]], [[Data Skew]], [[Adaptive Query Execution]]

## Recall

Spill::Spark writing intermediate data to disk when task memory runs out; it slows jobs and shows in the Spark UI per stage.

> [!sources]- Sources (last verified: 2026-10-25)
> - [Skew and spill (AWS)](https://docs.databricks.com/aws/en/optimizations/spark-ui-guide/long-spark-stage-page)
> - [Spark memory issues (Google Cloud)](https://docs.databricks.com/gcp/en/optimizations/spark-ui-guide/spark-memory-issues)
