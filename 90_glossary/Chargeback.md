---
type: glossary
status: written
level: 90
section: Glossary
depth: 101
summary: "The practice of billing each team or department for the cloud and Databricks usage it consumed, based on tags and usage records."
related:
  - "[[Tagging for Chargeback]]"
  - "[[System Tables]]"
  - "[[Budgets and Usage Dashboards]]"
  - "[[FinOps]]"
  - "[[DBUs]]"
  - "[[Cost Management Basics]]"
aliases:
  - "Showback"
  - "Cost allocation"
  - "Cost attribution"
last_verified: 2026-10-26
tags:
  - glossary
  - flashcards
---

# Chargeback

> [!eli5] Summary
> Chargeback means sending each team its share of the data platform bill, based on what it actually used. Showback is the same report without moving money.

**In data work:** Chargeback assigns shared platform costs to the teams, projects, or customers that generated them. It needs two things: usage records detailed enough to split, and a reliable label on each workload that says who owns it. **Showback** reports the same numbers without an internal transfer of budget. Both are core [[FinOps]] practices.

**In Databricks:** Databricks records usage in the `system.billing.usage` [[System Tables|system table]]. The `custom_tags` column carries tags from compute resources and from serverless budget policies, and `usage_metadata` identifies the job, warehouse, or endpoint. You join usage to `system.billing.list_prices` to estimate list-price cost; these are estimates, not invoiced amounts. Untagged serverless usage can be attributed with serverless budget policies. See [[Tagging for Chargeback]] for a tagging scheme and [[Budgets and Usage Dashboards]] for reporting.

Small-business example: a 30-person retailer tags compute with `team = marketing` or `team = finance` and runs one monthly query grouped by that tag, so each manager sees the [[DBUs]] their workloads used.

Seen in: [[Tagging for Chargeback]], [[System Tables]], [[Budgets and Usage Dashboards]]

## Recall

What is the difference between chargeback and showback?::Chargeback bills teams for their usage; showback only reports it.
Which system table holds Databricks billable usage?::system.billing.usage

> [!sources]- Sources (last verified: 2026-10-26)
> - [Monitor costs using system tables (AWS)](https://docs.databricks.com/aws/en/admin/usage/system-tables)
> - [Billable usage system table reference (AWS)](https://docs.databricks.com/aws/en/admin/system-tables/billing)
> - [Attribute usage with serverless budget policies (GCP)](https://docs.databricks.com/gcp/en/admin/usage/budget-policies)
