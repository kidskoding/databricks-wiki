---
type: glossary
status: written
level: 90
section: Glossary
depth: 101
summary: "Serializer/deserializer: the Hive component that tells an engine how to turn file bytes into table rows and back."
related:
  - "[[Apache Hive]]"
  - "[[Hive Metastore]]"
  - "[[Serialization]]"
  - "[[Files and File Formats]]"
  - "[[Hive Metastore Migration to Unity Catalog]]"
  - "[[CSV and JSON]]"
aliases:
  - "Hive SerDe"
  - "serializer/deserializer"
  - "ROW FORMAT SERDE"
last_verified: 2026-10-26
tags:
  - glossary
  - flashcards
---

# SerDe

> [!eli5] Summary
> A SerDe is a translator between stored files and table rows. It reads raw bytes into columns, and writes columns back out as bytes.

**In data work:** [[Apache Hive]] separated a table's definition from its files. Each Hive table names an input format (how to split files into records), an output format, and a SerDe class that deserializes each record into columns on read and serializes columns into a record on write. Hive shipped SerDes for delimited text, regular expressions, JSON, Avro, and others, and teams wrote custom SerDes for unusual log formats. This flexibility is what let Hive put tables over arbitrary files ([[Schema-on-Read|schema-on-read]]).

**In Databricks:** Hive-format tables are legacy, but you still meet SerDes when migrating from Hadoop.
- `CREATE TABLE ... ROW FORMAT SERDE '<class>'` defines a Hive-format table with a SerDe. It works only with `TEXTFILE`, `SEQUENCEFILE`, and `RCFILE` storage; `ROW FORMAT DELIMITED` works only with `TEXTFILE`.
- `CREATE TABLE ... USING HIVE OPTIONS (serde '<class>', ...)` is the equivalent with `USING`.
- A custom SerDe JAR must be installed on the compute.

When migrating, convert SerDe-based tables to Delta: read them once with their SerDe and write the result as a Delta table, so the format and schema live in the table instead of in a Java class. See [[Hive Metastore Migration to Unity Catalog]] and [[Migrating from Hadoop]].

Seen in: [[Apache Hive]], [[Hive Metastore]], [[Migrating from Hadoop]]

## Recall

SerDe::Serializer/deserializer: the Hive class that converts between file records and table columns.
Which storage formats support ROW FORMAT SERDE in Databricks?::TEXTFILE, SEQUENCEFILE, and RCFILE.

> [!sources]- Sources (last verified: 2026-10-26)
> - [CREATE TABLE with Hive format (AWS)](https://docs.databricks.com/aws/en/sql/language-manual/sql-ref-syntax-ddl-create-table-hiveformat)
> - [CREATE TABLE with Hive format (Azure Databricks)](https://learn.microsoft.com/en-us/azure/databricks/sql/language-manual/sql-ref-syntax-ddl-create-table-hiveformat)
> - [CREATE TABLE [USING] (AWS)](https://docs.databricks.com/aws/en/sql/language-manual/sql-ref-syntax-ddl-create-table-using)
> - [Apache Hive LanguageManual DDL](https://hive.apache.org/docs/latest/language/languagemanual-ddl/)
