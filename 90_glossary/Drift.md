---
type: glossary
status: written
level: 90
section: Glossary
depth: 101
summary: "A change over time in data or in the relationship a model learned, which degrades results without any code change."
related:
  - "[[Data Quality Monitoring]]"
  - "[[Machine Learning Basics]]"
  - "[[Model Serving]]"
  - "[[Models in Unity Catalog]]"
  - "[[Schema Enforcement and Evolution]]"
  - "[[Inference]]"
aliases:
  - "data drift"
  - "model drift"
  - "concept drift"
  - "schema drift"
last_verified: 2026-10-25
tags:
  - glossary
  - flashcards
---

# Drift

> [!eli5] Summary
> Drift means the data a system receives slowly stops looking like the data it was built for, so its results become less accurate.

**In data work:** Data drift is a change in input distributions, such as a rise in average order value or a new country appearing. Concept drift is a change in the relationship between inputs and outcomes, such as a churn model whose signals stop predicting churn. Schema drift is a change in the columns themselves, such as a renamed source field. Drift is detected by comparing recent data with a previous period or a baseline.

**In Databricks:** [[Data Quality Monitoring]] includes data profiling (formerly Lakehouse Monitoring). A profile (snapshot, time series, or inference) writes a profile metrics table and a drift metrics table to Unity Catalog. Drift is computed against the previous window and, optionally, a baseline table, using tests such as Kolmogorov-Smirnov, chi-squared, and population stability index. Inference profiles track model inputs and predictions from a [[Model Serving]] request log. When drift is confirmed, retrain and register a new version in [[Models in Unity Catalog]].

Seen in: [[Data Quality Monitoring]], [[Machine Learning Basics]], [[Model Serving]], [[Schema Enforcement and Evolution]]

## Recall

What is the difference between data drift and concept drift?::Data drift changes the inputs; concept drift changes the relationship between inputs and the outcome.
Which two tables does a Databricks data profile produce?::A profile metrics table and a drift metrics table.

> [!sources]- Sources (last verified: 2026-10-25)
> - [Data profiling (AWS)](https://docs.databricks.com/aws/en/data-governance/unity-catalog/data-quality-monitoring/data-profiling)
> - [Data profiling metric tables (AWS)](https://docs.databricks.com/aws/en/data-governance/unity-catalog/data-quality-monitoring/data-profiling/monitor-output)
