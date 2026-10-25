---
type: glossary
status: written
level: 90
section: Glossary
depth: 101
summary: "Storing a copy of data or query results in faster storage so repeated requests return sooner."
related:
  - "[[Query Performance and Caching]]"
  - "[[SQL Warehouses]]"
  - "[[Databricks SQL]]"
  - "[[Apache Spark]]"
  - "[[Storage vs Compute]]"
  - "[[AI-BI Dashboards]]"
aliases:
  - "cache"
  - "disk cache"
  - "result cache"
  - "Delta cache"
  - "DBIO cache"
last_verified: 2026-10-25
tags:
  - glossary
  - flashcards
---

# Caching

> [!eli5] Summary
> Caching keeps a copy of frequently used data close to where it is needed. The first request does the work; later requests reuse the saved copy.

**In data work:** A cache holds a copy in a faster location: memory instead of disk, local disk instead of remote storage, or a stored result instead of a recomputation. A cache must be invalidated or refreshed when the source changes, or it returns stale data. Example: a dashboard opened by 30 employees each morning computes its queries once and serves the cached results to everyone else.

**In Databricks:** Databricks has several caches. The **disk cache** (formerly the Delta cache and DBIO cache) copies remote Parquet and Delta files to local SSDs on the compute; it works automatically on worker types with SSDs and detects changed files. The **query result cache** on [[SQL Warehouses]] has a local cache for the warehouse's lifetime and, on serverless, a remote cache shared across warehouses; entries last 24 hours and are invalidated when underlying tables change. Disable it for benchmarking with `SET use_cached_result = false`. [[AI-BI Dashboards]] keep their own 24-hour cache. Spark's `df.cache()` stores DataFrames in memory, but Databricks recommends the disk cache for Parquet and Delta data.

Seen in: [[Query Performance and Caching]], [[SQL Warehouses]], [[Databricks SQL]], [[Apache Spark]]

## Recall

What does the Databricks disk cache store, and what was it formerly called?::Local copies of remote Parquet and Delta files on SSD; formerly the Delta cache.
How long do SQL warehouse result-cache entries last?::24 hours, or until the underlying tables change.

> [!sources]- Sources (last verified: 2026-10-25)
> - [Optimize performance with caching (Azure)](https://learn.microsoft.com/en-us/azure/databricks/optimizations/disk-cache)
> - [Query caching (AWS)](https://docs.databricks.com/aws/en/sql/user/queries/query-caching)
> - [Dataset optimization and caching (AWS)](https://docs.databricks.com/aws/en/dashboards/caching)
