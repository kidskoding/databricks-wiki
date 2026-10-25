---
type: chapter
status: written
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
last_verified: 2026-10-25
tags:
  - chapter
---

# Chapter 08 - Data Engineering

> [!story] Context
> [[Chapter 07 - Unity Catalog and Governance|Chapter 07]] established one governance layer for every table, file, and model, ending with [[Hive Metastore Migration to Unity Catalog|the migration of legacy tables]] into it. Governance defines where data lives and who can use it. It does not move data into the platform, clean it, or keep it current. This chapter covers those jobs.

**Getting data in, cleaning it, and running it on schedule with Lakeflow.**

## The story of this chapter

This chapter covers data engineering on Databricks: getting data from source systems into [[Unity Catalog]] tables, transforming it through the [[Medallion Architecture|medallion]] layers, checking its quality, and running the whole process on a schedule. On Databricks these jobs belong to one product family, [[Lakeflow]].

**The problem.** In the [[Chapter 04 - The Modern Data Stack|modern data stack]], each of these jobs used a separate tool. An [[Fivetran and ELT Tools|ingestion service]] copied data from applications, [[dbt]] or Spark code transformed it, and an orchestrator such as [[Apache Airflow]] scheduled it. Each tool had its own credentials, permissions, monitoring, and billing, and lineage stopped at each tool boundary. Teams also wrote the same infrastructure code repeatedly: incremental file tracking, retry logic, change data capture, and data quality checks.

**Ingestion.** Data reaches the platform in three ways:

- [[Lakeflow Connect]] provides managed connectors for applications and databases such as Salesforce, Workday, Google Analytics, SQL Server, ServiceNow, SharePoint, and Shopify. Release status varies by connector; several are GA and others are in Preview or Beta as of October 2026.
- [[Auto Loader]] incrementally loads files as they arrive in cloud storage or a [[Volumes|volume]], with schema inference and evolution.
- [[COPY INTO]] loads files with a single, idempotent SQL command.

**Transformation.** [[Lakeflow Spark Declarative Pipelines]] (formerly Delta Live Tables) lets you declare tables in SQL or Python. The engine derives the dependency graph, processes data incrementally, retries failures, and records lineage and metrics. Pipelines contain two main dataset types: [[Streaming Tables|streaming tables]], which process each new input row once, and [[Materialized Views|materialized views]], which store a query result and refresh it when sources change. [[Expectations and Data Quality|Expectations]] attach row-level quality rules that warn, drop, or fail. For sources that update and delete rows, [[Change Data Capture|AUTO CDC]] applies change records in order, and [[Slowly Changing Dimensions]] determines whether history is overwritten (type 1) or kept (type 2).

**Orchestration.** [[Lakeflow Jobs]] (formerly Workflows) runs tasks in dependency order: pipelines, connectors, notebooks, SQL, dbt, and more. [[Tasks Triggers and Schedules]] covers the task types, conditional logic, loops, retries, and the four trigger types: scheduled, file arrival, table update, and continuous.

**Other ways to build.** [[Lakeflow Designer]] is a no-code canvas that produces Lakeflow pipelines, for analysts who do not write code. [[Structured Streaming on Databricks]] covers direct streaming code, Kafka sources, checkpoints, and real-time mode for sub-second latency. [[dbt on Databricks]] covers running existing dbt projects against SQL warehouses and as job tasks.

**Engineering practice.** [[CI-CD for Data Pipelines]] uses [[Declarative Automation Bundles]] (formerly Databricks Asset Bundles) to keep pipelines and jobs in Git and deploy them to separate development and production targets. [[Testing Data Pipelines]] covers unit tests for transformation logic, data tests on tables, and run-time checks.

**Running example.** Several notes use the same small-business scenario: an online shop with orders in Shopify and invoices in QuickBooks. Shopify data arrives through its Lakeflow Connect connector (Beta as of October 2026). QuickBooks has no managed connector in the documentation, so nightly CSV exports land in a volume and Auto Loader loads them. A pipeline builds bronze, silver, and gold tables, and a nightly job runs ingestion, transformation, and a reconciliation check. The full build is in [[Lakeflow]].

**Outcome.** At the end of this chapter, data arrives on a schedule, is cleaned and checked, and is stored as governed gold tables. The next requirement is making that data usable by analysts and business users through SQL, dashboards, natural-language questions, and applications. [[Chapter 09 - SQL BI and Apps]] covers that layer.

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

> [!nextup] Next
> [[Lakeflow]]
