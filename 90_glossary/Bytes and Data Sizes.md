---
type: glossary
status: written
level: 90
section: Glossary
depth: 101
summary: "The units for measuring data volume, from kilobytes to petabytes."
related:
  - "[[What Is Data]]"
  - "[[The Three Vs of Big Data]]"
  - "[[Object Storage]]"
  - "[[Signs You Have Outgrown Spreadsheets]]"
  - "[[Estimating Costs for a Small Business]]"
  - "[[Columnar Storage]]"
aliases:
  - "KB"
  - "MB"
  - "GB"
  - "TB"
  - "PB"
  - "KiB"
  - "kilobyte"
  - "megabyte"
  - "gigabyte"
  - "terabyte"
  - "petabyte"
last_verified: 2026-10-25
tags:
  - glossary
  - flashcards
---

# Bytes and Data Sizes

> [!eli5] Summary
> Data is measured in bytes. One byte holds about one character of text, and larger units such as megabytes and gigabytes are multiples of it.

**In data work:** Each decimal unit is 1,000 times the previous one: kilobyte (KB), megabyte (MB), gigabyte (GB), terabyte (TB), petabyte (PB). Binary units use powers of 1,024: kibibyte (KiB), mebibyte (MiB), gibibyte (GiB), and so on. Tools differ in which convention they display. For scale, one sales record is typically a few hundred bytes, and a small business's complete sales history is often a few gigabytes. [[The Three Vs of Big Data|Big data]] refers to volumes that do not fit comfortably on one machine.

**In Databricks:** Data size drives two meters: [[Object Storage]] bills by data stored per month, and compute time grows with the bytes a query reads. Compressed, [[Columnar Storage|columnar]] formats such as [[Apache Parquet]] reduce both. The [[Spark UI]] and query profiles report the data each stage reads, shuffles, and [[Spill|spills]]; Databricks' Spark UI guide uses these values to identify skew, spill, and I/O-bound stages.

Seen in: [[The Three Vs of Big Data]], [[Signs You Have Outgrown Spreadsheets]], [[Estimating Costs for a Small Business]], [[Columnar Storage]]

## Recall

Order these units from smallest to largest: TB, KB, PB, GB, MB.::KB, MB, GB, TB, PB.
What is the difference between a KB and a KiB?::A KB is 1,000 bytes; a KiB is 1,024 bytes.

> [!sources]- Sources (last verified: 2026-10-25)
> - [Diagnose cost and performance issues using the Spark UI (AWS)](https://docs.databricks.com/aws/en/optimizations/spark-ui-guide/)
