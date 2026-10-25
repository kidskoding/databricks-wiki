---
type: glossary
status: written
level: 90
section: Glossary
depth: 101
summary: "Running the steps of a data process in the right order, on schedule, with retries and alerts."
related:
  - "[[Lakeflow Jobs]]"
  - "[[Apache Airflow]]"
  - "[[DAG]]"
  - "[[Tasks Triggers and Schedules]]"
  - "[[Data Pipeline]]"
  - "[[Jobs Stages and Tasks]]"
aliases:
  - "workflow orchestration"
  - "scheduler"
  - "job orchestration"
last_verified: 2026-10-25
tags:
  - glossary
  - flashcards
---

# Orchestration

> [!eli5] Summary
> Orchestration is running the steps of a data process in the correct order and on schedule, with retries and alerts when a step fails.

**In data work:** An orchestrator runs the tasks of a [[Data Pipeline|data pipeline]] in dependency order, usually drawn as a [[DAG]]: first load raw sales, then clean them, then rebuild the dashboard tables. It handles schedules and triggers, retries failed steps, passes parameters, and alerts someone when things break. [[Apache Airflow]] is the best-known open-source orchestrator; cron is the simplest one. A small bakery chain's nightly orchestration might pull point-of-sale exports at 1 a.m., refresh inventory at 2 a.m., and email a report at 6 a.m., but only if the earlier steps succeeded.

**In Databricks:** Databricks' built-in orchestrator is [[Lakeflow Jobs]] (formerly Workflows). A job is a DAG of tasks (notebooks, SQL, pipelines, dbt, Python) with [[Tasks Triggers and Schedules|schedules, file-arrival triggers, and retries]]. Many teams that used Airflow move simple schedules into Lakeflow Jobs; others keep Airflow and call Databricks from it. Do not confuse this with Spark's own [[Jobs Stages and Tasks]], which describe how one query runs.

Seen in: [[Lakeflow Jobs]], [[Apache Airflow]], [[Tasks Triggers and Schedules]]

## Recall

Orchestration::Coordinating pipeline tasks in dependency order with schedules, retries, and alerts; in Databricks this is Lakeflow Jobs.

> [!sources]- Sources (last verified: 2026-10-25)
> - [What is Orchestration? (Databricks glossary)](https://www.databricks.com/glossary/orchestration)
> - [Announcing the General Availability of Databricks Lakeflow](https://www.databricks.com/blog/announcing-general-availability-databricks-lakeflow)
