---
type: glossary
status: written
level: 90
section: Glossary
depth: 101
summary: "In streaming, a moving cutoff that says how late an event may arrive and still be counted."
related:
  - "[[Structured Streaming]]"
  - "[[Structured Streaming on Databricks]]"
  - "[[Event]]"
  - "[[Batch vs Streaming]]"
  - "[[Streaming Tables]]"
  - "[[Exactly-Once Processing]]"
aliases:
  - "watermarking"
  - "event-time watermark"
  - "withWatermark"
  - "late data threshold"
last_verified: 2026-10-25
tags:
  - glossary
  - flashcards
---

# Watermark

> [!eli5] Summary
> A watermark is a time limit in stream processing that defines how late data may arrive and still be included in results. It lets the system finalize results and discard old state.

**In data work:** Streams receive [[Event|events]] out of order: a phone loses signal and sends its readings late. When you count events per five-minute window, the system must decide how long to wait for stragglers. A watermark is the latest event time seen minus an allowed delay; windows older than the watermark are finalized and their stored state is freed. Events that arrive within the threshold are always processed; later ones might be, but that is not guaranteed. Without a watermark, state grows forever. A food truck's IoT fridge sensors might use a ten-minute watermark when averaging temperature per five minutes.

**In Databricks:** In Spark [[Structured Streaming]] you set it with `df.withWatermark("event_time", "10 minutes")` before a windowed aggregation, stream-stream join, or deduplication; in SQL the equivalent is the `WATERMARK` clause. The same applies in [[Structured Streaming on Databricks]] and in streaming tables in [[Lakeflow Spark Declarative Pipelines]]. Choose the delay from how late your data actually arrives: a short watermark keeps less state and lowers latency but tolerates little late data; a long one tolerates more but holds more state and delays results.

Seen in: [[Structured Streaming]], [[Structured Streaming on Databricks]], [[Streaming Tables]]

## Recall

Watermark::A streaming cutoff (max event time minus allowed lateness) after which windows are finalized and late events are dropped, keeping state bounded.

> [!sources]- Sources (last verified: 2026-10-25)
> - [Apply watermarks to control data processing thresholds (AWS)](https://docs.databricks.com/aws/en/structured-streaming/watermarks)
> - [Apply watermarks (Azure Databricks)](https://learn.microsoft.com/en-us/azure/databricks/structured-streaming/watermarks)
> - [WATERMARK clause (AWS)](https://docs.databricks.com/aws/en/sql/language-manual/sql-ref-syntax-qry-select-watermark)
