---
type: glossary
status: written
level: 90
section: Glossary
depth: 101
summary: "A family of non-relational databases (key-value, document, wide-column, and graph) built for flexible schemas and horizontal scale."
related:
  - "[[Relational Databases]]"
  - "[[Apache HBase]]"
  - "[[Sharding]]"
  - "[[CAP Theorem]]"
  - "[[Semi-Structured Data]]"
  - "[[OLTP vs OLAP]]"
aliases:
  - "non-relational database"
  - "NoSQL database"
  - "document database"
  - "key-value store"
last_verified: 2026-10-26
tags:
  - glossary
  - flashcards
---

# NoSQL

> [!eli5] Summary
> NoSQL databases store data in shapes other than fixed tables, such as documents or key-value pairs. They trade some features of traditional databases for flexibility and the ability to spread across many machines.

**In data work:** "NoSQL" covers several designs that do not use the relational table model:

| Type | Stores | Example |
|---|---|---|
| Key-value | A value looked up by a key | Session caches |
| Document | JSON-like documents | MongoDB |
| Wide-column | Rows with flexible column families | [[Apache HBase]] (modeled after Google Bigtable) |
| Graph | Nodes and relationships | Recommendation graphs |

Most NoSQL systems were designed for [[Sharding|sharding]] across many servers, and many relax strict transactions or joins in exchange for scale and availability (see [[CAP Theorem]]). They serve application traffic ([[OLTP vs OLAP|OLTP]]), not analytics. An online store might keep shopping carts in a document database and still analyze orders elsewhere.

**In Databricks:** Databricks is not a NoSQL database. Teams ingest data from NoSQL systems into [[Delta Lake]] tables for analytics, and they store nested JSON from those systems in the [[VARIANT Data Type|VARIANT]] type (see [[Semi-Structured Data]]). For application data, [[Lakebase]] provides managed Postgres, which is relational.

Seen in: [[Relational Databases]], [[Apache HBase]], [[Semi-Structured Data]]

## Recall

NoSQL::Non-relational databases (key-value, document, wide-column, graph) designed for flexible schemas and horizontal scale.
Which Hadoop-era database is a wide-column NoSQL store?::Apache HBase.

> [!sources]- Sources (last verified: 2026-10-26)
> - [Database Sharding: Concepts and Examples (MongoDB)](https://www.mongodb.com/resources/products/capabilities/database-sharding-explained)
> - [Apache HBase home page](https://hbase.apache.org/2.1/)
> - [Query variant data (AWS)](https://docs.databricks.com/aws/en/semi-structured/variant)
