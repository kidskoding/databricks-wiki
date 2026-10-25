---
type: glossary
status: written
level: 90
section: Glossary
depth: 101
summary: "A request to read or change data, usually written in SQL."
related:
  - "[[SQL]]"
  - "[[Databricks SQL]]"
  - "[[SQL Editor]]"
  - "[[SQL Warehouses]]"
  - "[[Catalyst Optimizer]]"
  - "[[Query Performance and Caching]]"
aliases:
  - "queries"
  - "SQL query"
  - "SELECT statement"
last_verified: 2026-10-25
tags:
  - glossary
  - flashcards
---

# Query

> [!eli5] Summary
> A query is a request to read or change data, usually written in SQL.

**In data work:** A query is a statement sent to a database or engine, most often in [[SQL]]. Read queries (`SELECT`) return rows; write statements (`INSERT`, `UPDATE`, `MERGE`) change them. The engine turns the query into a plan, decides which files or indexes to read, and runs it. Query performance depends on how much data must be scanned, the [[Join|joins]], and the compute behind it. Example query: `SELECT product, SUM(amount) FROM sales WHERE sale_date >= '2026-10-01' GROUP BY product ORDER BY 2 DESC`.

**In Databricks:** In Databricks you write queries in the [[SQL Editor]] or [[Notebooks]], and they run on [[SQL Warehouses]] or clusters. Spark's [[Catalyst Optimizer]] and [[Photon]] plan and execute them. Query history shows each run, its duration, and its profile, and [[Query Performance and Caching]] explains how to make slow queries fast. [[Genie]] can write queries for you from plain English.

Seen in: [[SQL]], [[SQL Editor]], [[Databricks SQL]], [[Query Performance and Caching]]

## Recall

Query::A request to read or change data, usually in SQL; in Databricks it runs on a SQL warehouse or cluster and appears in query history.
