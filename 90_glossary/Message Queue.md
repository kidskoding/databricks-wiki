---
type: glossary
status: written
level: 90
section: Glossary
depth: 101
summary: "A holding line for messages, so one system can send data and another can pick it up later."
related:
  - "[[Apache Kafka]]"
  - "[[Structured Streaming]]"
  - "[[Structured Streaming on Databricks]]"
  - "[[Batch vs Streaming]]"
  - "[[Event]]"
aliases:
  - "message broker"
  - "event stream"
  - "pub/sub"
  - "queue"
last_verified: 2026-10-25
tags:
  - glossary
  - flashcards
---

# Message Queue

> [!eli5] Summary
> A message queue holds messages between systems: one system writes messages and another reads them when it is ready. Neither system has to wait for the other.

**In data work:** A message queue (or broker) stores messages from producers until consumers read them. It decouples systems: the checkout page does not need to wait for the warehouse system to be online. Classic queues (RabbitMQ, Amazon SQS) usually delete a message once it is handled. Log-style systems such as [[Apache Kafka]], Azure Event Hubs, Amazon Kinesis, and Google Pub/Sub keep an ordered stream of [[Event|events]] that many readers can replay. An online florist might publish every order event to a stream, which the delivery app, the inventory system, and the analytics pipeline each read on their own.

**In Databricks:** Databricks reads from these systems with [[Structured Streaming on Databricks|Structured Streaming]], which has connectors for Kafka, Kinesis, Event Hubs (through its Kafka-compatible endpoint), and Pub/Sub. The usual pattern is to land the raw stream in a bronze [[Streaming Tables|streaming table]], then clean it in [[Lakeflow Spark Declarative Pipelines]]. See [[Batch vs Streaming]] for when a queue is worth it.

Seen in: [[Apache Kafka]], [[Structured Streaming on Databricks]], [[Batch vs Streaming]]

## Recall

Message Queue::A buffer that holds messages from senders until receivers read them, so systems do not have to wait for each other; Kafka is the best-known example.
