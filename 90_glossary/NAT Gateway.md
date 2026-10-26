---
type: glossary
status: written
level: 90
section: Glossary
depth: 101
summary: "A cloud network service that lets machines without public IP addresses make outbound internet connections through a fixed public IP."
related:
  - "[[Secure Cluster Connectivity]]"
  - "[[VNet Injection]]"
  - "[[Public vs Private IP]]"
  - "[[Egress]]"
  - "[[Subnet]]"
  - "[[Customer-Managed VPC on AWS]]"
aliases:
  - "NAT"
  - "network address translation gateway"
  - "Azure NAT Gateway"
  - "Cloud NAT"
last_verified: 2026-10-26
tags:
  - glossary
  - flashcards
---

# NAT Gateway

> [!eli5] Summary
> A NAT gateway is a shared exit door to the internet for computers that have no public address of their own. Everything leaving through it appears to come from one known address.

**In data work:** Network address translation (NAT) rewrites the private source address of outbound traffic to the gateway's public address and routes replies back. Machines behind it can reach the internet (to download packages or call APIs), but the internet cannot open connections to them. Because the outbound address is fixed, partners can add it to their firewall allow lists. A shop whose supplier only accepts API calls from approved IPs can give the supplier the NAT gateway's address.

**In Databricks:** Classic compute with [[Secure Cluster Connectivity|secure cluster connectivity]] has no [[Public vs Private IP|public IPs]], so outbound traffic needs a NAT path.
- **Azure, managed VNet:** Azure Databricks creates a NAT gateway in the [[Managed Resource Group|managed resource group]], which you cannot modify.
- **Azure, [[VNet Injection]]:** Databricks recommends attaching your own Azure NAT gateway to both workspace [[Subnet|subnets]] for stable egress IPs. Do not use an egress load balancer with secure cluster connectivity. New Azure VNets created after March 31, 2026 have no default outbound internet access, so they need an explicit method such as a NAT gateway.
- **AWS and Google Cloud:** The equivalents are the AWS NAT gateway and Cloud NAT, configured as part of a [[Customer-Managed VPC on AWS]] or [[Customer-Managed VPC on Google Cloud]].

NAT gateways are billed by the cloud provider for hours and data processed (see [[Egress]]).

Seen in: [[Secure Cluster Connectivity]], [[VNet Injection]], [[Network Security Overview]]

## Recall

NAT gateway::A managed service that gives private machines outbound internet access through a fixed public IP, without allowing inbound connections.
What does Databricks recommend for stable egress IPs with Azure VNet injection?::An Azure NAT gateway attached to both workspace subnets.

> [!sources]- Sources (last verified: 2026-10-26)
> - [Enable secure cluster connectivity (Azure Databricks)](https://learn.microsoft.com/en-us/azure/databricks/security/network/classic/secure-cluster-connectivity)
> - [Deploy Azure Databricks in your Azure virtual network (VNet injection)](https://learn.microsoft.com/en-us/azure/databricks/security/network/classic/vnet-inject)
> - [Azure NAT Gateway frequently asked questions](https://learn.microsoft.com/en-us/azure/nat-gateway/faq)
