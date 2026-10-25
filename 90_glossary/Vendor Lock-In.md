---
type: glossary
status: written
level: 90
section: Glossary
depth: 101
summary: "Being so tied to one vendor's product that leaving would be slow, costly, or risky."
related:
  - "[[Open Table Formats]]"
  - "[[Open Source]]"
  - "[[Delta Lake]]"
  - "[[Delta UniForm]]"
  - "[[Apache Iceberg]]"
  - "[[Databricks vs Alternatives for Small Teams]]"
aliases:
  - "lock-in"
  - "vendor lock in"
  - "proprietary lock-in"
last_verified: 2026-10-25
tags:
  - glossary
  - flashcards
---

# Vendor Lock-In

> [!eli5] Summary
> Vendor lock-in is dependence on one vendor's product to the point where switching away is slow, costly, or risky.

**In data work:** Lock-in comes from proprietary data formats, vendor-specific code and SQL dialects, contracts, and the skills a team builds around one tool. Lock-in is a trade-off: deep integration can save work, but it means losing bargaining power and paying a large migration cost if prices rise or the product no longer fits. Ways to reduce it include storing data in open formats in storage you control, keeping code in [[Git]], and using standard SQL. A small business that keeps its sales history only inside a SaaS tool's export-limited database is locked in.

**In Databricks:** Databricks reduces data lock-in by storing tables as open [[Delta Lake]] files in your own cloud storage, readable by other engines, and [[Delta UniForm]] lets [[Apache Iceberg]] clients read the same tables (see [[Open Table Formats]]). Code in [[Apache Spark]], [[MLflow]], and SQL is portable. Proprietary pieces such as [[Photon]], serverless, and some AI features are not, so evaluate them as a deliberate choice.

Seen in: [[Open Table Formats]], [[Delta UniForm]], [[Databricks vs Alternatives for Small Teams]]

## Recall

Vendor Lock-In::Dependence on one vendor that makes switching costly; open formats in your own storage reduce it.
