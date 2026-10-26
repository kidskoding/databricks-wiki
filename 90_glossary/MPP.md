---
type: glossary
status: written
level: 90
section: Glossary
depth: 101
summary: "Massively parallel processing: a query engine design that splits one query across many machines, each working on its own slice of the data."
related:
  - "[[Data Warehouses]]"
  - "[[Photon]]"
  - "[[Distributed Systems]]"
  - "[[Scaling Up vs Scaling Out]]"
  - "[[Amazon Redshift]]"
  - "[[Snowflake]]"
aliases:
  - "massively parallel processing"
  - "MPP database"
  - "MPP engine"
last_verified: 2026-10-26
tags:
  - glossary
  - flashcards
---

# MPP

> [!eli5] Summary
> MPP means many computers work on one question at the same time. Each computer handles its own share of the data, and the partial answers are combined at the end.

**In data work:** An MPP system divides a table across many [[Node|nodes]]. When a query runs, each node scans, filters, and aggregates its own slice in parallel, and a coordinator combines the partial results. Classic MPP [[Data Warehouses|data warehouses]] use a shared-nothing design: each node has its own CPU, memory, and disk. [[Amazon Redshift]] provisioned clusters, for example, have a leader node that plans queries and compute nodes that execute them. Because data lives on the nodes, adding capacity in a classic MPP warehouse often means redistributing data. A retailer whose monthly sales report takes an hour on one database server can see it finish in minutes when ten nodes each scan a tenth of the rows.

**In Databricks:** [[Apache Spark]] and [[Photon]] run each query in parallel across the executors of a [[Cluster|cluster]] or [[SQL Warehouses|SQL warehouse]], so Databricks SQL behaves as an MPP engine. Databricks describes Photon-powered Databricks SQL in these terms. The difference from a classic MPP warehouse is that storage is separate from compute: tables live in [[Object Storage|object storage]], so you can resize or stop compute without moving data (see [[Storage vs Compute]]).

Seen in: [[Data Warehouses]], [[Photon]], [[Amazon Redshift]], [[Scaling Up vs Scaling Out]]

## Recall

MPP::Massively parallel processing: one query is split across many nodes that each process their own slice of the data in parallel.
How does Databricks differ from a classic shared-nothing MPP warehouse?::Storage is separate from compute, so compute can be resized or stopped without redistributing data.

> [!sources]- Sources (last verified: 2026-10-26)
> - [Databricks Sets Official Data Warehousing Performance Record (Databricks blog, 2021)](https://www.databricks.com/blog/2021/11/02/databricks-sets-official-data-warehousing-performance-record.html)
> - [Amazon Redshift provisioned clusters (AWS docs)](https://docs.aws.amazon.com/redshift/latest/mgmt/working-with-clusters.html)
