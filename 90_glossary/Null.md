---
type: glossary
status: written
level: 90
section: Glossary
depth: 101
summary: "The empty value: Python's None and SQL's NULL mean the value is missing or unknown."
related:
  - "[[SQL]]"
  - "[[Python for Data]]"
  - "[[Data Quality]]"
  - "[[Expectations and Data Quality]]"
  - "[[Schema Enforcement and Evolution]]"
  - "[[Join]]"
aliases:
  - "Null"
  - "NULL"
  - "null value"
  - "missing value"
  - "NaN"
last_verified: 2026-10-25
tags:
  - glossary
  - flashcards
---

# Null

> [!eli5] Summary
> None (in Python) and NULL (in SQL) mark a value as missing or unknown. A missing value is different from zero or an empty string.

**In data work:** In Python, `None` is the value for nothing. In [[SQL]] the same idea is `NULL`, and in [[Pandas]] missing numbers often show up as `NaN`. NULL is not zero and not an empty string: a customer with a NULL phone number has an unknown number, while an empty string means someone typed nothing. NULL follows three-valued logic, so `NULL = NULL` is not true, and you must write `IS NULL`. Aggregates such as `AVG` skip NULLs, which can quietly change results. A salon whose old booking system left the tip field blank needs to decide whether blank means no tip (0) or unknown, before reporting average tips.

**In Databricks:** Spark and Databricks SQL use SQL NULL semantics; in PySpark, Python `None` becomes NULL in a DataFrame. Columns can be declared `NOT NULL` in a Delta table, and [[Expectations and Data Quality|pipeline expectations]] can drop or flag rows with missing values. NULL keys are a common surprise in [[Join|joins]], because rows with NULL keys never match. `COALESCE` and `IFNULL` replace NULLs with a default.

Seen in: [[SQL]], [[Expectations and Data Quality]], [[Data Quality]]

## Recall

None (NULL)::A marker for a missing or unknown value; it is not zero or empty text, and in SQL you test it with IS NULL, not = NULL.
