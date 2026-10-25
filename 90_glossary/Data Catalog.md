---
type: glossary
status: written
level: 90
section: Glossary
depth: 101
summary: "A searchable inventory of an organization's datasets with their descriptions, owners, lineage, and access rules."
related:
  - "[[Unity Catalog]]"
  - "[[Catalogs Schemas and Tables]]"
  - "[[Hive Metastore]]"
  - "[[Data Lineage]]"
  - "[[Data Classification]]"
  - "[[Three-Level Namespace]]"
aliases:
  - "catalog"
  - "metadata catalog"
  - "data dictionary"
last_verified: 2026-10-25
tags:
  - glossary
  - flashcards
---

# Data Catalog

> [!eli5] Summary
> A data catalog is an index of all the data a company has. It shows what each dataset contains, who owns it, and who may use it.

**In data work:** A data catalog stores [[Metadata|metadata]] about datasets: names, columns, descriptions, owners, tags, [[Data Lineage|lineage]], and permissions. It lets people find the right dataset and judge whether to trust it. Without a catalog, teams create duplicate and conflicting copies of the same data, which turns a lake into a [[Data Lake vs Data Swamp|swamp]].

**In Databricks:** [[Unity Catalog]] is the Databricks catalog. It registers tables, views, [[Volumes|volumes]], functions, and models in a [[Three-Level Namespace]] (`catalog.schema.table`) with comments, tags, owners, and permissions. **Catalog Explorer** is the UI for browsing them; it requires at least the `BROWSE` privilege and no running compute. In Unity Catalog, "catalog" also names the top level of the namespace ([[Catalogs Schemas and Tables]]). Unity Catalog replaces the per-workspace [[Hive Metastore]].

Seen in: [[Unity Catalog]], [[Catalogs Schemas and Tables]], [[Hive Metastore]], [[Data Lineage]]

## Recall

What does a data catalog store?::Metadata about datasets: names, columns, descriptions, owners, tags, lineage, and permissions.
Which privilege is required to view an object in Catalog Explorer?::BROWSE.

> [!sources]- Sources (last verified: 2026-10-25)
> - [What is Catalog Explorer? (AWS)](https://docs.databricks.com/aws/en/catalog-explorer)
> - [What is Unity Catalog? (AWS)](https://docs.databricks.com/aws/en/data-governance/unity-catalog/)
