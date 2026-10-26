---
type: glossary
status: written
level: 90
section: Glossary
depth: 101
summary: "Applying a schema when data is read rather than when it is written, so raw files can land first and be interpreted later."
related:
  - "[[Schema Enforcement and Evolution]]"
  - "[[Data Lakes]]"
  - "[[Schema]]"
  - "[[Apache Hive]]"
  - "[[Auto Loader]]"
  - "[[Data Swamps]]"
aliases:
  - "schema on read"
  - "schema-on-write"
  - "schema on write"
last_verified: 2026-10-26
tags:
  - glossary
  - flashcards
---

# Schema-on-Read

> [!eli5] Summary
> Schema-on-read means you store data as it arrives and decide its structure only when you query it. Schema-on-write means you check the structure before the data is saved.

**In data work:**

| Approach | When structure is checked | Typical system | Trade-off |
|---|---|---|---|
| Schema-on-write | At load time | Relational databases, [[Data Warehouses\|data warehouses]] | Bad data is rejected early, but every source needs a model before loading |
| Schema-on-read | At query time | [[Data Lakes\|Data lakes]], [[Apache Hive]] on HDFS | Anything can land quickly, but errors surface late, in every query |

Schema-on-read made Hadoop-era data lakes easy to fill, because files were copied in and a Hive table definition was laid over them. Without checks, the same flexibility produced [[Data Swamps|data swamps]]: columns that changed meaning, malformed rows, and queries that failed months later.

**In Databricks:** The lakehouse combines both.
- **Bronze (raw):** [[Auto Loader]] infers a schema from incoming files and stores values that do not match it in a `_rescued_data` column instead of dropping them. Nested JSON can land as [[VARIANT Data Type|VARIANT]].
- **Silver and gold:** Delta tables enforce their schema on write ([[Schema Enforcement and Evolution|schema enforcement]]) and change it only through explicit schema evolution.

A small business loading CSV exports from a point-of-sale system can land them raw first, then enforce a clean schema in the next layer (see [[Medallion Architecture]]).

Seen in: [[Data Lakes]], [[Schema Enforcement and Evolution]], [[Apache Hive]]

## Recall

Schema-on-read::Applying structure to data at query time instead of when it is written.
Where does Auto Loader put values that do not match the inferred schema?::The _rescued_data column.

> [!sources]- Sources (last verified: 2026-10-26)
> - [Schema enforcement (AWS)](https://docs.databricks.com/aws/en/tables/schema-enforcement)
> - [Configure schema inference and evolution in Auto Loader (AWS)](https://docs.databricks.com/aws/en/ingestion/cloud-object-storage/auto-loader/schema)
> - [Lakehouse: A New Generation of Open Platforms (CIDR 2021)](https://vldb.org/cidrdb/2021/lakehouse-a-new-generation-of-open-platforms-that-unify-data-warehousing-and-advanced-analytics.html)
