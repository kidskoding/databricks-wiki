---
type: glossary
status: written
level: 90
section: Glossary
depth: 101
summary: "The US government program that standardizes security assessment and authorization of cloud services for federal agencies; Databricks on AWS GovCloud holds a FedRAMP High authorization."
related:
  - "[[Databricks on AWS GovCloud]]"
  - "[[Compliance Security Profile]]"
  - "[[SOC 2]]"
  - "[[HIPAA]]"
  - "[[PCI DSS]]"
  - "[[Encryption]]"
aliases:
  - "Federal Risk and Authorization Management Program"
  - "FedRAMP High"
  - "FedRAMP Moderate"
last_verified: 2026-10-26
tags:
  - glossary
  - flashcards
---

# FedRAMP

> [!eli5] Summary
> FedRAMP is the US federal government's security approval for cloud services. A US agency generally needs a cloud product to hold it before the agency can use that product.

**In data work:** FedRAMP (Federal Risk and Authorization Management Program) defines a common set of security controls and an assessment process, so a cloud service is authorized once and reused across agencies. Authorizations are issued at impact levels (Low, Moderate, High) based on the sensitivity of the data. An authorization covers the provider's controls; the customer still implements its own share, documented in the package's customer responsibility matrix.

**In Databricks:** Databricks documents **FedRAMP High** authorization for [[Databricks on AWS GovCloud]]. On GovCloud the [[Compliance Security Profile|compliance security profile]] is enabled by default on every workspace, adding a hardened compute image, enhanced security monitoring, and automatic cluster updates. Single sign-on and [[AWS PrivateLink|PrivateLink]] for front-end and back-end connections are required. Some features, including serverless compute, are in Public Preview on GovCloud as of October 2026. A separate DoD IL5 option exists. This note does not confirm Azure Databricks FedRAMP scope; check Microsoft's Azure compliance documentation for Azure Government.

Small-business consideration: most small companies can ignore FedRAMP. It matters only if you sell software or data services to US federal agencies and must process their data in an authorized environment.

Seen in: [[Databricks on AWS GovCloud]], [[Compliance Security Profile]]

## Recall

What does FedRAMP authorize?::Cloud services for use by US federal agencies, at Low, Moderate, or High impact levels.
Which Databricks deployment documents FedRAMP High authorization?::Databricks on AWS GovCloud.

> [!sources]- Sources (last verified: 2026-10-26)
> - [FedRAMP High (AWS)](https://docs.databricks.com/aws/en/security/privacy/fedramp-high)
> - [Databricks on AWS GovCloud](https://docs.databricks.com/aws/en/security/privacy/gov-cloud)
> - [DoD IL5 (AWS)](https://docs.databricks.com/aws/en/security/privacy/il5)
