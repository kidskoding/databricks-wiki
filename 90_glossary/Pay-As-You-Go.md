---
type: glossary
status: written
level: 90
section: Glossary
depth: 101
summary: "A billing model where you pay only for what you use, metered per unit, with no upfront commitment."
related:
  - "[[How Databricks Pricing Works]]"
  - "[[DBUs]]"
  - "[[AWS Marketplace and Billing]]"
  - "[[Azure Billing and Commit Units]]"
  - "[[Google Cloud Marketplace and Billing]]"
  - "[[SKU]]"
aliases:
  - "PAYG"
  - "pay as you go"
  - "on-demand pricing"
  - "usage-based pricing"
last_verified: 2026-10-26
tags:
  - glossary
  - flashcards
---

# Pay-As-You-Go

> [!eli5] Summary
> Pay-as-you-go means you are billed for what you actually use, like a utility meter. There is no upfront contract, and the bill goes down when usage goes down.

**In data work:** Cloud services meter usage in units such as compute-hours, gigabytes stored, or requests, and bill each unit at a list price. Pay-as-you-go suits new or irregular workloads because nothing is paid in advance. The alternative is a commitment: you agree to a level of spend for one or more years in exchange for a discount. The usual path is to start on pay-as-you-go, measure steady usage, and commit only to what you are confident you will use.

**In Databricks:** Databricks pay-as-you-go usage is measured in [[DBUs]] and billed per second at list price. Each type of compute has its own [[SKU]] and rate, and classic compute also incurs separate cloud provider charges for virtual machines and storage.
- **AWS:** Pay-as-you-go is available directly or through AWS Marketplace, billed on the AWS invoice (see [[AWS Marketplace and Billing]]).
- **Azure:** Billed through the Azure subscription; Databricks commit units can be prepurchased for a discount (see [[Azure Billing and Commit Units]]).
- **Google Cloud:** Billed through Google Cloud Marketplace (see [[Google Cloud Marketplace and Billing]]).

Usage per SKU is recorded in the `system.billing.usage` [[System Tables|system table]]. A small team that runs a nightly job and a small [[SQL Warehouses|SQL warehouse]] with [[Auto Termination|auto termination]] pays only for those minutes. Rates are on the official [Databricks pricing page](https://www.databricks.com/product/pricing).

Seen in: [[How Databricks Pricing Works]], [[Estimating Costs for a Small Business]]

## Recall

Pay-as-you-go::Paying list price for metered usage with no upfront commitment.
In what unit is Databricks pay-as-you-go usage measured?::DBUs, billed per second at list price.

> [!sources]- Sources (last verified: 2026-10-26)
> - [Databricks pricing](https://www.databricks.com/product/pricing)
> - [Databricks pay-as-you-go on AWS Marketplace (press release)](https://www.databricks.com/company/newsroom/press-releases/databricks-strengthens-scope-of-work-with-aws)
> - [Optimize Azure Databricks costs with a prepurchase (Microsoft Learn)](https://learn.microsoft.com/en-us/azure/cost-management-billing/reservations/prepay-databricks-reserved-capacity)
> - [Monitor costs using system tables (AWS)](https://docs.databricks.com/aws/en/admin/usage/system-tables)
