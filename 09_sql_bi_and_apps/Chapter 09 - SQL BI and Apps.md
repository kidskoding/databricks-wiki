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

> [!story] Previously
> [[Chapter 08 - Data Engineering|Chapter 08]] ended with pipelines we can trust: data arrives through [[Lakeflow Connect]], flows through bronze, silver, and gold layers, runs on a schedule in [[Lakeflow Jobs]], and is checked by [[Testing Data Pipelines|tests]] before anyone sees it. The tables are clean and governed by [[Unity Catalog]]. But so far only engineers can use them. The people who actually run the business are still waiting for a number.

**Analysts and app builders, covering Databricks SQL, dashboards, Genie, Power BI, Databricks Apps, and Lakebase.**

## The story of this chapter

Every chapter so far has been about getting data *in*: storing it, processing it, organizing it, and governing it. This chapter is about getting answers *out*, to the people who never open a notebook.

Think about who asks questions in a business. The owner of a three-store bakery wants yesterday's sales by store on her phone before the shops open. The finance manager wants the same revenue number in Power BI that the operations team sees in its own report. A shift supervisor wants a message the moment one store's sales fall below normal. None of them writes Python, and most of them should never need to write SQL either.

In the old world of [[The Two-Tier Architecture Problem|two tiers]], serving these people meant copying data out of the lake into a separate [[Data Warehouses|data warehouse]], then pointing [[BI Tools|BI tools]] at the copy. The lakehouse removes the copy, but only if the lakehouse can do the warehouse's job as well as a warehouse does. That is where the chapter starts.

**First, a warehouse on the lake.** [[Databricks SQL]] gives analysts compute built for SQL: [[SQL Warehouses|SQL warehouses]] that start in seconds on serverless, a browser-based [[SQL Editor]], and query history. Because a dashboard is the same question asked again and again, speed depends on two things you can learn to read: the query profile and the caches ([[Query Performance and Caching]]).

**Next, answers for people who do not write SQL.** [[AI-BI Dashboards]] turn saved queries into pages of charts that can be shared beyond the data team. [[Genie]] goes a step further and lets someone type a question in plain English and get a table or a chart back. Both raise an old problem in a new form. If the dashboard, Genie, and Power BI each compute "revenue" their own way, the business gets three different answers. [[Metric Views]] fix that by defining a metric once in Unity Catalog, so every tool computes it the same way. [[SQL Alerts]] close the loop by watching a number and sending a message when it crosses a line, so nobody has to remember to look.

**Then, the tools the business already owns.** Most companies did not arrive at Databricks with an empty desk. They have years of reports in Power BI, Tableau, or Excel. Rebuilding all of them on day one would be a waste. [[Connecting Power BI]] and [[Connecting Tableau and Other BI Tools]] show how those tools query the same governed tables over standard [[JDBC and ODBC|drivers]], and [[Partner Connect]] shortens the setup for common partner products.

**After that, the line between analytics and applications blurs.** [[AI Functions in SQL]] let an analyst call a [[LLM|large language model]] from a SQL query, for example to sort a thousand customer reviews by mood without writing any code outside SQL. [[Databricks Apps]] let a team host a small internal web app, such as a stock-reorder form, right next to the data it uses. Apps need somewhere to save what users type, and an analytical lakehouse table is the wrong shape for thousands of tiny, fast writes ([[OLTP vs OLAP]]). [[Lakebase]] adds a managed Postgres database for that job inside the platform.

**Finally, one front door.** With dashboards, Genie spaces, and apps all in place, a business user needs one simple place to find them without wading through the engineer's workspace. That place is [[Databricks One]].

By the end of the chapter, the bakery owner opens her phone and sees "daily sales by store", asks a follow-up question in plain words, and gets an alert when the downtown shop has a bad morning. All of it reads the same tables the engineers built in chapter 08, under the same permissions.

That covers looking backward: what sold, where, and when. The next question is about looking forward. People can now query and chart their data, so what about predictions and AI? Can the platform forecast next week's sales, recommend what to reorder, or answer customers on its own? That is [[Chapter 10 - AI and ML]].

## Notes in reading order

<!-- GENERATED:reading-order START (scripts/scaffold.py) -->

| # | Note | Depth | What it covers |
|---|---|---|---|
| 1 | [[Databricks SQL]] | 101 Beginner | Databricks' data warehouse experience, with SQL warehouses, editor, dashboards, and alerts. |
| 2 | [[SQL Editor]] | 101 Beginner | Writing, running, and sharing queries in the browser. |
| 3 | [[Query Performance and Caching]] | 301 Advanced | Query profiles, result and disk caches, and why a query is slow. |
| 4 | [[AI-BI Dashboards]] | 101 Beginner | Databricks' native dashboards, built with AI help and shareable with anyone. |
| 5 | [[Genie]] | 101 Beginner | Asking questions of your data in plain English and getting answers and charts. |
| 6 | [[Metric Views]] | 301 Advanced | Defining a business metric once in Unity Catalog so every tool computes it the same way. |
| 7 | [[SQL Alerts]] | 201 Practitioner | Getting an email or Slack message when a number crosses a line. |
| 8 | [[Connecting Power BI]] | 201 Practitioner | Live and import connections from Power BI to Databricks, and publishing from Unity Catalog. |
| 9 | [[Connecting Tableau and Other BI Tools]] | 201 Practitioner | Tableau, Looker, Sigma, Excel, and anything with JDBC or ODBC. |
| 10 | [[Partner Connect]] | 201 Practitioner | One-click trials and connections to Fivetran, dbt, Power BI, and other partners. |
| 11 | [[AI Functions in SQL]] | 201 Practitioner | Calling LLMs from plain SQL to classify, summarize, extract, and translate. |
| 12 | [[Databricks Apps]] | 201 Practitioner | Hosting internal web apps in Streamlit, Dash, React, and others right next to your data. |
| 13 | [[Lakebase]] | 301 Advanced | A managed Postgres database (OLTP) inside the lakehouse, for apps and agents. |
| 14 | [[Databricks One]] | 101 Beginner | The simplified business-user home for dashboards, Genie, and apps. |

<!-- GENERATED:reading-order END -->

> [!nextup] Up next
> [[Databricks SQL]]
