---
type: concept
status: stub
level: 15
section: Migrating to Databricks
depth: 101
summary: Moving a spreadsheet-run business into governed tables, with file uploads, Volumes, a first dashboard, and Genie.
personas:
  - solo
  - analyst
  - owner
chapter: "[[Chapter 15 - Migrating to Databricks]]"
prev: "[[Assessing Your Current Data Estate]]"
next: "[[Migrating from SQL Server]]"
evolved_from:
  - "[[Spreadsheets]]"
evolved_into: []
cloud_equivalent: []
related:
  - "[[Signs You Have Outgrown Spreadsheets]]"
  - "[[Volumes]]"
  - "[[Catalogs Schemas and Tables]]"
  - "[[AI-BI Dashboards]]"
  - "[[Genie]]"
  - "[[Databricks One]]"
  - "[[Single Source of Truth]]"
  - "[[CSV and JSON]]"
  - "[[Databricks Free Edition and Trials]]"
aliases:
  - Excel to Databricks
  - Access to Databricks
  - Migrating from Spreadsheets
prereqs:
  - "[[Spreadsheets]]"
  - "[[What Is Data]]"
  - "[[SQL]]"
unlocks:
  - "[[AI-BI Dashboards]]"
  - "[[Genie]]"
  - "[[Volumes]]"
clouds:
  - aws
  - azure
  - gcp
mastery: new
last_verified:
tags:
  - concept
  - flashcards
---

# Migrating from Excel and Access

Mastery: `INPUT[inlineSelect(option(new), option(learning), option(solid)):mastery]`

> [!todo] Draft, not yet verified
> This body is an unverified draft. Its facts were checked against the open-source Lakebridge repo, the Terraform provider, and the Databricks SDK, which the vault's source policy does not accept. It must be re-verified against docs.databricks.com, learn.microsoft.com/azure/databricks, or databricks.com before `status: written` is set. Do not answer from it.

> [!story] Previously
> [[Assessing Your Current Data Estate]] gave us an inventory. For many small businesses, that inventory is mostly spreadsheets on a shared drive and one Microsoft Access file that "only Linda knows how to use". This is the gentlest migration in the chapter, and a good first one even for companies with bigger systems.

> [!eli5] In one breath
> Right now your business lives in many separate spreadsheet files that people copy, email, and overwrite. Moving to Databricks means putting each list (customers, orders, products) in one shared place where everyone sees the same numbers, nobody overwrites anyone, and you can ask questions in plain English.

> [!analogy] Analogy: from a filing cabinet of notebooks to one library
> - **Each Excel file** is a personal notebook. Useful, but everyone has their own copy, and the copies disagree.
> - **A table** is one official ledger on a library shelf. Everyone reads the same one.
> - **A [[Volumes|Volume]]** is the library's document drawer, where the original files (PDFs, the raw spreadsheets) are kept safely.
> - **A [[Catalogs Schemas and Tables|catalog and schema]]** are the library floor and the shelf: `finance.sales` is "finance floor, sales shelf".
> - **A [[AI-BI Dashboards|dashboard]]** is the noticeboard by the entrance that updates itself.
> - **[[Genie]]** is the librarian you can ask, "How many orders did we ship in March?"

## Why it exists

Spreadsheets are a great way to start a business and a painful way to run one past a certain size. The usual signs (see [[Signs You Have Outgrown Spreadsheets]]):

- Three versions of `Customers_FINAL_v3.xlsx` and nobody sure which is right.
- Monthly reports take two days of copy-paste.
- A formula breaks silently when someone inserts a column.
- Files get too big to open, or Access hits its 2 GB file limit.
- Nobody can say who changed a number, or when.

Moving to tables gives you a [[Single Source of Truth|single source of truth]], history, permissions, and dashboards that refresh themselves.

## What it actually is

There are only four things to learn:

