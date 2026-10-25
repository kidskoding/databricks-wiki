---
type: glossary
status: written
level: 90
section: Glossary
depth: 101
summary: "A public IP address is reachable from the internet; a private one works only inside a private network."
related:
  - "[[Secure Cluster Connectivity]]"
  - "[[Subnet]]"
  - "[[VPC and VNet]]"
  - "[[Network Security Overview]]"
  - "[[IP Access Lists]]"
  - "[[Firewall]]"
aliases:
  - "public IP"
  - "private IP"
  - "IP address"
  - "no public IP"
  - "NPIP"
last_verified: 2026-10-25
tags:
  - glossary
  - flashcards
---

# Public vs Private IP

> [!eli5] Summary
> A public IP address can be reached from the internet. A private IP address works only inside a private network, which keeps machines hidden from outside traffic.

**In data work:** An IP address identifies a machine on a network. Public addresses are globally unique and reachable over the internet. Private addresses come from ranges reserved for internal use and are only routable inside a private network such as a [[VPC and VNet|VPC or VNet]]. Machines with only private IPs reach the internet through a NAT gateway, which keeps them invisible to inbound traffic. A shop's office printer has a private IP; its website has a public one. Fewer public IPs means less exposed attack surface.

**In Databricks:** With [[Secure Cluster Connectivity]] (also called no public IP), Databricks cluster nodes get only private IPs, and they connect out to the control plane instead of accepting inbound connections. It is the default for all new workspaces. On Google Cloud, clusters have no public IPs by default either, so reaching the internet needs a Cloud NAT or allowed URLs. Serverless compute resources also have no public IPs. [[IP Access Lists]] restrict which public IPs can reach the workspace UI and APIs, and private connectivity options like [[Azure Private Link]], [[AWS PrivateLink]], and [[Private Service Connect]] keep traffic off the public internet entirely.

Seen in: [[Secure Cluster Connectivity]], [[Network Security Overview]], [[IP Access Lists]]

## Recall

Public vs Private IP::Public IPs are reachable from the internet, private IPs only inside a private network; Databricks clusters use private IPs with secure cluster connectivity.

> [!sources]- Sources (last verified: 2026-10-25)
> - [Classic compute plane networking (AWS)](https://docs.databricks.com/aws/en/security/network/classic)
> - [Classic compute plane networking (Azure Databricks)](https://learn.microsoft.com/en-us/azure/databricks/security/network/classic/)
> - [Phase 4: Design network architecture (Google Cloud)](https://docs.databricks.com/gcp/en/lakehouse-architecture/deployment-guide/network)
