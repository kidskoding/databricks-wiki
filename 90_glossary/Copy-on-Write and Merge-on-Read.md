---
type: glossary
status: written
level: 90
section: Glossary
depth: 101
summary: "Two strategies for updating rows in immutable data files: copy-on-write rewrites affected files at write time, while merge-on-read records changes separately and applies them when the table is read."
related:
  - "[[Deletion Vectors]]"
  - "[[Open Table Formats]]"
  - "[[Apache Iceberg]]"
  - "[[Apache Hudi]]"
  - "[[MERGE and Upserts]]"
  - "[[Delta Lake]]"
aliases:
  - "Copy-on-write"
  - "Merge-on-read"
  - "COW"
  - "MOR"
last_verified: 2026-10-26
tags:
  - glossary
  - flashcards
---

# Copy-on-Write and Merge-on-Read

> [!eli5] Summary
> Data lake files cannot be edited in place. To change one row, a system either rewrites the whole file right away, or writes a small note saying which rows changed and combines the two when someone reads the table.

**In data work:** [[Open Table Formats|Open table formats]] store data in immutable Parquet files. **Copy-on-write (COW)** rewrites every file that contains a changed row during the `UPDATE`, `DELETE`, or `MERGE`; writes are slower, reads have no extra work. **Merge-on-read (MOR)** writes small delete or change files instead; writes are fast, and readers merge the changes until compaction rewrites the files. [[Apache Iceberg]] exposes this as `write.delete.mode`, `write.update.mode`, and `write.merge.mode`, defaulting to `copy-on-write`; merge-on-read needs format v2 or later. [[Apache Hudi]] names its table types COW and MOR.

**In Databricks:** [[Delta Lake]] on Databricks implements merge-on-read with [[Deletion Vectors|deletion vectors]]: a `DELETE` or `UPDATE` marks rows as removed in a small bitmap rather than rewriting the file. `OPTIMIZE` and `REORG TABLE` later apply the marks physically. Databricks also supports deletion vectors on Iceberg v3 tables. You cannot enable deletion vectors on a Delta table that has Iceberg reads ([[Delta UniForm]]) enabled.

Small-business example: a nightly job that corrects a few hundred order rows in a large table finishes faster with deletion vectors because it no longer rewrites whole files.

Seen in: [[Deletion Vectors]], [[Apache Iceberg]], [[Apache Hudi]]

## Recall

Which strategy makes writes faster but reads slower: copy-on-write or merge-on-read?::Merge-on-read.
How does Delta Lake implement merge-on-read?::With deletion vectors.

> [!sources]- Sources (last verified: 2026-10-26)
> - [Configuration, write.delete.mode (iceberg.apache.org)](https://iceberg.apache.org/docs/latest/configuration/)
> - [RowLevelOperationMode Javadoc (iceberg.apache.org)](https://iceberg.apache.org/javadoc/1.4.3/org/apache/iceberg/RowLevelOperationMode.html)
> - [Use Apache Iceberg v3 features (AWS)](https://docs.databricks.com/aws/en/iceberg/iceberg-v3)
> - [Read Delta Lake tables with Iceberg clients (AWS)](https://docs.databricks.com/aws/en/delta/iceberg-reads)
