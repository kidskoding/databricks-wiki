---
type: glossary
status: written
level: 90
section: Glossary
depth: 101
summary: "Standard database connectivity interfaces that let BI tools, spreadsheets, and applications run SQL against a database through a driver."
related:
  - "[[Connecting Tableau and Other BI Tools]]"
  - "[[Connecting Power BI]]"
  - "[[SQL Warehouses]]"
  - "[[BI Tools]]"
  - "[[Authentication - Tokens and OAuth]]"
  - "[[Lakehouse Federation]]"
aliases:
  - "JDBC"
  - "ODBC"
  - "Java Database Connectivity"
  - "Open Database Connectivity"
  - "database driver"
last_verified: 2026-10-25
tags:
  - glossary
  - flashcards
---

# JDBC and ODBC

> [!eli5] Summary
> JDBC and ODBC are standard ways for programs to connect to a database. Any tool that supports them can query any database that provides a driver.

**In data work:** ODBC (Open Database Connectivity) is a language-independent standard used by Excel and most [[BI Tools]]. JDBC (Java Database Connectivity) is the equivalent standard for Java applications. Each database vendor supplies a driver that implements the standard for its own protocol. A connection is configured with a host, port, path or database, and credentials.

**In Databricks:** Databricks provides its own JDBC and ODBC drivers; Databricks recommends the current Databricks JDBC Driver over the older Simba-based driver. To connect, open a [[SQL Warehouses|SQL warehouse]], select the **Connection details** tab, and copy the **Server hostname**, **Port** (443), and **HTTP path**. A JDBC URL has the form `jdbc:databricks://<server-hostname>:443;httpPath=<http-path>`. Authenticate with OAuth or a personal access token ([[Authentication - Tokens and OAuth]]). The user or service principal needs `CAN USE` on the warehouse, which starts automatically if stopped. See [[Connecting Power BI]] and [[Connecting Tableau and Other BI Tools]].

Seen in: [[Connecting Tableau and Other BI Tools]], [[Connecting Power BI]], [[SQL Warehouses]], [[BI Tools]]

## Recall

What is the difference between JDBC and ODBC?::JDBC is the standard for Java applications; ODBC is language-independent and common in BI tools and Excel.
Which values from a SQL warehouse are needed to configure a driver connection?::Server hostname, port 443, and HTTP path, plus credentials.

> [!sources]- Sources (last verified: 2026-10-25)
> - [Configure a connection using the Databricks JDBC Driver (Azure)](https://learn.microsoft.com/en-us/azure/databricks/integrations/jdbc-oss/configure)
> - [Compute settings for the Databricks ODBC Driver (AWS)](https://docs.databricks.com/aws/en/integrations/odbc/compute)