| Old world | New world in Databricks | Why it is better |
|---|---|---|
| An Excel sheet or an Access table | A **table** in [[Unity Catalog]], such as `finance.sales.orders` | One copy, typed columns, history ([[Time Travel]]), permissions |
| A folder of files on a shared drive | A **[[Volumes\|Volume]]**, such as `/Volumes/finance/sales/raw_files/` | Files are governed and can be loaded with SQL |
| A pivot table or chart | An **[[AI-BI Dashboards\|AI/BI dashboard]]** | Refreshes from the table; shareable by link |
| "Ask Linda" | A **[[Genie]] space** | Ask questions in plain English, get a table or chart |

Access is a little different because it is a database *and* an app. Its **tables** become Databricks tables, its **queries** become SQL views, and its **forms and reports** have to be rebuilt, usually as dashboards, or as a small [[Databricks Apps|Databricks App]] if people type data in.

## How it works

```mermaid
flowchart LR
  A["Excel / Access"] --> B["Tidy the sheet<br/>one header row"]
  B --> C["Save as CSV<br/>(or keep .xlsx)"]
  C --> D["Upload in the UI<br/>creates a table"]
  C --> E["Or drop in a Volume<br/>load with SQL"]
  D --> F["AI/BI dashboard"]
  E --> F
  F --> G["Genie space<br/>plain-English questions"]
```

### Step 0: get a workspace and a place to put things

If you do not have Databricks yet, start with [[Databricks Free Edition and Trials]]. Then ask whoever set it up (or do it yourself) to create a catalog and schema. In the [[SQL Editor]]:

```sql
CREATE CATALOG IF NOT EXISTS finance;
CREATE SCHEMA  IF NOT EXISTS finance.sales;
```

### Step 1: tidy each sheet before moving it

Tables are stricter than spreadsheets. Ten minutes of tidying saves hours later:

- **One table per sheet, one header row.** Delete titles, notes, and blank rows above the headers.
- **No merged cells, no subtotal rows, no colour-as-data.** "Red means overdue" must become a column called `is_overdue`.
- **Simple column names.** `Order Date` becomes `order_date`. Avoid symbols such as `%`, `#`, and `/`.
- **One kind of value per column.** Dates are all dates; amounts are all numbers (no "TBC" in a price column).
- **Save as CSV (UTF-8)** if you want the most predictable result. Databricks has been adding direct Excel support; check the file-upload page in your workspace to see whether `.xlsx` is accepted, but CSV always works.

### Step 2a: the easy way, upload through the UI

1. In the left sidebar, click **New**, then **Add or upload data**.
2. Choose **Create or modify table** (the file upload option).
3. Drag your CSV in. Databricks previews the rows and guesses each column's [[Data Type|type]].
4. Pick the catalog `finance` and schema `sales`, name the table `orders`, check the types (dates as `DATE`, money as `DECIMAL`), and click **Create table**.

That is it: you now have `finance.sales.orders`. Menu labels can move slightly between releases, but the flow is the same.

### Step 2b: the repeatable way, a Volume plus SQL

When the same file arrives every week, keep the raw files in a [[Volumes|Volume]] and load them with SQL so the process is repeatable:

```sql
-- A governed folder for raw files
CREATE VOLUME IF NOT EXISTS finance.sales.raw_files;
```

Upload files into it from **Catalog** (Catalog Explorer): open `finance` → `sales` → `raw_files`, then **Upload to this volume**. Then:

```sql
-- Peek at the files before loading
SELECT * FROM read_files(
  '/Volumes/finance/sales/raw_files/orders/',
  format => 'csv', header => true
) LIMIT 20;

-- Create a table from every CSV in the folder
CREATE OR REPLACE TABLE finance.sales.orders AS
SELECT
  CAST(order_id   AS BIGINT)        AS order_id,
  CAST(order_date AS DATE)          AS order_date,
  customer_name,
  CAST(amount     AS DECIMAL(12,2)) AS amount
FROM read_files('/Volumes/finance/sales/raw_files/orders/',
                format => 'csv', header => true);
```

