---
type: glossary
status: written
level: 90
section: Glossary
depth: 101
summary: "A shared layer of business definitions (revenue, active customer) that every tool reads from, so numbers match."
related:
  - "[[Metric Views]]"
  - "[[KPI]]"
  - "[[Genie Agents]]"
  - "[[AI-BI Dashboards]]"
  - "[[BI Tools]]"
  - "[[Single Source of Truth]]"
aliases:
  - "semantic model"
  - "metrics layer"
  - "metric layer"
  - "business layer"
last_verified: 2026-10-25
tags:
  - glossary
  - flashcards
---

# Semantic Layer

> [!eli5] Summary
> A semantic layer is a shared set of business definitions, such as how revenue is calculated, that every report and tool uses. It keeps numbers consistent across reports.

**In data work:** A semantic layer sits between raw tables and the people asking questions. It defines measures (total revenue, average order value), dimensions (region, product line), and how tables join, in business terms. Without it, each analyst and dashboard tool writes its own SQL and three reports show three revenue figures. A gift shop with a part-time analyst might define net sales once as gross sales minus refunds and discounts, then point every dashboard at that definition.

**In Databricks:** Databricks' semantic layer is [[Metric Views]] in [[Unity Catalog]]: measures and dimensions defined once in YAML and queried with SQL, including from [[AI-BI Dashboards]] and [[Genie Agents]]. Because metric views are Unity Catalog objects, they get the same permissions, lineage, and discovery as tables. Power BI users may still keep their own semantic model on top (see [[Connecting Power BI]]).

Seen in: [[Metric Views]], [[Genie Agents]], [[BI Tools]]

## Recall

Semantic Layer::Shared business definitions of measures and dimensions that all tools query; in Databricks this is Unity Catalog metric views.

> [!sources]- Sources (last verified: 2026-10-25)
> - [Unity Catalog metric views (AWS)](https://docs.databricks.com/aws/en/uc-semantics/metric-views/)
> - [Unity Catalog metric views (Azure Databricks)](https://learn.microsoft.com/en-us/azure/databricks/uc-semantics/metric-views/)
