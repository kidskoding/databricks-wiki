---
type: glossary
status: written
level: 90
section: Glossary
depth: 101
summary: "The degree to which data is accurate, complete, timely, and consistent enough for its intended use."
related:
  - "[[Expectations and Data Quality]]"
  - "[[Data Quality Monitoring]]"
  - "[[Testing Data Pipelines]]"
  - "[[Schema Enforcement and Evolution]]"
  - "[[Medallion Architecture]]"
  - "[[Data Lineage]]"
aliases:
  - "DQ"
  - "data validation"
  - "data checks"
last_verified: 2026-10-25
tags:
  - glossary
  - flashcards
---

# Data Quality

> [!eli5] Summary
> Data quality describes whether data can be trusted. Missing, duplicated, late, or wrong data leads to wrong decisions.

**In data work:** Data quality is assessed along dimensions: accuracy, completeness, freshness, uniqueness, validity (values in allowed ranges or formats), and consistency across tables. Quality checks run inside pipelines and alert on, quarantine, or block bad data. Example: every order must have a customer ID, prices must be positive, and the previous day's data must arrive by 06:00.

**In Databricks:** [[Schema Enforcement and Evolution|Schema enforcement]] in [[Delta Lake]] rejects writes with mismatched columns or types. [[Expectations and Data Quality|Expectations]] in [[Lakeflow Spark Declarative Pipelines]] apply row-level rules such as `CONSTRAINT valid_price EXPECT (price > 0)` with one of three actions: warn (default; keep and record the row), `ON VIOLATION DROP ROW`, or `ON VIOLATION FAIL UPDATE`. [[Data Quality Monitoring]] adds table-level data profiling (formerly Lakehouse Monitoring) and anomaly detection. See [[Testing Data Pipelines]].

Seen in: [[Expectations and Data Quality]], [[Data Quality Monitoring]], [[Testing Data Pipelines]], [[Medallion Architecture]]

## Recall

Name four dimensions of data quality.::Accuracy, completeness, freshness, and uniqueness (also validity and consistency).
What are the three expectation violation actions in Lakeflow pipelines?::Warn (default), drop the row, or fail the update.

> [!sources]- Sources (last verified: 2026-10-25)
> - [Manage data quality with pipeline expectations (AWS)](https://docs.databricks.com/aws/en/ldp/expectations)
> - [Data quality monitoring (AWS)](https://docs.databricks.com/aws/en/data-governance/unity-catalog/data-quality-monitoring/)
