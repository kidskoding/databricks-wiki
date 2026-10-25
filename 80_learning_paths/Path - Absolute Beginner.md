---
type: path
status: written
level: 80
section: Learning Paths
depth: 101
summary: Zero to "I get what Databricks is" in about 20 notes.
personas:
  - everyone
chapter: "[[Chapter 80 - Learning Paths]]"
prev: "[[Chapter 80 - Learning Paths]]"
next: "[[Path - Business Owner]]"
evolved_from: []
evolved_into: []
cloud_equivalent: []
related:
  - "[[What Databricks Is in Plain English]]"
  - "[[Databricks Free Edition and Trials]]"
  - "[[SQL]]"
  - "[[Storage vs Compute]]"
  - "[[Apache Spark]]"
  - "[[The Two-Tier Architecture Problem]]"
  - "[[The Lakehouse Idea]]"
  - "[[Delta Lake]]"
  - "[[Notebooks]]"
  - "[[Unity Catalog]]"
  - "[[Medallion Architecture]]"
  - "[[Genie]]"
  - "[[Path - Business Owner]]"
  - "[[Path - Analyst]]"
  - "[[Path - Data Engineer]]"
  - "[[Path - One-Person Data Team]]"
aliases:
  - Beginner Path
  - Start From Zero
prereqs: []
unlocks:
  - "[[Path - Analyst]]"
  - "[[Path - Data Engineer]]"
  - "[[Path - Business Owner]]"
  - "[[Path - Data Scientist and ML Engineer]]"
clouds:
  - aws
  - azure
  - gcp
mastery: new
last_verified: 2026-10-25
tags:
  - path
---

# Path - Absolute Beginner

> [!persona] Who this is for
> **Who:** anyone who has heard the word "Databricks" and has no data background. A student, a manager, a career switcher, a curious owner.
> **Goal:** understand what Databricks is, why it exists, and what people do in it, without drowning in jargon.
> **Outcome:** in about 20 notes and a few hours, you can explain Databricks to a friend, log in to a free workspace, run a query, save a table, and build a tiny dashboard.

## Before you start

You need nothing but curiosity and a browser. No SQL, no Python, no cloud account. For the checkpoints, sign up for [[Databricks Free Edition and Trials|Databricks Free Edition]], which is free and needs no credit card. Read each note's `[!eli5]` block first; skip the `[!deepdive]` blocks on this path.

## The route

### Stage 1: What data is, and where it lives (101)

**Goal:** learn the five ideas every other note assumes.

1. [[What Databricks Is in Plain English]]: the one-page answer, so you know where you are heading.
2. [[What Is Data]]: data is recorded facts; everything starts here.
3. [[SQL]]: the language for asking a table a question, and still the most useful data skill.
4. [[Servers and the Cloud]]: Databricks runs on computers rented from Microsoft, Amazon, or Google.
5. [[Storage vs Compute]]: the split between where data sits and what crunches it, the most important idea in the vault.
6. [[Databricks Free Edition and Trials]]: how to get a workspace to practice in today.

> [!check] Checkpoint
> Sign up for Free Edition and open the **SQL Editor**. Run `SELECT * FROM samples.nyctaxi.trips LIMIT 10;`, then `SELECT COUNT(*) FROM samples.nyctaxi.trips;`. You just asked a table two questions. If the `samples` catalog is missing, open **Catalog** in the left bar and pick any sample table you see.

### Stage 2: How we got here (101)

**Goal:** see the problem Databricks was built to solve.

1. [[The Three Vs of Big Data]]: why one computer stopped being enough.
2. [[The Pain of Hadoop]]: the first answer worked, but it was slow and hard to run.
3. [[Apache Spark]]: the faster engine from UC Berkeley that Databricks' founders built.
4. [[The Two-Tier Architecture Problem]]: companies kept two copies of data, a lake and a warehouse, and paid twice.
5. [[The Lakehouse Idea]]: one copy of data that is both cheap and reliable.

> [!check] Checkpoint
> In Free Edition, create a **notebook** and run one cell of SQL and one cell of Python:
> ```python
> df = spark.table("samples.nyctaxi.trips")
> display(df.groupBy("pickup_zip").count().orderBy("count", ascending=False).limit(5))
> ```
> Both cells ran on Spark. Write one sentence in a text cell explaining why that matters for a table with billions of rows.

