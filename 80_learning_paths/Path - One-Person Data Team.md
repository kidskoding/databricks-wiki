---
type: path
status: written
level: 80
section: Learning Paths
depth: 101
summary: The shortest route for a small business with one data person doing every job.
personas:
  - solo
chapter: "[[Chapter 80 - Learning Paths]]"
prev: "[[Path - Platform Admin]]"
next: "[[Path - Azure Deep Dive]]"
evolved_from: []
evolved_into: []
cloud_equivalent: []
related:
  - "[[Signs You Have Outgrown Spreadsheets]]"
  - "[[Databricks Free Edition and Trials]]"
  - "[[Serverless Compute]]"
  - "[[Migrating from Excel and Access]]"
  - "[[Lakeflow Connect]]"
  - "[[Lakehouse Federation]]"
  - "[[Medallion Architecture]]"
  - "[[Lakeflow Spark Declarative Pipelines]]"
  - "[[Lakeflow Jobs]]"
  - "[[AI-BI Dashboards]]"
  - "[[Genie Agents]]"
  - "[[Cost Optimization Checklist]]"
  - "[[Migration Checklist]]"
  - "[[Path - Business Owner]]"
  - "[[Path - Analyst]]"
  - "[[Path - Data Engineer]]"
  - "[[Path - Platform Admin]]"
aliases:
  - Solo Path
  - Small Business Path
prereqs: []
unlocks:
  - "[[Path - Data Engineer]]"
  - "[[Path - Platform Admin]]"
clouds:
  - aws
  - azure
  - gcp
mastery: new
last_verified: 2026-10-25
tags:
  - path
---

# Path - One-Person Data Team

> [!persona] Who this is for
> **Who:** the one person at a small business who handles all data work: pulling exports, fixing spreadsheets, building reports, and now setting up a data platform. This person may also be the owner.
> **Goal:** move from spreadsheets and one database to a small, low-cost, reliable Databricks setup without learning every feature first.
> **Outcome:** within about a month, your sources load automatically each night into bronze, silver, and gold tables, a dashboard and a Genie agent answer the common questions, and you know what it costs and who can see what.

## Before you start

You need basic SQL and a working knowledge of your business's systems. Start in [[Databricks Free Edition and Trials|Free Edition]] to learn, then move to a paid workspace on your cloud when you connect real business data. This path uses serverless and managed tools throughout, so you do not operate clusters.

## The route

### Stage 1: Decide and set up (101)

**Goal:** confirm the fit and get a workspace with sensible defaults.

1. [[Signs You Have Outgrown Spreadsheets]]: confirm that you need a data platform.
2. [[When Databricks Is Not the Right Fit]]: confirm that a simpler tool would not suffice.
3. [[Databricks Free Edition and Trials]]: practice for free first.
4. [[How Databricks Pricing Works]]: the billing meter to monitor.
5. [[Serverless Compute]]: why to run almost every workload on serverless.
6. [[Choosing a Cloud for Databricks]]: usually the cloud your email and files already live on.
7. Your cloud's setup note: [[Creating an Azure Databricks Workspace]], [[Account Setup on AWS]], or [[Account Setup on Google Cloud]].

