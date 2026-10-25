---
type: glossary
status: written
level: 90
section: Glossary
depth: 101
summary: "The planned point in a migration when users and workloads switch from the old system to the new one."
related:
  - "[[Running Old and New in Parallel]]"
  - "[[Migration Strategy Overview]]"
  - "[[Migration Checklist]]"
  - "[[Migrating BI Reports]]"
  - "[[Lift and Shift]]"
  - "[[Lakehouse Federation]]"
aliases:
  - "cut-over"
  - "switchover"
  - "go-live"
last_verified: 2026-10-25
tags:
  - glossary
  - flashcards
---

# Cutover

> [!eli5] Summary
> Cutover is the moment a business stops using its old system and starts using the new one as the official source of data.

**In data work:** In a migration, cutover is when reports, users, and pipelines start reading from the new system and the old one is frozen or retired. It normally follows a period of [[Running Old and New in Parallel|parallel running]] in which outputs from both systems are reconciled. A cutover plan specifies the date, a change freeze on the old system, a checklist of steps, validation checks, and a rollback procedure.

**In Databricks:** A Databricks migration loads and reconciles data, converts code (for example with [[Lakebridge]]), repoints reports ([[Migrating BI Reports]]), runs old and new in parallel, and then cuts over. [[Lakehouse Federation]] can query the source database in place, which allows workloads to move in stages rather than in a single cutover. The [[Migration Checklist]] includes a cutover section.

Seen in: [[Running Old and New in Parallel]], [[Migration Strategy Overview]], [[Migration Checklist]], [[Migrating from SQL Server]]

## Recall

What is a cutover?::The planned switch from the old system to the new one as the system of record.
What should a cutover plan include besides a date?::A change freeze, a step checklist, validation checks, and a rollback procedure.
