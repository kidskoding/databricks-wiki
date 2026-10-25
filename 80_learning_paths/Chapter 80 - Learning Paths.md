---
type: chapter
status: written
part: 4
level: 80
section: Learning Paths
summary: Curated routes through the graph for each kind of reader, from total beginner to expert.
prev: "[[Migration Checklist]]"
next: "[[Path - Absolute Beginner]]"
notes:
  - "[[Path - Absolute Beginner]]"
  - "[[Path - Business Owner]]"
  - "[[Path - Analyst]]"
  - "[[Path - Data Engineer]]"
  - "[[Path - Data Scientist and ML Engineer]]"
  - "[[Path - AI App Developer]]"
  - "[[Path - Platform Admin]]"
  - "[[Path - One-Person Data Team]]"
  - "[[Path - Azure Deep Dive]]"
  - "[[Path - AWS Deep Dive]]"
  - "[[Path - Google Cloud Deep Dive]]"
  - "[[Path - Certification Prep]]"
last_verified: 2026-10-25
tags:
  - chapter
---

# Chapter 80 - Learning Paths

> [!story] Previously
> The [[Migration Checklist]] closed the story: a business has moved its data, its pipelines, and its reports onto Databricks. That story runs to more than 300 notes. Nobody has to read all of them, and almost nobody should read them in order. This chapter gives each kind of reader a shorter road.

**Curated routes through the graph for each kind of reader, from total beginner to expert.**

## The story of this chapter

The vault is organized two ways, and the paths sit on top of both.

1. **Story order.** Chapters 00 to 15 are one chronological story: data basics, the Hadoop era, Spark, the modern data stack, the lakehouse, then Databricks itself, the three clouds, administration, and migration. Each note's `prev` and `next` walk you through it. Story order is the best way to understand *why* things exist, because every tool is the answer to the pain in the chapter before it.
2. **Depth tiers.** Every note carries a `depth`: **101** (beginner, no background needed), **201** (practitioner, you use it at work), **301** (advanced, you design or tune it), and **401** (expert, the rare and sharp edges). Depth tells you how hard a note is, not how important it is.

A **learning path** cuts across both. It picks the notes one persona needs, puts them in an order that builds skill, and groups them into 3 to 5 **stages** that climb from 101 toward 301 and 401. Each stage ends with a `[!check]` checkpoint: a small, real task in a Databricks workspace (most work in [[Databricks Free Edition and Trials|Free Edition]]; the admin and cloud ones need a trial or paid workspace on your cloud). If you can do the checkpoint, move on. If not, re-read the stage.

How to use them:

- **Pick one path by role.** If you are unsure, start with [[Path - Absolute Beginner]]. Small-business readers should look at [[Path - Business Owner]] or [[Path - One-Person Data Team]].
- **Follow the links, not the folders.** A path jumps between chapters. When a note mentions an earlier idea you have not met, its `[!story]` callout and `prev` link take you back.
- **Take the rabbit holes later.** Each path lists optional side trips, including the cloud deep dives ([[Path - Azure Deep Dive]], [[Path - AWS Deep Dive]], [[Path - Google Cloud Deep Dive]]).
- **Use the Recall sections.** Every concept note ends with flashcards. Reviewing them with the Spaced Repetition plugin is the fastest way to make a path stick.

Paths only link to notes that exist. Some linked notes may still be stubs while the vault is being written; a stub's `status: stub` tells you so.

## Notes in reading order

<!-- GENERATED:reading-order START (scripts/scaffold.py) -->

| # | Note | Depth | What it covers |
|---|---|---|---|
| 1 | [[Path - Absolute Beginner]] | 101 Beginner | Zero to "I get what Databricks is" in about 20 notes. |
| 2 | [[Path - Business Owner]] | 101 Beginner | Everything a decision-maker needs, covering fit, cost, risk, and the first 30 days. |
| 3 | [[Path - Analyst]] | 101 Beginner | From Excel and SQL to Databricks SQL, dashboards, Genie, and Power BI. |
| 4 | [[Path - Data Engineer]] | 201 Practitioner | Ingestion, the lakehouse, pipelines, orchestration, and CI/CD. |
| 5 | [[Path - Data Scientist and ML Engineer]] | 201 Practitioner | Notebooks, Spark, MLflow, the feature store, and serving. |
| 6 | [[Path - AI App Developer]] | 201 Practitioner | LLMs, RAG, vector search, agents, Databricks Apps, and Lakebase. |
| 7 | [[Path - Platform Admin]] | 301 Advanced | Accounts, identity, Unity Catalog, networking, and cost controls on your cloud. |
| 8 | [[Path - One-Person Data Team]] | 101 Beginner | The shortest route for a small business with one data person doing every job. |
| 9 | [[Path - Azure Deep Dive]] | 301 Advanced | Every Azure-specific rabbit hole in order. |
| 10 | [[Path - AWS Deep Dive]] | 301 Advanced | Every AWS-specific rabbit hole in order. |
| 11 | [[Path - Google Cloud Deep Dive]] | 301 Advanced | Every Google Cloud-specific rabbit hole in order. |
| 12 | [[Path - Certification Prep]] | 301 Advanced | Which Databricks certifications exist and which notes map to each exam. |

<!-- GENERATED:reading-order END -->

> [!nextup] Up next
> [[Path - Absolute Beginner]]
