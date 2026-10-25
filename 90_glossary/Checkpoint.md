---
type: glossary
status: written
level: 90
section: Glossary
depth: 101
summary: "A saved record of a job's progress and state, used to resume after a failure without reprocessing or losing data."
related:
  - "[[Structured Streaming]]"
  - "[[Structured Streaming on Databricks]]"
  - "[[Auto Loader]]"
  - "[[Exactly-Once Processing]]"
  - "[[Delta Transaction Log]]"
  - "[[Fault Tolerance]]"
aliases:
  - "checkpointing"
  - "checkpointLocation"
  - "checkpoint location"
last_verified: 2026-10-25
tags:
  - glossary
  - flashcards
---

# Checkpoint

> [!eli5] Summary
> A checkpoint is a saved bookmark of how far a job has progressed. After a restart, the job continues from the bookmark instead of starting over.

**In data work:** Long-running jobs, especially streaming queries, periodically record which input they have processed and any intermediate state, such as running totals. After a failure or restart, the job reads the checkpoint and resumes from the last committed point. Checkpoints are one of the requirements for [[Exactly-Once Processing|exactly-once]] results.

**In Databricks:** Every [[Structured Streaming]] write needs a checkpoint location, set with `.option("checkpointLocation", "<path>")`. Each query must have its own location; deleting it or pointing to a new path makes the query start from the beginning. Changes to sources, stateful operations, or sink type generally require a new checkpoint. [[Auto Loader]] stores discovered-file metadata in a RocksDB store inside its checkpoint. [[Lakeflow Spark Declarative Pipelines]] manage checkpoints automatically. Separately, the [[Delta Transaction Log]] writes Parquet checkpoint files that capture the full table state so readers do not replay every commit.

Seen in: [[Structured Streaming]], [[Structured Streaming on Databricks]], [[Auto Loader]], [[Delta Transaction Log]]

## Recall

What happens if a streaming query's checkpoint is deleted?::The query loses its progress and starts from the beginning of its source.
Can two streaming queries share a checkpoint location?::No. Each query must have its own checkpoint location.

> [!sources]- Sources (last verified: 2026-10-25)
> - [Structured Streaming checkpoints (AWS)](https://docs.databricks.com/aws/en/structured-streaming/checkpoints)
> - [What is Auto Loader? (AWS)](https://docs.databricks.com/aws/en/ingestion/cloud-object-storage/auto-loader)
> - [Understanding the Delta Lake transaction log (Databricks blog)](https://www.databricks.com/blog/2019/08/21/diving-into-delta-lake-unpacking-the-transaction-log.html)
