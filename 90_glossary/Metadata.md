---
type: glossary
status: written
level: 90
section: Glossary
depth: 101
summary: "Data about data: names, types, owners, sizes, locations, and history of your tables and files."
related:
  - "[[Unity Catalog]]"
  - "[[Metastore]]"
  - "[[Data Catalog]]"
  - "[[Delta Transaction Log]]"
  - "[[Data Lineage]]"
  - "[[System Tables]]"
aliases:
  - "data about data"
  - "technical metadata"
  - "business metadata"
last_verified: 2026-10-25
tags:
  - glossary
  - flashcards
---

# Metadata

> [!eli5] Summary
> Metadata is information that describes data, such as a table's name, columns, owner, size, and change history. It makes data findable and governable.

**In data work:** Metadata describes data rather than being the data. Technical metadata covers table names, column names and [[Data Type|types]], file locations, sizes, and row counts. Business metadata covers owners, descriptions, and sensitivity tags. Operational metadata records who changed what and when. A spreadsheet's column headers are a simple form of metadata; a [[Data Catalog|data catalog]] is a searchable store of it. A clinic might tag columns holding patient names as sensitive so tools can hide them automatically.

**In Databricks:** [[Unity Catalog]] is Databricks' metadata layer: its [[Metastore|metastore]] records every catalog, schema, table, volume, and model, plus owners, comments, and tags. Each [[Delta Lake]] table also keeps metadata in its [[Delta Transaction Log|transaction log]], such as the schema and file-level statistics used for [[Data Skipping|data skipping]]. You can query metadata with `information_schema` and [[System Tables]], and follow it across tables with [[Data Lineage]].

Seen in: [[Unity Catalog]], [[Metastore]], [[Delta Transaction Log]], [[System Tables]]

## Recall

Metadata::Data about data, such as names, types, owners, locations, and change history; in Databricks it lives mainly in Unity Catalog and the Delta log.
