---
type: path
status: written
level: 80
section: Learning Paths
depth: 101
summary: From Excel and SQL to Databricks SQL, dashboards, Genie, and Power BI.
personas:
  - analyst
chapter: "[[Chapter 80 - Learning Paths]]"
prev: "[[Path - Business Owner]]"
next: "[[Path - Data Engineer]]"
evolved_from: []
evolved_into: []
cloud_equivalent: []
related:
  - "[[SQL]]"
  - "[[Star Schema]]"
  - "[[Databricks SQL]]"
  - "[[SQL Warehouses]]"
  - "[[SQL Editor]]"
  - "[[Three-Level Namespace]]"
  - "[[AI-BI Dashboards]]"
  - "[[Genie Agents]]"
  - "[[Connecting Power BI]]"
  - "[[Materialized Views]]"
  - "[[Metric Views]]"
  - "[[Query Performance and Caching]]"
  - "[[Path - Absolute Beginner]]"
  - "[[Path - Data Engineer]]"
  - "[[Path - Certification Prep]]"
aliases:
  - BI Developer Path
  - SQL Analyst Path
prereqs:
  - "[[Path - Absolute Beginner]]"
unlocks:
  - "[[Path - Data Engineer]]"
  - "[[Path - Certification Prep]]"
clouds:
  - aws
  - azure
  - gcp
mastery: new
last_verified: 2026-10-25
tags:
  - path
---

# Path - Analyst

> [!persona] Who this is for
> **Who:** an analyst, BI developer, or spreadsheet specialist who builds reports. You know spreadsheets well and some SQL.
> **Goal:** do your job in Databricks: find trusted tables, query them, build dashboards, give business users [[Genie Agents]], and keep Power BI or Tableau working.
> **Outcome:** you can model a small star schema, publish dashboards and Genie agents, connect a BI tool, define a governed metric, and diagnose a slow query.

## Before you start

You should be comfortable with a spreadsheet and know `SELECT`, `WHERE`, and `GROUP BY`. If not, read [[SQL]] and work through its examples. A [[Databricks Free Edition and Trials|Free Edition]] workspace is enough for Stages 1 to 3. For Power BI, have Power BI Desktop installed.

## The route

### Stage 1: Modeling and SQL refresher (101 to 201)

**Goal:** review tables, keys, and grain before using Databricks.

1. [[Spreadsheets]]: what you already know, and where spreadsheets reach their limits.
2. [[SQL]]: the core skill for this path.
3. [[Primary and Foreign Keys]]: how tables point at each other, so joins make sense.
4. [[OLTP vs OLAP]] (201): why reporting tables look different from app tables.
5. [[Data Modeling Basics]] (201): entities, grain, and which tables to build.
6. [[Star Schema]] (201): facts and dimensions, the classic shape for BI.
7. [[Data Warehouses]]: the systems your SQL habits came from.
8. [[BI Tools]]: where your work ends up.

> [!check] Checkpoint
> In the SQL Editor, join the TPC-H sample tables into a small star:
> ```sql
> SELECT c.c_mktsegment, YEAR(o.o_orderdate) AS yr, SUM(o.o_totalprice) AS revenue
> FROM samples.tpch.orders o
> JOIN samples.tpch.customer c ON o.o_custkey = c.c_custkey
> GROUP BY ALL
> ORDER BY yr, revenue DESC;
> ```
> Name the fact table, the dimension table, and the grain of the result.

### Stage 2: Databricks basics (101)

**Goal:** learn where tables live, what runs your SQL, and how layers are organized.

1. [[Databricks SQL]]: the warehouse experience inside Databricks.
2. [[SQL Warehouses]]: the compute behind every query and dashboard.
3. [[SQL Editor]]: writing, saving, and sharing queries.
4. [[Three-Level Namespace]]: `catalog.schema.table`.
5. [[Catalogs Schemas and Tables]]: how those objects are organized and secured.
6. [[Delta Lake]]: the format under every table, and why updates are safe.
7. [[Medallion Architecture]]: bronze, silver, and gold, and why analysts mostly read gold.
8. [[Genie Code]]: the AI helper that writes and explains SQL.

