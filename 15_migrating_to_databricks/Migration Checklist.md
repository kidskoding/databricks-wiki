---
type: concept
status: written
level: 15
section: Migrating to Databricks
depth: 101
summary: A printable, start-to-finish checklist for a small business migration.
personas:
  - owner
  - solo
  - engineer
chapter: "[[Chapter 15 - Migrating to Databricks]]"
prev: "[[Running Old and New in Parallel]]"
next: "[[Chapter 80 - Learning Paths]]"
evolved_from: []
evolved_into: []
cloud_equivalent: []
related:
  - "[[Migration Strategy Overview]]"
  - "[[Assessing Your Current Data Estate]]"
  - "[[Running Old and New in Parallel]]"
  - "[[Lakebridge]]"
  - "[[Lakehouse Federation]]"
  - "[[Lakeflow Connect]]"
  - "[[Migrating BI Reports]]"
  - "[[Your First 30 Days on Databricks]]"
  - "[[Cost Optimization Checklist]]"
  - "[[Cutover]]"
aliases:
  - Migration Runbook
  - Migration To-Do List
prereqs:
  - "[[Migration Strategy Overview]]"
unlocks:
  - "[[Path - Business Owner]]"
  - "[[Path - One-Person Data Team]]"
  - "[[Cost Optimization Checklist]]"
clouds:
  - aws
  - azure
  - gcp
mastery: new
last_verified: 2026-10-25
tags:
  - concept
  - flashcards
---

# Migration Checklist

Mastery: `INPUT[inlineSelect(option(new), option(learning), option(solid)):mastery]`

> [!story] Context
> [[Running Old and New in Parallel]] described the final gate before switch-over. This note condenses the whole chapter into one checklist, ordered by phase, that a small business can print and work through.

> [!eli5] Summary
> This is the moving-day checklist. Each line is one task. Work from top to bottom, tick each box, and do not start a phase until the one before it is finished.

## Background

Each playbook in this chapter follows the same phases from [[Migration Strategy Overview]]. The details differ by source system, but missed steps are usually the same: an unlisted report, permissions recreated late, no agreed tolerance for validation, or no date to turn the old system off. A checklist prevents those omissions.

## Overview

The migration checklist is a phase-by-phase list of the tasks for moving a business's data and reports to Databricks.

| Phase | Goal | Detail |
|---|---|---|
| 1. Assess | Know what exists and what is used | [[Assessing Your Current Data Estate]] |
| 2. Land the platform | A governed, secure workspace | [[Your First 30 Days on Databricks]] |
| 3. Coexist | Query the old system from Databricks | [[Lakehouse Federation]] |
| 4. Ingest | Data lands on schedule | [[Lakeflow Connect]], [[Auto Loader]] |
| 5. Convert | Code runs on Databricks | [[Lakebridge]], [[Migrating ETL Tools]] |
| 6. Validate | Outputs match within tolerance | [[Running Old and New in Parallel]] |
| 7. Switch over | Users and reports on Databricks | [[Migrating BI Reports]], [[Cutover]] |
| 8. Decommission | Old system turned off | This note |

## How it works

### Phase 1: assess

- [ ] List every source system: databases, warehouses, file shares, spreadsheets, [[SaaS PaaS and IaaS|SaaS]] apps.
- [ ] List every table, view, and file that reports depend on, with owner and last-read date.
- [ ] List every scheduled job, stored procedure (saved database code), and [[ETL vs ELT|ETL]] package.
- [ ] List every report and dashboard, with its audience and last-opened date.
- [ ] Record current costs: licences, servers, cloud bills, support contracts.
- [ ] Record freshness expectations ("sales by 7 a.m.").
- [ ] Mark columns with personal or sensitive data.
- [ ] Remove unused objects from scope.
- [ ] Run the Lakebridge Analyzer on exported code (optional for small estates).
- [ ] Group the remaining objects into waves. Wave 1 is useful but not critical.
- [ ] Write the plan: waves, owners, dates, and the decommission date.

