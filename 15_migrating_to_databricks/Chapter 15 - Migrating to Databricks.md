---
type: chapter
status: written
part: 3
level: 15
section: Migrating to Databricks
summary: Playbooks for moving a business onto Databricks from spreadsheets, databases, warehouses, and Hadoop.
prev: "[[Disaster Recovery]]"
next: "[[Migration Strategy Overview]]"
notes:
  - "[[Migration Strategy Overview]]"
  - "[[Assessing Your Current Data Estate]]"
  - "[[Migrating from Excel and Access]]"
  - "[[Migrating from SQL Server]]"
  - "[[Migrating from Postgres and MySQL]]"
  - "[[Migrating from Snowflake]]"
  - "[[Migrating from Amazon Redshift]]"
  - "[[Migrating from Google BigQuery]]"
  - "[[Migrating from Hadoop]]"
  - "[[Migrating ETL Tools]]"
  - "[[Lakebridge]]"
  - "[[Migrating BI Reports]]"
  - "[[Running Old and New in Parallel]]"
  - "[[Migration Checklist]]"
last_verified: 2026-10-25
tags:
  - chapter
---

# Chapter 15 - Migrating to Databricks

> [!story] Context
> [[Chapter 14 - Admin Security and Cost|Chapter 14]] ended with [[Disaster Recovery]]: how a running Databricks estate is administered, secured, costed, and protected. This chapter covers how an organization gets there from the systems it runs today, whether spreadsheets, databases, cloud warehouses, or Hadoop.

**Playbooks for moving a business onto Databricks from spreadsheets, databases, warehouses, and Hadoop.**

## The story of this chapter

A migration moves three things: data, the code that builds it, and the reports and people that use it. Copying data is usually the smallest part. Converting code, validating results, and moving users take most of the effort.

[[Migration Strategy Overview]] defines the eight phases used throughout the chapter: assess, land the platform, coexist, ingest, convert, validate, switch over, and decommission. Work moves in waves, each small enough to validate in one or two weeks. [[Assessing Your Current Data Estate]] covers the first phase: an inventory of sources, objects, code, consumers, and costs, scored by value and effort.

The source-system playbooks share one pattern:

| Phase | Typical Databricks tool |
|---|---|
| Coexist | [[Lakehouse Federation]]: query the old system in place through a Unity Catalog connection and foreign catalog |
| Ingest | [[Lakeflow Connect]] for databases and SaaS, or file exports loaded with [[Auto Loader]] and [[COPY INTO]] |
| Convert | [[Lakebridge]] transpilers, or the agentic code converter (Beta in October 2026) |
| Validate | Lakebridge Reconcile and SQL comparisons |

The playbooks run from simplest to most complex. [[Migrating from Excel and Access]] moves files into governed tables, dashboards, and Genie agents. [[Migrating from SQL Server]] and [[Migrating from Postgres and MySQL]] move analytics off application databases using change tracking, CDC, logical replication, or binlog replication, without replacing the application database. The cloud warehouse playbooks cover [[Migrating from Snowflake]] (query and catalog federation, Iceberg-based coexistence, Morpheus conversion), [[Migrating from Amazon Redshift]] (`UNLOAD` to S3, BladeBridge conversion), and [[Migrating from Google BigQuery]] (Storage API federation, `EXPORT DATA`, no built-in transpiler). [[Migrating from Hadoop]] covers HDFS data, Hive metastore federation, and job and security changes.

[[Migrating ETL Tools]] converts the scheduled layer: SSIS and DataStage through BladeBridge, Airflow and PySpark through the experimental Switch transpiler, and stored procedures into Databricks SQL scripting. Tools without a converter, such as Informatica and Talend, are rebuilt. [[Lakebridge]] describes the toolkit itself: the Profiler and Analyzer for assessment, the Morpheus, BladeBridge, and Switch transpilers, and Reconcile. It grew out of the Databricks Labs Remorph project and is free, without a formal support SLA.

The last three notes cover the user-facing end. [[Migrating BI Reports]] repoints Power BI and Tableau to SQL warehouses or rebuilds reports as AI/BI dashboards. [[Running Old and New in Parallel]] defines tolerances, daily reconciliation, exit criteria, and a rollback window. [[Migration Checklist]] condenses the chapter into one printable list.

At the end of this chapter, a business has a plan to move onto Databricks and turn off the old system. The remaining question is what to learn next for each role. [[Chapter 80 - Learning Paths]] provides ordered routes through the vault for owners, analysts, engineers, admins, and others.

## Notes in reading order

<!-- GENERATED:reading-order START (scripts/scaffold.py) -->

| # | Note | Depth | What it covers |
|---|---|---|---|
| 1 | [[Migration Strategy Overview]] | 101 Beginner | The phases of every migration, from assess and plan to move, validate, and switch over. |
| 2 | [[Assessing Your Current Data Estate]] | 201 Practitioner | Taking inventory of sources, reports, users, and costs before moving anything. |
| 3 | [[Migrating from Excel and Access]] | 101 Beginner | Moving a spreadsheet-run business into tables, with uploads, Volumes, and a first dashboard. |
| 4 | [[Migrating from SQL Server]] | 201 Practitioner | Moving off an on-premises or Azure SQL Server, using federation first and Lakeflow Connect after. |
| 5 | [[Migrating from Postgres and MySQL]] | 201 Practitioner | Moving app-database analytics into the lakehouse without hurting the app. |
| 6 | [[Migrating from Snowflake]] | 301 Advanced | Code conversion, data movement, and Iceberg-based coexistence. |
| 7 | [[Migrating from Amazon Redshift]] | 301 Advanced | Unloading to S3, converting SQL, and switching over workloads. |
| 8 | [[Migrating from Google BigQuery]] | 301 Advanced | Federation, exports to GCS, and converting BigQuery SQL. |
| 9 | [[Migrating from Hadoop]] | 301 Advanced | Moving HDFS data, Hive tables, and Spark jobs off an old cluster. |
| 10 | [[Migrating ETL Tools]] | 301 Advanced | Converting SSIS, Informatica, Talend, and stored procedures. |
| 11 | [[Lakebridge]] | 301 Advanced | Databricks' free migration toolkit for profiling, SQL conversion, and data reconciliation. |
| 12 | [[Migrating BI Reports]] | 201 Practitioner | Repointing Power BI and Tableau reports, or rebuilding them as AI-BI dashboards. |
| 13 | [[Running Old and New in Parallel]] | 201 Practitioner | Parallel runs, reconciliation, and a safe switch-over plan. |
| 14 | [[Migration Checklist]] | 101 Beginner | A printable, start-to-finish checklist for a small business migration. |

<!-- GENERATED:reading-order END -->

> [!nextup] Next
> [[Migration Strategy Overview]] starts the chapter with the phases every migration follows. After the final note, [[Chapter 80 - Learning Paths]] continues the vault.
