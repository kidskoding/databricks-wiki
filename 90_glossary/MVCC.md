---
type: glossary
status: written
level: 90
section: Glossary
depth: 101
summary: "Multi-version concurrency control: keeping several versions of data so readers see a consistent snapshot while writers make changes."
related:
  - "[[ACID Transactions]]"
  - "[[Delta Transaction Log]]"
  - "[[Optimistic Concurrency]]"
  - "[[Isolation Level]]"
  - "[[Time Travel]]"
  - "[[OPTIMIZE and VACUUM]]"
aliases:
  - "multi-version concurrency control"
  - "multiversion concurrency control"
last_verified: 2026-10-26
tags:
  - glossary
  - flashcards
---

# MVCC

> [!eli5] Summary
> MVCC lets a database keep older copies of data while new changes are written. People reading the data see a complete, consistent picture and never a half-finished change.

**In data work:** Without MVCC, a reader and a writer touching the same rows must take turns, usually through locks. With MVCC, a write creates a new version instead of overwriting the old one. Each reader works from the version that was current when its query started, so readers do not block writers and writers do not block readers. Old versions are cleaned up once no reader needs them. If a bookkeeper runs a quarter-end report while the order system is still writing, MVCC makes sure the report sees one consistent point in time.

**In Databricks:** [[Delta Lake]] uses MVCC to provide snapshot isolation and [[Time Travel|time travel]]. Data files are never modified in place. Each commit to the [[Delta Transaction Log|transaction log]] adds new files and marks old ones as removed, creating a new table version. A query reads the files that belong to one version, so a concurrent `MERGE` cannot change what it sees. Old files stay until `VACUUM` removes them, with a default retention threshold of 7 days (see [[OPTIMIZE and VACUUM]]). Writers coordinate through [[Optimistic Concurrency|optimistic concurrency]] rather than locks, and the [[Isolation Level|isolation level]] controls how strict the conflict checks are.

Seen in: [[ACID Transactions]], [[Delta Transaction Log]], [[Time Travel]], [[Isolation Level]]

## Recall

MVCC::Multi-version concurrency control: writes create new versions so readers see a consistent snapshot without locks.
What removes old data file versions in Delta Lake?::VACUUM, with a default retention threshold of 7 days.

> [!sources]- Sources (last verified: 2026-10-26)
> - [Concurrency Control in DBMS: Locking, MVCC and Optimistic Strategies (Databricks blog)](https://www.databricks.com/blog/concurrency-control)
> - [Delta Lake: High-Performance ACID Table Storage over Cloud Object Stores (PVLDB 2020)](https://www.vldb.org/pvldb/vol13/p3411-armbrust.pdf)
> - [Isolation levels: WriteSerializable and Serializable (AWS)](https://docs.databricks.com/aws/en/optimizations/isolation/isolation-levels)
