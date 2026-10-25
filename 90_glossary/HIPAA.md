---
type: glossary
status: written
level: 90
section: Glossary
depth: 101
summary: "The US healthcare law that sets national standards for protecting the privacy and security of protected health information (PHI)."
related:
  - "[[Compliance Security Profile]]"
  - "[[Encryption]]"
  - "[[Audit Logs]]"
  - "[[Row Filters and Column Masks]]"
  - "[[Data Governance]]"
  - "[[Data Classification]]"
aliases:
  - "Health Insurance Portability and Accountability Act"
  - "PHI"
  - "protected health information"
  - "BAA"
  - "business associate agreement"
last_verified: 2026-10-25
tags:
  - glossary
  - flashcards
---

# HIPAA

> [!eli5] Summary
> HIPAA is a US law that protects medical information. Healthcare organizations and the vendors that handle patient data for them must keep it secure and private.

**In data work:** HIPAA establishes privacy, security, and breach-notification rules for protected health information (PHI): information that links a person to their health, treatment, or payment for care. It applies to covered entities (such as providers and insurers) and to business associates that create, receive, maintain, transmit, or access PHI on their behalf. A cloud service provider that handles PHI is a business associate and signs a business associate agreement (BAA).

**In Databricks:** Each workspace that processes PHI must have the [[Compliance Security Profile]] enabled with HIPAA selected; enabling it constitutes agreement to the Databricks BAA unless a separate BAA is in place. The profile adds a CIS Level 1 hardened image, FIPS 140 validated encryption modules, and enhanced security monitoring. Only supported preview features may be used with PHI, and PHI must not be placed in free-text fields such as workspace or job names. Customers remain responsible for encrypting PHI in their own storage. HIPAA controls are available on AWS, Azure, and Google Cloud. Within the workspace, use [[Data Classification]], [[Row Filters and Column Masks]], and [[Audit Logs]].

Seen in: [[Compliance Security Profile]], [[Encryption]], [[Audit Logs]], [[Who Uses Databricks - Business Types]]

## Recall

What does PHI stand for?::Protected health information.
What must be enabled on a Databricks workspace that processes PHI?::The compliance security profile with HIPAA selected.

> [!sources]- Sources (last verified: 2026-10-25)
> - [HIPAA (AWS)](https://docs.databricks.com/aws/en/security/privacy/hipaa)
> - [HIPAA (Azure)](https://learn.microsoft.com/en-us/azure/databricks/security/privacy/hipaa)
> - [HIPAA (GCP)](https://docs.databricks.com/gcp/en/security/privacy/hipaa)
> - [Compliance security profile (AWS)](https://docs.databricks.com/aws/en/security/privacy/security-profile)
