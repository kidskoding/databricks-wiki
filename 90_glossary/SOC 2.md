---
type: glossary
status: written
level: 90
section: Glossary
depth: 101
summary: "An independent audit report showing a service provider protects customer data with proper security controls."
related:
  - "[[Compliance Security Profile]]"
  - "[[HIPAA]]"
  - "[[GDPR]]"
  - "[[Audit Logs]]"
  - "[[Encryption]]"
  - "[[Data Governance]]"
aliases:
  - "SOC 2 Type II"
  - "SOC 2 Type 1"
  - "Service Organization Control 2"
  - "SOC2"
last_verified: 2026-10-25
tags:
  - glossary
  - flashcards
---

# SOC 2

> [!eli5] Summary
> SOC 2 is an independent audit report that shows how a service provider protects customer data. Business customers often require it from vendors.

**In data work:** SOC 2 is a report in which an independent auditor examines a service company's controls in areas such as security, availability, and confidentiality. The version business customers usually ask for is the SOC 2 Type II report, and many will not sign with a vendor that cannot provide one. A small payroll company buying a data platform would review the vendor's report, and may be asked for its own by clients.

**In Databricks:** Databricks lists its attestations in its Trust Center, and its SOC 2 Type II report is requested through your account team rather than downloaded publicly. A vendor's SOC 2 covers the vendor's controls, not yours: you still configure access with [[Unity Catalog]], keep [[Audit Logs]], and use [[Encryption]]. For regulated workloads such as [[HIPAA]], Databricks requires the [[Compliance Security Profile]].

Seen in: [[Compliance Security Profile]], [[Audit Logs]], [[Network Security Overview]]

## Recall

SOC 2::An independent audit report on a service provider's security controls; customers usually ask vendors for the SOC 2 Type II report.

> [!sources]- Sources (last verified: 2026-10-25)
> - [Databricks Trust: Compliance](https://www.databricks.com/trust/compliance)
> - [Databricks Trust Center](https://www.databricks.com/trust/trust)
