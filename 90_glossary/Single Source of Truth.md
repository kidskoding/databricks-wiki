---
type: glossary
status: written
level: 90
section: Glossary
depth: 101
summary: "One agreed, trusted place for each piece of data, so everyone works from the same numbers."
related:
  - "[[The Lakehouse Idea]]"
  - "[[The Two-Tier Architecture Problem]]"
  - "[[Unity Catalog]]"
  - "[[Semantic Layer]]"
  - "[[Medallion Architecture]]"
  - "[[Data Governance]]"
aliases:
  - "SSOT"
  - "single version of the truth"
  - "golden record"
last_verified: 2026-10-25
tags:
  - glossary
  - flashcards
---

# Single Source of Truth

> [!eli5] Summary
> A single source of truth is one agreed, authoritative place for each piece of data. Every report reads from it, so reports agree.

**In data work:** A single source of truth (SSOT) means each important fact (a customer's address, last month's revenue) has one authoritative home and one agreed definition. Copies may exist for speed, but they are derived from the source, not edited separately. Without an SSOT, the same number appears in spreadsheets, a CRM export, and a warehouse, and each says something different. A small chain with three shop managers each keeping their own sales spreadsheet has no SSOT; a central sales table that all reports read from is one.

**In Databricks:** The [[The Lakehouse Idea|lakehouse]] pitch is largely an SSOT pitch: one copy of data in open tables serves BI, data science, and AI, instead of copying it between a lake and a warehouse (see [[The Two-Tier Architecture Problem]]). [[Unity Catalog]] gives one place to find and govern it, gold tables in the [[Medallion Architecture]] hold the trusted versions, and [[Metric Views]] give one definition per metric.

Seen in: [[The Lakehouse Idea]], [[The Two-Tier Architecture Problem]], [[Medallion Architecture]]

## Recall

Single Source of Truth::One authoritative home and definition for each piece of data, so every report uses the same numbers.
