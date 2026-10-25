---
type: glossary
status: written
level: 90
section: Glossary
depth: 101
summary: "Running a pipeline over past time periods to fill in or recompute historical data."
related:
  - "[[Lakeflow Jobs]]"
  - "[[Lakeflow Spark Declarative Pipelines]]"
  - "[[Tasks Triggers and Schedules]]"
  - "[[Idempotency]]"
  - "[[MERGE and Upserts]]"
  - "[[Apache Airflow]]"
aliases:
  - "backfilling"
  - "backfill run"
  - "historical load"
  - "reprocessing"
last_verified: 2026-10-25
tags:
  - glossary
  - flashcards
---

# Backfill

> [!eli5] Summary
> A backfill runs a regular data job again for past dates. It is used to load history or to correct results after a fix.

**In data work:** Scheduled pipelines usually process one time slice per run, such as the previous day. A backfill reruns the same logic for earlier slices: when a pipeline is first created, after a bug corrupts past results, or when a new column needs history. Backfills are safe only if each run is [[Idempotency|idempotent]], so rerunning a date replaces that date's output instead of duplicating it. Example: after adding a `discount_amount` column, a retailer backfills two years of daily sales.

**In Databricks:** [[Lakeflow Jobs]] supports backfill runs. Next to **Run now**, choose **Run backfill**, select a date range and an interval, and Databricks creates one run per interval with the dates passed as job parameters. The job must use those parameters to select its data. For [[Lakeflow Spark Declarative Pipelines]], Databricks recommends backfilling with an append once flow. Use `INSERT INTO ... REPLACE WHERE` to replace one date range atomically, and [[Time Travel]] to restore a table after a faulty backfill. In the pre-Databricks stack, [[Apache Airflow]] handled backfills.

Seen in: [[Lakeflow Jobs]], [[Lakeflow Spark Declarative Pipelines]], [[Apache Airflow]], [[MERGE and Upserts]]

## Recall

What is a backfill?::Rerunning a pipeline over past time periods to fill in or recompute historical data.
What must a Lakeflow job do to support backfill runs?::Read the date parameters each backfill run passes and process only that slice.

> [!sources]- Sources (last verified: 2026-10-25)
> - [Backfill jobs (AWS)](https://docs.databricks.com/aws/en/jobs/backfill-jobs)
> - [Set up a recurring query with backfill support (AWS)](https://docs.databricks.com/aws/en/jobs/how-to/create-recurring-job)
> - [Selectively overwrite data with Delta Lake (AWS)](https://docs.databricks.com/aws/en/delta/selective-overwrite)
