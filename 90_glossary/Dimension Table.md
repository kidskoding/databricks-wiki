---
type: glossary
status: written
level: 90
section: Glossary
depth: 101
summary: "A table of descriptive attributes, such as customer, product, or date, that fact tables reference by key."
related:
  - "[[Star Schema]]"
  - "[[Slowly Changing Dimensions]]"
  - "[[Fact Table]]"
  - "[[Primary and Foreign Keys]]"
  - "[[Metric Views]]"
  - "[[Change Data Capture]]"
aliases:
  - "dimension"
  - "dimensions"
  - "dim table"
last_verified: 2026-10-25
tags:
  - glossary
  - flashcards
---

# Dimension Table

> [!eli5] Summary
> A dimension table describes the things a business records events about, such as customers, products, and stores. Reports use it to label and group the numbers.

**In data work:** In a [[Star Schema|star schema]], dimension tables (`dim_customer`, `dim_product`, `dim_store`, `dim_date`) hold the attributes used to filter and group, such as category, city, or month. Each row has a key that [[Fact Table|fact tables]] reference. Dimensions are usually much smaller than facts. How attribute changes are handled, by overwriting or by keeping history, is defined by the [[Slowly Changing Dimensions|slowly changing dimension]] type.

**In Databricks:** Dimensions are [[Delta Lake]] tables, usually in the gold layer. In [[Lakeflow Spark Declarative Pipelines]], `AUTO CDC` maintains SCD Type 1 (`STORED AS SCD TYPE 1`, the default) or Type 2 (`STORED AS SCD TYPE 2`, which adds `__START_AT` and `__END_AT` columns) from a change feed ([[Change Data Capture]]). [[Primary and Foreign Keys|Primary and foreign key]] constraints on Unity Catalog tables are informational: they document relationships but are not enforced. [[Metric Views]] use dimensions as the fields that metrics are grouped by.

Seen in: [[Star Schema]], [[Slowly Changing Dimensions]], [[Data Modeling Basics]], [[Change Data Capture]]

## Recall

What does a dimension table contain?::Descriptive attributes that fact rows reference by key.
Does Databricks enforce primary key constraints on Unity Catalog tables?::No. Primary and foreign keys are informational only.

> [!sources]- Sources (last verified: 2026-10-25)
> - [AUTO CDC INTO (pipelines) (AWS)](https://docs.databricks.com/aws/en/ldp/developer/ldp-sql-ref-apply-changes-into)
> - [Constraints on Databricks (AWS)](https://docs.databricks.com/aws/en/tables/constraints)
