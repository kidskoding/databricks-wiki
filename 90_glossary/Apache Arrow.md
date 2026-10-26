---
type: glossary
status: written
level: 90
section: Glossary
depth: 101
summary: "An open, columnar in-memory data format that lets tools such as Spark and pandas exchange data without slow row-by-row conversion."
related:
  - "[[PySpark]]"
  - "[[Pandas]]"
  - "[[Columnar Storage]]"
  - "[[Serialization]]"
  - "[[UDF]]"
  - "[[Spark Connect]]"
aliases:
  - "Arrow"
  - "PyArrow"
last_verified: 2026-10-26
tags:
  - glossary
  - flashcards
---

# Apache Arrow

> [!eli5] Summary
> Apache Arrow is a shared way of laying out tables in memory. When two programs both understand it, they can pass data to each other quickly instead of translating it piece by piece.

**In data work:** Arrow stores data column by column in memory, the in-memory counterpart of [[Columnar Storage|columnar]] file formats such as [[Apache Parquet]]. Because the layout is standardized, a Java process and a Python process can share batches of rows without per-row [[Serialization|serialization]]. The Python library is `pyarrow`.

**In Databricks:** PySpark uses Arrow to speed up `DataFrame.toPandas()` and `spark.createDataFrame(pandas_df)`, controlled by `spark.sql.execution.arrow.pyspark.enabled`. Apache Spark 4.2 enables it by default; Spark 3.5 did not. Databricks documents it as enabled by default on most compute, with exceptions for some access modes, so set it explicitly when behavior matters. `toPandas()` still collects every row to the driver, so use it only on small results. Pandas [[UDF|UDFs]] also exchange data with Python through Arrow, and [[Spark Connect]] returns results to the client as Arrow-encoded batches.

Small-business example: an analyst pulls a 50,000-row monthly sales summary into pandas for a chart. With Arrow the conversion takes seconds rather than minutes.

Seen in: [[PySpark]], [[Pandas API on Spark]], [[Spark Connect]]

## Recall

What does Apache Arrow standardize?::A columnar in-memory data layout that different tools can share without row-by-row conversion.
Which Spark setting turns on Arrow for toPandas()?::spark.sql.execution.arrow.pyspark.enabled

> [!sources]- Sources (last verified: 2026-10-26)
> - [Apache Arrow in PySpark (spark.apache.org)](https://spark.apache.org/docs/latest/api/python/tutorial/sql/arrow_pandas.html)
> - [Convert between PySpark and pandas DataFrames (AWS)](https://docs.databricks.com/aws/en/pandas/pyspark-pandas-conversion)
> - [Spark Connect Overview (spark.apache.org)](https://spark.apache.org/docs/latest/spark-connect-overview.html)
