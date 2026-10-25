---
type: glossary
status: written
level: 90
section: Glossary
depth: 101
summary: "The kind of value a column can hold, such as integers, decimals, strings, dates, or nested structures."
related:
  - "[[Schema Enforcement and Evolution]]"
  - "[[Relational Databases]]"
  - "[[SQL]]"
  - "[[DataFrames]]"
  - "[[Structured vs Unstructured Data]]"
  - "[[CSV and JSON]]"
aliases:
  - "data types"
  - "type"
  - "column type"
  - "dtype"
last_verified: 2026-10-25
tags:
  - glossary
  - flashcards
---

# Data Type

> [!eli5] Summary
> A data type defines what kind of value a column may contain, such as whole numbers, text, or dates. It prevents invalid values, such as text in a price column.

**In data work:** Every column has a type. Common scalar types are `INT` and `BIGINT` (integers), `DECIMAL(p,s)` (exact numbers with precision `p` and scale `s`), `DOUBLE` (8-byte floating point), `STRING`, `BOOLEAN`, `DATE`, and `TIMESTAMP`. Complex types hold nested data: `ARRAY`, `MAP`, and `STRUCT`. The type determines valid operations and storage size. Use `DECIMAL` for currency, because floating-point types introduce rounding error; store dates as `DATE`, not as text.

**In Databricks:** Databricks SQL and [[Delta Lake]] support these types, including the complex types for semi-structured [[CSV and JSON|JSON]]. `DECIMAL` precision can be up to 38. `MAP` keys must be unique and non-null. [[Schema Enforcement and Evolution|Schema enforcement]] rejects writes with mismatched types. When loading files with [[Auto Loader]] or [[COPY INTO]], verify inferred types before building on the table. In [[DataFrames]], `df.printSchema()` lists column types.

Seen in: [[Schema Enforcement and Evolution]], [[Relational Databases]], [[SQL]], [[DataFrames]]

## Recall

Which data type should store currency amounts?::DECIMAL, because it stores exact values.
Name the three complex types in Databricks SQL.::ARRAY, MAP, and STRUCT.

> [!sources]- Sources (last verified: 2026-10-25)
> - [Data types (AWS)](https://docs.databricks.com/aws/en/sql/language-manual/sql-ref-datatypes)
> - [MAP type (AWS)](https://docs.databricks.com/aws/en/sql/language-manual/data-types/map-type)
