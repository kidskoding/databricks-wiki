---
type: glossary
status: written
level: 90
section: Glossary
depth: 101
summary: "The automatic process that frees memory a program no longer uses; in Spark it runs in each JVM, and long garbage collection pauses slow tasks down."
related:
  - "[[JVM]]"
  - "[[Driver and Executors]]"
  - "[[Spark UI]]"
  - "[[Spill]]"
  - "[[Caching]]"
  - "[[Serialization]]"
aliases:
  - "GC"
  - "JVM garbage collection"
  - "GC pause"
  - "G1GC"
last_verified: 2026-10-26
tags:
  - glossary
  - flashcards
---

# Garbage Collection

> [!eli5] Summary
> Garbage collection is a program cleaning up memory it has finished with. If too much memory is in use, the cleanup runs often and the program pauses while it works.

**In data work:** Languages such as Java, Scala, and Python manage memory automatically. The garbage collector finds objects no longer referenced and reclaims their memory. Most collectors pause application threads for part of the work. When a process is short of memory, collections become frequent and long, and throughput drops. The word is also used loosely for removing unreferenced files from storage.

**In Databricks:** [[Apache Spark]] [[Driver and Executors|executors]] run in a [[JVM]]. The Spark tuning guide recommends checking GC first when tasks are slow: Spark 4.0 and later run on JDK 17, where G1GC is the default collector. The [[Spark UI]] shows **GC Time** per task and executor; if it is a large share of task time, reduce memory pressure. Typical fixes are to use a larger worker type, cache less or cache in serialized form ([[Caching]]), lower partition size, or avoid collecting large results to the driver. Flags go in `spark.executor.extraJavaOptions`, but heap size is set with `spark.executor.memory`, not `-Xmx`. On [[Serverless Compute|serverless compute]] Databricks manages these settings.

In [[Delta Lake]], removing data files that are no longer referenced by the table is done with `VACUUM` (see [[OPTIMIZE and VACUUM]]), not by the JVM collector.

Seen in: [[Driver and Executors]], [[Spark UI]], [[JVM]]

## Recall

Where do you see garbage collection time for a Spark task?::In the Spark UI, as GC Time on the Stages and Executors pages.
Which garbage collector is the default for Spark 4.0 and later on JDK 17?::G1GC.

> [!sources]- Sources (last verified: 2026-10-26)
> - [Tuning Spark, Garbage Collection Tuning (spark.apache.org)](https://spark.apache.org/docs/latest/tuning.html)
> - [Configuration (spark.apache.org)](https://spark.apache.org/docs/latest/configuration.html)
