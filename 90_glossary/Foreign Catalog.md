---
type: glossary
status: written
level: 90
section: Glossary
depth: 101
summary: "A Unity Catalog catalog that mirrors a database in an external system, such as PostgreSQL or SQL Server, so you can query it from Databricks without copying the data."
related:
  - "[[Lakehouse Federation]]"
  - "[[Catalogs Schemas and Tables]]"
  - "[[Unity Catalog]]"
  - "[[Securable Object]]"
  - "[[Hive Metastore Federation for AWS Glue]]"
  - "[[Migrating from Postgres and MySQL]]"
aliases:
  - "CREATE FOREIGN CATALOG"
  - "Federated catalog"
last_verified: 2026-10-26
tags:
  - glossary
  - flashcards
---

# Foreign Catalog

> [!eli5] Summary
> A foreign catalog is a window into another company database. Its tables appear in Databricks next to your own, but the data stays in the original system.

**In data work:** Query federation lets one engine read tables that live in another database. The external database's schemas and tables are exposed under a local name, and queries against them are pushed down to the source where possible.

**In Databricks:** In [[Lakehouse Federation]], you first create a **connection** (a [[Securable Object|securable]] that stores the host and credentials, ideally from [[Secrets Management|secrets]]), then a foreign catalog that uses it:

```sql
CREATE CONNECTION pg_shop TYPE postgresql
  OPTIONS (host 'db.example.com', port '5432',
           user secret('shop', 'pg_user'), password secret('shop', 'pg_pw'));

CREATE FOREIGN CATALOG shop_pg USING CONNECTION pg_shop
  OPTIONS (database 'shop');
```

Creating the catalog requires `CREATE CATALOG` on the metastore and ownership of, or `CREATE FOREIGN CATALOG` on, the connection. Foreign catalogs are read-only, except when catalog federation is used for a legacy Hive metastore. Unity Catalog permissions and lineage apply to them like any other catalog. Some sources use a different option, for example `service_name` for Oracle.

Small-business example: an accountant joins live invoices in the shop's PostgreSQL database with Delta tables of ad spend, without building an ingestion pipeline first.

Seen in: [[Lakehouse Federation]], [[Catalogs Schemas and Tables]], [[Migrating from Postgres and MySQL]]

## Recall

Which object must exist before you can create a foreign catalog?::A Unity Catalog connection.
Can you write to a foreign catalog from a federated database such as PostgreSQL?::No. Foreign catalogs are read-only, except for Hive metastore catalog federation.

> [!sources]- Sources (last verified: 2026-10-26)
> - [Federated queries (Lakehouse Federation) (AWS)](https://docs.databricks.com/aws/en/sql/language-manual/sql-ref-federated-queries)
> - [Run federated queries on PostgreSQL (AWS)](https://docs.databricks.com/aws/en/query-federation/postgresql)
> - [Manage connections for Lakehouse Federation (Azure)](https://learn.microsoft.com/en-us/azure/databricks/query-federation/connections)
