---
type: glossary
status: written
level: 90
section: Glossary
depth: 101
summary: "A timestamped record that something happened, such as a click, payment, or sensor reading."
related:
  - "[[Apache Kafka]]"
  - "[[Batch vs Streaming]]"
  - "[[Structured Streaming]]"
  - "[[Structured Streaming on Databricks]]"
  - "[[Change Data Capture]]"
  - "[[IoT]]"
aliases:
  - "events"
  - "event data"
  - "message"
  - "record"
last_verified: 2026-10-25
tags:
  - glossary
  - flashcards
---

# Event

> [!eli5] Summary
> An event is a record of one thing that happened at a specific time, such as a purchase or a sensor reading. A sequence of events describes what happened over time.

**In data work:** An event has a timestamp, a type, and attributes, for example `{"time": "2026-10-25T15:02:11Z", "type": "purchase", "store": 7, "amount": 4.50}`. Events are usually immutable: new events are appended, existing ones are not edited. They arrive continuously from websites, applications, payment terminals, [[IoT]] devices, and database change logs. Event time (when it happened) differs from processing time (when it was received), so streaming systems use [[Watermark|watermarks]] to bound how long to wait for late events.

**In Databricks:** Events typically reach Databricks through a message broker. [[Structured Streaming]] reads Apache Kafka, Amazon Kinesis, Google Pub/Sub (format `pubsub`), and Apache Pulsar; Azure Event Hubs is read through its Kafka-compatible endpoint. [[Streaming Tables]] in [[Lakeflow Spark Declarative Pipelines]] store events in Delta tables. [[Change Data Capture]] turns database changes into events. See [[Structured Streaming on Databricks]].

Seen in: [[Apache Kafka]], [[Batch vs Streaming]], [[Structured Streaming]], [[Change Data Capture]]

## Recall

What is the difference between event time and processing time?::Event time is when the event occurred; processing time is when the system handled it.
How does Databricks read Azure Event Hubs in Structured Streaming?::Through the Event Hubs Kafka-compatible endpoint with the Kafka connector.

> [!sources]- Sources (last verified: 2026-10-25)
> - [Streaming connectors (Azure)](https://learn.microsoft.com/en-us/azure/databricks/ingestion/lakeflow-connect/streaming-overview)
> - [Use Azure Event Hubs as a pipeline data source (AWS)](https://docs.databricks.com/aws/en/ldp/event-hubs)
