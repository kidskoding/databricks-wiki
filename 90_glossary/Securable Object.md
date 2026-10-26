---
type: glossary
status: written
level: 90
section: Glossary
depth: 101
summary: "Any object in Unity Catalog that privileges can be granted on, such as a catalog, schema, table, volume, or external location."
related:
  - "[[Unity Catalog]]"
  - "[[Privileges and Grants]]"
  - "[[Three-Level Namespace]]"
  - "[[Catalogs Schemas and Tables]]"
  - "[[Storage Credentials and External Locations]]"
  - "[[Metastore]]"
aliases:
  - "securable"
  - "securables"
  - "securable objects"
last_verified: 2026-10-26
tags:
  - glossary
  - flashcards
---

# Securable Object

> [!eli5] Summary
> A securable object is anything in Unity Catalog you can put a permission on. Tables, folders of files, and connections to other systems are all securables.

**In data work:** Access control systems need a list of the things that can be protected. In a database, those are usually databases, tables, and views. In a lakehouse, the list is longer, because governance also covers files, models, functions, and the credentials used to reach cloud storage and outside systems.

**In Databricks:** [[Unity Catalog]] securables form a hierarchy under the [[Metastore|metastore]].

| Level | Securables |
|---|---|
| Metastore | The top-level container for one region |
| Catalog | First level of the [[Three-Level Namespace\|three-level namespace]] |
| Schema | Second level |
| Inside a schema | Tables, views, materialized views, volumes, functions, registered models |
| Beside the hierarchy | Storage credentials, external locations, service credentials, connections, shares, recipients, providers, clean rooms |

Privileges granted on a parent are inherited by its children. Granting `SELECT` on a schema gives read access to every current and future table in it:

```sql
GRANT USE CATALOG ON CATALOG shop TO `analysts`;
GRANT USE SCHEMA, SELECT ON SCHEMA shop.sales TO `analysts`;
```

For a small team, granting at the catalog or schema level to groups keeps the number of grants small. See [[Privileges and Grants]].

Seen in: [[Unity Catalog]], [[Privileges and Grants]], [[Storage Credentials and External Locations]]

## Recall

Securable object::Any Unity Catalog object that privileges can be granted on, from the metastore down to tables, volumes, and functions.
Do privileges on a schema apply to tables created later?::Yes. Privileges are inherited by current and future child objects.

> [!sources]- Sources (last verified: 2026-10-26)
> - [Unity Catalog securable objects reference (AWS)](https://docs.databricks.com/aws/en/data-governance/unity-catalog/securable-objects)
> - [Unity Catalog securable objects reference (Azure Databricks)](https://learn.microsoft.com/en-us/azure/databricks/data-governance/unity-catalog/securable-objects)
> - [Unity Catalog privileges and securable objects (AWS)](https://docs.databricks.com/aws/en/data-governance/unity-catalog/manage-privileges/privileges)
