---
type: glossary
status: written
level: 90
section: Glossary
depth: 101
summary: "Splitting data into separate related tables so each fact is stored only once."
related:
  - "[[Denormalization]]"
  - "[[Relational Databases]]"
  - "[[Primary and Foreign Keys]]"
  - "[[Data Modeling Basics]]"
  - "[[Star Schema]]"
  - "[[OLTP vs OLAP]]"
aliases:
  - "normalisation"
  - "normal forms"
  - "3NF"
  - "third normal form"
last_verified: 2026-10-25
tags:
  - glossary
  - flashcards
---

# Normalization

> [!eli5] Summary
> Normalization is a way of designing database tables so each fact is stored in exactly one place. Changes then happen in one place instead of many.

**In data work:** Normalization is a way of designing [[Relational Databases|relational]] tables so that each piece of information lives in one place, linked by [[Primary and Foreign Keys|keys]]. Instead of repeating the customer's name and address on every order row, you keep a customers table and an orders table with a customer ID. The levels are called normal forms; third normal form (3NF) is the usual target for transactional systems. It prevents update mistakes and saves space, but answering a question may need many [[Join|joins]]. Its opposite, [[Denormalization|denormalization]], copies data into wider tables to make reading faster.

**In Databricks:** Source systems you ingest into Databricks (a shop's Postgres or SQL Server database) are usually normalized. In the lakehouse you often keep that shape in the silver layer, then denormalize into a [[Star Schema|star schema]] or wide tables in gold for dashboards (see [[Medallion Architecture]] and [[Data Modeling Basics]]). [[OLTP vs OLAP]] explains why each side prefers its shape.

Seen in: [[Data Modeling Basics]], [[Relational Databases]], [[Star Schema]]

## Recall

Normalization::Designing tables so each fact is stored once and linked by keys; good for transactional systems, while analytics often denormalizes.