For files that keep arriving, [[COPY INTO]] loads only new files each time you run it, and [[Auto Loader]] does the same continuously.

### Step 3: turn formulas into SQL

Most spreadsheet formulas have a direct SQL equivalent, and once written they never break when someone inserts a column.

| Excel / Access | SQL in Databricks |
|---|---|
| `VLOOKUP` / `XLOOKUP` | `JOIN` on the key column |
| `SUMIFS(amount, region, "West")` | `SUM(amount) ... WHERE region = 'West'` or `GROUP BY region` |
| Pivot table | `GROUP BY` (or let the dashboard do it) |
| `IF(x > 0, "yes", "no")` / Access `IIf()` | `CASE WHEN x > 0 THEN 'yes' ELSE 'no' END` or `if(x > 0, 'yes', 'no')` |
| Access `Nz(x, 0)` | `coalesce(x, 0)` |
| Access `"A" & "B"` | `concat('A', 'B')` or `'A' \|\| 'B'` |
| Access `LIKE "Smi*"` | `LIKE 'Smi%'` |
| Access date literal `#2026-03-01#` | `DATE'2026-03-01'` |

A saved Access query becomes a view:

```sql
CREATE OR REPLACE VIEW finance.sales.monthly_revenue AS
SELECT date_trunc('MONTH', o.order_date) AS month,
       c.region,
       SUM(o.amount) AS revenue
FROM finance.sales.orders o
JOIN finance.sales.customers c ON o.customer_id = c.customer_id
GROUP BY ALL;
```

**Getting data out of Access:** for each table, use **External Data → Export → Text File** (CSV with field names on the first row), then upload as above. Export queries as SQL text so you can rewrite them as views.

### Step 4: a first dashboard

1. Click **New → Dashboard**.
2. On the **Data** tab, add a dataset: pick the `monthly_revenue` view, or write a short SQL query.
3. On the canvas, add a visual: a bar chart of `revenue` by `month`, coloured by `region`. You can also describe the chart you want in words and let the assistant draft it.
4. Add a filter widget for `region`, then **Publish** and share it with your team.

See [[AI-BI Dashboards]] for more. Business users who only read dashboards can use [[Databricks One]], a simpler view of the same workspace.

### Step 5: a Genie space for plain-English questions

1. Click **Genie → New**, and add the tables `orders`, `customers`, and the `monthly_revenue` view.
2. Add a few lines of instructions, such as "Revenue means the sum of `amount`. Our fiscal year starts in April."
3. Ask: "What were our top 5 customers by revenue last quarter?" Genie writes the SQL, runs it, and shows the answer. You can check the SQL it used.

Good table and column descriptions make Genie much more accurate, so add them in Catalog Explorer.

> [!smallbiz] For a small business
> A realistic first week for a 10-person shop: Monday, tidy the three spreadsheets that matter most (customers, orders, products). Tuesday, upload them and check the types. Wednesday, write two views that replace your monthly copy-paste report. Thursday, build one dashboard. Friday, open a Genie space and let the owner ask questions.
>
> **What it costs:** storing small tables costs very little; you pay mainly when compute runs, measured in [[DBUs]]. A [[SQL Warehouses|serverless SQL warehouse]] with [[Auto Termination|auto-stop]] only bills while queries run. See [[Estimating Costs for a Small Business]].
>
> **What to keep in Excel:** quick one-off analysis is fine in Excel. Connect Excel to Databricks through [[JDBC and ODBC|ODBC]] to read the official tables instead of copying them.

## On each cloud

> [!azure]- Azure Databricks
> Nothing differs in the steps. Many Excel and Access users are already on Microsoft 365, so once tables exist, Power BI connects to them directly; see [[Power BI on Azure Databricks]] and [[Connecting Power BI]]. Sign-in uses your Microsoft Entra ID work account.

