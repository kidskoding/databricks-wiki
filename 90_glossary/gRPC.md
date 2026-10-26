---
type: glossary
status: written
level: 90
section: Glossary
depth: 101
summary: "An open-source remote procedure call framework that sends compact Protocol Buffers messages over HTTP/2; Spark Connect and Databricks Connect use it between client and cluster."
related:
  - "[[Spark Connect]]"
  - "[[Databricks Connect]]"
  - "[[APIs]]"
  - "[[REST]]"
  - "[[Serialization]]"
  - "[[Apache Arrow]]"
aliases:
  - "Protocol Buffers"
  - "protobuf"
  - "Remote procedure call"
last_verified: 2026-10-26
tags:
  - glossary
  - flashcards
---

# gRPC

> [!eli5] Summary
> gRPC is a fast way for one program to ask another program, often on a different machine, to do something. It packs requests into a small binary format instead of text.

**In data work:** A remote procedure call (RPC) lets a client call a function on a server as if it were local. gRPC defines services and messages in `.proto` files, encodes them with Protocol Buffers, and sends them over HTTP/2, which supports streaming in both directions. Compared with JSON over [[REST]], messages are smaller and typed, at the cost of being harder to inspect by hand.

**In Databricks:** [[Spark Connect]] (Apache Spark 3.4 and later) is a gRPC-based client-server protocol. The client turns DataFrame operations into unresolved logical plans, encodes them as Protocol Buffers, and sends them over gRPC; results return as [[Apache Arrow]] batches. Spark Connect has no built-in authentication; deployments place an authenticating layer in front. [[Databricks Connect]] builds on Spark Connect, so code in your IDE talks to Databricks compute over gRPC with Databricks authentication. Serverless notebooks and standard-access compute also use the Spark Connect architecture. The Databricks [[Databricks SDKs and REST API|REST API]] itself is JSON over HTTPS, not gRPC.

Small-business consideration: you do not write gRPC code. Know the term so you can recognize it in Databricks Connect error messages and network reviews.

Seen in: [[Spark Connect]], [[Databricks Connect]]

## Recall

What encoding and transport does gRPC use?::Protocol Buffers over HTTP/2.
Which Spark feature uses gRPC between client and server?::Spark Connect.

> [!sources]- Sources (last verified: 2026-10-26)
> - [Spark Connect Overview (spark.apache.org)](https://spark.apache.org/docs/latest/spark-connect-overview.html)
> - [Compare Spark Connect to Spark Classic (GCP)](https://docs.databricks.com/gcp/en/spark/connect-vs-classic)
> - [Databricks Connect (AWS)](https://docs.databricks.com/aws/en/dev-tools/databricks-connect)
