---
type: chapter
status: written
part: 0
level: 0
section: Is Databricks for You?
summary: The front door. Who uses Databricks, what it costs, when it fits a small business, and when it does not.
prev: "[[start_here]]"
next: "[[What Databricks Is in Plain English]]"
notes:
  - "[[What Databricks Is in Plain English]]"
  - "[[Who Uses Databricks - Roles]]"
  - "[[Who Uses Databricks - Business Types]]"
  - "[[Signs You Have Outgrown Spreadsheets]]"
  - "[[When Databricks Is Not the Right Fit]]"
  - "[[Databricks vs Alternatives for Small Teams]]"
  - "[[How Databricks Pricing Works]]"
  - "[[Estimating Costs for a Small Business]]"
  - "[[Databricks Free Edition and Trials]]"
  - "[[Choosing a Cloud for Databricks]]"
  - "[[Your First 30 Days on Databricks]]"
  - "[[Building a Business Case]]"
last_verified: 2026-10-25
tags:
  - chapter
---

# Chapter 00 - Is Databricks for You

> [!story] Context
> This chapter is the entry point for business readers who are deciding whether to adopt Databricks. It follows [[start_here]] and precedes Part 1, which explains the history and technology in chronological order starting with [[Chapter 01 - Foundations]].

**The front door. Who uses Databricks, what it costs, when it fits a small business, and when it does not.**

## The story of this chapter

This chapter answers a practical question before the rest of the vault explains how Databricks works: should a given business use it, what will it cost, and how should the business start. It is written for owners, managers, finance staff, and the one person who runs data at a small company. No technical background is assumed.

**What the platform is.** [[What Databricks Is in Plain English]] defines Databricks as a cloud data platform that stores, transforms, governs, analyzes, and applies AI to an organization's data in one place. It runs on Microsoft Azure, Amazon Web Services, and Google Cloud, stores tables in open formats in cloud object storage, and is billed by usage. The chapters that follow explain why the platform is designed this way: the history of databases, big data, Apache Spark, and the split between data lakes and data warehouses that the lakehouse architecture resolves.

**Who uses it.** [[Who Uses Databricks - Roles]] describes the eight job roles that work in the platform, from the owner who reads dashboards in Genie One (formerly Databricks One) to the engineer who schedules pipelines and the finance user who monitors spend. In a small company one person often covers several roles. [[Who Uses Databricks - Business Types]] maps ten kinds of business, including e-commerce, multi-location retail, franchises, clinics, logistics, manufacturing, SaaS, agencies, nonprofits, and Microsoft-centric organizations, to their usual data sources, the relevant features, and an assessment of fit.

**Whether it fits.** [[Signs You Have Outgrown Spreadsheets]] provides a ten-point checklist of indicators such as conflicting copies, manual consolidation, and key-person dependency. [[When Databricks Is Not the Right Fit]] lists the situations in which a smaller tool, such as an application's own reports, Power BI, Looker Studio, Postgres, or DuckDB, is the better choice. [[Databricks vs Alternatives for Small Teams]] compares Databricks with Snowflake, BigQuery, Microsoft Fabric, Power BI alone, Postgres, and DuckDB or MotherDuck, and provides a weighted scorecard.

**What it costs.** [[How Databricks Pricing Works]] explains the DBU, the SKU that sets the price per DBU for each kind of workload, the retirement of the Standard tier, the difference between serverless and classic compute, and why most customers receive one bill from Databricks and one from the cloud provider (on Azure, both appear on one Microsoft invoice). It also covers pay-as-you-go, committed-use contracts, and Azure prepurchase. [[Estimating Costs for a Small Business]] turns this model into a fill-in formula and worksheet, then corrects the estimate with usage measured during a trial. The vault does not quote prices; each note links to the official pricing pages and calculators.

**How to start.** [[Databricks Free Edition and Trials]] distinguishes Free Edition, the no-cost, non-commercial learning environment launched in June 2025 to replace Community Edition, from the 14-day free trial on each cloud. [[Choosing a Cloud for Databricks]] recommends the cloud the business already uses for identity, data, and billing. [[Your First 30 Days on Databricks]] gives a week-by-week plan that replaces one labor-intensive report with an automated, trusted dashboard. [[Building a Business Case]] uses the measured cost and benefit from that first month to support an approval decision.

**Where the vault goes next.** A reader who decides to proceed needs to understand the concepts the platform is built on. Part 1 begins with [[Chapter 01 - Foundations]] (data, files, databases, SQL, and the cloud), continues through the big data era and Apache Spark to the lakehouse, and introduces the Databricks platform in [[Chapter 06 - The Databricks Platform]]. Readers who prefer a guided route can use [[Path - Business Owner]] or [[Path - One-Person Data Team]].

## Notes in reading order

<!-- GENERATED:reading-order START (scripts/scaffold.py) -->

| # | Note | Depth | What it covers |
|---|---|---|---|
| 1 | [[What Databricks Is in Plain English]] | 101 Beginner | Databricks in one page, with no jargon, for someone who has never heard of it. |
| 2 | [[Who Uses Databricks - Roles]] | 101 Beginner | The eight job roles that log in to Databricks, what each one does there, and which tools they use. |
| 3 | [[Who Uses Databricks - Business Types]] | 101 Beginner | Kinds of businesses, from e-commerce to clinics to factories, that get real value from Databricks, with example use cases. |
| 4 | [[Signs You Have Outgrown Spreadsheets]] | 101 Beginner | The warning signs that a business needs a real data platform instead of Excel, Access, or one reporting tool. |
| 5 | [[When Databricks Is Not the Right Fit]] | 101 Beginner | An honest list of situations where a simpler or cheaper tool is the better choice. |
| 6 | [[Databricks vs Alternatives for Small Teams]] | 201 Practitioner | How Databricks compares with Snowflake, BigQuery, Microsoft Fabric, Power BI alone, and plain Postgres for a small team. |
| 7 | [[How Databricks Pricing Works]] | 101 Beginner | DBUs, SKUs, serverless versus classic, committed use, and why there are usually two bills. |
| 8 | [[Estimating Costs for a Small Business]] | 201 Practitioner | A worked, back-of-the-envelope monthly cost estimate for a small company's first workloads. |
| 9 | [[Databricks Free Edition and Trials]] | 101 Beginner | The free ways to try Databricks (Free Edition and the 14-day trial), what each one includes, and what it leaves out. |
| 10 | [[Choosing a Cloud for Databricks]] | 101 Beginner | How to pick Azure, AWS, or Google Cloud, based mostly on what the business already uses. |
| 11 | [[Your First 30 Days on Databricks]] | 101 Beginner | A week-by-week plan from sign-up to the first trusted dashboard. |
| 12 | [[Building a Business Case]] | 201 Practitioner | How to justify Databricks to a boss or a board, covering costs, savings, risks, and a proof of concept. |

<!-- GENERATED:reading-order END -->

> [!nextup] Next
> [[What Databricks Is in Plain English]] defines the platform without assuming any technical background.
