---
type: glossary
status: written
level: 90
section: Glossary
depth: 101
summary: "A group of computers that work together as one system; Databricks now mostly calls these compute resources."
related:
  - "[[Compute Types]]"
  - "[[Driver and Executors]]"
  - "[[All-Purpose Compute]]"
  - "[[Jobs Compute]]"
  - "[[Distributed Systems]]"
  - "[[Compute Policies]]"
aliases:
  - "clusters"
  - "compute"
  - "compute resource"
  - "Spark cluster"
last_verified: 2026-10-25
tags:
  - glossary
  - flashcards
---

# Cluster

> [!eli5] Summary
> A cluster is a group of computers that share one job. One computer coordinates the work and the others carry it out, so large jobs finish faster.

**In data work:** In [[Distributed Systems|distributed computing]], a cluster is a set of [[Node|nodes]] connected by a network and managed as one system. In [[Apache Spark]], one node runs the driver, which plans work, and the others run executors, which perform it ([[Driver and Executors]]). On-premises [[Apache Hadoop]] clusters were long-lived; cloud clusters are created on demand and deleted when no longer needed.

**In Databricks:** Databricks documentation and UI now use the term **compute**; "cluster" remains in the Clusters API, policy attribute names such as `cluster_name`, the `cluster-policies` CLI command group, and older docs. Classic compute types are [[All-Purpose Compute]] for interactive work and [[Jobs Compute]] for scheduled runs. [[SQL Warehouses]] and [[Serverless Compute]] manage clusters for you. Each classic compute resource runs a [[Databricks Runtime]] version, and admins restrict configurations with [[Compute Policies]]. See [[Compute Types]].

Seen in: [[Compute Types]], [[Driver and Executors]], [[All-Purpose Compute]], [[Jobs Compute]], [[Distributed Systems]]

## Recall

In a Spark cluster, what does the driver do?::It plans the job and assigns tasks to executors on the worker nodes.
What term does Databricks now use for clusters in its UI and docs?::Compute.

> [!sources]- Sources (last verified: 2026-10-25)
> - [Create and manage compute policies (AWS)](https://docs.databricks.com/aws/en/admin/clusters/policies)
> - [cluster-policies command group (AWS)](https://docs.databricks.com/aws/en/dev-tools/cli/reference/cluster-policies-commands)
