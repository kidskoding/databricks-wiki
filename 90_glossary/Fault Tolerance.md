---
type: glossary
status: written
level: 90
section: Glossary
depth: 101
summary: "The ability of a system to continue operating, or recover without data loss, when a component fails."
related:
  - "[[Distributed Systems]]"
  - "[[RDDs]]"
  - "[[HDFS]]"
  - "[[Apache Spark]]"
  - "[[Checkpoint]]"
  - "[[Tasks Triggers and Schedules]]"
aliases:
  - "fault-tolerant"
  - "resilience"
  - "failure recovery"
last_verified: 2026-10-25
tags:
  - glossary
  - flashcards
---

# Fault Tolerance

> [!eli5] Summary
> Fault tolerance means a system keeps working, or recovers its work, when one of its machines or steps fails.

**In data work:** In a large cluster, individual machine failures are routine, so [[Distributed Systems|distributed systems]] are designed for them. Common techniques are [[Replication|replication]] (storing several copies), recomputation of lost work, retries, and [[Checkpoint|checkpointing]]. [[HDFS]] is typically configured with 3x replication, keeping each block on multiple nodes, with at least one copy on a different rack.

**In Databricks:** [[Apache Spark]] tracks the lineage of each dataset ([[RDDs]]), so lost data can be rebuilt automatically on another executor after a failure. Streaming queries recover from checkpoints. [[Delta Lake]] transactions prevent partially written data from becoming visible. In [[Lakeflow Jobs]], each task can retry a set number of times, and **Repair run** reruns only failed tasks and their dependents in multi-task jobs. Repairs do not make tasks idempotent, so use overwrite or `MERGE` instead of append where duplicates matter ([[Tasks Triggers and Schedules]]).

Seen in: [[Distributed Systems]], [[RDDs]], [[HDFS]], [[Apache Spark]], [[Lakeflow Jobs]]

## Recall

How does Spark recover lost data after an executor fails?::It recomputes the data from its recorded lineage.
What does a Lakeflow Jobs repair run rerun?::Only the unsuccessful tasks and their dependent tasks.

> [!sources]- Sources (last verified: 2026-10-25)
> - [Apache Spark key terms, explained (Databricks blog)](https://www.databricks.com/blog/2016/06/22/apache-spark-key-terms-explained.html)
> - [What is HDFS? (Databricks glossary)](https://www.databricks.com/glossary/hadoop-distributed-file-system-hdfs)
> - [Troubleshoot and repair job failures (AWS)](https://docs.databricks.com/aws/en/jobs/repair-job-failures)
