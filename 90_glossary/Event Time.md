---
type: glossary
status: written
level: 90
section: Glossary
depth: 101
summary: "The time at which an event actually happened, as recorded in the data, as opposed to the time the system received or processed it."
related:
  - "[[Watermark]]"
  - "[[Structured Streaming]]"
  - "[[Structured Streaming on Databricks]]"
  - "[[Batch vs Streaming]]"
  - "[[Event]]"
  - "[[Aggregation]]"
aliases:
  - "Event-time"
  - "Processing time"
  - "Ingestion time"
last_verified: 2026-10-26
tags:
  - glossary
  - flashcards
---

# Event Time

> [!eli5] Summary
> Event time is when something really happened, such as when a customer tapped Buy. It can differ from when the data reached your system, because phones go offline and networks are slow.

**In data work:** Streaming systems distinguish **event time** (a timestamp in the record), **ingestion time** (when it arrived), and **processing time** (when the engine handled it). Aggregating by event time gives correct answers even when data arrives late or out of order, but the engine must decide how long to wait for stragglers. That limit is the [[Watermark|watermark]].

**In Databricks:** In [[Structured Streaming]] you group by an event-time column with `window()` and bound late data with `withWatermark()`:

```python
from pyspark.sql.functions import window
(orders
  .withWatermark("order_ts", "10 minutes")
  .groupBy(window("order_ts", "5 minutes"))
  .count())
```

Spark keeps state for a window until the watermark (the maximum event time seen minus the delay) passes the window's end, then drops older records. The guarantee is one-directional: data later than the threshold may or may not be counted. The same APIs apply on Databricks ([[Structured Streaming on Databricks]]) and in [[Lakeflow Spark Declarative Pipelines]].

Small-business example: a point-of-sale tablet that loses Wi-Fi uploads sales an hour late. Windowing by event time keeps those sales in the correct hour of the daily report.

Seen in: [[Structured Streaming]], [[Watermark]], [[Structured Streaming on Databricks]]

## Recall

What is the difference between event time and processing time?::Event time is when the event happened; processing time is when the system handled it.
Which Spark method bounds how late event-time data can arrive?::withWatermark()

> [!sources]- Sources (last verified: 2026-10-26)
> - [Structured Streaming Programming Guide, Spark 4.2 (spark.apache.org)](https://spark.apache.org/docs/latest/streaming/apis-on-dataframes-and-datasets.html)
> - [pyspark.sql.DataFrame.withWatermark (spark.apache.org)](https://spark.apache.org/docs/latest/api/python/reference/pyspark.sql/api/pyspark.sql.DataFrame.withWatermark.html)
