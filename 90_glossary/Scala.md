---
type: glossary
status: written
level: 90
section: Glossary
depth: 101
summary: "A programming language for the Java virtual machine, and the language Apache Spark itself is written in."
related:
  - "[[Apache Spark]]"
  - "[[JVM]]"
  - "[[PySpark]]"
  - "[[DataFrames]]"
  - "[[Databricks Runtime]]"
  - "[[Libraries and Environments]]"
aliases:
  - "Scala language"
last_verified: 2026-10-25
tags:
  - glossary
  - flashcards
---

# Scala

> [!eli5] Summary
> Scala is a programming language that runs on the Java virtual machine. Apache Spark, the engine under Databricks, was originally written in it.

**In data work:** Scala is a statically typed language that mixes object-oriented and functional styles and runs on the [[JVM]], so it can use Java libraries. Apache Spark's core is written in Scala, and early Spark users wrote jobs in Scala for speed and access to the newest APIs. Today most data work on Spark uses Python ([[PySpark]]) or [[SQL]], and the [[DataFrames|DataFrame]] API performs about the same in all three because the engine does the heavy lifting. Scala still appears in older pipelines and in teams with Java backgrounds.

**In Databricks:** Databricks notebooks support Scala alongside Python, SQL, and R, and you can attach JVM libraries (JAR files) through [[Libraries and Environments]]. Support depends on compute: standard access mode supports Scala on Databricks Runtime 13.3 LTS and above, while [[Serverless Compute]] does not run Scala in notebooks but can run Scala packaged as a JAR task. Free Edition does not support Scala. Databricks recommends Python and SQL for new projects.

Seen in: [[Apache Spark]], [[PySpark]], [[AMPLab and the Birth of Spark]]

## Recall

Scala::A JVM programming language that Spark is written in; Databricks supports it, but most new work uses Python or SQL.

> [!sources]- Sources (last verified: 2026-10-25)
> - [Choose a development language (AWS)](https://docs.databricks.com/aws/en/languages/overview)
> - [Serverless compute limitations (AWS)](https://docs.databricks.com/aws/en/compute/serverless/limitations)
> - [Standard compute overview (AWS)](https://docs.databricks.com/aws/en/compute/standard-overview)
