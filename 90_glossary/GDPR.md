---
type: glossary
status: written
level: 90
section: Glossary
depth: 101
summary: "The European Union regulation that governs how personal data of people in the EU and EEA is collected, processed, and erased."
related:
  - "[[Data Governance]]"
  - "[[Data Classification]]"
  - "[[Row Filters and Column Masks]]"
  - "[[OPTIMIZE and VACUUM]]"
  - "[[Deletion Vectors]]"
  - "[[Audit Logs]]"
aliases:
  - "General Data Protection Regulation"
  - "right to be forgotten"
  - "right to erasure"
last_verified: 2026-10-25
tags:
  - glossary
  - flashcards
---

# GDPR

> [!eli5] Summary
> GDPR is a European privacy law. It requires organizations to protect personal information, use it only for lawful purposes, and delete it when a person is entitled to ask.

**In data work:** The General Data Protection Regulation was adopted in 2016 and has been enforceable since 25 May 2018. It applies to personal data of people in the EU and EEA. Obligations include a lawful basis for processing, data minimization, security, breach notification, and individual rights such as access and erasure (the "right to be forgotten"). Personal data overlaps heavily with [[PII]].

**In Databricks:** Erasure in [[Delta Lake]] takes three steps. First, `DELETE` the rows from every affected table, including downstream tables, and from upstream sources such as Kafka and files. Second, for tables with [[Deletion Vectors]], run `REORG TABLE ... APPLY (PURGE)` to rewrite files that still contain soft-deleted rows. Third, run [[OPTIMIZE and VACUUM|VACUUM]] after the retention period (default 7 days) to remove old file versions kept for [[Time Travel]]. Predictive optimization runs `VACUUM` automatically on Unity Catalog managed tables. [[Data Classification]] tags personal data, and [[Row Filters and Column Masks]] and [[Audit Logs]] control and record access.

Seen in: [[Data Governance]], [[Data Classification]], [[OPTIMIZE and VACUUM]], [[Compliance Security Profile]]

## Recall

Since when has GDPR been enforceable?::25 May 2018.
Why is DELETE alone insufficient for GDPR erasure in Delta Lake?::Deleted rows remain in older files (and in deletion-vector files) until REORG PURGE and VACUUM remove them.

> [!sources]- Sources (last verified: 2026-10-25)
> - [Prepare your data for GDPR compliance (AWS)](https://docs.databricks.com/aws/en/security/privacy/gdpr-delta)
> - [Implementing the right to be forgotten in Delta Lake (Databricks blog)](https://www.databricks.com/blog/2022/03/23/implementing-the-gdpr-right-to-be-forgotten-in-delta-lake.html)
> - [Remove unused data files with vacuum (AWS)](https://docs.databricks.com/aws/en/delta/vacuum)
> - [Databricks GDPR compliance](https://www.databricks.com/trust/compliance/gdpr)