> [!check] Checkpoint
> Upload a CSV with **New > Add or upload data**. Then build a gold table from it with `CREATE OR REPLACE TABLE ... AS SELECT`, add a description with `COMMENT ON TABLE`, and ask [[Genie Code]] to explain one of your queries. Find the table in **Catalog** by its three-part name.

### Stage 3: Dashboards, Genie Agents, and BI tools (101 to 201)

**Goal:** publish answers that people can use.

1. [[AI-BI Dashboards]]: native dashboards, built with AI help.
2. [[Genie Agents]]: plain-English questions for business users.
3. [[SQL Alerts]] (201): notify someone when a value crosses a threshold.
4. [[Genie One]]: the simple home where business users find your work.
5. [[Connecting Power BI]] (201): import, DirectQuery, and publishing from Unity Catalog.
6. [[Connecting Tableau and Other BI Tools]] (201): Tableau, Looker, Excel, and anything with JDBC or ODBC.
7. [[Time Travel]] (201): query a table as it was at an earlier point in time.
8. [[AI Functions in SQL]] (201): classify, summarize, and extract text from plain SQL.

> [!check] Checkpoint
> Build a dashboard on your gold table with a filter, a line chart, and a counter, and publish it. Create a Genie agent on the same tables, add two example questions and one instruction ("revenue means `SUM(o_totalprice)`"), and test it. If you have Power BI Desktop and a workspace that allows it, connect to your SQL warehouse and build one visual.

### Stage 4: Governed metrics and speed (201 to 301)

**Goal:** make metrics consistent across tools and speed up slow queries.

1. [[Materialized Views]] (201): precomputed results that refresh incrementally.
2. [[dbt on Databricks]] (201): SQL models with tests and version control.
3. [[Lakehouse Federation]] (201): query an existing SQL Server or Postgres database in place during migration.
4. [[Data Lineage]] (201): see what feeds your dashboard before someone changes it.
5. [[Metric Views]] (301): define "revenue" once so every tool agrees.
6. [[Query Performance and Caching]] (301): read a query profile and fix the slow part.
7. [[Slowly Changing Dimensions]] (301): keep history when a customer moves or a price changes.
8. [[Migrating BI Reports]] (201): repoint or rebuild reports when moving to Databricks.

> [!check] Checkpoint
> Turn your heaviest dashboard query into a materialized view (`CREATE MATERIALIZED VIEW ... AS SELECT ...`) and point a dashboard widget at it. Run the original query, open its **query profile**, and note which step took longest. Open the **Lineage** tab on your gold table and confirm the dashboard appears downstream.

## Rabbit holes

- **Where SQL on big data came from:** [[Apache Hive]], [[Spark SQL]], [[Columnar Storage]].
- **Other warehouses you may be migrating from:** [[Snowflake]], [[Amazon Redshift]], [[Google BigQuery]], and [[BigQuery Integration]].
- **Microsoft shops:** [[Power BI on Azure Databricks]] and [[Microsoft Fabric and OneLake vs Databricks]], then [[Path - Azure Deep Dive]] if you also administer it. AWS and Google Cloud readers can skim [[Path - AWS Deep Dive]] or [[Path - Google Cloud Deep Dive]].
- **No-code pipelines:** [[Lakeflow Designer]].
- **Python for analysts:** [[DataFrames]] and [[Python for Data]].
- **Quick models:** [[AutoML]].
- **Exams:** the Data Analyst track in [[Path - Certification Prep]].

## You are done when

- You can design a small star schema and say its grain.
- You can find any table by its three-part name and read its lineage.
- You have published a dashboard, a Genie agent, and an alert.
- You can connect Power BI or another BI tool to a SQL warehouse.
- You can explain when to use a materialized view or a metric view.
- You can open a query profile and point to the slow step.

> [!nextup] Next
> [[Path - Data Engineer]] covers building the tables that analysts query.

> [!sources]- Sources (last verified: 2026-10-25)
> - Route assembled on 2026-10-25 from the vault index (`llms.txt`) and the `analyst` persona tags in `_meta/manifest.yaml`. Product facts and official documentation links live in each linked note's `[!sources]` callout.
> - The `samples.tpch` tables and the SQL in the checkpoints use standard Databricks SQL. Free Edition availability of Genie, alerts, materialized views, and BI connections was not re-checked for this path; see [[Databricks Free Edition and Trials]].
