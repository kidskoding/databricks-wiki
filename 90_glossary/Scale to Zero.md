---
type: glossary
status: written
level: 90
section: Glossary
depth: 101
summary: "The ability of a service to release all compute when idle, so no compute is billed until the next request arrives."
related:
  - "[[Serverless Compute]]"
  - "[[Model Serving]]"
  - "[[SQL Warehouses]]"
  - "[[Auto Termination]]"
  - "[[Autoscaling]]"
  - "[[Latency]]"
aliases:
  - "scale-to-zero"
  - "scale_to_zero_enabled"
  - "cold start"
last_verified: 2026-10-26
tags:
  - glossary
  - flashcards
---

# Scale to Zero

> [!eli5] Summary
> Scale to zero means a service turns itself fully off when nobody is using it and turns back on when a request comes in. You stop paying for idle machines, but the first request after a pause is slower.

**In data work:** [[Autoscaling]] adds and removes capacity as load changes; scale to zero lets the minimum be zero. The trade-off is the **cold start**: the first request after an idle period waits while compute starts. Scale to zero suits workloads with long idle gaps, such as a dashboard used during business hours or a model called a few times a day. It does not suit endpoints that must answer quickly at any moment.

**In Databricks:**
- **[[Model Serving]]:** Scale to zero is optional per endpoint (`scale_to_zero_enabled`). An endpoint scales to zero after 30 minutes of inactivity. Scaling back up usually takes 10 to 20 seconds but can take minutes, with no SLA. Databricks advises against it for production workloads that need consistent uptime.
- **[[SQL Warehouses]]:** Serverless SQL warehouses start in about 2 to 6 seconds, so you can stop them when idle with little penalty. Classic and pro warehouses take minutes to start.
- **Classic compute:** Clusters do not scale to zero, but [[Auto Termination|auto termination]] stops them after a set idle time.

For a small business, a serverless SQL warehouse with a short auto-stop and a scale-to-zero model endpoint for internal tools keep idle costs near zero.

Seen in: [[Serverless Compute]], [[Model Serving]], [[SQL Warehouses]]

## Recall

Scale to zero::Releasing all compute when idle so nothing is billed until the next request, at the cost of a cold start.
After how long idle does a Model Serving endpoint with scale to zero scale down?::30 minutes.

> [!sources]- Sources (last verified: 2026-10-26)
> - [Create custom model serving endpoints (AWS)](https://docs.databricks.com/aws/en/machine-learning/model-serving/create-manage-serving-endpoints)
> - [Custom models overview (AWS)](https://docs.databricks.com/aws/en/machine-learning/model-serving/custom-models)
> - [SQL warehouse types (AWS)](https://docs.databricks.com/aws/en/compute/sql-warehouse/warehouse-types)
> - [Best practices for cost optimization (AWS)](https://docs.databricks.com/aws/en/lakehouse-architecture/cost-optimization/best-practices)
