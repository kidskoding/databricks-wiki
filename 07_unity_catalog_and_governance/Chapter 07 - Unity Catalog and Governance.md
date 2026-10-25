---
type: chapter
status: stub
part: 1
level: 7
section: Unity Catalog & Governance
summary: One place to find, secure, track, and share every data and AI asset.
prev: "[[Libraries and Environments]]"
next: "[[Unity Catalog]]"
notes:
  - "[[Unity Catalog]]"
  - "[[Metastore]]"
  - "[[Three-Level Namespace]]"
  - "[[Catalogs Schemas and Tables]]"
  - "[[Managed vs External Tables]]"
  - "[[Volumes]]"
  - "[[Storage Credentials and External Locations]]"
  - "[[Privileges and Grants]]"
  - "[[Row Filters and Column Masks]]"
  - "[[Attribute-Based Access Control]]"
  - "[[Data Lineage]]"
  - "[[Audit Logs]]"
  - "[[System Tables]]"
  - "[[Lakehouse Federation]]"
  - "[[OpenSharing]]"
  - "[[Clean Rooms]]"
  - "[[Databricks Marketplace]]"
  - "[[Data Classification]]"
  - "[[Hive Metastore Migration to Unity Catalog]]"
last_verified:
tags:
  - chapter
---

# Chapter 07 - Unity Catalog and Governance

> [!story] Previously
> (to write)

**One place to find, secure, track, and share every data and AI asset.**

## The story of this chapter

(to write)

## Notes in reading order

<!-- GENERATED:reading-order START (scripts/scaffold.py) -->

| # | Note | Depth | What it covers |
|---|---|---|---|
| 1 | [[Unity Catalog]] | 101 Beginner | Databricks' governance layer for permissions, discovery, lineage, and auditing across every workspace. |
| 2 | [[Metastore]] | 201 Practitioner | The top-level Unity Catalog container, one per region. |
| 3 | [[Three-Level Namespace]] | 101 Beginner | catalog.schema.table, the address of everything. |
| 4 | [[Catalogs Schemas and Tables]] | 101 Beginner | The securable objects in Unity Catalog and how to organize them. |
| 5 | [[Managed vs External Tables]] | 201 Practitioner | Who owns the files, and what happens when you drop a table. |
| 6 | [[Volumes]] | 201 Practitioner | Governed folders for non-table files like CSVs, images, and PDFs. |
| 7 | [[Storage Credentials and External Locations]] | 301 Advanced | How Unity Catalog is allowed to reach your cloud storage. |
| 8 | [[Privileges and Grants]] | 201 Practitioner | GRANT and REVOKE, privilege inheritance, and ownership. |
| 9 | [[Row Filters and Column Masks]] | 301 Advanced | Showing each person only the rows and values they are allowed to see. |
| 10 | [[Attribute-Based Access Control]] | 301 Advanced | Policies driven by tags instead of per-table grants. |
| 11 | [[Data Lineage]] | 201 Practitioner | An automatic map of where every column came from and where it goes. |
| 12 | [[Audit Logs]] | 301 Advanced | A record of who did what and when, across the account. |
| 13 | [[System Tables]] | 201 Practitioner | Databricks' own operational data (billing, audit, lineage, compute) as queryable tables. |
| 14 | [[Lakehouse Federation]] | 201 Practitioner | Querying Postgres, SQL Server, Snowflake, and others in place, without copying. |
| 15 | [[OpenSharing]] | 201 Practitioner | The open protocol, formerly Delta Sharing, for sharing live data and AI assets with anyone. |
| 16 | [[Clean Rooms]] | 301 Advanced | Two companies analyzing combined data without seeing each other's raw records. |
| 17 | [[Databricks Marketplace]] | 201 Practitioner | Finding and getting datasets, models, and apps from other providers. |
| 18 | [[Data Classification]] | 301 Advanced | Automatically finding and tagging sensitive data like PII. |
| 19 | [[Hive Metastore Migration to Unity Catalog]] | 301 Advanced | Upgrading older workspaces off the legacy Hive metastore. |

<!-- GENERATED:reading-order END -->

> [!nextup] Up next
> [[Unity Catalog]]
