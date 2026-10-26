---
type: glossary
status: written
level: 90
section: Glossary
depth: 101
summary: "The most popular Python library for working with tables of data on one computer."
related:
  - "[[Python for Data]]"
  - "[[DataFrames]]"
  - "[[PySpark]]"
  - "[[Spreadsheets]]"
  - "[[UDF]]"
  - "[[Notebooks]]"
  - "[[Pandas API on Spark]]"
aliases:
  - "pandas"
  - "pd"
  - "pandas DataFrame"
  - "pandas API on Spark"
  - "Koalas"
last_verified: 2026-10-25
tags:
  - glossary
  - flashcards
---

# Pandas

> [!eli5] Summary
> pandas is a Python library for working with tables of data in code. It runs on one computer, so it is limited by that computer's memory.

**In data work:** pandas is an open-source Python library that gives you a [[DataFrames|DataFrame]]: a table with named columns you can filter, group, join, and reshape in code. It is widely used by analysts and data scientists. Its limit is that it holds all data in the memory of one machine, so it slows or crashes on data much larger than RAM. A florist's analyst might load a year of order CSVs into pandas and compute monthly sales per product in a few lines. When data outgrows one machine, [[PySpark]] spreads the same kind of work across a [[Cluster|cluster]].

**In Databricks:** pandas is preinstalled in [[Databricks Runtime]] and works in [[Notebooks]] as usual. For bigger data there is the pandas API on Spark (`pyspark.pandas`, formerly Koalas), which keeps pandas syntax but runs on Spark. You can convert with `df.toPandas()`, which pulls everything to the driver, so use it only on small results. Pandas UDFs let you run pandas code on chunks of a Spark DataFrame (see [[UDF]]).

Seen in: [[Python for Data]], [[PySpark]], [[DataFrames]]

## Recall

Pandas::A Python library for in-memory tables on one machine; on Databricks, PySpark or the pandas API on Spark handle data too big for it.

> [!sources]- Sources (last verified: 2026-10-25)
> - [Pandas API on Spark (AWS)](https://docs.databricks.com/aws/en/pandas/pandas-on-spark)
> - [Pandas API on Spark (Azure Databricks)](https://learn.microsoft.com/en-us/azure/databricks/pandas/pandas-on-spark)
> - [Pandas API on Apache Spark 3.2 (Databricks blog)](https://www.databricks.com/blog/2021/10/04/pandas-api-on-upcoming-apache-spark-3-2.html)
