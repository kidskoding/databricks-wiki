---
type: chapter
status: written
part: 1
level: 5
section: The Lakehouse
summary: Warehouse reliability on lake storage, through Delta Lake, open table formats, and the medallion architecture.
prev: "[[The Two-Tier Architecture Problem]]"
next: "[[The Lakehouse Idea]]"
notes:
  - "[[The Lakehouse Idea]]"
  - "[[The Lakehouse Paper]]"
  - "[[ACID Transactions]]"
  - "[[Open Table Formats]]"
  - "[[Delta Lake]]"
  - "[[Delta Transaction Log]]"
  - "[[Time Travel]]"
  - "[[Schema Enforcement and Evolution]]"
  - "[[MERGE and Upserts]]"
  - "[[Apache Iceberg]]"
  - "[[Apache Hudi]]"
  - "[[Delta UniForm]]"
  - "[[Medallion Architecture]]"
  - "[[Liquid Clustering]]"
  - "[[Deletion Vectors]]"
  - "[[Change Data Feed]]"
  - "[[OPTIMIZE and VACUUM]]"
last_verified: 2026-10-25
tags:
  - chapter
---

# Chapter 05 - The Lakehouse

> [!story] Context
> [[Chapter 04 - The Modern Data Stack|Chapter 04]] ended with [[The Two-Tier Architecture Problem]]: companies ran a [[Data Lakes|data lake]] for raw files and machine learning and a [[Data Warehouses|data warehouse]] for BI, connected by copy jobs. This chapter covers the lakehouse, which combines both roles in one copy of data in open files on cloud object storage.

**Warehouse reliability on lake storage, through Delta Lake, open table formats, and the medallion architecture.**

## The story of this chapter

By the late 2010s, most organizations with significant data ran two systems. A data lake on [[Object Storage|object storage]] held raw files cheaply and served data science, but it had no transactions, no enforced schemas, and no safe way to update rows, so it tended to become a [[Data Swamps|data swamp]]. A data warehouse held curated tables with strong guarantees and fast SQL, but in proprietary storage at higher cost, and it served machine learning poorly. Nightly ETL jobs copied data from one to the other. The result was two copies, two sets of permissions, stale warehouse data, and figures that did not always match.

[[The Lakehouse Idea]] removes the second tier. Data stays as [[Apache Parquet]] files in the customer's own cloud storage, and a transactional metadata layer makes those files behave like warehouse tables. [[The Lakehouse Paper]], published at CIDR in January 2021 by Michael Armbrust, Ali Ghodsi, Reynold Xin, and Matei Zaharia, named the pattern and argued that it would replace the two-tier design.

The core mechanism is the open table format. [[ACID Transactions]] defines the guarantees a reliable table needs. [[Open Table Formats]] explains how a log of metadata stored next to the data files provides them. Three formats emerged in the late 2010s:

| Format | Origin | Role on Databricks |
|---|---|---|
| [[Delta Lake]] | Databricks; open-sourced 2019, hosted by the [[Linux Foundation]] | Default table format |
| [[Apache Iceberg]] | Netflix; Apache Software Foundation | Managed and foreign Iceberg tables in Unity Catalog, GA as of October 2026 |
| [[Apache Hudi]] | Uber; Apache Software Foundation | Not a Unity Catalog table type |

The Delta notes follow the format from the inside out. The [[Delta Transaction Log]] is the `_delta_log` folder of ordered JSON commits and Parquet checkpoints. [[Time Travel]] reads and restores earlier versions recorded in that log. [[Schema Enforcement and Evolution]] rejects mismatched writes and allows deliberate schema changes. [[MERGE and Upserts]] applies inserts, updates, and deletes in one transaction, which makes incremental pipelines possible on lake storage.

The formats then converge. Iceberg v3 adds deletion vectors, row lineage, and the `VARIANT` type, features Delta also supports. [[Delta UniForm]] generates Iceberg metadata for a Delta table so Iceberg clients can read it without a copy. After acquiring Tabular, the company founded by Iceberg's creators, in June 2024, Databricks stated format compatibility as a goal, and [[Unity Catalog]] now manages both formats side by side.

