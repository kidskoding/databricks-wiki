---
type: glossary
status: written
level: 90
section: Glossary
depth: 101
summary: "A data lake stores raw data of any type in cheap storage; a data swamp is a data lake that has become unusable for lack of organization and governance."
related:
  - "[[Data Lakes]]"
  - "[[Data Swamps]]"
  - "[[Object Storage]]"
  - "[[Unity Catalog]]"
  - "[[Medallion Architecture]]"
  - "[[The Lakehouse Idea]]"
aliases:
  - "data swamp"
  - "swamp"
last_verified: 2026-10-25
tags:
  - glossary
  - flashcards
---

# Data Lake vs Data Swamp

> [!eli5] Summary
> A data lake is a large store for all of a company's raw data. It becomes a data swamp when nobody keeps track of what is stored, who owns it, or whether it is correct.

**In data work:** A [[Data Lakes|data lake]] stores files of any format (CSV, JSON, Parquet, images, logs) in [[Object Storage]] without enforcing structure on write. A [[Data Swamps|data swamp]] is the result of missing rules: duplicate copies, unknown owners, partial writes, undocumented folders, and no way to identify the current version.

**In Databricks:** The lakehouse keeps the lake's open storage and adds governance. [[Delta Lake]] adds [[ACID Transactions|transactions]] and [[Schema Enforcement and Evolution|schema enforcement]] so partial or malformed writes do not land. [[Unity Catalog]] adds a catalog, ownership, permissions, and [[Data Lineage|lineage]]. The [[Medallion Architecture]] defines the path from raw bronze data to curated gold tables. See [[The Lakehouse Idea]].

Seen in: [[Data Lakes]], [[Data Swamps]], [[The Two-Tier Architecture Problem]], [[The Lakehouse Idea]]

## Recall

What turns a data lake into a data swamp?::Missing ownership, documentation, quality controls, and organization.
Which two Databricks components address the data swamp problem most directly?::Delta Lake for reliable tables and Unity Catalog for cataloging and governance.
