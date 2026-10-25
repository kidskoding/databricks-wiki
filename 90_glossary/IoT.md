---
type: glossary
status: written
level: 90
section: Glossary
depth: 101
summary: "The Internet of Things: physical devices such as sensors, meters, and machines that send data over a network."
related:
  - "[[Event]]"
  - "[[Batch vs Streaming]]"
  - "[[Structured Streaming on Databricks]]"
  - "[[Apache Kafka]]"
  - "[[Streaming Tables]]"
  - "[[Who Uses Databricks - Business Types]]"
aliases:
  - "Internet of Things"
  - "IIoT"
  - "telemetry"
  - "connected devices"
last_verified: 2026-10-25
tags:
  - glossary
  - flashcards
---

# IoT

> [!eli5] Summary
> IoT refers to everyday devices that report data automatically, such as temperature sensors, delivery-vehicle trackers, and factory machines.

**In data work:** IoT devices emit a continuous flow of small [[Event|events]] (telemetry), each with a timestamp, device ID, and readings. The data is high-volume, often arrives late or out of order, and needs cleaning for missing or faulty readings. Typical uses are monitoring, alerting, and predictive maintenance. Example: temperature sensors on six fermentation tanks report every few seconds, and an alert fires when a tank exceeds its range.

**In Databricks:** IoT data usually reaches Databricks through a message broker read by [[Structured Streaming on Databricks|Structured Streaming]] or by [[Streaming Tables]] in a Lakeflow pipeline: [[Apache Kafka]], Amazon Kinesis, Google Pub/Sub, or Azure Event Hubs through its Kafka-compatible endpoint. Windowed aggregations with [[Watermark|watermarks]] handle late readings, [[Delta Lake]] stores history, and [[SQL Alerts]] or job notifications report threshold breaches. See [[Who Uses Databricks - Business Types]].

Seen in: [[Event]], [[Batch vs Streaming]], [[Structured Streaming on Databricks]], [[Who Uses Databricks - Business Types]]

## Recall

What does IoT stand for?::The Internet of Things.
Why do IoT streaming pipelines use watermarks?::Device readings often arrive late or out of order, and watermarks bound how long to wait for them.

> [!sources]- Sources (last verified: 2026-10-25)
> - [Streaming connectors (Azure)](https://learn.microsoft.com/en-us/azure/databricks/ingestion/lakeflow-connect/streaming-overview)
> - [Real-time mode reference (AWS)](https://docs.databricks.com/aws/en/structured-streaming/real-time/reference)
