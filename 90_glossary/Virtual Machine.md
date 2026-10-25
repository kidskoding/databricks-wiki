---
type: glossary
status: written
level: 90
section: Glossary
depth: 101
summary: "A software computer that runs on a shared physical server, rented by the hour from a cloud provider."
related:
  - "[[Servers and the Cloud]]"
  - "[[Node]]"
  - "[[Cluster]]"
  - "[[EC2 Instance Types and Graviton]]"
  - "[[Compute on Google Cloud]]"
  - "[[Spot Instances]]"
aliases:
  - "VM"
  - "VMs"
  - "instance"
  - "EC2 instance"
  - "Azure VM"
  - "Compute Engine VM"
last_verified: 2026-10-25
tags:
  - glossary
  - flashcards
---

# Virtual Machine

> [!eli5] Summary
> A virtual machine is a software-defined computer that runs on shared physical hardware. Cloud providers rent virtual machines by size and by time used.

**In data work:** A VM gets a slice of a physical server's CPU, memory, and disk through software called a hypervisor, and behaves like a separate computer with its own operating system. Clouds sell VMs in fixed sizes called instance types (AWS EC2, Azure Virtual Machines, Google Compute Engine), billed by the second or hour. You pick the size by workload: memory-optimized for big joins, compute-optimized for CPU-heavy work, GPU instances for AI. A consultant can rent a large VM for one afternoon of number crunching instead of buying a server.

**In Databricks:** Each [[Node|node]] of a Databricks classic [[Cluster|cluster]] or classic SQL warehouse is a VM in your cloud account, of the instance type you choose (see [[EC2 Instance Types and Graviton]] and [[Compute on Google Cloud]]). You pay the cloud for the VMs and Databricks for [[DBUs]]. [[Serverless Compute]] runs VMs in Databricks' account instead, so you never pick or see them.

Seen in: [[Servers and the Cloud]], [[Compute Types]], [[EC2 Instance Types and Graviton]]

## Recall

Virtual Machine::A software-defined computer on shared hardware, rented by instance type; each classic Databricks cluster node is one VM.
