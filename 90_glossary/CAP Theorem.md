---
type: glossary
status: written
level: 90
section: Glossary
depth: 101
summary: "The result that a distributed data store cannot guarantee consistency, availability, and partition tolerance all at once, so it must trade consistency against availability when the network splits."
related:
  - "[[Distributed Systems]]"
  - "[[Replication]]"
  - "[[Fault Tolerance]]"
  - "[[ACID Transactions]]"
  - "[[NoSQL]]"
  - "[[Apache HBase]]"
aliases:
  - "CAP"
  - "Brewer's theorem"
  - "Brewer's conjecture"
last_verified: 2026-10-26
tags:
  - glossary
  - flashcards
---

# CAP Theorem

> [!eli5] Summary
> The CAP theorem says that when parts of a networked database lose contact with each other, it has to choose between always answering and always giving the latest answer. It cannot promise both.

**In data work:** CAP names three properties of a replicated data service: **Consistency** (every read sees the latest write), **Availability** (every request gets a response), and **Partition tolerance** (the system keeps working when network links between nodes fail). Eric Brewer stated it as a conjecture in 2000, and Seth Gilbert and Nancy Lynch published a formal proof in 2002. In practice, network partitions happen, so the real design choice is what the system does during one: refuse some requests (CP) or answer with possibly stale data (AP). Many [[NoSQL]] systems built in the [[Chapter 02 - The Big Data Era|big data era]] chose availability and eventual consistency.

**In Databricks:** You rarely configure CAP trade-offs directly on Databricks. [[Delta Lake]] tables rely on the cloud [[Object Storage|object store]] and an atomic commit to the [[Delta Transaction Log|transaction log]], which gives [[ACID Transactions|ACID]] guarantees per table. The term is useful background when you compare Databricks with distributed databases you already run, such as [[Apache HBase]] or a replicated operational store.

Seen in: [[Distributed Systems]], [[Apache HBase]]

## Recall

What are the three properties in the CAP theorem?::Consistency, availability, and partition tolerance.
During a network partition, what must a distributed store choose between?::Consistency and availability.

> [!sources]- Sources (last verified: 2026-10-26)
> - [Gilbert and Lynch, Brewer's conjecture and the feasibility of consistent, available, partition-tolerant web services (cited in Vogels, Eventually Consistent, CACM)](https://dl.acm.org/doi/10.1145/1435417.1435432)