### Stage 3: Databricks itself (101)

**Goal:** know the main parts of the platform by name.

1. [[The Data Intelligence Platform]]: Databricks' name for the lakehouse plus AI that understands your data.
2. [[Accounts and Workspaces]]: the company account and the rooms teams work in.
3. [[Compute Types]]: the different kinds of "engine" you can attach to work.
4. [[Serverless Compute]]: compute Databricks runs for you, which is what Free Edition uses.
5. [[Notebooks]]: the documents where code, results, and notes live together.
6. [[Delta Lake]]: the table format under every Databricks table.

> [!check] Checkpoint
> In your notebook, save the result of a query as your own table:
> ```sql
> CREATE OR REPLACE TABLE busiest_zips AS
> SELECT pickup_zip, COUNT(*) AS trips
> FROM samples.nyctaxi.trips
> GROUP BY pickup_zip;
> ```
> Find `busiest_zips` in **Catalog** and look at its **History** tab. That history is Delta Lake at work.

### Stage 4: Finding, trusting, and using data (101 to 201)

**Goal:** see how data is organized, governed, and turned into answers.

1. [[Unity Catalog]]: one place that knows every table and who may see it.
2. [[Three-Level Namespace]]: `catalog.schema.table`, the address of everything.
3. [[Medallion Architecture]]: bronze, silver, and gold layers from raw to business-ready.
4. [[AI-BI Dashboards]]: charts built in Databricks and shared with anyone.
5. [[Genie]]: ask a question in plain English and get an answer and a chart.
6. [[Time Travel]] (201): look at a table as it was before, and undo mistakes.

> [!check] Checkpoint
> Build a one-chart **dashboard** on `busiest_zips`. Then create a **Genie space** on the same table and ask "Which five zip codes have the most trips?". Finally, run `DESCRIBE HISTORY busiest_zips;` and `SELECT * FROM busiest_zips VERSION AS OF 0 LIMIT 5;`.

## Rabbit holes

- **More history:** [[AMPLab and the Birth of Spark]], [[The Founding of Databricks]], [[Apache Hadoop]], and the [[Timeline of Data Engineering]].
- **More basics:** [[Structured vs Unstructured Data]], [[Spreadsheets]], [[Relational Databases]], [[Python for Data]], [[Data Warehouses]], [[Data Lakes]].
- **AI in one sitting:** [[Machine Learning Basics]], [[Generative AI and LLMs]], [[Databricks Assistant]].
- **Money:** [[How Databricks Pricing Works]] and [[DBUs]].
- **Your cloud:** [[Choosing a Cloud for Databricks]], then [[Azure Databricks Overview]], [[Databricks on AWS Overview]], or [[Databricks on Google Cloud Overview]]. The full cloud routes are [[Path - Azure Deep Dive]], [[Path - AWS Deep Dive]], and [[Path - Google Cloud Deep Dive]].
- **Name changes:** [[Databricks Product Names and Renames]], because Databricks renames things often.

## You are done when

- You can explain, without notes, what Databricks is and what problem the lakehouse solves.
- You can say the difference between storage and compute, and between a lake and a warehouse.
- You can log in to a workspace, run SQL in the editor, and run a notebook cell.
- You have created your own table and found it in the catalog by its three-part name.
- You have built a dashboard and asked Genie a question.
- You know which path to take next: [[Path - Analyst]], [[Path - Data Engineer]], [[Path - Data Scientist and ML Engineer]], [[Path - Business Owner]], or [[Path - One-Person Data Team]].

> [!nextup] Up next
> Running a business and deciding whether Databricks is worth it? Continue with [[Path - Business Owner]].

> [!sources]- Sources (last verified: 2026-10-25)
> - Route assembled on 2026-10-25 from the vault index (`llms.txt`) and the persona tags in `_meta/manifest.yaml`. Product facts and official documentation links live in each linked note's `[!sources]` callout.
> - Checkpoints use Free Edition features (SQL Editor, notebooks on serverless, the `samples` catalog, dashboards, Genie). Feature availability in Free Edition was not re-checked for this path; see [[Databricks Free Edition and Trials]] and use a trial workspace if something is missing.
