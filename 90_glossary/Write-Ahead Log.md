---
type: glossary
status: written
level: 90
section: Glossary
depth: 101
summary: "A log in which a system records each change before applying it, so it can recover to a consistent state after a crash."
related:
  - "[[Delta Transaction Log]]"
  - "[[Checkpoint]]"
  - "[[Structured Streaming]]"
  - "[[ACID Transactions]]"
  - "[[Fault Tolerance]]"
  - "[[Exactly-Once Processing]]"
aliases:
  - "WAL"
  - "redo log"
  - "write-ahead logging"
last_verified: 2026-10-26
tags:
  - glossary
  - flashcards
---

# Write-Ahead Log

> [!eli5] Summary
> A write-ahead log is a diary a system writes before it acts. If it crashes halfway through, it reads the diary to finish or undo what it was doing.

**In data work:** Changing data in place is risky: a crash mid-write can leave a page half-updated. With write-ahead logging, a database first appends a description of each change to a sequential log and flushes it to durable storage. Only then does it update the data files. On restart, it replays the log to redo committed changes and discard incomplete ones. Sequential log writes are fast, so the database can delay the slower random writes to data files. Relational databases such as PostgreSQL use a WAL, and replication often works by streaming it to replicas.

**In Databricks:** The idea appears in three places.
- **[[Structured Streaming]]:** The engine records the offset range of each micro-batch in the [[Checkpoint|checkpoint]] before processing it, using checkpointing and write-ahead logs, and records a commit when the batch reaches the sink. After a failure, it replays the logged range, which supports [[Exactly-Once Processing|exactly-once]] results with idempotent sinks.
- **[[Delta Transaction Log]]:** Delta Lake is related but different. It writes new data files first, then atomically adds a commit entry that makes them visible. The log is the source of truth for table state, not a redo log.
- **[[Lakebase]]:** Lakebase runs Postgres, which relies on its WAL.

The older DStreams API had a separate receiver write-ahead log; it does not apply to Structured Streaming.

Seen in: [[Checkpoint]], [[Structured Streaming]], [[Delta Transaction Log]]

## Recall

Write-ahead log::A durable log of changes written before they are applied, used to recover after a crash.
What does Structured Streaming log before processing a micro-batch?::The offset range of the data in that batch.

> [!sources]- Sources (last verified: 2026-10-26)
> - [Structured Streaming Programming Guide (Spark 3.5.6)](https://spark.apache.org/docs/3.5.6/structured-streaming-programming-guide.html)
> - [Structured Streaming checkpoints (AWS)](https://docs.databricks.com/aws/en/structured-streaming/checkpoints)
> - [Spark Streaming programming guide (Spark 4.2)](https://spark.apache.org/docs/latest/streaming-programming-guide.html)
> - [Delta Lake: High-Performance ACID Table Storage over Cloud Object Stores (PVLDB 2020)](https://www.vldb.org/pvldb/vol13/p3411-armbrust.pdf)
