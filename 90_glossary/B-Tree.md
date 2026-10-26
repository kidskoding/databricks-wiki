---
type: glossary
status: written
level: 90
section: Glossary
depth: 101
summary: "A balanced tree data structure that keeps sorted keys so a database can find, insert, and range-scan rows quickly; it is the default index in most relational databases."
related:
  - "[[Index]]"
  - "[[Relational Databases]]"
  - "[[OLTP vs OLAP]]"
  - "[[Data Skipping]]"
  - "[[Liquid Clustering]]"
  - "[[Migrating from Postgres and MySQL]]"
aliases:
  - "B-tree index"
  - "B+ tree"
  - "Btree"
last_verified: 2026-10-26
tags:
  - glossary
  - flashcards
---

# B-Tree

> [!eli5] Summary
> A B-tree is the structure behind a database index. It keeps values in sorted order in a shallow tree, so the database can jump to the right row in a few steps instead of reading the whole table.

**In data work:** A B-tree stores keys in sorted order across nodes that each hold many keys, and it stays balanced as rows are inserted and deleted. Lookups, inserts, and deletes touch only a few levels of the tree. It handles equality (`=`) and range (`<`, `BETWEEN`) queries on any sortable column. In PostgreSQL, `CREATE INDEX` builds a B-tree unless you choose another method with `USING`. B-tree indexes suit [[OLTP vs OLAP|OLTP]] workloads that read or update a few rows at a time.

**In Databricks:** Delta tables do not have B-tree indexes. Databricks targets analytical scans, so it narrows reads with file-level statistics ([[Data Skipping]]), [[Liquid Clustering]], and [[Partition Pruning|partition pruning]] instead. When you migrate from PostgreSQL or SQL Server, do not look for a `CREATE INDEX` equivalent; cluster the table on the columns you filter by. For low-latency row lookups from an app, [[Lakebase]] is a managed Postgres service where B-tree indexes apply.

Small-business example: a shop's order database finds order 10452 through a B-tree on `order_id`. The same orders copied to Databricks for monthly reporting rely on clustering by `order_date` instead.

Seen in: [[Index]], [[Relational Databases]], [[Migrating from Postgres and MySQL]]

## Recall

What is the default index type in PostgreSQL?::B-tree.
Do Delta tables use B-tree indexes?::No. They rely on data skipping, liquid clustering, and partition pruning.

> [!sources]- Sources (last verified: 2026-10-26)
> - [Index Types, PostgreSQL 18 documentation](https://www.postgresql.org/docs/current/indexes-types.html)
