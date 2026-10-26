---
type: glossary
status: written
level: 90
section: Glossary
depth: 101
summary: "A notation such as 10.0.0.0/24 that describes a block of IP addresses; you use it to size the virtual networks and subnets that Databricks compute runs in."
related:
  - "[[Subnet]]"
  - "[[VPC and VNet]]"
  - "[[VNet Injection]]"
  - "[[Customer-Managed VPC on AWS]]"
  - "[[Customer-Managed VPC on Google Cloud]]"
  - "[[IP Access Lists]]"
aliases:
  - "CIDR block"
  - "CIDR range"
  - "Classless Inter-Domain Routing"
last_verified: 2026-10-26
tags:
  - glossary
  - flashcards
---

# CIDR

> [!eli5] Summary
> CIDR is a short way to write a range of network addresses. The number after the slash says how big the range is: a smaller number means more addresses.

**In data work:** CIDR (Classless Inter-Domain Routing) writes an address range as a base address plus a prefix length, for example `10.20.0.0/16`. The prefix is the number of fixed leading bits out of 32 in IPv4, so a `/24` holds 256 addresses, a `/26` holds 64, and a `/16` holds 65,536. Clouds reserve a few addresses in every [[Subnet|subnet]], so usable capacity is slightly lower. Ranges inside one network must not overlap, and ranges that you peer or connect over VPN must not overlap either.

**In Databricks:** You choose CIDR ranges when you deploy classic compute into your own network: [[VNet Injection]] on Azure, [[Customer-Managed VPC on AWS]], or [[Customer-Managed VPC on Google Cloud]]. [[IP Access Lists]] also take CIDR ranges. For Azure VNet injection, Microsoft documents a VNet between `/16` and `/24`, two dedicated subnets (host and container) of the same size, and a recommended minimum of `/26` per subnet. Azure reserves five addresses per subnet and each node uses one address in each subnet. Subnet ranges cannot be changed after deployment, so size for growth.

Small-business example: a 10-person team picks a `/24` VNet split into two `/25` subnets, which leaves room for roughly 120 nodes.

Seen in: [[VNet Injection]], [[Customer-Managed VPC on AWS]], [[IP Access Lists]]

## Recall

How many addresses does a /24 CIDR block contain?::256.
Which Azure Databricks subnets must you size with CIDR ranges for VNet injection?::The host subnet and the container subnet.

> [!sources]- Sources (last verified: 2026-10-26)
> - [Deploy Azure Databricks in your Azure virtual network (VNet injection)](https://learn.microsoft.com/en-us/azure/databricks/security/network/classic/vnet-inject)
> - [Phase 4: Design network architecture (Azure)](https://learn.microsoft.com/en-us/azure/databricks/lakehouse-architecture/deployment-guide/network)
