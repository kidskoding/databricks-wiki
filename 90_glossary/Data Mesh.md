---
type: glossary
status: written
level: 90
section: Glossary
depth: 101
summary: "A decentralized approach in which business domains own their data and publish it as products under shared governance."
related:
  - "[[Unity Catalog]]"
  - "[[Catalogs Schemas and Tables]]"
  - "[[OpenSharing]]"
  - "[[Accounts and Workspaces]]"
  - "[[Data Governance]]"
aliases:
  - "data products"
  - "domain-oriented data ownership"
last_verified: 2026-10-25
tags:
  - glossary
  - flashcards
---

# Data Mesh

> [!eli5] Summary
> In a data mesh, each department manages and publishes its own data for others to use, following company-wide rules, instead of one central team handling all data.

**In data work:** Data mesh rests on four principles: domain ownership (the team that knows the data owns it), data as a product (documented, reliable, with internal customers), self-service infrastructure, and federated governance (shared rules enforced consistently). It is an organizational model more than a technology, and it targets organizations with many data-producing teams. A small business with one data team rarely needs it.

**In Databricks:** Databricks supports mesh-style designs through [[Unity Catalog]]: a catalog per domain with its own owners ([[Catalogs Schemas and Tables]]), workspaces per team attached to one metastore ([[Accounts and Workspaces]]), and central policies and auditing. [[OpenSharing]] (formerly Delta Sharing) publishes data products to other teams or organizations without copying.

Seen in: [[Unity Catalog]], [[Catalogs Schemas and Tables]], [[OpenSharing]], [[Data Governance]]

## Recall

What are the four principles of data mesh?::Domain ownership, data as a product, self-service infrastructure, and federated governance.
Which Unity Catalog object commonly maps to a data mesh domain?::A catalog.

> [!sources]- Sources (last verified: 2026-10-25)
> - [What is Data Mesh? (Databricks glossary)](https://www.databricks.com/glossary/data-mesh)
> - [Databricks Lakehouse and Data Mesh, Part 1 (Databricks blog)](https://www.databricks.com/blog/databricks-lakehouse-and-data-mesh-part-1)
