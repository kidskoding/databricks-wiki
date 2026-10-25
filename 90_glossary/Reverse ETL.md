---
type: glossary
status: written
level: 90
section: Glossary
depth: 101
summary: "Copying cleaned data from the analytics platform back into the business tools people use every day."
related:
  - "[[ETL vs ELT]]"
  - "[[Lakebase]]"
  - "[[Fivetran and ELT Tools]]"
  - "[[Partner Connect]]"
  - "[[Single Source of Truth]]"
  - "[[Databricks Apps]]"
aliases:
  - "reverse-ETL"
  - "data activation"
  - "operational analytics"
last_verified: 2026-10-25
tags:
  - glossary
  - flashcards
---

# Reverse ETL

> [!eli5] Summary
> Reverse ETL copies cleaned, analyzed data from the data platform back into the business tools that staff use daily, such as a CRM or email tool.

**In data work:** Normal [[ETL vs ELT|ETL or ELT]] moves data from business apps into the warehouse or lakehouse. Reverse ETL moves modeled results the other way: into a CRM, an email marketing tool, a support desk, or an app's database. Examples are lifetime-value scores pushed into Salesforce or a VIP customer list synced to an email platform. A boutique might compute a customers who have not bought in 90 days list in the lakehouse each night and sync it to its email tool for a win-back campaign.

**In Databricks:** On Databricks, the built-in route is [[Lakebase]], the managed Postgres database: synced tables copy Unity Catalog tables into Postgres in snapshot, triggered, or continuous mode, and Databricks recommends treating them as read-only. Third-party reverse ETL tools are another option. [[Databricks Apps]] can then read from Lakebase. Either way, the lakehouse stays the [[Single Source of Truth|single source of truth]] and the business tools receive copies.

Seen in: [[Lakebase]], [[ETL vs ELT]], [[Partner Connect]]

## Recall

Reverse ETL::Syncing modeled data from the lakehouse back into business tools like a CRM or email platform.

> [!sources]- Sources (last verified: 2026-10-25)
> - [Reverse ETL with Lakebase (Databricks blog)](https://www.databricks.com/blog/reverse-etl-lakebase-activate-your-lakehouse-data-operational-analytics)
> - [Serve lakehouse data with synced tables (Azure Databricks)](https://learn.microsoft.com/en-us/azure/databricks/oltp/projects/sync-tables)
> - [Serve lakehouse data with synced tables (Google Cloud)](https://docs.databricks.com/gcp/en/oltp/projects/sync-tables)
