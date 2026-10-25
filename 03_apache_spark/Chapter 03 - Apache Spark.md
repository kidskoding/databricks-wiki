---
type: chapter
status: written
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
last_verified: 2026-10-25
tags:
  - chapter
---

# Chapter 03 - Apache Spark

> [!story] Context
> [[Chapter 02 - The Big Data Era|Chapter 02]] ended with [[The Pain of Hadoop]]. Hadoop processed large datasets on commodity machines, but every [[MapReduce]] step wrote its output to disk, which made iterative and interactive workloads slow and complex programs hard to write. This chapter covers Apache Spark, the in-memory engine that replaced MapReduce and became the foundation of Databricks.

**The faster, friendlier engine born at UC Berkeley that replaced MapReduce and became Databricks' foundation.**

## The story of this chapter

**Era.** Apache Spark started in 2009 at UC Berkeley's AMPLab, when [[Apache Hadoop]] was the standard platform for large-scale data processing. Hadoop's [[MapReduce]] model stored intermediate results on disk between steps so that work could survive machine failures. That design made iterative algorithms (such as machine-learning training) and interactive queries in [[Apache Hive]] slow, and anything beyond a simple map and reduce required chaining many jobs.

**Problem.** Memory is much faster than disk, but data held in memory is lost when a machine fails. A faster engine needed a way to keep data in memory across a cluster and still recover from failures without replicating everything.

**Core abstraction.** Matei Zaharia's research produced [[Apache Spark]] and the [[RDDs|resilient distributed dataset]] (RDD), described in an NSDI 2012 paper. An RDD records the transformations used to build it (its lineage). When a partition is lost, Spark recomputes only that partition from the lineage. This made in-memory processing fault tolerant. Two execution principles follow from it:

- [[Lazy Evaluation]]: Spark records operations as a plan and runs nothing until a result is requested.
- [[Transformations and Actions]]: every operation either adds a step to the plan or requests a result.

**Structured APIs and optimization.** [[DataFrames]] and [[Spark SQL]] added named, typed columns and standard SQL, and replaced Hive as the common way to run SQL on large datasets. The [[Catalyst Optimizer]] rewrites each query into an efficient plan, [[Tungsten]] improves CPU and memory efficiency through binary memory management and code generation, and [[Adaptive Query Execution]] (Spark 3.0) re-optimizes plans at runtime using actual data sizes.

**Execution model.** A [[Driver and Executors|driver]] plans the work and executors run it. Data is divided into [[Partitions]] processed in parallel. [[Shuffles]] move data between machines for grouping and joining and are the most expensive operation. Each query runs as [[Jobs Stages and Tasks|jobs, stages, and tasks]], which the [[Spark UI]] displays for diagnosis.

**One engine for many workloads.** [[PySpark]] provides the Python API. [[Structured Streaming]] runs the same DataFrame queries on continuously arriving data. [[MLlib]] provides distributed machine learning. [[Spark Connect]] (Spark 3.4) separates client applications from the Spark server; Databricks serverless compute and Databricks Connect are built on it.

**Current state.** Spark 4.0 made ANSI SQL behavior the default and expanded Spark Connect. Spark 4.1 (December 2025) added Spark Declarative Pipelines and a real-time mode for Structured Streaming. Spark 4.2 (July 2026) is the current release as of October 2026. The Spark creators founded Databricks in 2013 ([[The Founding of Databricks]]), and every Databricks cluster runs Spark inside the [[Databricks Runtime]].

**Limitation carried forward.** Spark improved processing but not storage. Data in a data lake remained plain files without transactions: concurrent writers could corrupt a table, failed jobs could leave partial output, row-level updates were impractical, and there was no shared catalog or access control. Organizations therefore kept a separate data warehouse for reporting and copied data between the two systems. [[Chapter 04 - The Modern Data Stack]] covers that two-tier architecture and the tools built around it.

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

> [!nextup] Next
> [[AMPLab and the Birth of Spark]] covers the research lab where Spark was created and the founding of Databricks.
