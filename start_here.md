---
type: hub
status: written
summary: The home page. Pick a door by who you are, or read the whole story from chapter 00.
related:
  - "[[Chapter 00 - Is Databricks for You]]"
  - "[[Timeline of Data Engineering]]"
  - "[[Persona Map]]"
tags: [hub]
---

# Databricks Brain

**A second brain for Databricks, from "what is a table?" to private networking on three clouds.**

It is written for anyone who knows nothing about data and wants to understand Databricks fast. That includes a small-business owner deciding whether to move onto it, the one person who will run it, and the engineer who wants every detail.

> [!eli5] What this is
> A big, linked notebook. Every page explains one idea in plain words first, then gets deeper. The pages link to each other like a map, so you can follow whatever you are curious about.

## Pick your door

| If you are... | Start here |
|---|---|
| Brand new to data | [[Path - Absolute Beginner]] |
| A business owner deciding on Databricks | [[Path - Business Owner]] |
| The one data person at a small company | [[Path - One-Person Data Team]] |
| An analyst who lives in Excel, SQL, or Power BI | [[Path - Analyst]] |
| A data engineer | [[Path - Data Engineer]] |
| A data scientist or ML engineer | [[Path - Data Scientist and ML Engineer]] |
| Building AI apps or agents | [[Path - AI App Developer]] |
| The admin, IT, or security person | [[Path - Platform Admin]] |
| Studying for a Databricks certification | [[Path - Certification Prep]] |

Every note has a **depth**: `101` beginner, `201` practitioner, `301` advanced, `401` expert. Read the 101s first. Each note's collapsed "Going deeper" box holds its expert material.

## The front door

- [[Chapter 00 - Is Databricks for You]]: who uses it, what it costs, and when it is the wrong choice.

## Part 1: The story

Read these in order and the platform makes sense, because each tool exists to fix the last one's pain.

| # | Chapter | The question it answers |
|---|---|---|
| 01 | [[Chapter 01 - Foundations\|Foundations]] | What are data, tables, SQL, and the cloud? |
| 02 | [[Chapter 02 - The Big Data Era\|The Big Data Era]] | What happens when data no longer fits on one computer? |
| 03 | [[Chapter 03 - Apache Spark\|Apache Spark]] | How did big data get fast and friendly? |
| 04 | [[Chapter 04 - The Modern Data Stack\|The Modern Data Stack]] | Why did companies end up with a lake *and* a warehouse? |
| 05 | [[Chapter 05 - The Lakehouse\|The Lakehouse]] | Can one system be both? |
| 06 | [[Chapter 06 - The Databricks Platform\|The Databricks Platform]] | What is Databricks, physically? |
| 07 | [[Chapter 07 - Unity Catalog and Governance\|Unity Catalog & Governance]] | Who can see what, and where did this number come from? |
| 08 | [[Chapter 08 - Data Engineering\|Data Engineering]] | How does data get in and stay clean? |
| 09 | [[Chapter 09 - SQL BI and Apps\|SQL, BI & Apps]] | How do people actually use the data? |
| 10 | [[Chapter 10 - AI and ML\|AI & ML]] | How do models and agents use the data? |

## Part 2: The clouds and running it

Databricks runs on all three major clouds. The ideas are the same everywhere, but the plumbing is different.

| # | Chapter | Why you would go here |
|---|---|---|
| 11 | [[Chapter 11 - Azure Databricks\|Azure Databricks]] | You are a Microsoft shop (Entra ID, Power BI, Azure bill) |
| 12 | [[Chapter 12 - Databricks on AWS\|Databricks on AWS]] | You run on Amazon Web Services |
| 13 | [[Chapter 13 - Databricks on Google Cloud\|Databricks on Google Cloud]] | You run on Google Cloud or BigQuery |
| 14 | [[Chapter 14 - Admin Security and Cost\|Admin, Security & Cost]] | You keep it safe and keep the bill sane |

Compare the clouds side by side in [[Cloud Comparison - Azure vs AWS vs GCP]].

## Part 3: Moving in

- [[Chapter 15 - Migrating to Databricks]]: playbooks for moving from spreadsheets, SQL Server, Snowflake, Redshift, BigQuery, or Hadoop.

## Hubs that tie it together

- [[Timeline of Data Engineering]]: every milestone on one page
- [[Open Source vs Databricks - Who Replaced What]]: the old tool and its Databricks successor
- [[Databricks Product Names and Renames]]: Databricks renames things often, so check here
- [[Persona Map]]: every note, grouped by who needs it
- [[Chapter 80 - Learning Paths]]: all learning paths
- Glossary: one short note per jargon word, in `90_glossary/`

## Progress

![[Vault Progress.base]]

> [!info]- For AI agents
> This vault is built to be read by agents as well as people. Start with `AGENTS.md` (how the vault is organized and how to answer from it) and `llms.txt` (a one-line map of every note). `_meta/vault_index.json` has every note and typed edge.
