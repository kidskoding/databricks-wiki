---
type: chapter
status: stub
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
last_verified:
tags:
  - chapter
---

# Chapter 02 - The Big Data Era

> [!story] Previously
> (to write)

**When data outgrew one computer, from Google's papers to Hadoop and the pain that came with it.**

## The story of this chapter

(to write)

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

> [!nextup] Up next
> [[The Three Vs of Big Data]]
