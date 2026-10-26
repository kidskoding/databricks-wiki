---
type: glossary
status: written
level: 90
section: Glossary
depth: 101
summary: "The cron expression format from the Quartz scheduler, with seconds as the first field, that Databricks uses for job schedules."
related:
  - "[[Tasks Triggers and Schedules]]"
  - "[[Lakeflow Jobs]]"
  - "[[Orchestration]]"
  - "[[SQL Alerts]]"
  - "[[Declarative Automation Bundles]]"
  - "[[Apache Airflow]]"
aliases:
  - "Quartz cron expression"
  - "quartz_cron_expression"
  - "cron expression"
  - "cron"
last_verified: 2026-10-26
tags:
  - glossary
  - flashcards
---

# Quartz Cron

> [!eli5] Summary
> A Quartz cron expression is a short line of text that describes a repeating schedule, such as "every day at 6:00 AM". Databricks uses it to decide when jobs run.

**In data work:** Unix cron uses five fields (minute, hour, day of month, month, day of week). Quartz cron, from the Java Quartz scheduler, adds a **seconds** field at the start and an optional year at the end. In Quartz, one of the two day fields must be `?` (no specific value), because you cannot set both day of month and day of week. Copying a five-field expression from Unix cron or [[Apache Airflow]] without adjusting it is a common mistake.

| Field | Position | Example |
|---|---|---|
| Seconds | 1 | `0` |
| Minutes | 2 | `30` |
| Hours | 3 | `6` |
| Day of month | 4 | `?` |
| Month | 5 | `*` |
| Day of week | 6 | `MON-FRI` |

**In Databricks:** [[Lakeflow Jobs]] schedules store a `quartz_cron_expression` and a `timezone_id` (a Java time zone ID such as `America/Chicago`). In the UI, select **Show Cron Syntax** on a schedule to edit the expression directly. The Databricks docs example `0 15 22 * * ?` runs daily at 22:15 in the job's time zone. Schedules have a minimum interval of 10 seconds between runs. Always set the time zone explicitly, so a bakery's 5:00 AM inventory load stays at 5:00 AM across daylight saving changes.

Seen in: [[Tasks Triggers and Schedules]], [[Lakeflow Jobs]]

## Recall

Quartz cron::A cron format with seconds as the first field and ? in one day field; used for Databricks job schedules.
What does 0 15 22 * * ? mean in Quartz cron?::Every day at 22:15:00.

> [!sources]- Sources (last verified: 2026-10-26)
> - [Run jobs on a schedule (AWS)](https://docs.databricks.com/aws/en/jobs/scheduled)
> - [Jobs API 2.0 (AWS)](https://docs.databricks.com/aws/en/reference/jobs-2.0-api)
> - [Job (Jobs API reference)](https://docs.databricks.com/api/jobs/v2/job)
