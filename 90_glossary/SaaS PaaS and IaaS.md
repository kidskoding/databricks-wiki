---
type: glossary
status: written
level: 90
section: Glossary
depth: 101
summary: "Three levels of cloud service: rent raw machines (IaaS), a platform to build on (PaaS), or finished software (SaaS)."
related:
  - "[[Servers and the Cloud]]"
  - "[[Control Plane and Compute Plane]]"
  - "[[Serverless Compute]]"
  - "[[First-Party Microsoft Service]]"
  - "[[Total Cost of Ownership]]"
aliases:
  - "SaaS"
  - "PaaS"
  - "IaaS"
  - "Software as a Service"
  - "Platform as a Service"
  - "Infrastructure as a Service"
last_verified: 2026-10-25
tags:
  - glossary
  - flashcards
---

# SaaS PaaS and IaaS

> [!eli5] Summary
> These are three levels of cloud service. IaaS rents raw machines, PaaS provides a managed platform for your own code, and SaaS delivers finished software.

**In data work:** IaaS (Infrastructure as a Service) rents [[Virtual Machine|virtual machines]], disks, and networks; you install and patch everything else (Amazon EC2, Azure VMs). PaaS (Platform as a Service) gives a managed runtime where you bring code and data but not servers (Azure App Service, managed databases). SaaS (Software as a Service) is a finished application you log in to (Gmail, QuickBooks Online, Shopify). Moving up the stack trades control for less operations work, which matters most to small teams with no IT staff.

**In Databricks:** Databricks sits between PaaS and SaaS. Its [[Control Plane and Compute Plane|control plane]] is run by Databricks like SaaS. With classic compute, the VMs run in your own cloud account, which feels more like managed PaaS on top of IaaS. With [[Serverless Compute]], Databricks runs the compute too, so it behaves almost like SaaS. On Azure, Databricks is also a [[First-Party Microsoft Service|first-party Azure service]], billed through Azure.

Seen in: [[Servers and the Cloud]], [[Control Plane and Compute Plane]], [[Serverless Compute]]

## Recall

SaaS PaaS and IaaS::IaaS rents machines, PaaS provides a managed platform for your code, SaaS delivers finished software; Databricks spans PaaS to SaaS.
