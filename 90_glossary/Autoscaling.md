---
type: glossary
status: written
level: 90
section: Glossary
depth: 101
summary: "Automatically adding compute capacity when the workload grows and removing it when the workload shrinks."
related:
  - "[[Scaling Up vs Scaling Out]]"
  - "[[All-Purpose Compute]]"
  - "[[Jobs Compute]]"
  - "[[SQL Warehouses]]"
  - "[[Serverless Compute]]"
  - "[[Cost Optimization Checklist]]"
aliases:
  - "auto-scaling"
  - "autoscale"
  - "elastic scaling"
last_verified: 2026-10-25
tags:
  - glossary
  - flashcards
---

# Autoscaling

> [!eli5] Summary
> Autoscaling adds computers when there is a lot of work and removes them when there is little. You pay for extra capacity only while it is needed.

**In data work:** An autoscaling system changes the number of [[Node|nodes]] it uses, between a minimum and a maximum, based on load. It is automated [[Scaling Up vs Scaling Out|scaling out]]. More nodes do not help every workload: a single long task or a [[Data Skew|skewed]] partition does not finish faster. Example: a nightly load that is heavy for 20 minutes runs on 2 to 8 workers instead of a fixed 8.

**In Databricks:** On classic compute, select **Enable autoscaling** and set **Min** and **Max** workers; the maximum must be greater than the minimum. Databricks adds workers when work queues and removes them gradually when nodes are idle. Classic and pro [[SQL Warehouses]] scale by adding or removing whole clusters between a configured minimum and maximum. Serverless SQL warehouses use Intelligent Workload Management instead of manual bounds. Databricks recommends about one warehouse cluster per 10 concurrent queries as a starting point.

Seen in: [[Scaling Up vs Scaling Out]], [[All-Purpose Compute]], [[Jobs Compute]], [[SQL Warehouses]], [[Compute Types]]

## Recall

Which two values configure autoscaling on classic compute?::The minimum and maximum number of workers.
How does a classic or pro SQL warehouse scale for more concurrent queries?::It adds or removes whole clusters between a configured minimum and maximum.

> [!sources]- Sources (last verified: 2026-10-25)
> - [Compute configuration reference (Azure)](https://learn.microsoft.com/en-us/azure/databricks/compute/configure)
> - [SQL warehouse sizing, scaling, and queuing behavior (AWS)](https://docs.databricks.com/aws/en/compute/sql-warehouse/warehouse-behavior)
> - [Create a SQL warehouse (AWS)](https://docs.databricks.com/aws/en/compute/sql-warehouse/create)
