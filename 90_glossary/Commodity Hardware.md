---
type: glossary
status: written
level: 90
section: Glossary
depth: 101
summary: "Ordinary, inexpensive, mass-produced servers, as opposed to specialized high-end machines; big data systems were designed to run on many of them and tolerate their failures."
related:
  - "[[Scaling Up vs Scaling Out]]"
  - "[[Google File System and MapReduce Papers]]"
  - "[[Apache Hadoop]]"
  - "[[Fault Tolerance]]"
  - "[[Distributed Systems]]"
  - "[[Node]]"
aliases:
  - "Commodity servers"
  - "Off-the-shelf hardware"
last_verified: 2026-10-26
tags:
  - glossary
  - flashcards
---

# Commodity Hardware

> [!eli5] Summary
> Commodity hardware means cheap, standard computers. Instead of buying one very expensive machine, early big data systems linked many cheap ones and expected some to break.

**In data work:** Before the 2000s, handling more data usually meant buying a larger, specialized server ([[Scaling Up vs Scaling Out|scaling up]]). The 2003 Google File System paper described a storage system built from hundreds or thousands of machines made of inexpensive commodity parts, and treated component failure as the norm rather than the exception. Software, not hardware, provided [[Fault Tolerance|fault tolerance]] through [[Replication|replication]] and automatic recovery. [[Apache Hadoop]] and [[HDFS]] copied this design, which made scaling out affordable.

**In Databricks:** On Databricks you do not buy hardware. The cloud provider supplies [[Virtual Machine|virtual machines]], and Databricks starts and stops them as cluster [[Node|nodes]]. The commodity-hardware idea survives in the platform's assumptions: [[Apache Spark]] retries failed tasks on other nodes, and [[Spot Instances|spot instances]] that the cloud can reclaim are a normal, supported option.

Seen in: [[Google File System and MapReduce Papers]], [[Apache Hadoop]], [[Scaling Up vs Scaling Out]]

## Recall

What design assumption did GFS make about commodity hardware?::Component failures are the norm, so software must detect and recover from them.
Commodity Hardware::Inexpensive standard servers used in large numbers, with fault tolerance handled in software.

> [!sources]- Sources (last verified: 2026-10-26)
> - [The Google File System (SOSP 2003, research.google)](https://research.google/pubs/the-google-file-system/)
> - [The Google File System (PDF)](https://static.googleusercontent.com/media/research.google.com/en//archive/gfs-sosp2003.pdf)
