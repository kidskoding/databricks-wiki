---
type: glossary
status: written
level: 90
section: Glossary
depth: 101
summary: "Using or sharing data where it already sits, without making a physical duplicate."
related:
  - "[[OpenSharing]]"
  - "[[Lakehouse Federation]]"
  - "[[Delta UniForm]]"
  - "[[Clean Rooms]]"
  - "[[Single Source of Truth]]"
  - "[[Storage vs Compute]]"
aliases:
  - "zero copy"
  - "zero-copy sharing"
  - "zero-copy clone"
  - "no-copy"
last_verified: 2026-10-25
tags:
  - glossary
  - flashcards
---

# Zero-Copy

> [!eli5] Summary
> Zero-copy means using or sharing data where it already is, without making a duplicate. It avoids extra storage and copies that drift out of date.

**In data work:** Copying data costs storage, time, and trust: every copy can drift from the source and must be secured separately. Zero-copy approaches avoid the duplicate by pointing at existing files, sharing access instead of exporting, or cloning only metadata. Examples include shallow clones that reference the original files, cross-engine reads of one open-format table, and query federation that reads a remote database in place. A franchise owner might give the head office direct read access to a sales table instead of emailing a nightly CSV.

**In Databricks:** Databricks offers several zero-copy patterns. [[OpenSharing]] (formerly Delta Sharing) grants another organization live read access to tables without exporting them. Shallow `CLONE` creates a table that references the source's files. [[Lakehouse Federation]] queries external databases in place, and [[Delta UniForm]] lets Iceberg readers use Delta tables without conversion. [[Clean Rooms]] let partners compute on data without seeing each other's raw rows.

Seen in: [[OpenSharing]], [[Lakehouse Federation]], [[Delta UniForm]], [[Clean Rooms]]

## Recall

Zero-Copy::Using or sharing data in place rather than duplicating it, as with OpenSharing, shallow clones, and Lakehouse Federation.

> [!sources]- Sources (last verified: 2026-10-25)
> - [CREATE TABLE CLONE (AWS)](https://docs.databricks.com/aws/en/sql/language-manual/delta-clone)
> - [Shallow clone for Unity Catalog tables (Azure Databricks)](https://learn.microsoft.com/en-us/azure/databricks/delta/clone-unity-catalog)
> - [Delta Sharing / OpenSharing product page](https://www.databricks.com/product/delta-sharing)
