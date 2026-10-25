---
type: glossary
status: written
level: 90
section: Glossary
depth: 101
summary: "A guarantee that each input affects the final result exactly once, with no loss and no duplication, even after failures."
related:
  - "[[Structured Streaming]]"
  - "[[Checkpoint]]"
  - "[[Idempotency]]"
  - "[[Delta Lake]]"
  - "[[ACID Transactions]]"
  - "[[Apache Kafka]]"
aliases:
  - "exactly-once"
  - "exactly-once semantics"
  - "at-least-once"
  - "at-most-once"
last_verified: 2026-10-25
tags:
  - glossary
  - flashcards
---

# Exactly-Once Processing

> [!eli5] Summary
> Exactly-once processing ensures every record is counted one time. After a crash and restart, nothing is skipped and nothing is counted twice.

**In data work:** Streaming systems offer three levels. At-most-once can lose data after a failure. At-least-once does not lose data but can process some records twice. Exactly-once makes the result equivalent to processing each record once. It requires a replayable source (such as [[Apache Kafka]] offsets), recorded progress ([[Checkpoint|checkpoints]]), and a sink where repeated writes have no extra effect ([[Idempotency|idempotent]] or transactional writes).

**In Databricks:** [[Structured Streaming]] writing to a [[Delta Lake]] table uses the transaction log to commit each micro-batch once. [[Auto Loader]] processes each file exactly once when `cloudFiles.allowOverwrites` is `false` (the default). `foreachBatch` provides at-least-once writes by default; for exactly-once, make the batch logic idempotent, for example by passing the Delta writer options `txnAppId` and `txnVersion` (bound to `batchId`) or by using an idempotent `MERGE`. For Lakeflow pipelines, Databricks advises treating non-Delta sinks as at-least-once.

Seen in: [[Structured Streaming]], [[Checkpoint]], [[Idempotency]], [[Structured Streaming on Databricks]]

## Recall

What three components does end-to-end exactly-once require?::A replayable source, checkpointed progress, and an idempotent or transactional sink.
What guarantee does foreachBatch provide by default?::At-least-once.

> [!sources]- Sources (last verified: 2026-10-25)
> - [Use foreachBatch to write to arbitrary data sinks (AWS)](https://docs.databricks.com/aws/en/structured-streaming/foreach)
> - [Delta Lake table streaming reads and writes (AWS)](https://docs.databricks.com/aws/en/structured-streaming/delta-lake)
> - [Auto Loader FAQ (AWS)](https://docs.databricks.com/aws/en/ingestion/cloud-object-storage/auto-loader/faq)
> - [Processing guarantees in Lakeflow pipelines (GCP)](https://docs.databricks.com/gcp/en/ldp/best-practices/processing-guarantees)
