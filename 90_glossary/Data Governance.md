---
type: glossary
status: written
level: 90
section: Glossary
depth: 101
summary: "The policies and controls that determine who can use which data, how it is protected, and whether it can be trusted."
related:
  - "[[Unity Catalog]]"
  - "[[Privileges and Grants]]"
  - "[[Data Lineage]]"
  - "[[Audit Logs]]"
  - "[[Data Classification]]"
  - "[[Row Filters and Column Masks]]"
aliases:
  - "governance"
  - "data stewardship"
last_verified: 2026-10-25
tags:
  - glossary
  - flashcards
---

# Data Governance

> [!eli5] Summary
> Data governance is the set of rules for a company's data: who can see or change it, how sensitive data is protected, and how use is recorded.

**In data work:** Governance covers access control, privacy (protecting [[PII]] and meeting laws such as [[GDPR]] and [[HIPAA]]), data quality, discovery, and auditing. It combines written policy with technical enforcement. Example: in a dental practice, front-desk staff see appointments, only clinicians see treatment notes, and every access to patient records is logged.

**In Databricks:** [[Unity Catalog]] provides governance across all workspaces in an account: [[Privileges and Grants|grants]] on catalogs, schemas, tables, and models; [[Row Filters and Column Masks]]; [[Attribute-Based Access Control|tag-based policies]]; automatic [[Data Lineage]]; [[Data Classification]] of sensitive columns; and [[Audit Logs]] and [[System Tables]] that record activity.

Seen in: [[Unity Catalog]], [[Privileges and Grants]], [[Data Lineage]], [[Audit Logs]], [[Chapter 07 - Unity Catalog and Governance]]

## Recall

Name four areas covered by data governance.::Access control, privacy, data quality, and auditing (also discovery).
Which Databricks layer provides governance across workspaces?::Unity Catalog.

> [!sources]- Sources (last verified: 2026-10-25)
> - [What is Unity Catalog? (AWS)](https://docs.databricks.com/aws/en/data-governance/unity-catalog/)
