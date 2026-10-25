---
type: glossary
status: written
level: 90
section: Glossary
depth: 101
summary: "Identity and access management: the systems and policies that establish who a user or service is and what it is allowed to do."
related:
  - "[[Users Groups and Service Principals]]"
  - "[[Cross-Account IAM Role]]"
  - "[[Instance Profiles]]"
  - "[[S3 Access via Unity Catalog]]"
  - "[[Google Service Accounts]]"
  - "[[Microsoft Entra ID Integration]]"
aliases:
  - "identity and access management"
  - "AWS IAM"
  - "IAM role"
  - "IAM policy"
last_verified: 2026-10-25
tags:
  - glossary
  - flashcards
---

# IAM

> [!eli5] Summary
> IAM decides who someone is and what they are allowed to do. It covers both signing in and the permissions attached to each person or program.

**In data work:** IAM has two parts: authentication (verifying identity, by password, single sign-on, or key) and authorization (granting permissions). Identities include users, groups, and service identities. Permissions are grouped into roles or policies and assigned following [[Least Privilege|least privilege]]. The term also names specific cloud services: AWS IAM (users, roles, policies) and Google Cloud IAM; on Azure, the equivalent is Microsoft Entra ID with Azure role-based access control.

**In Databricks:** Databricks has its own identities ([[Users Groups and Service Principals]]) and data permissions ([[Privileges and Grants]] in Unity Catalog), and it uses cloud IAM to reach cloud resources. On AWS, a [[Cross-Account IAM Role]] lets Databricks launch EC2 instances, and Unity Catalog storage credentials use IAM roles for [[S3 Access via Unity Catalog|S3 access]], replacing [[Instance Profiles]]. On Google Cloud, [[Google Service Accounts]] serve this purpose. On Azure, [[Microsoft Entra ID Integration|Entra ID]] and [[Managed Identity|managed identities]] do.

Seen in: [[Users Groups and Service Principals]], [[Cross-Account IAM Role]], [[S3 Access via Unity Catalog]], [[Google Service Accounts]]

## Recall

What are the two parts of IAM?::Authentication (who you are) and authorization (what you may do).
What does a Unity Catalog storage credential use on AWS to reach S3?::An IAM role.
