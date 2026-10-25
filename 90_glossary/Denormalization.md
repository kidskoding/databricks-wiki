---
type: glossary
status: written
level: 90
section: Glossary
depth: 101
summary: "Storing redundant copies of data in wider tables so queries need fewer joins."
related:
  - "[[Data Modeling Basics]]"
  - "[[Star Schema]]"
  - "[[Relational Databases]]"
  - "[[OLTP vs OLAP]]"
  - "[[Medallion Architecture]]"
  - "[[Normalization]]"
aliases:
  - "denormalize"
  - "denormalized"
  - "wide table"
  - "flattening"
last_verified: 2026-10-25
tags:
  - glossary
  - flashcards
---

# Denormalization

> [!eli5] Summary
> Denormalization repeats some information across rows, such as a customer's name on every order, so reports do not need to look it up in another table.

**In data work:** [[Normalization]] stores each fact once across many related tables, which suits transactional ([[OLTP vs OLAP|OLTP]]) applications. Denormalization copies attributes from related tables into one wide table, trading extra storage and harder updates for simpler and faster reads. A [[Star Schema|star schema]] is partially denormalized; a single flat table is fully denormalized. Example: an order-lines table that includes product name, category, and store city needs no [[Join|joins]] for most reports.

**In Databricks:** Denormalized tables are common in the gold layer of the [[Medallion Architecture]], where [[AI-BI Dashboards|dashboards]] and [[Genie Agents]] work best on wide, clearly named tables. [[Columnar Storage|Columnar]] storage reduces the cost of redundancy: repeated values [[Compression|compress]] well, and queries read only the columns they reference. Keep normalized silver tables as the source of truth and rebuild gold tables from them.

Seen in: [[Data Modeling Basics]], [[Star Schema]], [[OLTP vs OLAP]], [[Medallion Architecture]]

## Recall

What does denormalization trade for faster reads?::Extra storage and more complex updates.
Why is redundancy cheaper in columnar formats?::Repeated values compress well, and queries read only referenced columns.
