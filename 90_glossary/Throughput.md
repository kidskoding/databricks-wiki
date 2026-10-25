---
type: glossary
status: written
level: 90
section: Glossary
depth: 101
summary: "How much work a system finishes per unit of time, such as rows per second or queries per minute."
related:
  - "[[Latency]]"
  - "[[Batch vs Streaming]]"
  - "[[Scalability]]"
  - "[[SQL Warehouses]]"
  - "[[Structured Streaming on Databricks]]"
  - "[[Model Serving]]"
aliases:
  - "bandwidth"
  - "processing rate"
  - "rows per second"
  - "QPS"
last_verified: 2026-10-25
tags:
  - glossary
  - flashcards
---

# Throughput

> [!eli5] Summary
> Throughput is the amount of work a system completes per unit of time, such as rows per second or queries per minute.

**In data work:** Throughput measures volume over time: megabytes per second read from storage, events per second through a stream, or concurrent queries a system can handle. It is related to [[Latency|latency]] but different: batching work usually raises throughput while making each item wait longer. Bottlenecks can be CPU, memory, disk, network, or a single slow step. An e-commerce shop on Black Friday cares about throughput (for example, processing 50,000 orders an hour) more than about the latency of any one order.

**In Databricks:** Throughput shows up in [[Structured Streaming on Databricks|streaming]] as input and processing rates, in [[SQL Warehouses]] as how many queries run concurrently (warehouses add clusters, between a minimum and maximum you set, as queries queue up), and in [[Model Serving]] as requests per second an endpoint can sustain. [[Batch vs Streaming]] is largely a throughput-versus-latency trade.

Seen in: [[Batch vs Streaming]], [[SQL Warehouses]], [[Model Serving]]

## Recall

Throughput::Work completed per unit of time (rows/sec, queries/min); batching raises throughput but adds latency.

> [!sources]- Sources (last verified: 2026-10-25)
> - [SQL warehouse sizing, scaling, and queuing behavior (AWS)](https://docs.databricks.com/aws/en/compute/sql-warehouse/warehouse-behavior)
