---
type: glossary
status: written
level: 90
section: Glossary
depth: 101
summary: "The central table in a star schema that records business events and their numeric measures."
related:
  - "[[Star Schema]]"
  - "[[Dimension Table]]"
  - "[[Data Modeling Basics]]"
  - "[[Metric Views]]"
  - "[[Primary and Foreign Keys]]"
  - "[[Liquid Clustering]]"
aliases:
  - "fact"
  - "facts"
  - "fact tables"
last_verified: 2026-10-25
tags:
  - glossary
  - flashcards
---

# Fact Table

> [!eli5] Summary
> A fact table records business events, one row per event, with the numbers that matter, such as quantity and price. Other tables describe what the codes in each row mean.

**In data work:** In a [[Star Schema|star schema]], each fact-table row records one event at a defined grain (one order line, one shipment, one session). It contains foreign keys to [[Dimension Table|dimension tables]] and numeric measures such as quantity, revenue, or duration. Fact tables are long and narrow and grow continuously. Example: `fact_sales` with `date_key`, `store_key`, `product_key`, `quantity`, and `net_amount`; revenue reports [[Aggregation|aggregate]] it.

**In Databricks:** Fact tables are [[Delta Lake]] tables in the gold layer, typically loaded incrementally with `MERGE` or from [[Streaming Tables]]. Because they are the largest tables, layout matters: Databricks recommends [[Liquid Clustering]] on frequently filtered columns, such as the date, which improves [[Data Skipping|data skipping]]. [[Metric Views]] define measures such as `SUM(net_amount)` on top of fact tables so every tool computes them identically.

Seen in: [[Star Schema]], [[Dimension Table]], [[Data Modeling Basics]], [[Metric Views]]

## Recall

What two kinds of columns does a fact table contain?::Foreign keys to dimension tables and numeric measures.
What is the grain of a fact table?::What a single row represents, such as one order line.

> [!sources]- Sources (last verified: 2026-10-25)
> - [Use liquid clustering for tables (AWS)](https://docs.databricks.com/aws/en/tables/clustering)
> - [Unity Catalog metric views (AWS)](https://docs.databricks.com/aws/en/uc-semantics/metric-views/)
