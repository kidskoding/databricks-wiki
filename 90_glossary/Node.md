---
type: glossary
status: written
level: 90
section: Glossary
depth: 101
summary: "One computer in a group of computers that work together."
related:
  - "[[Cluster]]"
  - "[[Driver and Executors]]"
  - "[[Virtual Machine]]"
  - "[[Distributed Systems]]"
  - "[[Compute Types]]"
  - "[[Autoscaling]]"
aliases:
  - "nodes"
  - "worker node"
  - "driver node"
  - "machine"
  - "instance"
last_verified: 2026-10-25
tags:
  - glossary
  - flashcards
---

# Node

> [!eli5] Summary
> A node is one computer in a group of computers that share a workload.

**In data work:** In distributed systems, a node is a single machine (today usually a cloud [[Virtual Machine|virtual machine]]) that is part of a [[Cluster|cluster]]. Nodes have roles: in Hadoop there were name nodes and data nodes; in Spark there is one driver node that plans the work and worker nodes that run it. Adding nodes is scaling out (see [[Scaling Up vs Scaling Out]]). If a report on two years of sales takes an hour on one node, ten worker nodes can often finish it in minutes, because each reads a slice of the files.

**In Databricks:** A Databricks classic cluster has one driver node and zero or more worker nodes, each a cloud VM of the instance type you choose (see [[Driver and Executors]] and [[EC2 Instance Types and Graviton]]). Single-node compute has no workers: the driver runs Spark locally, which is enough for small data. [[Autoscaling]] adds and removes worker nodes, and [[Serverless Compute]] hides nodes from you entirely.

Seen in: [[Driver and Executors]], [[Compute Types]], [[Distributed Systems]]

## Recall

Node::One machine in a cluster; a Databricks cluster has one driver node and zero or more worker nodes.

> [!sources]- Sources (last verified: 2026-10-25)
> - [Compute configuration reference (AWS)](https://docs.databricks.com/aws/en/compute/configure)
