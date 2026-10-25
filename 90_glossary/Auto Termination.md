---
type: glossary
status: written
level: 90
section: Glossary
depth: 101
summary: "A setting that shuts down idle compute after a set number of minutes so it stops incurring charges."
related:
  - "[[All-Purpose Compute]]"
  - "[[SQL Warehouses]]"
  - "[[Compute Policies]]"
  - "[[Cost Optimization Checklist]]"
  - "[[Serverless Compute]]"
  - "[[DBUs]]"
aliases:
  - "auto-termination"
  - "autotermination"
  - "auto stop"
  - "autotermination_minutes"
last_verified: 2026-10-25
tags:
  - glossary
  - flashcards
---

# Auto Termination

> [!eli5] Summary
> Auto termination turns off a computer that nobody is using. Cloud computers cost money while they run, so this setting stops charges for idle machines.

**In data work:** Cloud compute is billed while it runs, whether or not it is doing work. An auto-termination setting shuts a [[Cluster|cluster]] down after it has been idle for a set period. Example: an all-purpose cluster opened on Friday morning and left running over the weekend accrues more than 60 hours of idle charges unless auto termination is set.

**In Databricks:** On [[All-Purpose Compute]], set **Terminate after _N_ minutes of inactivity** in the compute form (API field `autotermination_minutes`). The value must be between 10 and 10,000 minutes; `0` disables auto termination. Admins can enforce limits with [[Compute Policies]]. [[Jobs Compute]] stops when its job ends. [[SQL Warehouses]] use **Auto stop**: serverless warehouses default to 10 minutes, and pro and classic warehouses to 45 minutes. Open JDBC or ODBC sessions can keep a warehouse running. See the [[Cost Optimization Checklist]].

Seen in: [[All-Purpose Compute]], [[SQL Warehouses]], [[Compute Policies]], [[Cost Optimization Checklist]], [[Cost Management Basics]]

## Recall

What range of values does all-purpose compute accept for auto termination?::10 to 10,000 minutes; 0 disables it.
What is the default auto stop for a serverless SQL warehouse?::10 minutes.

> [!sources]- Sources (last verified: 2026-10-25)
> - [Compute configuration reference (AWS)](https://docs.databricks.com/aws/en/compute/configure)
> - [Manage classic compute (AWS)](https://docs.databricks.com/aws/en/compute/clusters-manage)
> - [Create a SQL warehouse (AWS)](https://docs.databricks.com/aws/en/compute/sql-warehouse/create)
