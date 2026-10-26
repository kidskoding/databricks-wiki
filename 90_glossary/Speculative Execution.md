---
type: glossary
status: written
level: 90
section: Glossary
depth: 101
summary: "Launching a backup copy of a slow-running task on another machine and using whichever copy finishes first."
related:
  - "[[Straggler Task]]"
  - "[[Fault Tolerance]]"
  - "[[MapReduce]]"
  - "[[Jobs Stages and Tasks]]"
  - "[[Data Skew]]"
  - "[[Distributed Systems]]"
aliases:
  - "speculation"
  - "spark.speculation"
  - "backup tasks"
last_verified: 2026-10-26
tags:
  - glossary
  - flashcards
---

# Speculative Execution

> [!eli5] Summary
> Speculative execution starts a second copy of a task that is running unusually slowly, on a different machine. Whichever copy finishes first wins, and the other is cancelled.

**In data work:** In a large job, one slow machine (a failing disk, a noisy neighbor) can hold up thousands of finished tasks. The 2004 MapReduce paper addressed this with **backup tasks**: near the end of a job, the runtime launches duplicates of the remaining in-progress tasks. This works because tasks are deterministic, so either copy produces the same output. It costs extra compute and does not help when a task is slow because of its data.

**In Databricks:** Apache Spark calls this speculation. It is off by default.

| Setting | Default | Meaning |
|---|---|---|
| `spark.speculation` | `false` | Turns speculation on |
| `spark.speculation.multiplier` | `1.5` | How many times slower than the median a task must be |
| `spark.speculation.quantile` | `0.75` | Fraction of tasks in a stage that must finish first |
| `spark.speculation.interval` | `100ms` | How often Spark checks for slow tasks |

Set these in the cluster's Spark configuration. Speculation helps with bad machines, not with [[Data Skew|data skew]]: a duplicate of a task with too much data is just as slow. Diagnose skew in the [[Spark UI]] first, and use [[Adaptive Query Execution]] for skewed joins. Tasks with side effects, such as writing to an external system, should be [[Idempotency|idempotent]] before you enable it.

Seen in: [[Distributed Systems]], [[Jobs Stages and Tasks]], [[Google File System and MapReduce Papers]]

## Recall

Speculative execution::Running a backup copy of a slow task on another machine and keeping the first result.
Does speculative execution fix data skew?::No. The duplicate processes the same oversized partition and is just as slow.

> [!sources]- Sources (last verified: 2026-10-26)
> - [Configuration (Spark 3.5.6 documentation)](https://spark.apache.org/docs/3.5.6/configuration.html)
> - [What is speculative execution in Spark in Azure HDInsight? (Microsoft Learn)](https://learn.microsoft.com/en-us/azure/hdinsight/spark/what-is-speculative-execution-in-spark)
> - [MapReduce: Simplified Data Processing on Large Clusters (OSDI 2004), Google Research](https://research.google/pubs/pub62/?hl=es)
