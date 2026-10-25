---
type: glossary
status: written
level: 90
section: Glossary
depth: 101
summary: "Moving a system to a new platform as-is, without redesigning it."
related:
  - "[[Migration Strategy Overview]]"
  - "[[Migration Checklist]]"
  - "[[Running Old and New in Parallel]]"
  - "[[Lakebridge]]"
  - "[[Cutover]]"
aliases:
  - "rehost"
  - "rehosting"
  - "lift-and-shift migration"
last_verified: 2026-10-25
tags:
  - glossary
  - flashcards
---

# Lift and Shift

> [!eli5] Summary
> Lift and shift is moving a system to a new platform without redesigning it. It is fast to plan, but it keeps the old design's problems.

**In data work:** A lift-and-shift migration copies existing code, tables, and jobs onto a new platform with as few changes as possible. It is fast and low-risk to plan, but it carries old problems along, and it rarely uses the new platform's strengths. The alternative is re-architecting: rewriting pipelines to fit the new system. Many teams do both in stages: lift and shift first to switch off the old system, then improve. A shop moving nightly SQL Server stored procedures to the cloud might run them almost unchanged at first, then rebuild the slowest ones properly.

**In Databricks:** [[Migration Strategy Overview]] compares lift and shift with redesigning for the lakehouse. [[Lakebridge]] helps with the lift-and-shift part by assessing and converting SQL from other warehouses into Databricks SQL. Whichever approach you choose, [[Running Old and New in Parallel]] and a planned [[Cutover|cutover]] keep the business safe while you compare results.

Seen in: [[Migration Strategy Overview]], [[Lakebridge]], [[Migrating from SQL Server]]

## Recall

Lift and Shift::Moving a system to a new platform as-is, with minimal changes; quick, but it carries old design problems along.

> [!sources]- Sources (last verified: 2026-10-25)
> - [Introducing Lakebridge (Databricks blog)](https://www.databricks.com/blog/introducing-lakebridge-free-open-data-migration-databricks-sql)
> - [Databricks Lakebridge](https://www.databricks.com/solutions/migration/lakebridge)
