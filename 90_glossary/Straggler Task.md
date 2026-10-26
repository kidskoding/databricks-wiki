---
type: glossary
status: written
level: 90
section: Glossary
depth: 101
summary: "A task that runs much longer than the other tasks in the same stage, holding up the whole stage."
related:
  - "[[Speculative Execution]]"
  - "[[Data Skew]]"
  - "[[Spark UI]]"
  - "[[Spill]]"
  - "[[Jobs Stages and Tasks]]"
  - "[[Adaptive Query Execution]]"
aliases:
  - "straggler"
  - "stragglers"
  - "slow task"
  - "long-tail task"
last_verified: 2026-10-26
tags:
  - glossary
  - flashcards
---

# Straggler Task

> [!eli5] Summary
> A straggler is the one slow worker the rest of the team is waiting for. In Spark, a stage is not done until its slowest task finishes.

**In data work:** A Spark stage runs many tasks in parallel, one per [[Partitions|partition]], and the next stage starts only when all of them finish. If 199 tasks take 10 seconds and one takes 10 minutes, the stage takes 10 minutes and most of the cluster sits idle. Common causes:
- **[[Data Skew|Data skew]]:** One partition holds far more rows, often a single popular key in a join or group-by.
- **[[Spill]]:** A task runs out of memory and writes intermediate data to disk.
- **A bad node:** Slow disk or network on one machine.
- **Expensive records:** A few very large or complex values.

**In Databricks:** Find stragglers in the [[Spark UI]]. On the stage page, compare the maximum task duration with the median and 75th percentile; a maximum far above the others points to skew, and the spill columns show memory pressure. Fixes depend on the cause:
1. For skewed joins, rely on [[Adaptive Query Execution]], which splits oversized partitions at run time.
2. For skewed keys, salt the key or filter out the hot value and process it separately.
3. For spill, use more partitions or a larger instance type.
4. For a bad node, enable [[Speculative Execution|speculative execution]].

A small team usually meets stragglers when one customer or product accounts for a large share of all rows.

Seen in: [[Data Skew]], [[Spark UI]], [[Distributed Systems]]

## Recall

Straggler task::A task much slower than its siblings in a stage, which delays the whole stage.
What Spark UI comparison suggests skew?::A maximum task duration far above the median and 75th percentile.

> [!sources]- Sources (last verified: 2026-10-26)
> - [Skew and spill (AWS)](https://docs.databricks.com/aws/en/optimizations/spark-ui-guide/long-spark-stage-page)
> - [Skew and spill (Azure)](https://learn.microsoft.com/en-us/azure/databricks/optimizations/spark-ui-guide/long-spark-stage-page)
> - [Adaptive query execution (AWS)](https://docs.databricks.com/aws/en/optimizations/aqe)
