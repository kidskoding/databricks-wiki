---
type: glossary
status: written
level: 90
section: Glossary
depth: 101
summary: "The Payment Card Industry Data Security Standard: security requirements for any business that stores, processes, or transmits payment card data."
related:
  - "[[Compliance Security Profile]]"
  - "[[HIPAA]]"
  - "[[SOC 2]]"
  - "[[PII]]"
  - "[[Encryption]]"
  - "[[Audit Logs]]"
aliases:
  - "PCI"
  - "PCI-DSS"
  - "Payment Card Industry Data Security Standard"
  - "PCI DSS v4.0"
last_verified: 2026-10-26
tags:
  - glossary
  - flashcards
---

# PCI DSS

> [!eli5] Summary
> PCI DSS is the rulebook the card industry sets for anyone who handles credit card numbers. It covers how card data is stored, protected, and monitored.

**In data work:** PCI DSS applies to cardholder data such as the primary account number. Its requirements cover network security, [[Encryption|encryption]], access control, logging, and regular testing. Scope is the key cost driver: every system that stores or touches card data is in scope. Most small businesses reduce scope by letting a payment processor handle card numbers, so their own systems keep only order totals and the processor's transaction references. That data is not cardholder data, and the analytics platform stays out of PCI scope.

**In Databricks:** PCI-DSS is one of the standards you can select with the [[Compliance Security Profile|compliance security profile]], alongside HIPAA, HITRUST, C5, and TISAX.
- **When it is required:** Only for workspaces that process data regulated under that standard.
- **What it adds:** A hardened compute image, FIPS 140 validated encryption modules, enhanced security monitoring, and automatic cluster updates. [[Single Sign-On|Single sign-on]] must be configured.
- **It is hard to undo:** Once a workspace has processed regulated data, the profile cannot be disabled.
- **Feature limits:** [[Foundation Model APIs]] pay-per-token workloads do not support PCI-DSS; provisioned throughput does.
- **Azure:** From February 1, 2027, all workspaces with the compliance security profile must enable Azure Virtual Network encryption.

Databricks states that customers remain responsible for their own compliance.

Seen in: [[Compliance Security Profile]], [[HIPAA]], [[SOC 2]]

## Recall

PCI DSS::The card industry's security standard for any system that stores, processes, or transmits payment card data.
Which Databricks setting supports PCI-DSS workloads?::The compliance security profile with the PCI-DSS standard selected.

> [!sources]- Sources (last verified: 2026-10-26)
> - [Compliance security profile (GCP)](https://docs.databricks.com/gcp/en/security/privacy/security-profile)
> - [Configure enhanced security and compliance settings (AWS)](https://docs.databricks.com/aws/en/security/privacy/enhanced-security-compliance)
> - [Compliance (Azure Databricks)](https://learn.microsoft.com/en-us/azure/databricks/security/privacy/)
> - [Foundation Model APIs compliance and security (AWS)](https://docs.databricks.com/aws/en/machine-learning/foundation-model-apis/compliance)
