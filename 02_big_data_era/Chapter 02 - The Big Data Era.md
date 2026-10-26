---
type: chapter
status: written
part: 1
level: 2
section: The Big Data Era
summary: When data outgrew one computer, from Google's papers to Hadoop and the pain that came with it.
prev: "[[Batch vs Streaming]]"
next: "[[The Three Vs of Big Data]]"
notes:
  - "[[The Three Vs of Big Data]]"
  - "[[Scaling Up vs Scaling Out]]"
  - "[[Distributed Systems]]"
  - "[[Google File System and MapReduce Papers]]"
  - "[[Apache Hadoop]]"
  - "[[HDFS]]"
  - "[[MapReduce]]"
  - "[[YARN]]"
  - "[[Apache Hive]]"
  - "[[Hive Metastore]]"
  - "[[Apache HBase]]"
  - "[[Cloudera and Hortonworks]]"
  - "[[Columnar Storage]]"
  - "[[Apache Parquet]]"
  - "[[Apache ORC]]"
  - "[[The Pain of Hadoop]]"
last_verified: 2026-10-25
tags:
  - chapter
---

# Chapter 02 - The Big Data Era

> [!story] Context
> [[Chapter 01 - Foundations|Chapter 01]] covers data on a single machine: files, [[Relational Databases|relational databases]], [[SQL]], and [[Batch vs Streaming|batch versus streaming]] processing. This chapter covers the period, roughly 2003 to the late 2010s, when data outgrew single machines and the industry adopted distributed storage and processing on clusters of commodity servers.

**When data outgrew one computer, from Google's papers to Hadoop and the pain that came with it.**

## The story of this chapter

This chapter covers the big data era: the problem, the Hadoop stack built to solve it, and the limitations that led to Apache Spark.

### The problem

In the early 2000s, web search, e-commerce, and server logs produced data that exceeded the storage and processing capacity of one server. The difficulty is usually described with three properties, [[The Three Vs of Big Data|volume, velocity, and variety]]. Buying a larger machine has a hard ceiling and rising cost, so the alternative was to [[Scaling Up vs Scaling Out|scale out]] across many inexpensive machines. Scaling out requires software that partitions data, coordinates work, and recovers from routine machine failure, which is the subject of [[Distributed Systems]].

### The designs

Google published two peer-reviewed papers describing its internal systems ([[Google File System and MapReduce Papers]]):

| Year | Paper | Contribution |
|---|---|---|
| 2003 | *The Google File System* (SOSP) | Large files split into 64 MB chunks, replicated across commodity machines, with a single metadata master |
| 2004 | *MapReduce* (OSDI) | A programming model in which users write `map` and `reduce` functions and the runtime handles distribution and failures |

Google did not release the software. The papers served as designs for open-source implementations.

### The Hadoop stack

[[Apache Hadoop]] implemented both designs as open source and became an Apache top-level project in January 2008. A typical deployment combined several layers:

| Layer | Component | Function |
|---|---|---|
| Storage | [[HDFS]] | Files split into replicated blocks (typically 128 MB, three copies) tracked by a NameNode |
| Processing | [[MapReduce]] | Batch jobs in map, shuffle, and reduce phases |
| Resource management | [[YARN]] | Cluster scheduling, generally available in Hadoop 2.2.0 (October 2013) |
| SQL | [[Apache Hive]] | HiveQL compiled to cluster jobs, created at Facebook |
| Catalog | [[Hive Metastore]] | Shared table definitions, later adopted by Spark and early Databricks |
| Key-value access | [[Apache HBase]] | Low-latency row access, modeled after Google's Bigtable |
| File formats | [[Columnar Storage\|Columnar]] formats [[Apache Parquet]] and [[Apache ORC]] | Column-oriented files that reduce data read by analytical queries (both from 2013) |

Most enterprises ran these components as a vendor distribution. [[Cloudera and Hortonworks]], the two largest vendors, announced an all-stock merger in October 2018 and completed it in January 2019.

### The limitations

[[The Pain of Hadoop]] summarizes the problems that accumulated in production:

1. **Performance:** MapReduce writes intermediate data to disk between every step, so multi-step and iterative jobs are slow, and Hive queries take minutes.
2. **Programming effort:** Simple computations require Java classes for map, reduce, and job configuration.
3. **Coupled storage and compute:** Each node holds disks and CPUs, so clusters are sized for peak load and run continuously.
4. **Operations:** Many separately versioned projects require specialist teams and make upgrades risky.
5. **Governance and updates:** Permissions are split across tools, and files cannot be updated reliably in place.

### What comes next

These limitations define the next chapters. [[Chapter 03 - Apache Spark|Chapter 03]] covers [[Apache Spark]], the in-memory engine from UC Berkeley that replaced MapReduce. Later chapters cover cloud [[Object Storage|object storage]] replacing HDFS, [[Delta Lake]] adding transactions on Parquet files, and [[Unity Catalog]] replacing the Hive Metastore.

> [!note] Verification status
> Historical facts in this chapter come from the original papers, Apache project documentation and Apache Software Foundation board records, and company filings. Claims that no allowed source could confirm were removed from the individual notes.

## Notes in reading order

<!-- GENERATED:reading-order START (scripts/scaffold.py) -->

| # | Note | Depth | What it covers |
|---|---|---|---|
| 1 | [[The Three Vs of Big Data]] | 101 Beginner | Volume, velocity, and variety, the three ways data got too big for one machine. |
| 2 | [[Scaling Up vs Scaling Out]] | 101 Beginner | Buying a bigger computer versus using many small ones. |
| 3 | [[Distributed Systems]] | 201 Practitioner | Many computers acting as one, and the new failure modes that come with it. |
| 4 | [[Google File System and MapReduce Papers]] | 201 Practitioner | The 2003 and 2004 Google papers that started the big data era. |
| 5 | [[Apache Hadoop]] | 101 Beginner | The open-source system that let ordinary companies store and process huge data on cheap machines. |
| 6 | [[HDFS]] | 201 Practitioner | Hadoop's distributed file system, which splits files into replicated blocks across many machines. |
| 7 | [[MapReduce]] | 201 Practitioner | Hadoop's map-then-reduce processing model, which was powerful, slow, and painful to write. |
| 8 | [[YARN]] | 301 Advanced | Hadoop's resource manager, which decides which job gets which machines. |
| 9 | [[Apache Hive]] | 201 Practitioner | SQL on Hadoop, which made big data queryable by analysts. |
| 10 | [[Hive Metastore]] | 201 Practitioner | The table directory Hive introduced, which Spark and early Databricks inherited. |
| 11 | [[Apache HBase]] | 301 Advanced | A fast key-value database on top of HDFS, modeled after Google Bigtable. |
| 12 | [[Cloudera and Hortonworks]] | 201 Practitioner | The companies that sold supported Hadoop, and why they merged in 2019. |
| 13 | [[Columnar Storage]] | 201 Practitioner | Storing data column by column so analytics reads only what it needs. |
| 14 | [[Apache Parquet]] | 201 Practitioner | The open columnar file format underneath Delta Lake, Iceberg, and most of the lakehouse. |
| 15 | [[Apache ORC]] | 301 Advanced | Hive's columnar format, Parquet's sibling and rival. |
| 16 | [[The Pain of Hadoop]] | 101 Beginner | Why Hadoop clusters became slow, expensive, and hard to staff, which set the stage for Spark and the cloud. |

<!-- GENERATED:reading-order END -->

> [!nextup] Next
> [[The Three Vs of Big Data]] defines the three properties that made data too large for a single machine.
