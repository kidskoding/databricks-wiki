---
type: glossary
status: written
level: 90
section: Glossary
depth: 101
summary: "A network control that allows or blocks traffic according to rules on source, destination, port, and protocol."
related:
  - "[[Network Security Overview]]"
  - "[[IP Access Lists]]"
  - "[[VNet Injection]]"
  - "[[Customer-Managed VPC on AWS]]"
  - "[[Customer-Managed VPC on Google Cloud]]"
  - "[[Serverless Network Security]]"
aliases:
  - "firewalls"
  - "network firewall"
  - "security group"
  - "NSG"
  - "network security group"
last_verified: 2026-10-25
tags:
  - glossary
  - flashcards
---

# Firewall

> [!eli5] Summary
> A firewall checks network connections against a list of rules and blocks the ones that are not allowed, both coming in and going out.

**In data work:** A firewall evaluates each connection against rules on source and destination address, port, and protocol. Inbound rules protect systems from unwanted access; outbound ([[Egress|egress]]) rules prevent data from leaving to unapproved destinations. Cloud equivalents include Azure network security groups (NSGs), AWS security groups and network ACLs, and Google Cloud firewall rules, plus managed firewall services for central control.

**In Databricks:** [[IP Access Lists]] restrict access to the workspace and the account console by source IP; block lists are evaluated first, and once any allow list exists, only listed addresses are admitted. Databricks now recommends context-based ingress as the primary account-level control. With classic compute in your own network ([[VNet Injection]], [[Customer-Managed VPC on AWS]], [[Customer-Managed VPC on Google Cloud]]), you control subnet rules and can route outbound traffic through a firewall. Serverless egress is controlled with network policies ([[Serverless Network Security]]).

Seen in: [[Network Security Overview]], [[IP Access Lists]], [[VNet Injection]], [[Serverless Network Security]]

## Recall

What is the difference between inbound and outbound firewall rules?::Inbound rules control incoming traffic; outbound rules control traffic leaving the network.
In Databricks IP access lists, which list is evaluated first?::The block list.

> [!sources]- Sources (last verified: 2026-10-25)
> - [Manage IP access lists (AWS)](https://docs.databricks.com/aws/en/security/network/front-end/ip-access-list)
> - [Context-based network policies (AWS)](https://docs.databricks.com/aws/en/security/network/context-based-policies)
> - [Manage network policies for serverless egress control (AWS)](https://docs.databricks.com/aws/en/security/network/serverless-network-security/manage-network-policies)
