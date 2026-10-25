---
type: glossary
status: written
level: 90
section: Glossary
depth: 101
summary: "Encoding data in fewer bytes to reduce storage and read time, at the cost of CPU work to compress and decompress."
related:
  - "[[Apache Parquet]]"
  - "[[Columnar Storage]]"
  - "[[Files and File Formats]]"
  - "[[CSV and JSON]]"
  - "[[OPTIMIZE and VACUUM]]"
  - "[[Delta Lake]]"
aliases:
  - "compressed"
  - "codec"
  - "Snappy"
  - "Zstandard"
  - "zstd"
  - "gzip"
last_verified: 2026-10-25
tags:
  - glossary
  - flashcards
---

# Compression

> [!eli5] Summary
> Compression stores the same data in less space. The data is unpacked automatically when it is read.

**In data work:** A compression codec encodes repeated patterns compactly. Common codecs include gzip, Snappy, and Zstandard (zstd), which trade compression ratio against speed. [[Columnar Storage|Columnar]] formats compress well because each column holds similar values. Smaller files reduce storage cost and the bytes a query must read. Example: an order export stored as [[Apache Parquet|Parquet]] is typically much smaller than the same data as [[CSV and JSON|CSV]].

**In Databricks:** [[Delta Lake]] tables store data as compressed Parquet files. New managed tables created on Databricks Runtime 16.0 and above use Zstandard by default instead of Snappy. Existing tables keep their codec; change it with the `delta.parquet.compression.codec` table property, and run `OPTIMIZE ... FULL` (Runtime 16.0 and above) to rewrite existing files with the new codec. File layout usually matters more than the codec: [[OPTIMIZE and VACUUM|OPTIMIZE]] compacts small files into larger ones.

Seen in: [[Apache Parquet]], [[Columnar Storage]], [[Files and File Formats]], [[Delta Lake]]

## Recall

Why do columnar formats compress well?::Each column stores similar values together, which encode compactly.
Which codec do new managed Delta tables use by default on Databricks Runtime 16.0 and above?::Zstandard (zstd).

> [!sources]- Sources (last verified: 2026-10-25)
> - [October 2025 release notes (AWS)](https://docs.databricks.com/aws/en/release-notes/product/2025/october)
> - [Read Delta tables with Iceberg clients using UniForm (Azure)](https://learn.microsoft.com/en-us/azure/databricks/delta/uniform)
> - [What is Parquet? (Databricks glossary)](https://databricks.com/glossary/what-is-parquet)