> [!aws]- Databricks on AWS
> Nothing differs in the steps. Upload, Volumes, dashboards, and Genie work the same way.

> [!gcp]- Databricks on Google Cloud
> Nothing differs in the steps. If your spreadsheets live in Google Sheets, export them as CSV first.

## Going deeper

> [!deepdive]- Expert notes (301–401)
> - **Data entry needs a new home.** Dashboards are read-only. If people typed data into Access forms, give them a small app ([[Databricks Apps]]) backed by a table, or an OLTP database such as [[Lakebase]], rather than letting them edit tables by hand.
> - **Schema drift in weekly files.** When someone adds a column to next week's file, `read_files` and [[Auto Loader]] can evolve the schema. Decide whether that should fail loudly or be accepted; see [[Schema Enforcement and Evolution]].
> - **Types matter for money.** Use `DECIMAL(p, s)` for currency, never `DOUBLE`, or totals drift by fractions of a cent.
> - **Keep the raw files.** Leaving the original files in the Volume gives you an audit trail and lets you rebuild a table if a load goes wrong.
> - **Access relationships.** Access enforces relationships; Databricks lets you declare [[Primary and Foreign Keys|primary and foreign keys]] (informational, not enforced). Declare them anyway: they help Genie and BI tools understand joins.

## Common confusions

> [!confusion] Uploading a file is not linking to it
> An uploaded CSV becomes a copy inside a table. Editing the original Excel file afterwards does not change the table. Re-upload, or use a Volume plus [[COPY INTO]] for recurring files.

> [!confusion] A Volume is not a table
> A [[Volumes|Volume]] holds files exactly as they are. A table holds rows and columns you can query. You usually keep files in a Volume and load them into tables.

## Recall

What does an Excel sheet become in Databricks?::A table in Unity Catalog, addressed as catalog.schema.table.
What is a Volume?::A governed folder in Unity Catalog for storing files, with paths like /Volumes/catalog/schema/volume/.
What SQL replaces VLOOKUP?::A JOIN on the key column.
What SQL function reads CSV files from a Volume?::`read_files`, for example `read_files('/Volumes/finance/sales/raw_files/', format => 'csv', header => true)`.
What becomes of a saved Access query?::A SQL view.
What replaces Access's Nz(x, 0)?::`coalesce(x, 0)`
Which data type should you use for money?::DECIMAL, never DOUBLE.
What is Genie?::A Databricks feature where people ask questions about tables in plain English and get answers backed by generated SQL.
Why tidy a sheet before uploading?::Tables need one header row, one value type per column, and no merged cells or subtotal rows.

## Where next

> [!path] Learning path
> **Needs first:** [[Spreadsheets]], [[What Is Data]], [[SQL]]
> **Unlocks next:** [[AI-BI Dashboards]], [[Genie]], [[Volumes]]

> [!nextup] Up next in the story
> Spreadsheets are where many businesses start, but the most common next step up is a SQL Server database. [[Migrating from SQL Server]] shows how to query it in place first and replicate it after.

> [!sources]- Sources (not yet verified under the source policy)
> - [Managed vs external volumes (Databricks, AWS)](https://docs.databricks.com/aws/en/volumes/managed-vs-external)
> - [Volumes (Databricks)](https://docs.databricks.com/en/connect/unity-catalog/volumes.html)
> - [Volumes REST API (Databricks)](https://docs.databricks.com/api/workspace/volumes)
> - [AI/BI dashboards (Databricks)](https://docs.databricks.com/en/dashboards/index.html)
> - [Auto Loader schema inference and evolution (Databricks, AWS)](https://docs.databricks.com/aws/en/ingestion/cloud-object-storage/auto-loader/schema#how-does-auto-loader-schema-evolution-work)
> - Note: the upload-UI menu names and Genie steps follow the vault's existing descriptions; the official upload and Genie pages could not be re-checked on 2026-10-25 (search unavailable). Confirm labels in your workspace.
