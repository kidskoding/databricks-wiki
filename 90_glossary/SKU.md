---
type: glossary
status: written
level: 90
section: Glossary
depth: 101
summary: "Stock keeping unit: a specific billable product line, such as one Databricks compute type with its own DBU rate."
related:
  - "[[DBUs]]"
  - "[[How Databricks Pricing Works]]"
  - "[[System Tables]]"
  - "[[Budgets and Usage Dashboards]]"
  - "[[Pay-As-You-Go]]"
  - "[[Azure Billing and Commit Units]]"
aliases:
  - "stock keeping unit"
  - "sku_name"
  - "SKUs"
last_verified: 2026-10-26
tags:
  - glossary
  - flashcards
---

# SKU

> [!eli5] Summary
> A SKU is a product code. In a shop it identifies one item on the shelf; in a cloud bill it identifies one kind of service with its own price.

**In data work:** Retailers use SKUs to track each product variant, such as one size and color of a shirt. Cloud providers and software vendors use the same idea for billing: each meter is a SKU with a unit and a list price. Reading a bill or a usage export means grouping charges by SKU to see which service drives cost.

**In Databricks:** Each kind of compute is a separate SKU with its own [[DBUs|DBU]] rate, for example jobs compute, all-purpose compute, SQL warehouses, and serverless products. The `system.billing.usage` [[System Tables|system table]] records the `sku_name` and `usage_unit` (for compute, `DBU`) of every usage record, and `system.billing.list_prices` holds the list price per SKU.

```sql
-- DBUs by SKU for the last 30 days
SELECT sku_name, SUM(usage_quantity) AS dbus
FROM system.billing.usage
WHERE usage_date >= current_date() - INTERVAL 30 DAYS
  AND usage_unit = 'DBU'
GROUP BY sku_name
ORDER BY dbus DESC;
```

Join to `system.billing.list_prices` on `sku_name` to estimate list cost. A small team often finds that most spend sits in one or two SKUs, such as an all-purpose cluster left running, which points to the first fix. Rates per SKU are on the official [Databricks pricing page](https://www.databricks.com/product/pricing).

Seen in: [[How Databricks Pricing Works]], [[Budgets and Usage Dashboards]], [[System Tables]]

## Recall

SKU::A billable product line with its own unit and price; in Databricks, each compute type is a SKU with its own DBU rate.
Which column in system.billing.usage identifies the SKU?::sku_name.

> [!sources]- Sources (last verified: 2026-10-26)
> - [Billable usage system table reference (Azure Databricks)](https://learn.microsoft.com/en-us/azure/databricks/admin/system-tables/billing)
> - [Monitor costs using system tables (AWS)](https://docs.databricks.com/aws/en/admin/usage/system-tables)
> - [Pricing system table reference (AWS)](https://docs.databricks.com/aws/en/admin/system-tables/pricing)
> - [Databricks pricing](https://www.databricks.com/product/pricing)
