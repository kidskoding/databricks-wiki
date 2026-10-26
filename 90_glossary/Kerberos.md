---
type: glossary
status: written
level: 90
section: Glossary
depth: 101
summary: "A network authentication protocol that uses tickets from a trusted key distribution center; it secured Hadoop clusters, while Databricks uses OAuth and single sign-on instead."
related:
  - "[[Apache Hadoop]]"
  - "[[Migrating from Hadoop]]"
  - "[[Authentication - Tokens and OAuth]]"
  - "[[Single Sign-On]]"
  - "[[OAuth]]"
  - "[[Identity Provider]]"
aliases:
  - "Kerberos authentication"
  - "KDC"
  - "keytab"
  - "SPNEGO"
last_verified: 2026-10-26
tags:
  - glossary
  - flashcards
---

# Kerberos

> [!eli5] Summary
> Kerberos is an older system for proving who you are on a company network. You log in once and receive tickets that let you use other services without typing your password again.

**In data work:** Kerberos uses a trusted Key Distribution Center (KDC). A user or service authenticates once, receives a ticket-granting ticket, and then requests service tickets for each server it contacts. Identities are **principals** such as `alice@EXAMPLE.COM` or `nn/host@EXAMPLE.COM`; services store their keys in **keytab** files. Active Directory uses Kerberos for Windows domain logins.

**In Databricks:** In secure mode, [[Apache Hadoop]] requires every service and user to authenticate with Kerberos, configured with `hadoop.security.authentication = kerberos`, per-service principals, and keytabs. When you [[Migrating from Hadoop|migrate from Hadoop]], Kerberos does not move with you. Databricks authenticates people with [[Single Sign-On|single sign-on]] through your [[Identity Provider|identity provider]] and authenticates tools with [[OAuth]] or [[Personal Access Token|personal access tokens]] (see [[Authentication - Tokens and OAuth]]). The Databricks JDBC driver uses Kerberos (SPNEGO) only to authenticate to a proxy server. Some [[Lakehouse Federation]] connectors do not support Kerberos; for example, the Teradata connector lists it as unsupported, so check each connector page.

Small-business consideration: you will meet Kerberos only if you are leaving an on-premises Hadoop cluster or a Windows-domain database. Plan to replace it with SSO and service principals.

Seen in: [[Apache Hadoop]], [[Migrating from Hadoop]]

## Recall

What does a Kerberos keytab file contain?::The stored key for a principal, so a service can authenticate without a password prompt.
What replaces Hadoop's Kerberos authentication on Databricks?::Single sign-on through an identity provider, plus OAuth or personal access tokens for tools.

> [!sources]- Sources (last verified: 2026-10-26)
> - [Hadoop in Secure Mode (hadoop.apache.org)](https://hadoop.apache.org/docs/current/hadoop-project-dist/hadoop-common/SecureMode.html)
> - [Configure a connection using the Databricks JDBC Driver (AWS)](https://docs.databricks.com/aws/en/integrations/jdbc-oss/configure)
> - [Run federated queries on Teradata (AWS)](https://docs.databricks.com/aws/en/query-federation/teradata)