### Phase 2: land the platform

- [ ] Choose a cloud and region close to the source data ([[Choosing a Cloud for Databricks]]).
- [ ] Create the workspace and confirm Unity Catalog is enabled.
- [ ] Create catalogs by purpose (for example `raw`, `analytics`, `sandbox`, or `dev` and `prod`).
- [ ] Sync users and groups from the [[Identity Provider|identity provider]]; grant to groups only.
- [ ] Map old database roles to Unity Catalog grants.
- [ ] Configure network access from Databricks compute to each source.
- [ ] Store source credentials in a secret scope (a protected store for passwords and keys).
- [ ] Set up a budget and usage dashboard ([[Budgets and Usage Dashboards]]).
- [ ] Create a serverless SQL warehouse with auto-stop.

### Phase 3: coexist

- [ ] Create a Unity Catalog connection to each source database or warehouse.
- [ ] Create [[Catalogs Schemas and Tables|foreign catalogs]] and grant read access to the right groups.
- [ ] Point federation at a read replica (a read-only copy of the database) where one exists.
- [ ] Build the first new dashboard on federated data.

### Phase 4: ingest

- [ ] Choose a method per table: managed connector, file export plus Auto Loader, or scheduled federated copy.
- [ ] Prepare the source for change capture where needed (change tracking, [[Change Data Capture|CDC]], logical replication, binlog).
- [ ] Load history once; record the cutoff point.
- [ ] Start incremental loads from that cutoff; check for gaps and duplicates.
- [ ] Schedule pipelines as Lakeflow Jobs with failure notifications.
- [ ] Confirm row counts match the source for each table.

### Phase 5: convert

- [ ] Export views, procedures, and ETL packages to files.
- [ ] Split large, single-file SQL scripts with the SQL Splitter.
- [ ] Transpile (automatically translate the code) with the recommended Lakebridge transpiler, or the agentic code converter.
- [ ] Fix every error and review every warning.
- [ ] Rewrite unsupported parts (script tasks, unsupported components).
- [ ] Replace `FLOAT` money columns with `DECIMAL`; check collation (text sorting and comparison rules) and time zones.
- [ ] Put converted code in [[Git]] and deploy with [[Declarative Automation Bundles|bundles]].

### Phase 6: validate

- [ ] Agree tolerances and exit criteria in writing.
- [ ] Run old and new on the same inputs.
- [ ] Compare schemas, row counts, key totals, and row-level values daily.
- [ ] Investigate and fix every mismatch outside tolerance.
- [ ] Include at least one month-end if finance reports are in scope.
- [ ] Get sign-off from each report owner.

### Phase 7: switch over

- [ ] Announce the cutover date and freeze changes to old pipelines.
- [ ] Repoint or rebuild each report; compare totals after repointing.
- [ ] Update bookmarks, documentation, and Excel connections.
- [ ] Stop writes from old pipelines; keep the old system readable.
- [ ] Name the rollback owner and keep the rollback window open for the agreed period.

### Phase 8: decommission

- [ ] Disable old scheduled jobs and ETL packages.
- [ ] Take a final backup or snapshot of the old system; store it per retention policy.
- [ ] Revoke old credentials and service accounts.
- [ ] Remove network paths opened only for the migration.
- [ ] Cancel licences, support contracts, and reserved capacity.
- [ ] Shut down or delete old servers, clusters, or warehouses.
- [ ] Compare actual Databricks costs with the business case; review the [[Cost Optimization Checklist]].
- [ ] Record lessons learned for the next wave.

## Small-business considerations

> [!smallbiz] Small-business considerations
> For a business with one data person, a single wave is often enough:
> 1. One week for phases 1 and 2.
> 2. Two to four weeks for phases 3 to 5.
> 3. Two to four weeks of parallel running (phase 6).
> 4. One day for switch-over, then a short rollback window.
>
> The two items most often skipped are written tolerances (phase 6) and cancelling old contracts (phase 8). Without the first, sign-off stalls; without the second, there are no savings.

