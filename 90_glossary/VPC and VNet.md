---
type: glossary
status: written
level: 90
section: Glossary
depth: 101
summary: "Your own private, isolated network inside a cloud: called a VPC on AWS and Google Cloud, and a VNet on Azure."
related:
  - "[[VNet Injection]]"
  - "[[Customer-Managed VPC on AWS]]"
  - "[[Customer-Managed VPC on Google Cloud]]"
  - "[[Subnet]]"
  - "[[Network Security Overview]]"
  - "[[Secure Cluster Connectivity]]"
aliases:
  - "VPC"
  - "VNet"
  - "Virtual Private Cloud"
  - "Virtual Network"
  - "Azure Virtual Network"
last_verified: 2026-10-25
tags:
  - glossary
  - flashcards
---

# VPC and VNet

> [!eli5] Summary
> A VPC (on AWS and Google Cloud) or VNet (on Azure) is a private, isolated network inside a cloud account. You control which traffic can enter and leave it.

**In data work:** A Virtual Private Cloud (AWS, Google Cloud) or Virtual Network (Azure) is a logically isolated network with its own IP address range, divided into [[Subnet|subnets]], with route tables, gateways, and [[Firewall|firewall]] rules (security groups, network security groups, firewall rules). You control what can reach the internet, which on-premises networks connect through VPN or private links, and which services talk to each other.

**In Databricks:** By default Databricks can create the network for you. Companies with security requirements deploy into their own network instead: [[VNet Injection]] on Azure, [[Customer-Managed VPC on AWS]], and [[Customer-Managed VPC on Google Cloud]]. That lets you add private endpoints, firewall egress, and connections to on-premises databases. [[Network Security Overview]] puts the pieces together.

Seen in: [[VNet Injection]], [[Customer-Managed VPC on AWS]], [[Customer-Managed VPC on Google Cloud]], [[Network Security Overview]]

## Recall

VPC and VNet::A private isolated network in the cloud (VPC on AWS and Google Cloud, VNet on Azure); Databricks can deploy into one you manage.

> [!sources]- Sources (last verified: 2026-10-25)
> - [Deploy Azure Databricks in your Azure virtual network (VNet injection)](https://learn.microsoft.com/en-us/azure/databricks/security/network/classic/vnet-inject)
> - [Configure a customer-managed VPC (AWS)](https://docs.databricks.com/aws/en/security/network/classic/customer-managed-vpc)
> - [Configure a customer-managed VPC (Google Cloud)](https://docs.databricks.com/gcp/en/security/network/classic/customer-managed-vpc)
