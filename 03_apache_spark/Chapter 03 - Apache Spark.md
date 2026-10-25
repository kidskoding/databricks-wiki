---
type: chapter
status: stub
part: 1
level: 3
section: Apache Spark
summary: The faster, friendlier engine born at UC Berkeley that replaced MapReduce and became Databricks' foundation.
prev: "[[The Pain of Hadoop]]"
next: "[[AMPLab and the Birth of Spark]]"
notes:
  - "[[AMPLab and the Birth of Spark]]"
  - "[[Apache Spark]]"
  - "[[RDDs]]"
  - "[[Lazy Evaluation]]"
  - "[[Transformations and Actions]]"
  - "[[DataFrames]]"
  - "[[Spark SQL]]"
  - "[[Catalyst Optimizer]]"
  - "[[Tungsten]]"
  - "[[Driver and Executors]]"
  - "[[Partitions]]"
  - "[[Shuffles]]"
  - "[[Jobs Stages and Tasks]]"
  - "[[PySpark]]"
  - "[[Structured Streaming]]"
  - "[[MLlib]]"
  - "[[Adaptive Query Execution]]"
  - "[[Spark Connect]]"
  - "[[Spark UI]]"
last_verified:
tags:
  - chapter
---

# Chapter 03 - Apache Spark

> [!story] Previously
> (to write)

**The faster, friendlier engine born at UC Berkeley that replaced MapReduce and became Databricks' foundation.**

## The story of this chapter

(to write)

## Notes in reading order

<!-- GENERATED:reading-order START (scripts/scaffold.py) -->

| # | Note | Depth | What it covers |
|---|---|---|---|
| 1 | [[AMPLab and the Birth of Spark]] | 101 Beginner | How a Berkeley research lab built Spark in 2009, and how its creators went on to found Databricks. |
| 2 | [[Apache Spark]] | 101 Beginner | The open-source engine for processing big data in memory across a cluster. |
| 3 | [[RDDs]] | 301 Advanced | Resilient distributed datasets, Spark's original low-level building block. |
| 4 | [[Lazy Evaluation]] | 201 Practitioner | Why Spark plans the whole job before running any of it. |
| 5 | [[Transformations and Actions]] | 201 Practitioner | The two kinds of Spark operations, ones that describe work and ones that trigger it. |
| 6 | [[DataFrames]] | 101 Beginner | Tables in code, the main way people use Spark today. |
| 7 | [[Spark SQL]] | 101 Beginner | Running SQL on Spark, the bridge from Hive to Databricks SQL. |
| 8 | [[Catalyst Optimizer]] | 301 Advanced | The query planner that rewrites your code into a faster plan. |
| 9 | [[Tungsten]] | 401 Expert | Spark's memory and code-generation engine work, the precursor to Photon. |
| 10 | [[Driver and Executors]] | 201 Practitioner | The boss process and the worker processes in every Spark cluster. |
| 11 | [[Partitions]] | 201 Practitioner | How Spark slices data so many machines can work on it at once. |
| 12 | [[Shuffles]] | 301 Advanced | Moving data between machines, the most expensive thing Spark does. |
| 13 | [[Jobs Stages and Tasks]] | 301 Advanced | How Spark breaks one query into units of work you can see in the Spark UI. |
| 14 | [[PySpark]] | 101 Beginner | Spark from Python, the most-used Spark interface. |
| 15 | [[Structured Streaming]] | 201 Practitioner | Spark's engine for treating a live stream like a table that keeps growing. |
| 16 | [[MLlib]] | 201 Practitioner | Spark's built-in machine-learning library. |
| 17 | [[Adaptive Query Execution]] | 301 Advanced | Spark re-planning a query mid-flight based on what it learns. |
| 18 | [[Spark Connect]] | 301 Advanced | The client-server split that lets thin clients talk to Spark remotely. |
| 19 | [[Spark UI]] | 201 Practitioner | The built-in web page for seeing what a Spark job did and why it was slow. |

<!-- GENERATED:reading-order END -->

> [!nextup] Up next
> [[AMPLab and the Birth of Spark]]
