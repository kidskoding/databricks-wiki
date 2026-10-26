---
type: glossary
status: written
level: 90
section: Glossary
depth: 101
summary: "A read-only copy of a database that serves queries so the primary can focus on writes."
related:
  - "[[Lakebase]]"
  - "[[Replication]]"
  - "[[Relational Databases]]"
  - "[[OLTP vs OLAP]]"
  - "[[Scalability]]"
  - "[[Migrating from Postgres and MySQL]]"
aliases:
  - "read-only replica"
  - "replica"
  - "read replicas"
last_verified: 2026-10-26
tags:
  - glossary
  - flashcards
---

# Read Replica

> [!eli5] Summary
> A read replica is a second copy of a database that only answers questions and never takes changes. It takes reporting load off the main database.

**In data work:** In a traditional database, a read replica receives a stream of changes from the primary through [[Replication|replication]] and applies them to its own copy of the data. Applications send writes to the primary and send read-heavy work, such as reports and dashboards, to replicas. Replicas usually lag the primary by a short time (replication lag), so a query on a replica may not see a change made a moment ago. A small online shop can point its reporting tool at a replica so a slow report never slows checkout.

**In Databricks:** In [[Lakebase]] (managed Postgres), read replicas are read-only compute instances that share the same storage as the primary. Because no data is copied, they can start in seconds and do not multiply storage. Lakebase compute can also attach to a past point in time to read the database as it was, without restoring data (see [[Point-in-Time Recovery]]). For analytics on Delta tables, replicas are not needed: many [[SQL Warehouses|SQL warehouses]] and clusters can read the same tables in [[Object Storage|object storage]] at once.

Seen in: [[Lakebase]], [[Replication]], [[Migrating from Postgres and MySQL]]

## Recall

Read replica::A read-only copy of a database that serves queries so the primary handles writes.
How do Lakebase read replicas differ from traditional replicas?::They are read-only computes on shared storage, so no data is copied and they start in seconds.

> [!sources]- Sources (last verified: 2026-10-26)
> - [Core concepts (Lakebase, AWS)](https://docs.databricks.com/aws/en/oltp/projects/core-concepts)
> - [Lakebase architecture (AWS)](https://docs.databricks.com/aws/en/oltp/projects/architecture)
> - [Manage projects (Lakebase, Azure Databricks)](https://learn.microsoft.com/en-us/azure/databricks/oltp/create/)
