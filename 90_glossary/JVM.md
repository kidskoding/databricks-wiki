---
type: glossary
status: written
level: 90
section: Glossary
depth: 101
summary: "The Java Virtual Machine: the runtime that executes Java and Scala bytecode, and the process in which Spark's driver and executors run."
related:
  - "[[Apache Spark]]"
  - "[[Driver and Executors]]"
  - "[[PySpark]]"
  - "[[Photon]]"
  - "[[Tungsten]]"
  - "[[Spark Connect]]"
aliases:
  - "Java Virtual Machine"
  - "JRE"
  - "garbage collection"
  - "GC"
last_verified: 2026-10-25
tags:
  - glossary
  - flashcards
---

# JVM

> [!eli5] Summary
> The JVM is the software layer that runs programs written in Java and Scala. Spark is written in Scala, so every Spark machine runs a JVM.

**In data work:** The JVM executes compiled bytecode from Java, [[Scala]], and other JVM languages on any operating system, and manages memory through garbage collection (GC). Much of the big-data stack runs on the JVM, including [[Apache Hadoop]], [[Apache Kafka]], [[Apache Hive]], and [[Apache Spark]]. An `OutOfMemoryError` or long GC pauses in a Spark job indicate that a JVM ran short of heap memory.

**In Databricks:** On classic compute, each Spark [[Driver and Executors|driver and executor]] is a JVM process, and the [[Databricks Runtime]] ships a specific Java version. [[PySpark]] code runs in Python and sends instructions to the JVM. [[Tungsten]] reduced JVM overhead with off-heap memory management. [[Photon]] is a vectorized engine written in C++; it is loaded into the JVM process and exchanges data with Spark through JNI using off-heap memory, while the [[Catalyst Optimizer]] still plans queries. Operations that Photon does not support fall back to the Spark runtime. [[Spark Connect]] lets thin clients use Spark remotely.

Seen in: [[Apache Spark]], [[Driver and Executors]], [[PySpark]], [[Photon]], [[Tungsten]]

## Recall

Which language is Apache Spark written in?::Scala, which runs on the JVM.
How does Photon exchange data with the JVM-based Spark runtime?::Through JNI, passing pointers to off-heap memory.

> [!sources]- Sources (last verified: 2026-10-25)
> - [What is Photon? (AWS)](https://docs.databricks.com/aws/en/compute/photon)
> - [Announcing Photon Public Preview (Databricks blog, 2021)](https://www.databricks.com/blog/2021/06/17/announcing-photon-public-preview-the-next-generation-query-engine-on-the-databricks-lakehouse-platform.html)
