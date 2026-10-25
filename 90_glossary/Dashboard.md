---
type: glossary
status: written
level: 90
section: Glossary
depth: 101
summary: "A single view of charts, tables, and key metrics that summarizes the state of a business or system."
related:
  - "[[AI-BI Dashboards]]"
  - "[[BI Tools]]"
  - "[[Databricks SQL]]"
  - "[[Genie Agents]]"
  - "[[Connecting Power BI]]"
  - "[[Metric Views]]"
aliases:
  - "dashboards"
  - "BI dashboard"
last_verified: 2026-10-25
tags:
  - glossary
  - flashcards
---

# Dashboard

> [!eli5] Summary
> A dashboard shows the most important numbers and charts on one screen, so people can check performance at a glance.

**In data work:** A dashboard combines several visualizations and [[KPI|KPIs]] on one page, usually with filters such as date range or region. It reads from prepared, aggregated tables rather than raw data, so it loads quickly and shows consistent figures. Dashboards are built in [[BI Tools]] such as Power BI, Tableau, and Looker, or in the data platform itself. Example: a café's dashboard shows daily sales, top items, and labor cost as a share of revenue.

**In Databricks:** [[AI-BI Dashboards]] are the native Databricks dashboards, built on [[SQL Warehouses]]. Published dashboards can be shared with users and groups in the Databricks account, including account users who are not members of the workspace, who get view-only access. Queries run with either the publisher's data permissions (default) or each viewer's own. Published dashboards include a companion Genie agent for follow-up questions ([[Genie Agents]]). Power BI and Tableau connect through [[Connecting Power BI]] and [[Connecting Tableau and Other BI Tools]], and [[Metric Views]] keep definitions consistent across tools.

Seen in: [[AI-BI Dashboards]], [[BI Tools]], [[Databricks SQL]], [[Your First 30 Days on Databricks]]

## Recall

Should a dashboard query raw or prepared tables?::Prepared, aggregated tables, for speed and consistency.
Whose permissions do AI/BI dashboard queries use by default?::The publisher's data permissions.

> [!sources]- Sources (last verified: 2026-10-25)
> - [Share a dashboard (AWS)](https://docs.databricks.com/aws/en/dashboards/share/share)
> - [Dashboards (AWS)](https://docs.databricks.com/aws/en/dashboards/)
