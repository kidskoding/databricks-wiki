---
type: glossary
status: written
level: 90
section: Glossary
depth: 101
summary: "How well a system keeps working as data, users, or traffic grow."
related:
  - "[[Scaling Up vs Scaling Out]]"
  - "[[Autoscaling]]"
  - "[[Distributed Systems]]"
  - "[[Storage vs Compute]]"
  - "[[Serverless Compute]]"
  - "[[The Three Vs of Big Data]]"
aliases:
  - "scalable"
  - "scale"
  - "elasticity"
last_verified: 2026-10-25
tags:
  - glossary
  - flashcards
---

# Scalability

> [!eli5] Summary
> Scalability is a system's ability to handle more data, users, or traffic by adding resources, without a redesign.

**In data work:** A scalable system handles more load by adding resources, ideally without redesign and with cost growing roughly in step with use. Vertical scaling (scaling up) means a bigger machine; horizontal scaling (scaling out) means more machines working in parallel (see [[Scaling Up vs Scaling Out]]). Elasticity adds the ability to shrink again when demand drops, so you stop paying for idle capacity. A spreadsheet stops scaling at about a million rows; a distributed engine can process billions by splitting the work across [[Node|nodes]].

**In Databricks:** Databricks scales by [[Storage vs Compute|separating storage from compute]]: data sits in cheap cloud object storage, and compute scales independently. Clusters can [[Autoscaling|autoscale]] workers, SQL warehouses add clusters as queries queue up, and [[Serverless Compute]] sizes itself. The same platform that runs a ten-gigabyte bakery dataset runs petabyte workloads, though small teams should size small and grow.

Seen in: [[Scaling Up vs Scaling Out]], [[Autoscaling]], [[Storage vs Compute]]

## Recall

Scalability::A system's ability to handle growing data or users by adding resources, ideally with cost tracking use.

> [!sources]- Sources (last verified: 2026-10-25)
> - [SQL warehouse sizing, scaling, and queuing behavior (AWS)](https://docs.databricks.com/aws/en/compute/sql-warehouse/warehouse-behavior)
> - [Compute configuration reference (AWS)](https://docs.databricks.com/aws/en/compute/configure)
