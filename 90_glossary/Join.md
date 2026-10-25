---
type: glossary
status: written
level: 90
section: Glossary
depth: 101
summary: "A query operation that combines rows from two tables based on matching values in one or more columns."
related:
  - "[[SQL]]"
  - "[[Primary and Foreign Keys]]"
  - "[[Star Schema]]"
  - "[[Shuffles]]"
  - "[[Adaptive Query Execution]]"
  - "[[Broadcast Join]]"
aliases:
  - "joins"
  - "JOIN"
  - "inner join"
  - "left join"
  - "outer join"
last_verified: 2026-10-25
tags:
  - glossary
  - flashcards
---

# Join

> [!eli5] Summary
> A join matches rows from two tables using a shared value, such as a customer ID, to produce one combined result.

**In data work:** A join matches rows on a key, usually a [[Primary and Foreign Keys|foreign key]] to a primary key. `INNER JOIN` keeps only matching rows. `LEFT JOIN` keeps every row from the left table and fills unmatched columns with nulls. `FULL OUTER JOIN` keeps all rows from both sides, and `CROSS JOIN` pairs every row with every row. Joining on a key that is not unique on one side duplicates rows and inflates totals.

**In Databricks:** In [[Apache Spark]], a join between large tables [[Shuffles|shuffles]] both sides so matching keys meet on the same executor; a [[Broadcast Join|broadcast join]] avoids this when one side is small. [[Adaptive Query Execution]] can switch join strategies at runtime and split [[Data Skew|skewed]] partitions in shuffle-based joins. Join hints (`BROADCAST`, `MERGE`, `SHUFFLE_HASH`, `SHUFFLE_REPLICATE_NL`) suggest a strategy, but not every strategy supports every join type. [[Metric Views]] can define joins once for analysts.

Seen in: [[SQL]], [[Primary and Foreign Keys]], [[Star Schema]], [[Shuffles]], [[Adaptive Query Execution]]

## Recall

What does a LEFT JOIN keep?::Every row from the left table, with nulls where the right table has no match.
What commonly causes inflated totals after a join?::Joining on a key that is not unique on one side, which duplicates rows.

> [!sources]- Sources (last verified: 2026-10-25)
> - [Hints (AWS)](https://docs.databricks.com/aws/en/sql/language-manual/sql-ref-syntax-qry-select-hints)
> - [Adaptive query execution (AWS)](https://docs.databricks.com/aws/en/optimizations/aqe)
