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

> [!story] Context
> The [[Migration Checklist]] is the last note in the story, which covers more than 300 notes in total. Most readers do not need every note or the full story order. This chapter defines a shorter route for each kind of reader.

**Curated routes through the graph for each kind of reader, from total beginner to expert.**

## The story of this chapter

The vault has two organizing schemes. Learning paths build on both.

1. **Story order.** Chapters 00 to 15 are one chronological story: data basics, the Hadoop era, Spark, the modern data stack, the lakehouse, then Databricks itself, the three clouds, administration, and migration. Each note's `prev` and `next` links follow this order. Story order explains *why* each tool exists, because each tool addresses a problem from the previous chapter.
2. **Depth tiers.** Every note carries a `depth`: **101** (beginner, no background needed), **201** (practitioner, you use it at work), **301** (advanced, you design or tune it), and **401** (expert, uncommon edge cases). Depth indicates difficulty, not importance.

A **learning path** selects the notes one persona needs, orders them to build skill, and groups them into 3 to 5 **stages** that progress from 101 toward 301 and 401. Each stage ends with a `[!check]` checkpoint: a small, real task in a Databricks workspace. Most checkpoints work in [[Databricks Free Edition and Trials|Free Edition]]; the admin and cloud checkpoints need a trial or paid workspace on your cloud. If you complete the checkpoint, continue to the next stage. If not, review the stage again.

To use a path:

1. **Choose one path by role.** If you are unsure, start with [[Path - Absolute Beginner]]. Small-business readers can use [[Path - Business Owner]] or [[Path - One-Person Data Team]].
2. **Follow the links, not the folders.** A path moves between chapters. When a note refers to an earlier concept, its `[!story]` callout and `prev` link point to it.
3. **Leave the rabbit holes for later.** Each path lists optional side topics, including the cloud deep dives ([[Path - Azure Deep Dive]], [[Path - AWS Deep Dive]], [[Path - Google Cloud Deep Dive]]).
4. **Review the Recall sections.** Every concept note ends with flashcards. Review them with the Spaced Repetition plugin to retain what you read.

Paths link only to existing notes. Some linked notes may still be stubs; those have `status: stub` in their frontmatter.

## Notes in reading order

<!-- GENERATED:reading-order START (scripts/scaffold.py) -->

| # | Note | Depth | What it covers |
|---|---|---|---|
| 1 | [[Path - Absolute Beginner]] | 101 Beginner | Zero to "I get what Databricks is" in about 20 notes. |
| 2 | [[Path - Business Owner]] | 101 Beginner | Everything a decision-maker needs, covering fit, cost, risk, and the first 30 days. |
| 3 | [[Path - Analyst]] | 101 Beginner | From Excel and SQL to Databricks SQL, dashboards, Genie Agents, and Power BI. |
| 4 | [[Path - Data Engineer]] | 201 Practitioner | Ingestion, the lakehouse, pipelines, orchestration, and CI/CD. |
| 5 | [[Path - Data Scientist and ML Engineer]] | 201 Practitioner | Notebooks, Spark, MLflow, the feature store, and serving. |
| 6 | [[Path - AI App Developer]] | 201 Practitioner | LLMs, RAG, AI Search, agents, Databricks Apps, and Lakebase. |
| 7 | [[Path - Platform Admin]] | 301 Advanced | Accounts, identity, Unity Catalog, networking, and cost controls on your cloud. |
| 8 | [[Path - One-Person Data Team]] | 101 Beginner | The shortest route for a small business with one data person doing every job. |
| 9 | [[Path - Azure Deep Dive]] | 301 Advanced | Every Azure-specific rabbit hole in order. |
| 10 | [[Path - AWS Deep Dive]] | 301 Advanced | Every AWS-specific rabbit hole in order. |
| 11 | [[Path - Google Cloud Deep Dive]] | 301 Advanced | Every Google Cloud-specific rabbit hole in order. |
| 12 | [[Path - Certification Prep]] | 301 Advanced | Which Databricks certifications exist and which notes map to each exam. |

<!-- GENERATED:reading-order END -->

> [!nextup] Next
> [[Path - Absolute Beginner]]
