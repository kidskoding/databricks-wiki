---
type: glossary
status: written
level: 90
section: Glossary
depth: 101
summary: "Spare cloud machines sold at a discount that the cloud can take back at short notice."
related:
  - "[[Cost Optimization Checklist]]"
  - "[[Autoscaling]]"
  - "[[Virtual Machine]]"
  - "[[EC2 Instance Types and Graviton]]"
  - "[[Compute Policies]]"
  - "[[Fault Tolerance]]"
aliases:
  - "spot VMs"
  - "Azure Spot VMs"
  - "preemptible VMs"
  - "Spot VMs"
  - "spot capacity"
last_verified: 2026-10-25
tags:
  - glossary
  - flashcards
---

# Spot Instances

> [!eli5] Summary
> Spot instances are spare cloud machines sold at a discount. The cloud provider can take them back at short notice.

**In data work:** Cloud providers sell unused capacity at a large discount: AWS spot instances, Azure Spot VMs, and Google Cloud preemptible VMs. The provider can reclaim them when it needs the capacity back; Azure, for example, evicts Spot VMs with 30 seconds' notice. They suit work that can restart or tolerate losing a machine, such as batch processing, and suit poorly anything that must not be interrupted.

**In Databricks:** Databricks classic compute can use spot (or preemptible) capacity for worker nodes, and the docs on all three clouds say to keep the driver on-demand so it is not reclaimed. On AWS and Google Cloud you can choose spot or preemptible with fallback to on-demand when spot capacity runs out; Azure Databricks can replace evicted spot workers with on-demand ones. Spark re-runs the tasks of lost workers ([[Fault Tolerance|fault tolerance]]), so batch [[Lakeflow Jobs]] often run well on spot workers. Admins can enforce spot use with [[Compute Policies]]. See the [[Cost Optimization Checklist]].

Seen in: [[Cost Optimization Checklist]], [[Compute Policies]], [[EC2 Instance Types and Graviton]]

## Recall

Spot Instances::Discounted spare cloud VMs that can be reclaimed at short notice; Databricks can use them for workers while the driver stays on-demand.

> [!sources]- Sources (last verified: 2026-10-25)
> - [Compute configuration reference (AWS)](https://docs.databricks.com/aws/en/compute/configure)
> - [Compute configuration reference (Google Cloud)](https://docs.databricks.com/gcp/en/compute/configure)
> - [Compute configuration reference (Azure Databricks)](https://learn.microsoft.com/en-us/azure/databricks/compute/configure)
> - [Pool best practices (Azure Databricks)](https://learn.microsoft.com/en-us/azure/databricks/compute/pool-best-practices)
