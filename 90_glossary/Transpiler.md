---
type: glossary
status: written
level: 90
section: Glossary
depth: 101
summary: "A tool that translates source code from one language or dialect into another at the same level, such as T-SQL into Databricks SQL."
related:
  - "[[Lakebridge]]"
  - "[[Migrating from SQL Server]]"
  - "[[Migrating ETL Tools]]"
  - "[[Migration Strategy Overview]]"
  - "[[SQL]]"
  - "[[Migrating from Snowflake]]"
aliases:
  - "source-to-source compiler"
  - "SQL transpiler"
  - "code converter"
  - "transpile"
last_verified: 2026-10-26
tags:
  - glossary
  - flashcards
---

# Transpiler

> [!eli5] Summary
> A transpiler rewrites code from one programming language into another. In a migration, it turns old SQL scripts into SQL the new platform understands.

**In data work:** A compiler turns source code into machine code; a transpiler turns source code into other source code. SQL is a common target, because every database speaks its own [[SQL]] dialect: T-SQL, PL/SQL, Teradata BTEQ, and Snowflake SQL differ in functions, data types, procedural syntax, and quirks. Rule-based transpilers parse the source into a syntax tree and apply translation rules. LLM-based converters use a language model to rewrite code by meaning. Neither converts everything: output still needs testing and review, and constructs without an equivalent are flagged for manual work.

**In Databricks:** [[Lakebridge]], a free Databricks Labs tool, includes three transpilers:

| Transpiler | Approach | Typical input |
|---|---|---|
| Morpheus | Rule-based, with a correctness focus | SQL files from dialects such as SQL Server, Synapse, and Snowflake |
| BladeBridge | Rule-based, many dialects | SQL and ETL code, such as Oracle and Teradata |
| Switch | LLM-based (experimental) | SQL, code, and other text files |

Lakebridge also profiles the source and reconciles results after migration. As a Databricks Labs project, it has no formal support SLA. For a small business moving a few dozen SQL Server stored procedures, a transpiler gives a fast first draft; plan time to test each converted object (see [[Migrating from SQL Server]]).

Seen in: [[Lakebridge]], [[Migration Strategy Overview]], [[Migrating ETL Tools]]

## Recall

Transpiler::A source-to-source translator, such as one that converts T-SQL into Databricks SQL.
Which three transpilers does Lakebridge include?::Morpheus, BladeBridge, and Switch.

> [!sources]- Sources (last verified: 2026-10-26)
> - [Introducing Lakebridge: Free, Open Data Migration to Databricks SQL (Databricks blog)](https://www.databricks.com/blog/introducing-lakebridge-free-open-data-migration-databricks-sql)
> - [Lakebridge documentation (Databricks Labs)](https://databrickslabs.github.io/lakebridge/)
> - [Databricks Lakebridge (product page)](https://www.databricks.com/solutions/migration/lakebridge)
