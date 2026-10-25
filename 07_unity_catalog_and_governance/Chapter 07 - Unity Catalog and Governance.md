---
type: chapter
status: written
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
last_verified: 2026-10-25
tags:
  - chapter
---

# Chapter 07 - Unity Catalog and Governance

> [!story] Context
> [[Chapter 06 - The Databricks Platform|Chapter 06]] introduced accounts, workspaces, compute, and notebooks. That platform can process data at scale, but it does not by itself answer who may access which data, where a value came from, or who changed what. This chapter covers the governance layer that answers those questions: [[Unity Catalog]].

**One place to find, secure, track, and share every data and AI asset.**

## The story of this chapter

Before Unity Catalog, governance on Databricks was scoped to the workspace. Each workspace had its own [[Hive Metastore]], its own table access control, and its own cluster-level credentials for cloud storage, such as [[Instance Profiles|instance profiles]]. A company with several workspaces had several inconsistent inventories, permissions that differed by workspace, and no built-in lineage or account-wide audit trail. This is the condition the lakehouse was meant to avoid: a [[Data Swamps|data swamp]] with better compute.

[[Unity Catalog]] moves governance to the account. One [[Metastore]] per cloud region holds the metadata and permissions for every attached workspace. Every object has a three-part address, `catalog.schema.object`, described in [[Three-Level Namespace]]. [[Catalogs Schemas and Tables]] covers the object types and common layouts, and [[Managed vs External Tables]] explains who manages the files behind a table. [[Volumes]] extend the same governance to non-tabular files, and [[Storage Credentials and External Locations]] move cloud storage credentials from clusters into the catalog, so compute receives short-lived, scoped access only for authorized requests.

Access control is layered:

| Layer | Question it answers | Note |
|---|---|---|
| Grants | May this principal use this object? | [[Privileges and Grants]] |
| Row filters and column masks | Which rows and values may this principal see in this table? | [[Row Filters and Column Masks]] |
| Tag-based policies | Which rules apply to every object with this tag? | [[Attribute-Based Access Control]] |

ABAC row filter and column mask policies, governed tags, and [[Data Classification]] became generally available in 2026. DENY policies and metastore-level policies are in Beta as of October 2026.

Observability is built in. [[Data Lineage]] records column-level lineage as queries run. [[Audit Logs]] record who did what and when. [[System Tables]] expose audit, lineage, billing, compute, job, and query data as read-only tables in the `system` catalog, so governance and cost reporting use ordinary SQL.

Governance also extends beyond Databricks-stored data. [[Lakehouse Federation]] registers external databases and catalogs, such as PostgreSQL, SQL Server, Snowflake, or a legacy Hive metastore, as foreign catalogs that are queried and governed in place. [[OpenSharing]], named Delta Sharing until June 2026 and now hosted by the [[Linux Foundation]], shares live data and AI assets with other organizations, on Databricks or not. [[Clean Rooms]] let up to ten organizations run approved analysis on combined data without exposing raw records. [[Databricks Marketplace]] uses the same sharing protocol to distribute datasets and models.

The chapter ends with two operational topics. [[Data Classification]] scans catalogs for sensitive data and tags it, so tag-based policies cover new columns. [[Hive Metastore Migration to Unity Catalog]] describes how older workspaces move from `hive_metastore` to Unity Catalog with federation, `SYNC`, `CLONE`, and the UCX utilities.

At the end of this chapter, data is cataloged, secured, traced, and shareable. Governance does not load data or keep it current. Data must still be ingested from source systems, transformed through layers such as the [[Medallion Architecture]], and refreshed on a schedule or as a stream. [[Chapter 08 - Data Engineering]] covers ingestion, pipelines, and orchestration on Databricks.

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

> [!nextup] Next
> [[Unity Catalog]]