With reliable tables available, the [[Medallion Architecture]] organizes them into bronze (raw), silver (validated), and gold (business-ready) layers.

The last four notes cover performance and maintenance:

- [[Liquid Clustering]] replaces Hive-style partitioning and Z-ordering. `CLUSTER BY AUTO` lets Databricks choose clustering keys from the query workload.
- [[Deletion Vectors]] mark deleted rows instead of rewriting whole files, which makes `DELETE`, `UPDATE`, and `MERGE` cheaper.
- [[Change Data Feed]] exposes row-level changes to downstream consumers. Automatic change data feed, computed from row tracking, is GA as of September 2026.
- [[OPTIMIZE and VACUUM]] compact small files and delete unreferenced ones. Predictive optimization runs both, plus `ANALYZE`, automatically on Unity Catalog managed tables, and it is enabled by default for accounts created on or after November 11, 2024.

At the end of this chapter, the storage layer is reliable, open, and largely self-maintaining. A lakehouse still needs an operating environment: compute to run queries and pipelines, workspaces for users, identity and access control, and services that schedule maintenance. Assembling and operating those pieces from open-source components is a substantial engineering effort. [[Chapter 06 - The Databricks Platform]] covers Databricks, the managed platform that provides them.

## Notes in reading order

<!-- GENERATED:reading-order START (scripts/scaffold.py) -->

| # | Note | Depth | What it covers |
|---|---|---|---|
| 1 | [[The Lakehouse Idea]] | 101 Beginner | One copy of data in open files on cheap storage, with warehouse-grade reliability and speed. |
| 2 | [[The Lakehouse Paper]] | 301 Advanced | The 2021 CIDR paper that named and argued for the lakehouse. |
| 3 | [[ACID Transactions]] | 201 Practitioner | The four guarantees that stop half-written, conflicting, or lost data. |
| 4 | [[Open Table Formats]] | 201 Practitioner | A metadata layer over Parquet files that turns a folder into a real table. |
| 5 | [[Delta Lake]] | 101 Beginner | Databricks' open-source table format and the default for every table on the platform. |
| 6 | [[Delta Transaction Log]] | 301 Advanced | The _delta_log folder of JSON commits that makes Delta Lake transactional. |
| 7 | [[Time Travel]] | 201 Practitioner | Querying a table as it was yesterday, and undoing mistakes. |
| 8 | [[Schema Enforcement and Evolution]] | 201 Practitioner | Rejecting bad columns, and safely adding new ones. |
| 9 | [[MERGE and Upserts]] | 201 Practitioner | Insert-or-update in one statement, the workhorse of incremental pipelines. |
| 10 | [[Apache Iceberg]] | 201 Practitioner | The Netflix-born table format, Delta's main rival, now first-class in Unity Catalog. |
| 11 | [[Apache Hudi]] | 301 Advanced | The Uber-born table format focused on upserts and incremental processing. |
| 12 | [[Delta UniForm]] | 301 Advanced | Writing Delta tables that Iceberg readers can also read. |
| 13 | [[Medallion Architecture]] | 101 Beginner | Bronze (raw), silver (cleaned), and gold (business-ready) layers of tables. |
| 14 | [[Liquid Clustering]] | 301 Advanced | Self-organizing data layout that replaced partitioning and Z-ordering for most tables. |
| 15 | [[Deletion Vectors]] | 401 Expert | Marking rows deleted instead of rewriting whole files. |
| 16 | [[Change Data Feed]] | 301 Advanced | A row-level log of what changed in a Delta table, for downstream incremental processing. |
| 17 | [[OPTIMIZE and VACUUM]] | 301 Advanced | Compacting small files and deleting old ones, and Predictive Optimization doing it for you. |

<!-- GENERATED:reading-order END -->

> [!nextup] Next
> [[The Lakehouse Idea]]
