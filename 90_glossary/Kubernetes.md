---
type: glossary
status: written
level: 90
section: Glossary
depth: 101
summary: "Open-source software that runs and restarts containers across a fleet of machines."
related:
  - "[[Serverless Compute]]"
  - "[[Distributed Systems]]"
  - "[[Compute Types]]"
  - "[[YARN]]"
  - "[[Servers and the Cloud]]"
aliases:
  - "K8s"
  - "container orchestration"
last_verified: 2026-10-25
tags:
  - glossary
  - flashcards
---

# Kubernetes

> [!eli5] Summary
> Kubernetes is open-source software that runs packaged applications across many computers. It decides where each one runs and restarts it if it fails.

**In data work:** Kubernetes (often written K8s) schedules [[Container|containers]] onto a cluster of machines, keeps the requested number running, restarts failed ones, and handles networking between them. A small online shop might run its website and order API on Kubernetes so a crashed web server comes back on its own. It does for containers roughly what [[YARN]] did for Hadoop jobs: decide which machine runs which piece of work.

**In Databricks:** You do not run Kubernetes to use Databricks. Databricks provisions and manages the [[Virtual Machine|virtual machines]] behind your [[Compute Types|compute]], and with [[Serverless Compute]] you do not even see the machines. Teams that already run Kubernetes often keep it for their own apps and call Databricks through its [[Databricks SDKs and REST API|REST API]]. Databricks' own engineering blog describes running thousands of Kubernetes clusters internally to operate its services, but that is hidden from customers. For Docker images on classic compute, see Databricks Container Services in the docs.

Seen in: [[Serverless Compute]], [[Compute Types]], [[YARN]]

## Recall

Kubernetes::Open-source software that schedules and restarts containers across many machines; Databricks manages compute for you, so you do not run it yourself.

> [!sources]- Sources (last verified: 2026-10-25)
> - [What is Orchestration? (Databricks glossary)](https://www.databricks.com/glossary/orchestration)
> - [Kubernetes Node Upgrade Using Operators (Databricks blog)](https://www.databricks.com/blog/scalable-kubernetes-upgrade-using-operators)
