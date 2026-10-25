---
type: glossary
status: written
level: 90
section: Glossary
depth: 101
summary: "Personally identifiable information: any data that can identify a specific person."
related:
  - "[[Data Classification]]"
  - "[[Row Filters and Column Masks]]"
  - "[[GDPR]]"
  - "[[HIPAA]]"
  - "[[Attribute-Based Access Control]]"
  - "[[Data Governance]]"
aliases:
  - "Personally Identifiable Information"
  - "personal data"
  - "sensitive data"
  - "PHI"
last_verified: 2026-10-25
tags:
  - glossary
  - flashcards
---

# PII

> [!eli5] Summary
> PII (personally identifiable information) is any data that can identify a specific person, such as a name, email address, or ID number. It requires stricter protection than other data.

**In data work:** PII covers direct identifiers (name, email, phone, government ID) and indirect ones that identify someone when combined (birth date plus ZIP code). Health data about a person is called PHI under [[HIPAA]], and EU law ([[GDPR]]) uses the broader term personal data. Handling PII well means collecting less, restricting who sees it, masking or hashing it in analytics, and being able to delete it on request. A dental clinic's appointment table holds PII, while a table of monthly visit counts by treatment type does not.

**In Databricks:** In Databricks, [[Data Classification]] scans Unity Catalog tables with AI and pattern matching and can apply system tags such as `class.email_address` to columns that look like PII. You then protect them with [[Row Filters and Column Masks]] or tag-driven [[Attribute-Based Access Control]], and audit access with [[Audit Logs]]. Deleting a person's rows from a Delta table also needs `VACUUM` to remove old files (see [[OPTIMIZE and VACUUM]]).

Seen in: [[Data Classification]], [[Row Filters and Column Masks]], [[GDPR]], [[Attribute-Based Access Control]]

## Recall

PII::Personally identifiable information, data that can identify a person (name, email, ID); protect it with masking, filters, and limited grants.

> [!sources]- Sources (last verified: 2026-10-25)
> - [Data Classification (Azure Databricks)](https://learn.microsoft.com/en-us/azure/databricks/data-governance/unity-catalog/data-classification)
> - [Find Sensitive Data at Scale with Data Classification (Databricks blog)](https://www.databricks.com/blog/find-sensitive-data-scale-data-classification-unity-catalog)
