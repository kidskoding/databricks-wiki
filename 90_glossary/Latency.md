---
type: glossary
status: written
level: 90
section: Glossary
depth: 101
summary: "The waiting time between asking for something and getting the answer."
related:
  - "[[Throughput]]"
  - "[[Batch vs Streaming]]"
  - "[[Serverless Compute]]"
  - "[[Photon]]"
  - "[[Model Serving]]"
  - "[[Query Performance and Caching]]"
aliases:
  - "response time"
  - "lag"
  - "delay"
last_verified: 2026-10-25
tags:
  - glossary
  - flashcards
---

# Latency

> [!eli5] Summary
> Latency is the time between a request and its result. Low latency means a short wait.

**In data work:** Latency measures delay for a single request or event: how many milliseconds a dashboard query takes, or how many minutes pass between a sale happening and it appearing in a report (often called data freshness). It is different from [[Throughput|throughput]], which counts how much work finishes per unit of time. A coffee chain might accept a nightly report with hours of latency for accounting, but want under a minute of latency for a stock-out alert. Lower latency usually costs more, because machines must stay ready and process smaller pieces of work more often.

**In Databricks:** On Databricks, latency shows up in several places. Query latency depends on [[SQL Warehouses]], [[Photon]], and caching (see [[Query Performance and Caching]]). Start-up latency is a big reason teams choose [[Serverless Compute]], which avoids waiting for your own cluster to boot. Pipeline latency is the [[Batch vs Streaming]] choice, from daily [[Lakeflow Jobs]] to [[Structured Streaming on Databricks|continuous streams]]. For AI apps, [[Model Serving]] endpoints are judged by response latency.

Seen in: [[Batch vs Streaming]], [[Serverless Compute]], [[Model Serving]], [[Query Performance and Caching]]

## Recall

Latency::The delay between a request (or an event) and its result; it is about speed for one item, while throughput is about volume per second.
