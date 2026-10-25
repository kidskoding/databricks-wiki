---
type: glossary
status: written
level: 90
section: Glossary
depth: 101
summary: "An automated sequence of steps that moves data from its sources to where it is used, transforming it along the way."
related:
  - "[[ETL vs ELT]]"
  - "[[Lakeflow]]"
  - "[[Lakeflow Spark Declarative Pipelines]]"
  - "[[Lakeflow Jobs]]"
  - "[[Medallion Architecture]]"
  - "[[Testing Data Pipelines]]"
aliases:
  - "pipeline"
  - "pipelines"
  - "ETL pipeline"
  - "data flow"
last_verified: 2026-10-25
tags:
  - glossary
  - flashcards
---

# Data Pipeline

> [!eli5] Summary
> A data pipeline is an automated process that collects data, cleans and combines it, and delivers it to reports or applications on a schedule or continuously.

**In data work:** A pipeline has three stages: [[Ingestion|ingest]] (copy data from sources such as databases and SaaS applications), transform (clean, join, aggregate), and serve (write tables for reports, models, or apps). It runs on a schedule or continuously ([[Batch vs Streaming]]) and requires [[Orchestration|orchestration]], monitoring, and tests. Example: hourly ingestion of online orders, removal of test orders, a join to the product list, and a refresh of a daily sales table.

**In Databricks:** [[Lakeflow]] groups the Databricks pipeline tools: [[Lakeflow Connect]] for managed ingestion, [[Lakeflow Spark Declarative Pipelines]] (formerly Delta Live Tables) for declarative transformations, and [[Lakeflow Jobs]] (formerly Workflows) for orchestration. [[Auto Loader]] ingests new files incrementally, and [[Expectations and Data Quality|expectations]] enforce data rules. See [[CI-CD for Data Pipelines]].

Seen in: [[ETL vs ELT]], [[Lakeflow]], [[Lakeflow Spark Declarative Pipelines]], [[Medallion Architecture]], [[Path - Data Engineer]]

## Recall

What are the three stages of a data pipeline?::Ingest, transform, and serve.
What was Lakeflow Spark Declarative Pipelines formerly called?::Delta Live Tables (DLT).

> [!sources]- Sources (last verified: 2026-10-25)
> - [What is Lakeflow Connect? (AWS)](https://docs.databricks.com/aws/en/ingestion/overview)
> - [Lakeflow Jobs (AWS)](https://docs.databricks.com/aws/en/jobs/)
> - [What are pipelines? (AWS)](https://docs.databricks.com/aws/en/ldp/concepts/pipelines)
