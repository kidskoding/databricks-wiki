---
type: glossary
status: written
level: 90
section: Glossary
depth: 101
summary: "A user-defined function: your own code that runs inside a query like a built-in function."
related:
  - "[[Spark SQL]]"
  - "[[PySpark]]"
  - "[[Pandas]]"
  - "[[Serialization]]"
  - "[[Photon]]"
  - "[[Catalogs Schemas and Tables]]"
aliases:
  - "user-defined function"
  - "UDFs"
  - "pandas UDF"
  - "Python UDF"
  - "SQL UDF"
  - "UDAF"
last_verified: 2026-10-25
tags:
  - glossary
  - flashcards
---

# UDF

> [!eli5] Summary
> A UDF (user-defined function) is a custom function you write and then call in queries like a built-in function.

**In data work:** Query engines ship with built-in functions (`UPPER`, `SUM`, `DATE_TRUNC`). A user-defined function lets you add your own, such as a function that turns a messy phone number into a standard format. UDFs can be written in SQL, Python, Scala, or Java. They are convenient but can be slow: the engine cannot optimize code it does not understand, and a Python UDF must send rows between the engine and Python (see [[Serialization]]). Vectorized pandas UDFs reduce that cost by processing batches with Apache Arrow. Use a built-in function when one exists.

**In Databricks:** In Databricks you can create SQL and Python functions as [[Unity Catalog]] objects (`CREATE FUNCTION catalog.schema.name ...`), so they are governed and shared like tables (see [[Catalogs Schemas and Tables]]). In [[PySpark]] you can also define session-scoped Python and [[Pandas|pandas]] UDFs. Python UDFs in Unity Catalog need a serverless or pro SQL warehouse or Databricks Runtime 13.3 LTS or above. [[Photon]] does not support UDFs, so those parts of a query fall back to the standard Spark engine; Databricks advises native functions first and pandas UDFs when you must write Python.

Seen in: [[Spark SQL]], [[PySpark]], [[Catalogs Schemas and Tables]]

## Recall

UDF::A user-defined function written in SQL, Python, or Scala and called in queries; prefer built-ins, since Python UDFs add serialization cost.

> [!sources]- Sources (last verified: 2026-10-25)
> - [What are user-defined functions (UDFs)? (AWS)](https://docs.databricks.com/aws/en/udf/)
> - [SQL and Python UDFs in Unity Catalog (AWS)](https://docs.databricks.com/aws/en/udf/unity-catalog)
> - [Batch Python UDFs in Unity Catalog (Azure Databricks)](https://learn.microsoft.com/en-us/azure/databricks/udf/python-batch-udf)
> - [What is Photon? (AWS)](https://docs.databricks.com/aws/en/compute/photon)
