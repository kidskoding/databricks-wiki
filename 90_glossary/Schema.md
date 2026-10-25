---
type: glossary
status: written
level: 90
section: Glossary
depth: 101
summary: "The structure of data (column names and types), and in Databricks also a folder-like container of tables."
related:
  - "[[Catalogs Schemas and Tables]]"
  - "[[Three-Level Namespace]]"
  - "[[Schema Enforcement and Evolution]]"
  - "[[Data Type]]"
  - "[[Relational Databases]]"
  - "[[Metadata]]"
aliases:
  - "schemas"
  - "table schema"
  - "database (schema)"
  - "data structure"
last_verified: 2026-10-25
tags:
  - glossary
  - flashcards
---

# Schema

> [!eli5] Summary
> A schema is the structure of data: the columns and the type of each one. In Databricks, a schema is also a container that groups related tables.

**In data work:** Schema has two common meanings. First, a table's schema is its blueprint: column names, [[Data Type|data types]], and whether values may be empty. Schema-on-write systems (classic warehouses) check data against the schema when it is saved; schema-on-read systems (raw data lakes) apply it only when reading, which is flexible but lets bad data in. Second, in many databases a schema is a named group of tables inside a database, such as `sales.orders` and `sales.customers`. A flower shop's orders table schema might be `order_id BIGINT, order_date DATE, total DECIMAL(10,2)`.

**In Databricks:** Databricks uses both meanings. In [[Unity Catalog]]'s [[Three-Level Namespace]] `catalog.schema.table`, a schema (also called a database) groups tables, views, volumes, and models (see [[Catalogs Schemas and Tables]]). Each Delta table also has a schema that Delta enforces on write and can evolve when you allow it (see [[Schema Enforcement and Evolution]]).

Seen in: [[Catalogs Schemas and Tables]], [[Three-Level Namespace]], [[Schema Enforcement and Evolution]]

## Recall

Schema::A table's structure (columns and types), and in Unity Catalog also the middle level of catalog.schema.table that groups tables.
