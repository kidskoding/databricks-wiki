---
type: glossary
status: written
level: 90
section: Glossary
depth: 101
summary: "The rule that defines how much concurrent transactions can see of each other's changes; Delta tables on Databricks offer WriteSerializable (default) and Serializable."
related:
  - "[[ACID Transactions]]"
  - "[[Optimistic Concurrency]]"
  - "[[MVCC]]"
  - "[[Delta Transaction Log]]"
  - "[[MERGE and Upserts]]"
aliases:
  - "Isolation levels"
  - "WriteSerializable"
  - "Serializable"
  - "delta.isolationLevel"
last_verified: 2026-10-26
tags:
  - glossary
  - flashcards
---

# Isolation Level

> [!eli5] Summary
> An isolation level decides how strictly a database keeps two people's simultaneous changes from interfering. Stricter rules are safer but let fewer changes happen at the same time.

**In data work:** Isolation is the I in [[ACID Transactions|ACID]]. Relational databases define levels such as Read Committed, Repeatable Read, Snapshot, and Serializable. Serializable is the strongest: the result equals some one-at-a-time order of the transactions. Weaker levels allow more concurrency at the cost of anomalies a reader might observe.

**In Databricks:** [[Delta Lake]] tables on Databricks use [[Optimistic Concurrency|optimistic concurrency control]], so there are no locks and no deadlocks; conflicting commits fail and can be retried. Two levels exist:

| Level | Guarantee | Notes |
|---|---|---|
| `WriteSerializable` (default) | Writes are serializable; readers may see a state that never appears in the log order. | Plain `INSERT`s rarely conflict with `UPDATE`, `DELETE`, or `MERGE`. |
| `Serializable` | Reads and writes are serializable. | Stricter; lowers concurrent write throughput. |

```sql
ALTER TABLE orders SET TBLPROPERTIES ('delta.isolationLevel' = 'Serializable');
```

Row-level concurrency further reduces conflicts between writers touching different rows.

Small-business consideration: keep the default. Change it only if an audit or financial process requires that every read reflects an exact commit order.

Seen in: [[ACID Transactions]], [[Delta Transaction Log]], [[MERGE and Upserts]]

## Recall

What is the default isolation level for Delta tables on Databricks?::WriteSerializable.
Which table property changes the isolation level?::delta.isolationLevel

> [!sources]- Sources (last verified: 2026-10-26)
> - [Isolation levels and write conflicts (AWS)](https://docs.databricks.com/aws/en/optimizations/isolation)
> - [Isolation levels (WriteSerializable and Serializable) (Azure)](https://learn.microsoft.com/en-us/azure/databricks/optimizations/isolation/isolation-levels)
> - [Row-level concurrency (AWS)](https://docs.databricks.com/aws/en/optimizations/isolation/row-level-concurrency)
