---
type: glossary
status: written
level: 90
section: Glossary
depth: 101
summary: "Granting permissions to roles or groups, then putting people in those groups, instead of granting to each person."
related:
  - "[[Privileges and Grants]]"
  - "[[Attribute-Based Access Control]]"
  - "[[Users Groups and Service Principals]]"
  - "[[Least Privilege]]"
  - "[[Admin Roles]]"
  - "[[SCIM Provisioning]]"
aliases:
  - "RBAC"
  - "role-based permissions"
  - "group-based access"
last_verified: 2026-10-25
tags:
  - glossary
  - flashcards
---

# Role-Based Access Control

> [!eli5] Summary
> Role-based access control assigns permissions to roles or groups and then assigns people to those groups. Access follows the job rather than the individual.

**In data work:** In RBAC, you define roles or groups such as analysts, finance, or pipeline-runners, grant permissions to those, and add or remove people. When someone joins or leaves, you change one group membership instead of dozens of grants. It is the main tool for [[Least Privilege|least privilege]] at scale. Its weakness is role explosion: if every exception needs a new role, the list grows unmanageable. [[Attribute-Based Access Control]] (ABAC) complements it by deciding access from tags on the data. A ten-person accounting firm might have three groups: partners, staff, and contractors, each with different access to client folders.

**In Databricks:** In [[Unity Catalog]], you grant [[Privileges and Grants|privileges]] on catalogs, schemas, tables, and other objects to account-level groups, ideally synced from your identity provider with [[SCIM Provisioning]]. Platform roles such as account admin and workspace admin are covered in [[Admin Roles]]. Tag-based policies are in [[Attribute-Based Access Control]].

Seen in: [[Privileges and Grants]], [[Users Groups and Service Principals]], [[Admin Roles]]

## Recall

Role-Based Access Control::Granting permissions to groups or roles and managing membership, rather than granting to individuals; in Unity Catalog you grant to groups.
