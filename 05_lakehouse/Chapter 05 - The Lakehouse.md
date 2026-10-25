---
type: chapter
status: stub
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
last_verified:
tags:
  - chapter
---

# Chapter 05 - The Lakehouse

> [!story] Previously
> (to write)

**Warehouse reliability on lake storage, through Delta Lake, open table formats, and the medallion architecture.**

## The story of this chapter

(to write)

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

> [!nextup] Up next
> [[The Lakehouse Idea]]
