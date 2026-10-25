---
type: glossary
status: written
level: 90
section: Glossary
depth: 101
summary: "Combining many rows into one summary value per group, such as a total, count, or average."
related:
  - "[[SQL]]"
  - "[[Star Schema]]"
  - "[[Materialized Views]]"
  - "[[Metric Views]]"
  - "[[Shuffles]]"
  - "[[Medallion Architecture]]"
aliases:
  - "aggregate"
  - "GROUP BY"
  - "rollup"
last_verified: 2026-10-25
tags:
  - glossary
  - flashcards
---

# Aggregation

> [!eli5] Summary
> Aggregation turns many detailed records into a few summary numbers, such as total sales per day. Most reports show aggregated data rather than individual records.

**In data work:** An aggregation applies a function such as `SUM`, `COUNT`, `AVG`, `MIN`, or `MAX` to a group of rows and returns one row per group. In [[SQL]], the groups are defined with `GROUP BY`. The level of detail of the result is its grain. Example: a bakery with 40,000 receipt lines per month runs `SELECT store, sale_date, SUM(total) FROM sales GROUP BY store, sale_date` to get daily revenue per store.

**In Databricks:** Aggregated tables usually form the gold layer of the [[Medallion Architecture]], which [[AI-BI Dashboards|dashboards]] and [[Genie]] query. [[Materialized Views]] store an aggregation and refresh it incrementally. [[Metric Views]] define measures (aggregate expressions) separately from the dimensions used to group them, so every tool computes a metric the same way. In [[Apache Spark]], a `GROUP BY` on a large table causes a [[Shuffles|shuffle]], because rows with the same key must be on the same executor.

Seen in: [[SQL]], [[Star Schema]], [[Materialized Views]], [[Metric Views]], [[Shuffles]]

## Recall

What does an aggregation return?::One summary row per group, computed with a function such as SUM, COUNT, or AVG.
Why does a large GROUP BY in Spark cause a shuffle?::Rows that share a grouping key must be moved to the same executor before they can be combined.

> [!sources]- Sources (last verified: 2026-10-25)
> - [Unity Catalog metric views (AWS)](https://docs.databricks.com/aws/en/uc-semantics/metric-views/)
