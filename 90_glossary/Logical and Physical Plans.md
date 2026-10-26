---
type: glossary
status: written
level: 90
section: Glossary
depth: 101
summary: "The two stages of a Spark query plan: the logical plan describes what result to compute, and the physical plan describes exactly how the cluster will compute it."
related:
  - "[[Catalyst Optimizer]]"
  - "[[Spark SQL]]"
  - "[[Adaptive Query Execution]]"
  - "[[Spark UI]]"
  - "[[Lazy Evaluation]]"
  - "[[Query Performance and Caching]]"
aliases:
  - "Logical plan"
  - "Physical plan"
  - "Query plan"
  - "Execution plan"
  - "EXPLAIN"
last_verified: 2026-10-26
tags:
  - glossary
  - flashcards
---

# Logical and Physical Plans

> [!eli5] Summary
> Before running a query, Spark first writes down what you asked for, then works out the fastest way to do it. The first is the logical plan and the second is the physical plan.

**In data work:** A query engine turns SQL or [[DataFrames|DataFrame]] code into a tree of operators. The **logical plan** lists relational operations (filter, join, aggregate) without saying how to run them. An optimizer rewrites it, for example by pushing filters down. The **physical plan** chooses concrete algorithms and data movement, such as a broadcast hash join versus a sort-merge join and where [[Shuffles|shuffles]] happen.

**In Databricks:** Spark's [[Catalyst Optimizer]] produces four plans: parsed (unresolved) logical, analyzed logical, optimized logical, and physical. Use `EXPLAIN` to see them:

```sql
EXPLAIN FORMATTED
SELECT region, sum(amount) FROM sales WHERE year = 2026 GROUP BY region;
```

`EXPLAIN` alone shows the physical plan; `EXTENDED` shows all four; `FORMATTED` gives an outline plus per-node details. In Python, call `df.explain(mode="formatted")`. In Databricks Runtime 16.0 and above, the output also lists tables with missing statistics. `EXPLAIN` does not run the query, so it shows the plan before [[Adaptive Query Execution]] changes it; the final plan is in the [[Spark UI]] or the query profile.

Small-business example: a slow dashboard query shows a `SortMergeJoin` against a small lookup table; adding a broadcast hint changes the physical plan to a [[Broadcast Join|broadcast join]].

Seen in: [[Catalyst Optimizer]], [[Spark SQL]], [[Adaptive Query Execution]]

## Recall

What is the difference between a logical and a physical plan?::The logical plan says what to compute; the physical plan says how, including join algorithms and shuffles.
Which EXPLAIN option shows parsed, analyzed, optimized, and physical plans?::EXPLAIN EXTENDED.

> [!sources]- Sources (last verified: 2026-10-26)
> - [EXPLAIN (AWS)](https://docs.databricks.com/aws/en/sql/language-manual/sql-ref-syntax-qry-explain)
> - [DataFrame.explain (Azure)](https://learn.microsoft.com/en-us/azure/databricks/pyspark/reference/classes/dataframe/explain)
