---
type: glossary
status: written
level: 90
section: Glossary
depth: 101
summary: "A join strategy that copies a small table to every executor so the large table does not have to be shuffled."
related:
  - "[[Shuffles]]"
  - "[[Adaptive Query Execution]]"
  - "[[Catalyst Optimizer]]"
  - "[[Driver and Executors]]"
  - "[[Query Performance and Caching]]"
  - "[[Join]]"
aliases:
  - "broadcast hash join"
  - "map-side join"
  - "BROADCAST hint"
last_verified: 2026-10-25
tags:
  - glossary
  - flashcards
---

# Broadcast Join

> [!eli5] Summary
> A broadcast join sends a full copy of a small table to every worker machine. Each worker can then match its share of the large table without moving data between machines.

**In data work:** A standard distributed [[Join|join]] [[Shuffles|shuffles]] both tables so that matching keys meet on the same executor. When one table is small, Spark can instead send a full copy of it to every [[Driver and Executors|executor]], and each executor joins its partitions of the large table locally. Example: joining 500 million sales rows to a 2,000-row store table broadcasts the store table. Broadcasting a table that is too large can exhaust driver or executor memory.

**In Databricks:** The [[Catalyst Optimizer]] chooses a broadcast join when statistics show a table is below a size threshold. [[Adaptive Query Execution]] can convert a sort-merge join to a broadcast hash join at runtime; on Databricks this conversion is controlled by `spark.databricks.adaptive.autoBroadcastJoinThreshold` (documented default 30 MB). A hint such as `SELECT /*+ BROADCAST(stores) */ ...` overrides the threshold. Some join types cannot broadcast a given side: AQE cannot broadcast the left side of a `LEFT OUTER JOIN`, and full outer joins do not support broadcast. Check the final plan in the [[Spark UI]] SQL tab.

Seen in: [[Shuffles]], [[Adaptive Query Execution]], [[Catalyst Optimizer]], [[Query Performance and Caching]]

## Recall

What does a broadcast join avoid?::Shuffling the large table, by copying the small table to every executor.
What overrides the broadcast size threshold in Databricks SQL?::A BROADCAST join hint on the table.

> [!sources]- Sources (last verified: 2026-10-25)
> - [Adaptive query execution (AWS)](https://docs.databricks.com/aws/en/optimizations/aqe)
> - [Hints (AWS)](https://docs.databricks.com/aws/en/sql/language-manual/sql-ref-syntax-qry-select-hints)
