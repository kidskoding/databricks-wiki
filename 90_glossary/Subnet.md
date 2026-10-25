---
type: glossary
status: written
level: 90
section: Glossary
depth: 101
summary: "A smaller slice of a private cloud network, with its own range of IP addresses."
related:
  - "[[VPC and VNet]]"
  - "[[VNet Injection]]"
  - "[[Customer-Managed VPC on AWS]]"
  - "[[Customer-Managed VPC on Google Cloud]]"
  - "[[Public vs Private IP]]"
  - "[[Network Security Overview]]"
aliases:
  - "subnets"
  - "subnetwork"
  - "CIDR block"
  - "address range"
last_verified: 2026-10-25
tags:
  - glossary
  - flashcards
---

# Subnet

> [!eli5] Summary
> A subnet is a subdivision of a private cloud network with its own range of addresses. Machines in the subnet get their addresses from that range.

**In data work:** A subnet divides a [[VPC and VNet|VPC or VNet]] into ranges of IP addresses written in CIDR notation, such as `10.0.1.0/24` (256 addresses). Each machine gets an address from its subnet. You attach routing and security rules per subnet, for example keeping databases in a subnet with no internet route. Sizing matters: a subnet that is too small runs out of addresses when more machines start. A small business might place its web servers in one subnet and its analytics machines in another, with a [[Firewall|firewall]] rule between them.

**In Databricks:** When you deploy Databricks into your own network, its cluster nodes take IP addresses from subnets you provide. [[VNet Injection]] on Azure needs two dedicated subnets per workspace (host and container); each node takes one IP in each, and Databricks does not recommend subnets smaller than /26. A [[Customer-Managed VPC on AWS]] needs at least two private subnets in different [[Availability Zone|availability zones]], each between /17 and /26, and each node uses two IPs. On [[Customer-Managed VPC on Google Cloud|Google Cloud]] the subnet must be in the workspace's region. Because nodes consume addresses, subnet size caps how many nodes can run at once.

Seen in: [[VNet Injection]], [[Customer-Managed VPC on AWS]], [[Customer-Managed VPC on Google Cloud]]

## Recall

Subnet::A sub-range of IP addresses inside a VPC or VNet; Databricks clusters draw node addresses from the subnets you give them, so size caps cluster size.

> [!sources]- Sources (last verified: 2026-10-25)
> - [Deploy Azure Databricks in your Azure virtual network (VNet injection)](https://learn.microsoft.com/en-us/azure/databricks/security/network/classic/vnet-inject)
> - [Configure a customer-managed VPC (AWS)](https://docs.databricks.com/aws/en/security/network/classic/customer-managed-vpc)
> - [Configure a customer-managed VPC (Google Cloud)](https://docs.databricks.com/gcp/en/security/network/classic/customer-managed-vpc)
