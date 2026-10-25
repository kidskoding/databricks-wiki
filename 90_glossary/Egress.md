---
type: glossary
status: written
level: 90
section: Glossary
depth: 101
summary: "Network traffic leaving a network, region, or cloud; it can incur transfer charges and is a common security control point."
related:
  - "[[Serverless Network Security]]"
  - "[[Network Security Overview]]"
  - "[[Region]]"
  - "[[Cost Management Basics]]"
  - "[[Firewall]]"
  - "[[VNet Injection]]"
aliases:
  - "data egress"
  - "egress fees"
  - "outbound traffic"
last_verified: 2026-10-25
tags:
  - glossary
  - flashcards
---

# Egress

> [!eli5] Summary
> Egress is data leaving a network. Cloud providers often charge for it, and security teams control where it is allowed to go.

**In data work:** Ingress is incoming traffic; egress is outgoing traffic. Cloud providers generally charge for data transferred out to the internet or between regions. Egress is also a security boundary: data exfiltration appears as unexpected outbound traffic, so organizations restrict outbound destinations. Keep compute and storage in the same [[Region|region]] to avoid cross-region transfer.

**In Databricks:** For classic compute deployed in your own network ([[VNet Injection]], [[Customer-Managed VPC on AWS]]), outbound traffic can be routed through a [[Firewall|firewall]]. For serverless compute, account admins configure network policies ([[Serverless Network Security]]): **Full access** or **Restricted access**, where only Unity Catalog external locations and listed FQDNs and storage destinations are allowed. Policies run in enforced or dry-run mode, and denials are logged to `system.access.outbound_network`. Network policies require the Enterprise tier on AWS and Premium on Azure. Transfer prices are on each cloud's pricing pages.

Seen in: [[Serverless Network Security]], [[Network Security Overview]], [[Cost Management Basics]], [[VNet Injection]]

## Recall

What is egress?::Network traffic leaving a network, region, or cloud.
Where are serverless egress denials logged?::In the system.access.outbound_network system table.

> [!sources]- Sources (last verified: 2026-10-25)
> - [Manage network policies for serverless egress control (AWS)](https://docs.databricks.com/aws/en/security/network/serverless-network-security/manage-network-policies)
> - [Manage network policies for serverless egress control (Azure)](https://learn.microsoft.com/en-us/azure/databricks/security/network/serverless-network-security/manage-network-policies)
