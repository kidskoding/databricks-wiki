---
type: glossary
status: written
level: 90
section: Glossary
depth: 101
summary: "A key performance indicator: one number a business watches to know whether it is on track."
related:
  - "[[AI-BI Dashboards]]"
  - "[[Metric Views]]"
  - "[[Genie]]"
  - "[[SQL Alerts]]"
  - "[[Databricks SQL]]"
aliases:
  - "Key Performance Indicator"
  - "KPIs"
  - "business metric"
last_verified: 2026-10-25
tags:
  - glossary
  - flashcards
---

# KPI

> [!eli5] Summary
> A KPI (key performance indicator) is one agreed number that shows whether a business is meeting a goal, such as weekly sales. Teams track it over time and act when it moves the wrong way.

**In data work:** A KPI is a measured value tied to a goal, with a fixed definition, a time window, and usually a target. Revenue per week, repeat-customer rate, and average delivery time are typical KPIs. The definition must be agreed in advance, for example whether weekly revenue includes refunds, tax, and gift cards. A bakery with two shops might track daily sales per shop, the share of orders from returning customers, and waste (unsold loaves as a percent of baked loaves). Each one becomes a [[Query|query]] over sales and inventory tables, with the result shown on a [[Dashboard|dashboard]].

**In Databricks:** KPIs usually live as tiles on [[AI-BI Dashboards]] built on [[Databricks SQL]]. To stop every analyst from computing revenue slightly differently, you can define the measure once as a [[Metric Views|metric view]] in [[Unity Catalog]] (the vault's [[Semantic Layer|semantic layer]]). [[Genie]] answers plain-English questions against those definitions, and [[SQL Alerts]] can notify you when a KPI crosses a threshold.

Seen in: [[AI-BI Dashboards]], [[Metric Views]], [[SQL Alerts]], [[Building a Business Case]]

## Recall

KPI::A key performance indicator: one agreed, measured number tied to a business goal, such as weekly revenue or repeat-customer rate.

> [!sources]- Sources (last verified: 2026-10-25)
> - [Unity Catalog metric views (AWS)](https://docs.databricks.com/aws/en/uc-semantics/metric-views/)
