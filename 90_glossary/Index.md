---
type: glossary
status: written
level: 90
section: Glossary
depth: 101
summary: "A data structure that lets a database locate rows without scanning the whole table."
related:
  - "[[Relational Databases]]"
  - "[[Data Skipping]]"
  - "[[Liquid Clustering]]"
  - "[[Vector Search]]"
  - "[[Lakebase]]"
  - "[[OLTP vs OLAP]]"
aliases:
  - "indexes"
  - "indices"
  - "B-tree index"
  - "database index"
last_verified: 2026-10-25
tags:
  - glossary
  - flashcards
---

# Index

> [!eli5] Summary
> An index works like the index of a book: it points directly to where a value is stored, so the database does not have to read every row.

**In data work:** In a [[Relational Databases|relational database]] such as PostgreSQL or SQL Server, an index (commonly a B-tree) on a column lets a query such as `WHERE customer_id = 1182` locate matching rows in a few steps. Indexes speed up reads but slow down writes and consume storage. They suit [[OLTP vs OLAP|OLTP]] workloads that fetch a few rows at a time. Analytical queries that scan many rows rely more on [[Columnar Storage|columnar]] layout and file statistics.

**In Databricks:** [[Delta Lake]] tables do not use B-tree indexes. They rely on [[Data Skipping|data skipping]] with per-file statistics, and on [[Liquid Clustering]] to colocate related rows. [[Lakebase]], the managed PostgreSQL database, supports standard PostgreSQL indexes for application lookups. In Databricks AI Search ([[Vector Search]]), an index stores [[Embedding|embeddings]] for similarity search; Delta Sync indexes stay synchronized with a source table, and Direct Vector Access indexes are updated through the API.

Seen in: [[Relational Databases]], [[Data Skipping]], [[Liquid Clustering]], [[Vector Search]], [[Lakebase]]

## Recall

What is the trade-off of adding a database index?::Faster lookups in exchange for slower writes and extra storage.
What do Delta tables use instead of B-tree indexes?::Data skipping with per-file statistics, together with liquid clustering.

> [!sources]- Sources (last verified: 2026-10-25)
> - [Data skipping (AWS)](https://docs.databricks.com/aws/en/tables/data-skipping)
> - [Create AI Search endpoints and indexes (AWS)](https://docs.databricks.com/aws/en/ai-search/create-ai-search)
