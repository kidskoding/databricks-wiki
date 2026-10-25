---
type: glossary
status: written
level: 90
section: Glossary
depth: 101
summary: "Encrypting data while it moves across a network, usually with TLS, so intermediaries cannot read or alter it."
related:
  - "[[Encryption]]"
  - "[[Network Security Overview]]"
  - "[[Secure Cluster Connectivity]]"
  - "[[Azure Private Link]]"
  - "[[AWS PrivateLink]]"
  - "[[Private Service Connect]]"
aliases:
  - "TLS"
  - "SSL"
  - "HTTPS"
  - "in-transit encryption"
  - "data in transit"
last_verified: 2026-10-25
tags:
  - glossary
  - flashcards
---

# Encryption in Transit

> [!eli5] Summary
> Encryption in transit protects data while it travels between computers, so anyone intercepting it cannot read it.

**In data work:** Data in transit moves between systems: a browser and a web service, an application and its database, or two servers. TLS (the successor to SSL, used by HTTPS) encrypts the connection and authenticates the server. Without it, any party on the network path can read or modify the data. Private network connectivity is a separate control: it keeps traffic off the public internet but does not replace encryption.

**In Databricks:** Databricks encrypts customer traffic with TLS 1.2 or higher between users and the control plane and between the control plane and the compute plane, including serverless compute. Traffic between worker nodes of a classic cluster is not encrypted by default on AWS and Azure; enable it with an init script that configures Spark network encryption. The [[JDBC and ODBC]] drivers connect over TLS on port 443. [[Secure Cluster Connectivity]] removes public IPs from nodes, and [[Azure Private Link]], [[AWS PrivateLink]], and [[Private Service Connect]] keep traffic on private networks. See [[Encryption]].

Seen in: [[Encryption]], [[Network Security Overview]], [[Secure Cluster Connectivity]]

## Recall

Which protocol usually provides encryption in transit?::TLS (Transport Layer Security).
Is traffic between classic cluster worker nodes encrypted by default on AWS?::No. It can be enabled with an init script.

> [!sources]- Sources (last verified: 2026-10-25)
> - [Encrypt traffic between cluster worker nodes (AWS)](https://docs.databricks.com/aws/en/security/keys/encrypt-otw)
> - [Databricks Security Addendum](https://www.databricks.com/legal/security-addendum)
> - [Serverless compute security (Databricks)](https://www.databricks.com/trust/security-features/serverless-security)
