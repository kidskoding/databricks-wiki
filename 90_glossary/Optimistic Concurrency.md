---
type: glossary
status: written
level: 90
section: Glossary
depth: 101
summary: "A concurrency strategy where writers work without locks and check for conflicts only at commit time, retrying if another write committed first."
related:
  - "[[MVCC]]"
  - "[[Isolation Level]]"
  - "[[Delta Transaction Log]]"
  - "[[ACID Transactions]]"
  - "[[MERGE and Upserts]]"
  - "[[Deletion Vectors]]"
aliases:
  - "optimistic concurrency control"
  - "OCC"
  - "ConcurrentModificationException"
last_verified: 2026-10-26
tags:
  - glossary
  - flashcards
---

# Optimistic Concurrency

> [!eli5] Summary
> Optimistic concurrency assumes two people rarely change the same data at once. Everyone works freely, and only when saving does the system check for a clash and ask the loser to try again.

**In data work:** Pessimistic systems lock data before changing it, so other writers wait. Optimistic systems skip the locks. Each writer reads the current state, does its work, and at commit time checks whether anything it depended on changed. If not, the commit succeeds. If so, the commit fails and the writer retries. This works well when conflicts are rare, which is typical for analytics tables written by a few scheduled jobs.

**In Databricks:** [[Delta Lake]] uses optimistic concurrency control on top of [[MVCC]].
1. A writer reads the latest table version to find the files it affects.
2. It writes new data files.
3. At commit, it validates that no conflicting change was committed in the meantime.
4. It writes the next numbered entry in the [[Delta Transaction Log|transaction log]]; only one writer can create each entry.

When a conflict is found, Delta Lake raises a concurrent modification exception and the job must retry. The table's [[Isolation Level|isolation level]] (`WriteSerializable` by default, or `Serializable`) sets how strict the check is. Row-level concurrency, which relies on [[Deletion Vectors|deletion vectors]], lets concurrent `MERGE`, `UPDATE`, and `DELETE` operations on different rows of the same files both succeed.

Seen in: [[ACID Transactions]], [[Delta Transaction Log]], [[Isolation Level]], [[MERGE and Upserts]]

## Recall

Optimistic concurrency::Writers proceed without locks and validate for conflicts at commit time, retrying if a conflicting commit happened first.
What is Delta Lake's default isolation level for writes?::WriteSerializable.

> [!sources]- Sources (last verified: 2026-10-26)
> - [Isolation levels and write conflicts (AWS)](https://docs.databricks.com/aws/en/optimizations/isolation/)
> - [Row-level concurrency (AWS)](https://docs.databricks.com/aws/en/optimizations/isolation/row-level-concurrency)
> - [Concurrency Control in DBMS (Databricks blog)](https://www.databricks.com/blog/concurrency-control)
> - [Delta Lake: High-Performance ACID Table Storage over Cloud Object Stores (PVLDB 2020)](https://www.vldb.org/pvldb/vol13/p3411-armbrust.pdf)
