---
type: glossary
status: written
level: 90
section: Glossary
depth: 101
summary: "Copying data from source systems, such as applications, databases, files, and streams, into the data platform."
related:
  - "[[Lakeflow Connect]]"
  - "[[Auto Loader]]"
  - "[[COPY INTO]]"
  - "[[Fivetran and ELT Tools]]"
  - "[[Change Data Capture]]"
  - "[[Medallion Architecture]]"
aliases:
  - "data ingestion"
  - "ingest"
  - "loading"
last_verified: 2026-10-25
tags:
  - glossary
  - flashcards
---

# Ingestion

> [!eli5] Summary
> Ingestion brings data from the systems where it is created into one central place where it can be analyzed.

**In data work:** Ingestion is the first stage of a [[Data Pipeline|pipeline]]. Sources include SaaS applications, operational databases, file exports, and event streams. Loads can be full (copy everything each time), incremental (only new or changed records, often through [[Change Data Capture]]), or continuous (streaming). Incremental loading reduces cost and load on the source.

**In Databricks:** [[Lakeflow Connect]] provides managed connectors for sources such as Salesforce, SQL Server, ServiceNow, and Google Analytics; they run on serverless compute and are governed by Unity Catalog. The SQL Server connector reads incrementally with change tracking or change data capture. [[Auto Loader]] ingests new files incrementally from S3, ADLS, and GCS, and [[COPY INTO]] loads files with SQL. [[Structured Streaming on Databricks|Structured Streaming]] reads event streams. Partner tools such as Fivetran also work ([[Fivetran and ELT Tools]]). Ingested data usually lands in bronze tables ([[Medallion Architecture]]).

Seen in: [[Lakeflow Connect]], [[Auto Loader]], [[COPY INTO]], [[Fivetran and ELT Tools]], [[Lakeflow]]

## Recall

What is the difference between full and incremental ingestion?::Full copies all data each time; incremental copies only new or changed records.
Which Databricks feature ingests new files incrementally from cloud storage?::Auto Loader.

> [!sources]- Sources (last verified: 2026-10-25)
> - [Lakeflow Connect connector concepts (AWS)](https://docs.databricks.com/aws/en/ingestion/lakeflow-connect/)
> - [Managed connector FAQs (AWS)](https://docs.databricks.com/aws/en/ingestion/lakeflow-connect/faq)
> - [Get started using COPY INTO (AWS)](https://docs.databricks.com/aws/en/ingestion/cloud-object-storage/copy-into/)
