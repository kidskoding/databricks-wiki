---
type: chapter
status: stub
part: 1
level: 8
section: Data Engineering
summary: Getting data in, cleaning it, and running it on schedule with Lakeflow.
prev: "[[Hive Metastore Migration to Unity Catalog]]"
next: "[[Lakeflow]]"
notes:
  - "[[Lakeflow]]"
  - "[[Lakeflow Connect]]"
  - "[[Auto Loader]]"
  - "[[COPY INTO]]"
  - "[[Lakeflow Spark Declarative Pipelines]]"
  - "[[Streaming Tables]]"
  - "[[Materialized Views]]"
  - "[[Expectations and Data Quality]]"
  - "[[Change Data Capture]]"
  - "[[Slowly Changing Dimensions]]"
  - "[[Lakeflow Jobs]]"
  - "[[Tasks Triggers and Schedules]]"
  - "[[Lakeflow Designer]]"
  - "[[Structured Streaming on Databricks]]"
  - "[[dbt on Databricks]]"
  - "[[CI-CD for Data Pipelines]]"
  - "[[Testing Data Pipelines]]"
last_verified:
tags:
  - chapter
---

# Chapter 08 - Data Engineering

> [!story] Previously
> (to write)

**Getting data in, cleaning it, and running it on schedule with Lakeflow.**

## The story of this chapter

(to write)

## Notes in reading order

<!-- GENERATED:reading-order START (scripts/scaffold.py) -->

| # | Note | Depth | What it covers |
|---|---|---|---|
| 1 | [[Lakeflow]] | 101 Beginner | Databricks' umbrella for ingestion (Connect), transformation (Pipelines), and orchestration (Jobs). |
| 2 | [[Lakeflow Connect]] | 101 Beginner | Managed connectors for Salesforce, SQL Server, Google Analytics, and other common sources. |
| 3 | [[Auto Loader]] | 201 Practitioner | Incrementally ingesting new files as they land in cloud storage. |
| 4 | [[COPY INTO]] | 201 Practitioner | The simple SQL command for loading files into a table once. |
| 5 | [[Lakeflow Spark Declarative Pipelines]] | 201 Practitioner | Declaring the tables you want and letting Databricks run, retry, and track the pipeline (formerly Delta Live Tables). |
| 6 | [[Streaming Tables]] | 201 Practitioner | Tables that keep themselves up to date from a stream or growing source. |
| 7 | [[Materialized Views]] | 201 Practitioner | Precomputed query results that refresh incrementally. |
| 8 | [[Expectations and Data Quality]] | 201 Practitioner | Rules on your data that warn, drop, or stop the pipeline when broken. |
| 9 | [[Change Data Capture]] | 301 Advanced | Copying only what changed in a source database, with AUTO CDC. |
| 10 | [[Slowly Changing Dimensions]] | 301 Advanced | SCD type 1 and type 2, which decide whether to keep history when a customer moves. |
| 11 | [[Lakeflow Jobs]] | 101 Beginner | Databricks' built-in orchestrator for scheduled multi-task workflows (formerly Workflows). |
| 12 | [[Tasks Triggers and Schedules]] | 201 Practitioner | Task types, dependencies, file-arrival and table-update triggers, and retries. |
| 13 | [[Lakeflow Designer]] | 101 Beginner | A no-code, drag-and-drop pipeline builder with AI help. |
| 14 | [[Structured Streaming on Databricks]] | 301 Advanced | Running Spark streams on Databricks, covering Kafka sources, checkpoints, and real-time mode. |
| 15 | [[dbt on Databricks]] | 201 Practitioner | Running dbt projects against Databricks SQL, and as job tasks. |
| 16 | [[CI-CD for Data Pipelines]] | 301 Advanced | Dev, staging, and prod, with tests and automated deployment for data code. |
| 17 | [[Testing Data Pipelines]] | 301 Advanced | Unit tests, data tests, and expectations for code that moves data. |

<!-- GENERATED:reading-order END -->

> [!nextup] Up next
> [[Lakeflow]]
