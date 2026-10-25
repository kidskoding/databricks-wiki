---
type: glossary
status: written
level: 90
section: Glossary
depth: 101
summary: "Encrypting stored data so it cannot be read without the key, even with direct access to the storage."
related:
  - "[[Encryption]]"
  - "[[Customer-Managed Keys on Azure]]"
  - "[[Customer-Managed Keys on AWS]]"
  - "[[Customer-Managed Keys on Google Cloud]]"
  - "[[Compliance Security Profile]]"
  - "[[Encryption in Transit]]"
aliases:
  - "at-rest encryption"
  - "storage encryption"
  - "data at rest"
last_verified: 2026-10-25
tags:
  - glossary
  - flashcards
---

# Encryption at Rest

> [!eli5] Summary
> Encryption at rest scrambles stored data so that anyone who obtains the disk or files cannot read them without the key.

**In data work:** Data at rest is data in storage: disks, object storage, and backups. Encrypting it protects against stolen hardware, exposed backups, and direct storage access. The key question is who controls the keys: the provider (platform-managed keys) or the customer (customer-managed keys in a key management service, which the customer can rotate or revoke). Compliance frameworks such as [[HIPAA]] and [[SOC 2]] expect it. See also [[Encryption in Transit]].

**In Databricks:** Databricks supports customer-managed keys for two use cases. **Managed services** covers control-plane data such as notebooks, secrets, and SQL query data. **Workspace storage** covers the workspace storage bucket and, on AWS, optionally cluster EBS volumes; Azure has a separate managed-disks key option. Keys come from AWS KMS, Azure Key Vault, or Cloud KMS ([[Customer-Managed Keys on AWS]], [[Customer-Managed Keys on Azure]], [[Customer-Managed Keys on Google Cloud]]). The feature requires the Enterprise tier on AWS. Serverless workspaces need only the managed services key. On Azure, existing data is not re-encrypted. See [[Encryption]].

Seen in: [[Encryption]], [[Customer-Managed Keys on Azure]], [[Customer-Managed Keys on AWS]], [[Compliance Security Profile]]

## Recall

What does encryption at rest protect against?::Reading stored data directly, for example from stolen disks, backups, or raw storage access.
What are the two Databricks customer-managed key use cases?::Managed services (control-plane data) and workspace storage.

> [!sources]- Sources (last verified: 2026-10-25)
> - [Customer-managed keys for encryption (AWS)](https://docs.databricks.com/aws/en/security/keys/customer-managed-keys)
> - [Customer-managed keys for managed services (Azure)](https://learn.microsoft.com/en-us/azure/databricks/security/keys/cmk-managed-services-azure/)
> - [Customer-managed keys for encryption (GCP)](https://docs.databricks.com/gcp/en/security/keys/customer-managed-keys)
