---
type: glossary
status: written
level: 90
section: Glossary
depth: 101
summary: "Turning data or objects in memory into bytes so they can be stored or sent, and back again."
related:
  - "[[Files and File Formats]]"
  - "[[Apache Parquet]]"
  - "[[CSV and JSON]]"
  - "[[Shuffles]]"
  - "[[Tungsten]]"
  - "[[UDF]]"
aliases:
  - "serialize"
  - "deserialization"
  - "SerDe"
  - "marshalling"
  - "pickling"
last_verified: 2026-10-25
tags:
  - glossary
  - flashcards
---

# Serialization

> [!eli5] Summary
> Serialization converts data in a program's memory into bytes so it can be saved or sent over a network. Deserialization converts it back.

**In data work:** Programs hold data in memory as objects. To write it to disk or send it across a network, it must be serialized into a byte format such as JSON, CSV, Parquet, Avro, Protocol Buffers, or Python's pickle. Formats differ in size, speed, whether people can read them, and whether they carry a [[Schema|schema]]. Serialization costs CPU time, and in distributed systems it is often a hidden bottleneck. When a Shopify webhook sends an order as JSON, the store's app deserializes that text into an order object.

**In Databricks:** Serialization happens all through Spark. Data moving between [[Node|nodes]] during [[Shuffles|shuffles]] is serialized, and [[Tungsten]] uses a compact binary format to keep this cheap. Python [[UDF|UDFs]] must serialize rows between the JVM and Python, which is why they are slower than built-in functions; pandas UDFs use Apache Arrow to do this in batches. Tables are serialized to disk as [[Apache Parquet]] files under Delta.

Seen in: [[Files and File Formats]], [[Shuffles]], [[UDF]]

## Recall

Serialization::Converting in-memory data into bytes for storage or transfer (and back); it is a hidden cost in shuffles and Python UDFs.
