---
type: glossary
status: written
level: 90
section: Glossary
depth: 101
summary: "A subset of a data warehouse modeled for one business area, such as sales or finance."
related:
  - "[[Data Warehouses]]"
  - "[[Star Schema]]"
  - "[[Medallion Architecture]]"
  - "[[Catalogs Schemas and Tables]]"
  - "[[Metric Views]]"
  - "[[Data Modeling Basics]]"
aliases:
  - "data marts"
  - "departmental mart"
last_verified: 2026-10-25
tags:
  - glossary
  - flashcards
---

# Data Mart

> [!eli5] Summary
> A data mart is a smaller collection of tables prepared for one department, so that team finds its data quickly.

**In data work:** A data mart contains the [[Star Schema|star schemas]] for one subject area: for example, a sales mart with order [[Fact Table|facts]] and customer and product [[Dimension Table|dimensions]]. Marts use the department's terminology and are permissioned to that team. They are usually derived from the same cleaned data as the rest of the [[Data Warehouses|warehouse]].

**In Databricks:** Data marts typically sit in the gold layer of the [[Medallion Architecture]], often as a schema or catalog per department in [[Unity Catalog]] (for example `gold.sales`), with [[Privileges and Grants|grants]] to the matching group. [[Materialized Views]] and [[Metric Views]] are common building blocks. Because marts are tables or views over the same Delta data, they do not require copying data into a separate system ([[The Two-Tier Architecture Problem]]).

Seen in: [[Data Warehouses]], [[Star Schema]], [[Medallion Architecture]], [[Data Modeling Basics]]

## Recall

What is a data mart?::A subset of the warehouse modeled for one business area.
Where do data marts usually sit in the medallion architecture?::In the gold layer.
