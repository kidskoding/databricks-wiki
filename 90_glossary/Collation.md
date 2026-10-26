---
type: glossary
status: written
level: 90
section: Glossary
depth: 101
summary: "The rules a database uses to compare and sort text, such as whether uppercase and lowercase letters, or accented and plain letters, count as equal."
related:
  - "[[Data Type]]"
  - "[[SQL]]"
  - "[[Databricks SQL]]"
  - "[[Migrating from SQL Server]]"
  - "[[Index]]"
aliases:
  - "Collations"
  - "UTF8_BINARY"
  - "UTF8_LCASE"
  - "UNICODE_CI"
last_verified: 2026-10-26
tags:
  - glossary
  - flashcards
---

# Collation

> [!eli5] Summary
> A collation decides whether two pieces of text count as the same and what order they sort in. For example, it decides whether 'Smith' and 'smith' match.

**In data work:** A collation defines string comparison and ordering. A binary collation compares raw bytes, so `'A' <> 'a'`. A case-insensitive collation treats them as equal, and an accent-insensitive one also treats `'resume'` and `'résumé'` as equal. Locale-aware collations sort in the order a language expects. Collation affects `=`, `ORDER BY`, `GROUP BY`, `DISTINCT`, and joins on text keys.

**In Databricks:** Databricks SQL supports collations from Databricks Runtime 16.1. The default is `UTF8_BINARY`. `UTF8_LCASE` lowercases and then compares bytes; it is fast and supports `LIKE` and `RLIKE`, but keeps accents distinct. `UNICODE_CI` and `UNICODE_CI_AI` use ICU locale rules for case-insensitive and case- and accent-insensitive comparison; many pattern-matching functions support only `UTF8_BINARY` and `UTF8_LCASE`. Column-level collation on [[Delta Lake|Delta]] tables requires Runtime 16.4 LTS or above.

```sql
CREATE TABLE customers (email STRING COLLATE UTF8_LCASE);
SELECT * FROM customers WHERE email = 'Ana@Example.com';  -- matches ana@example.com
```

Small-business example: a company moving from [[Migrating from SQL Server|SQL Server]], where its database compared text case-insensitively, sets `UTF8_LCASE` on customer email columns so lookups behave the same after migration.

Seen in: [[Databricks SQL]], [[Migrating from SQL Server]]

## Recall

What is the default collation in Databricks SQL?::UTF8_BINARY.
Which Databricks collation is case-insensitive and supports LIKE?::UTF8_LCASE.

> [!sources]- Sources (last verified: 2026-10-26)
> - [Collation (AWS)](https://docs.databricks.com/aws/en/sql/language-manual/sql-ref-collation)
> - [Collation support for Delta Lake (Azure)](https://learn.microsoft.com/en-us/azure/databricks/tables/features/collation)