> [!check] Checkpoint
> In Free Edition, upload your messiest business spreadsheet as a table and query it in the SQL Editor. Then write down your three most important data sources (for example the accounting system, the shop's point of sale, and the CRM) and how to extract data from each one: file export, database connection, or API.

### Stage 2: Ingest the data (101 to 201)

**Goal:** replace manual file copying with automated loads.

1. [[Migrating from Excel and Access]]: the playbook for the spreadsheets.
2. [[Lakeflow]]: the product family for ingestion, pipelines, and jobs.
3. [[Lakeflow Connect]]: managed connectors for SaaS apps and databases.
4. [[Lakehouse Federation]] (201): query the existing database in place on day one.
5. [[Volumes]] (201): a governed folder where exports land.
6. [[Medallion Architecture]]: bronze for raw, silver for clean, gold for reports.
7. [[Lakeflow Designer]]: drag-and-drop pipelines if you prefer not to code.
8. [[Partner Connect]] (201): one-click Fivetran, dbt, and BI connections when you need them.

> [!check] Checkpoint
> Create a catalog or schema for each layer (`bronze`, `silver`, `gold`) and a Volume in `bronze`. Load one source automatically: either a managed connector, a federated connection to your database, or exports dropped into the Volume. Confirm that new rows arrive without manual file handling.

### Stage 3: Automate (101 to 201)

**Goal:** a nightly pipeline, trusted numbers, and self-service answers for colleagues.

1. [[Lakeflow Spark Declarative Pipelines]] (201): declare bronze-to-gold tables and let Databricks run them.
2. [[Expectations and Data Quality]] (201): catch bad rows before they reach reports.
3. [[Lakeflow Jobs]]: schedule the pipeline and receive an email on failure.
4. [[AI-BI Dashboards]]: the weekly report, rebuilt once.
5. [[Genie Agents]]: let colleagues ask their own questions.
6. [[SQL Alerts]] (201): receive a notification when a value is out of range.
7. [[AutoML]]: a quick forecast or churn model when someone asks.

> [!check] Checkpoint
> Build a pipeline that cleans your bronze data into silver with at least one expectation, and builds one gold table. Schedule it nightly with a job that emails you on failure. Put a dashboard and a Genie agent on the gold table, share them with two coworkers, and add an alert for one key number.

### Stage 4: Cost, access, and handover (201 to 301)

**Goal:** control cost and access, retire the old system, and leave a setup someone else could run.

1. [[Cost Management Basics]]: the first five items to check.
2. [[Cost Optimization Checklist]] (201): auto-termination, serverless, sizing, and more.
3. [[Budgets and Usage Dashboards]] (201): a budget alert that warns before spend exceeds plan.
4. [[Users Groups and Service Principals]] (201): groups for people, a service principal for the nightly job.
5. [[Privileges and Grants]] (201): who can read gold, and who can change it.
6. [[Migrating from SQL Server]] or [[Migrating from Postgres and MySQL]] (201): moving off the old database for good.
7. [[Running Old and New in Parallel]] (201): compare numbers before switching.
8. [[Declarative Automation Bundles]] (301): keep the whole setup in Git so someone else can run it.
9. [[Migration Checklist]]: the final checklist.

> [!check] Checkpoint
> Set a monthly budget alert. Create groups `report-readers` and `data-admins`, grant `SELECT` on the gold schema to `report-readers`, and make the job run as a service principal. Run old and new reports side by side for one week and record any number that differs, then fix it or explain it.

## Rabbit holes

- **Costs in detail:** [[Estimating Costs for a Small Business]], [[DBUs]], [[Tagging for Chargeback]].
- **Comparing options:** [[Databricks vs Alternatives for Small Teams]] and [[Microsoft Fabric and OneLake vs Databricks]].
- **Your cloud:** [[Path - Azure Deep Dive]], [[Path - AWS Deep Dive]], or [[Path - Google Cloud Deep Dive]]. Read only the 101 and 201 notes at first.
- **AI for a small team:** [[Agent Bricks]], [[AI Functions in SQL]], [[Databricks Apps]].
- **Deeper roles when you hire help:** [[Path - Data Engineer]], [[Path - Analyst]], [[Path - Platform Admin]].
- **Presenting to leadership:** [[Path - Business Owner]] and [[Building a Business Case]].

## You are done when

- Every important source loads automatically each night.
- Your tables are split into bronze, silver, and gold, with quality rules on silver.
- A dashboard, a Genie agent, and alerts answer the everyday questions.
- You have a budget alert and know your monthly spend.
- Access is by group, and automation runs as a service principal.
- The old spreadsheets or database are retired, or have a retirement date.

> [!nextup] Next
> [[Path - Azure Deep Dive]] is the full route for Azure Databricks.

> [!sources]- Sources (last verified: 2026-10-25)
> - Route assembled on 2026-10-25 from the vault index (`llms.txt`) and the `solo` persona tags in `_meta/manifest.yaml`. Product facts, prices, and official documentation links live in each linked note's `[!sources]` callout.
> - Free Edition limits and connector availability were not re-checked for this path; see [[Databricks Free Edition and Trials]] and [[Lakeflow Connect]].