## Cloud differences

> [!azure]- Azure Databricks
> Phase 2 adds [[Microsoft Entra ID Integration|Entra ID]] sync, [[VNet Injection]] or [[Azure Private Link]] where required, and an [[ADLS and Access Connectors|Access Connector]] for storage. See [[Chapter 11 - Azure Databricks]].

> [!aws]- Databricks on AWS
> Phase 2 adds a [[Cross-Account IAM Role|cross-account IAM role]], an S3 bucket with a Unity Catalog storage credential, and optionally a [[Customer-Managed VPC on AWS|customer-managed VPC]]. See [[Chapter 12 - Databricks on AWS]].

> [!gcp]- Databricks on Google Cloud
> Phase 2 adds [[Google Service Accounts|service accounts]], a GCS bucket, and optionally [[Private Service Connect]]. See [[Chapter 13 - Databricks on Google Cloud]].

## Advanced topics

> [!deepdive]- Advanced topics (301–401)
> - **Track the checklist as data:** Load the inventory into a Delta table with a status column per object and phase, and chart progress on a dashboard.
> - **Automate the gates:** Make reconciliation queries a scheduled job that writes results to a table; gate the cutover on that table, not on memory.
> - **Waves overlap:** In larger estates, wave 2 can be in conversion while wave 1 is in validation. Keep each wave's checklist separate.
> - **Infrastructure as code:** Define workspaces, catalogs, and grants with the [[Terraform Provider]] and pipelines with [[Declarative Automation Bundles]], so environments can be recreated.

## Common misconceptions

> [!confusion] Decommissioning is part of the migration
> A migration is complete only when the old system is turned off and its costs stop. Plan the decommission date at the start, not after go-live.

> [!confusion] Checklists do not replace validation
> Ticking "converted" does not mean the outputs match. Phase 6 is where correctness is proven.

## Recall

What are the eight phases in the migration checklist?::Assess, land the platform, coexist, ingest, convert, validate, switch over, decommission.
Which two checklist items are most often skipped?::Written validation tolerances, and cancelling old licences and contracts.
What must be recorded when loading history before incremental loads start?::The cutoff point, so incremental loads start there without gaps or duplicates.
Who should grants go to in Unity Catalog?::Groups, not individual users.
When is a migration complete?::When the old system is turned off and its costs stop.
What should wave 1 contain?::Useful but non-critical workloads, plus small shared tables many reports depend on.

## Next steps

> [!path] Learning path
> **Needs first:** [[Migration Strategy Overview]]
> **Unlocks next:** [[Path - Business Owner]], [[Path - One-Person Data Team]], [[Cost Optimization Checklist]]

> [!nextup] Next
> [[Chapter 80 - Learning Paths]] offers ordered routes through the vault for each role, from business owner to platform admin.

> [!sources]- Sources (last verified: 2026-10-25)
> This checklist summarizes the playbooks in this chapter. Product facts are sourced in each linked note. Primary references:
> - [Migrate data applications to Databricks (AWS)](https://docs.databricks.com/aws/en/migration/)
> - [Migrate your data warehouse to the Databricks lakehouse (Azure Databricks)](https://learn.microsoft.com/en-us/azure/databricks/migration/warehouse-to-lakehouse)
> - [Migrate ETL pipelines to Databricks (AWS)](https://docs.databricks.com/aws/en/migration/etl)
> - [Lakebridge overview (Databricks Labs, GitHub)](https://github.com/databrickslabs/lakebridge/blob/main/docs/lakebridge/docs/overview.mdx)
> - [Connect to external databases and catalogs (Azure Databricks)](https://learn.microsoft.com/en-us/azure/databricks/query-federation/)
> - [Lakeflow Connect connector concepts (AWS)](https://docs.databricks.com/aws/en/ingestion/lakeflow-connect/)
