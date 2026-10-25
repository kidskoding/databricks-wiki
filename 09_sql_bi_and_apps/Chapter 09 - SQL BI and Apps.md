---
type: chapter
status: written
part: 1
level: 9
section: SQL, BI & Apps
summary: Analysts and app builders, covering Databricks SQL, dashboards, Genie, Power BI, Databricks Apps, and Lakebase.
prev: "[[Testing Data Pipelines]]"
next: "[[Databricks SQL]]"
notes:
  - "[[Databricks SQL]]"
  - "[[SQL Editor]]"
  - "[[Query Performance and Caching]]"
  - "[[AI-BI Dashboards]]"
  - "[[Genie]]"
  - "[[Metric Views]]"
  - "[[SQL Alerts]]"
  - "[[Connecting Power BI]]"
  - "[[Connecting Tableau and Other BI Tools]]"
  - "[[Partner Connect]]"
  - "[[AI Functions in SQL]]"
  - "[[Databricks Apps]]"
  - "[[Lakebase]]"
  - "[[Databricks One]]"
last_verified: 2026-10-25
tags:
  - chapter
---

# Chapter 09 - SQL BI and Apps

> [!story] Context
> [[Chapter 08 - Data Engineering|Chapter 08]] produced reliable pipelines: data arrives through [[Lakeflow Connect]], moves through bronze, silver, and gold layers, runs on a schedule in [[Lakeflow Jobs]], and is checked by [[Testing Data Pipelines|tests]]. The resulting tables are governed by [[Unity Catalog]]. This chapter covers how analysts, business users, and app builders consume those tables.

**Analysts and app builders, covering Databricks SQL, dashboards, Genie, Power BI, Databricks Apps, and Lakebase.**

## The story of this chapter

Chapters 01 to 08 cover getting data into the lakehouse: storage, processing, organization, and governance. This chapter covers getting answers out, to people who do not use notebooks.

In the [[The Two-Tier Architecture Problem|two-tier architecture]], serving business users meant copying data from the lake into a separate [[Data Warehouses|data warehouse]] and pointing [[BI Tools|BI tools]] at the copy. The lakehouse removes the copy only if it performs the warehouse's job. The chapter covers the Databricks features that do that, in five groups.

| Group | Notes | What they provide |
|---|---|---|
| SQL analytics | [[Databricks SQL]], [[SQL Editor]], [[Query Performance and Caching]] | [[SQL Warehouses\|SQL warehouses]], a browser-based editor, query profiles, and caches |
| Native BI | [[AI-BI Dashboards]], [[Genie]], [[Metric Views]], [[SQL Alerts]] | Dashboards, natural-language questions (Genie Agents), shared metric definitions, and threshold notifications |
| External BI tools | [[Connecting Power BI]], [[Connecting Tableau and Other BI Tools]], [[Partner Connect]] | Connections from Power BI, Tableau, Looker, Sigma, and Excel over [[JDBC and ODBC]] and native connectors |
| AI and applications | [[AI Functions in SQL]], [[Databricks Apps]], [[Lakebase]] | [[LLM]] calls from SQL, hosted internal web apps, and a managed Postgres database for [[OLTP vs OLAP\|OLTP]] workloads |
| Business-user entry point | [[Databricks One]] | Genie One (formerly Databricks One): one interface for dashboards, Genie Agents, and apps |

Key points:

- **One copy of the data.** Dashboards, Genie Agents, alerts, and external BI tools all query the same Unity Catalog tables on SQL warehouses, under the same permissions.
- **One definition per metric.** [[Metric Views]] define measures such as revenue once in Unity Catalog, so dashboards, Genie, and Power BI return the same number.
- **Analytical and transactional storage are separate.** Delta tables suit large scans. Apps that save many small records need a row store, which [[Lakebase]] provides.
- **Product names changed in 2026.** Databricks One became Genie (April 2026) and then Genie One (June 2026). Genie spaces became Genie Agents (July 2026). Databricks Assistant became Genie Code (March 2026). See [[Databricks Product Names and Renames]].

The chapter uses one running example: a three-store bakery whose owner reviews "daily sales by store" each morning, asks follow-up questions in plain language, and receives an alert when one store's sales fall below a threshold.

[[Chapter 10 - AI and ML]] moves from describing past results to predictions, models, and AI agents.

## Notes in reading order

<!-- GENERATED:reading-order START (scripts/scaffold.py) -->

| # | Note | Depth | What it covers |
|---|---|---|---|
| 1 | [[Databricks SQL]] | 101 Beginner | Databricks' data warehouse experience, with SQL warehouses, editor, dashboards, and alerts. |
| 2 | [[SQL Editor]] | 101 Beginner | Writing, running, and sharing queries in the browser. |
| 3 | [[Query Performance and Caching]] | 301 Advanced | Query profiles, result and disk caches, and why a query is slow. |
| 4 | [[AI-BI Dashboards]] | 101 Beginner | Databricks' native dashboards, built with AI help and shareable with anyone. |
| 5 | [[Genie]] | 101 Beginner | Genie Agents (formerly Genie spaces): asking questions of your data in plain English and getting answers and charts. |
| 6 | [[Metric Views]] | 301 Advanced | Defining a business metric once in Unity Catalog so every tool computes it the same way. |
| 7 | [[SQL Alerts]] | 201 Practitioner | Getting an email or Slack message when a number crosses a line. |
| 8 | [[Connecting Power BI]] | 201 Practitioner | Live and import connections from Power BI to Databricks, and publishing from Unity Catalog. |
| 9 | [[Connecting Tableau and Other BI Tools]] | 201 Practitioner | Tableau, Looker, Sigma, Excel, and anything with JDBC or ODBC. |
| 10 | [[Partner Connect]] | 201 Practitioner | One-click trials and connections to Fivetran, dbt, Power BI, and other partners. |
| 11 | [[AI Functions in SQL]] | 201 Practitioner | Calling LLMs from plain SQL to classify, summarize, extract, and translate. |
| 12 | [[Databricks Apps]] | 201 Practitioner | Hosting internal web apps in Streamlit, Dash, React, and others right next to your data. |
| 13 | [[Lakebase]] | 301 Advanced | A managed Postgres database (OLTP) inside the lakehouse, for apps and agents. |
| 14 | [[Databricks One]] | 101 Beginner | Genie One (formerly Databricks One): the simplified business-user home for dashboards, Genie Agents, and apps. |

<!-- GENERATED:reading-order END -->

> [!nextup] Next
> [[Databricks SQL]] introduces the SQL warehouse, the editor, and the warehouse types.
