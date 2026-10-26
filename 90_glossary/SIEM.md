---
type: glossary
status: written
level: 90
section: Glossary
depth: 101
summary: "Security information and event management: a system that collects logs from many sources, correlates them, and alerts on suspicious activity."
related:
  - "[[Audit Logs]]"
  - "[[System Tables]]"
  - "[[Azure Monitor and Diagnostic Logs]]"
  - "[[Compliance Security Profile]]"
  - "[[SQL Alerts]]"
  - "[[Data Governance]]"
aliases:
  - "security information and event management"
  - "SIEM tool"
last_verified: 2026-10-26
tags:
  - glossary
  - flashcards
---

# SIEM

> [!eli5] Summary
> A SIEM is a security control room for logs. It gathers activity records from many systems in one place and raises an alarm when something looks wrong.

**In data work:** A SIEM ingests logs from identity providers, firewalls, servers, and applications, normalizes them, and runs detection rules across sources. Examples of rules are many failed sign-ins followed by a success, an admin granting themselves new privileges, or a large data download at 3:00 AM. Security teams also use it for investigations and to keep logs for the retention periods auditors require. Splunk and Microsoft Sentinel are common SIEM products.

**In Databricks:** Databricks produces the logs; the SIEM consumes them.
- **Audit log system table:** `system.access.audit` records account and workspace events and keeps 365 days of history (see [[Audit Logs]] and [[System Tables]]).
- **Log delivery:** Audit logs can be delivered to cloud storage on AWS and Google Cloud, and to Azure Monitor destinations on Azure (see [[Azure Monitor and Diagnostic Logs]]), from where a SIEM ingests them.
- **Enhanced security monitoring:** With the [[Compliance Security Profile|compliance security profile]], antivirus and file integrity events from classic compute are written to the audit log. Ingesting them into a SIEM is your responsibility, as is securing exported logs.

A small business without a SIEM can schedule [[SQL Alerts|SQL alerts]] on `system.access.audit` for a few high-risk events, such as failed admin logins or permission changes.

Seen in: [[Audit Logs]], [[System Tables]], [[Azure Monitor and Diagnostic Logs]]

## Recall

SIEM::Security information and event management: a system that centralizes logs, correlates them, and alerts on threats.
Which Databricks system table holds audit events?::system.access.audit.

> [!sources]- Sources (last verified: 2026-10-26)
> - [Audit log reference (AWS)](https://docs.databricks.com/aws/en/admin/account-settings/audit-logs)
> - [System tables reference (AWS)](https://docs.databricks.com/aws/en/admin/system-tables/)
> - [Enhanced security monitoring (AWS)](https://docs.databricks.com/aws/en/security/privacy/enhanced-security-monitoring)
> - [Configure diagnostic log delivery (Azure Databricks)](https://learn.microsoft.com/en-us/azure/databricks/admin/account-settings/audit-log-delivery)
> - [Improve Lakehouse Security Monitoring using System Tables (Databricks blog)](https://www.databricks.com/blog/improve-lakehouse-security-monitoring-using-system-tables-databricks-unity-catalog)
