---
type: chapter
status: written
part: 1
level: 1
section: Foundations
summary: The words and ideas everything else is built on, such as data, tables, SQL, files, and the cloud.
prev: "[[Building a Business Case]]"
next: "[[What Is Data]]"
notes:
  - "[[What Is Data]]"
  - "[[Structured vs Unstructured Data]]"
  - "[[Files and File Formats]]"
  - "[[CSV and JSON]]"
  - "[[Spreadsheets]]"
  - "[[Relational Databases]]"
  - "[[SQL]]"
  - "[[Primary and Foreign Keys]]"
  - "[[OLTP vs OLAP]]"
  - "[[Data Modeling Basics]]"
  - "[[Star Schema]]"
  - "[[Servers and the Cloud]]"
  - "[[Storage vs Compute]]"
  - "[[Python for Data]]"
  - "[[APIs]]"
  - "[[ETL vs ELT]]"
  - "[[Batch vs Streaming]]"
last_verified: 2026-10-25
tags:
  - chapter
---

# Chapter 01 - Foundations

> [!story] Context
> [[Chapter 00 - Is Databricks for You|Chapter 00]] ended with [[Building a Business Case]] for a data platform. This chapter defines the concepts that the rest of the vault assumes: data, file formats, relational databases, SQL, data models, the cloud, and data pipelines. No prior technical background is required.

**The words and ideas everything else is built on, such as data, tables, SQL, files, and the cloud.**

## The story of this chapter

The concepts in this chapter predate Databricks and big data. They describe how a single business records, stores, and analyzes information, and they still underlie every feature covered in later chapters.

**Data and its shape.** [[What Is Data]] defines data as recorded facts and introduces records, fields, types, and grain. [[Structured vs Unstructured Data]] classifies data by how much fixed structure it has: tables, semi-structured formats such as JSON, and unstructured files such as PDFs, images, and audio.

**Files.** All data is stored as files at some level. [[Files and File Formats]] explains text versus binary and row versus column layouts, and why the format choice affects speed and cost. [[CSV and JSON]] covers the two plain-text formats used most often to exchange data, and their lack of enforced types. [[Spreadsheets]] covers the tool most small businesses use as their first data system, and the limits that appear when it becomes a shared system of record.

**Databases and SQL.** E. F. Codd's 1970 relational model, the basis of [[Relational Databases]], replaced pointer-based record systems with tables linked by shared values and introduced data independence. [[SQL]] is the declarative language for querying and changing those tables. [[Primary and Foreign Keys]] give rows stable identifiers and let tables reference each other. These notes also introduce the Databricks equivalents: tables governed by [[Unity Catalog]], informational key constraints with `RELY`, and [[Lakebase]] for operational Postgres workloads.

**Two kinds of workload.** [[OLTP vs OLAP]] separates systems that run a business (many small transactions) from systems that analyze it (large scans and aggregations). The two need different storage layouts and schemas, which is why organizations copy operational data into a separate analytical store. [[Data Modeling Basics]] covers how to choose tables, grain, and relationships, including normalization. [[Star Schema]] describes the standard analytical model of fact and dimension tables, which Databricks places at the gold layer of the [[Medallion Architecture]].

**Infrastructure.** [[Servers and the Cloud]] covers the shift from owned hardware to computing rented on demand from Microsoft, Amazon, and Google. [[Storage vs Compute]] explains why separating durable storage from temporary processing power lets a business keep all of its data at low cost and pay for compute only while it runs. This separation is the main architectural idea behind data lakes, the lakehouse, and Databricks.

**Working with data.** [[Python for Data]] introduces Python and pandas for tasks that SQL does not cover well, such as file cleanup, API calls, and machine learning. [[APIs]] explains how programs retrieve data from SaaS applications, the main source of data for most small businesses. [[ETL vs ELT]] describes the two patterns for moving data into an analytical store, and why cloud platforms made load-then-transform the common default. [[Batch vs Streaming]] covers pipeline cadence: scheduled chunks, continuous processing, or incremental runs that combine the two.

**Limits at the end of this chapter.** Every tool in this chapter assumes that one machine can store and process the data. A single database server scales by buying a larger server, and pandas holds all of its data in the memory of one computer. In the early 2000s, web companies produced data volumes that no single machine could hold or process in reasonable time. [[Chapter 02 - The Big Data Era]] covers the distributed systems built in response, starting with Google's papers and Apache Hadoop.

## Notes in reading order

<!-- GENERATED:reading-order START (scripts/scaffold.py) -->

| # | Note | Depth | What it covers |
|---|---|---|---|
| 1 | [[What Is Data]] | 101 Beginner | Data as recorded facts, and why businesses keep it. |
| 2 | [[Structured vs Unstructured Data]] | 101 Beginner | Tables versus documents, images, audio, and logs, and the semi-structured data in between. |
| 3 | [[Files and File Formats]] | 101 Beginner | What a file format is and why the choice of format decides how fast and cheap data is to use. |
| 4 | [[CSV and JSON]] | 101 Beginner | The two most common plain-text data formats and their limits at scale. |
| 5 | [[Spreadsheets]] | 101 Beginner | Why Excel runs the world, and where it breaks. |
| 6 | [[Relational Databases]] | 101 Beginner | Tables with rules and relationships, managed by software like Postgres, MySQL, and SQL Server. |
| 7 | [[SQL]] | 101 Beginner | The language for asking databases questions, and why it is still the most important data skill. |
| 8 | [[Primary and Foreign Keys]] | 101 Beginner | How rows get IDs and how tables point at each other. |
| 9 | [[OLTP vs OLAP]] | 201 Practitioner | Systems that run the business versus systems that analyze it. |
| 10 | [[Data Modeling Basics]] | 201 Practitioner | Deciding which tables to have and how they connect, covering normalization, entities, and grain. |
| 11 | [[Star Schema]] | 201 Practitioner | Fact and dimension tables, the classic shape for analytics. |
| 12 | [[Servers and the Cloud]] | 101 Beginner | Computers you rent by the minute from Microsoft, Amazon, or Google. |
| 13 | [[Storage vs Compute]] | 101 Beginner | The split between where data sits and what crunches it, the most important idea in modern data. |
| 14 | [[Python for Data]] | 101 Beginner | Why Python and pandas became the default language for data work. |
| 15 | [[APIs]] | 101 Beginner | How software talks to other software, and how most SaaS data gets pulled out. |
| 16 | [[ETL vs ELT]] | 101 Beginner | Extract, transform, load, and why the order flipped in the cloud. |
| 17 | [[Batch vs Streaming]] | 101 Beginner | Processing data in scheduled chunks versus continuously as it arrives. |

<!-- GENERATED:reading-order END -->

> [!nextup] Next
> [[What Is Data]]
