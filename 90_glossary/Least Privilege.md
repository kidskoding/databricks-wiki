---
type: glossary
status: written
level: 90
section: Glossary
depth: 101
summary: "Give each person or program only the access it needs for its job, and nothing more."
related:
  - "[[Privileges and Grants]]"
  - "[[Role-Based Access Control]]"
  - "[[Users Groups and Service Principals]]"
  - "[[Unity Catalog]]"
  - "[[Admin Roles]]"
  - "[[Row Filters and Column Masks]]"
aliases:
  - "principle of least privilege"
  - "PoLP"
  - "minimal access"
last_verified: 2026-10-25
tags:
  - glossary
  - flashcards
---

# Least Privilege

> [!eli5] Summary
> Least privilege is the security rule of giving each person or program only the access its job requires. It limits the damage from mistakes and stolen accounts.

**In data work:** The principle of least privilege is a security rule: every user, service account, and program gets the smallest set of permissions that lets it do its work, for as long as it needs them. If an account is stolen or a script has a bug, the damage stays small. In a small accounting firm, the part-time bookkeeper might read client invoices but never see payroll, and the nightly export script might write to one folder only. Least privilege is usually applied through [[Role-Based Access Control|roles or groups]] rather than by hand for each person.

**In Databricks:** [[Unity Catalog]] is built for this. You grant specific [[Privileges and Grants|privileges]] (such as `SELECT` on one schema) to groups, not individuals, and run production jobs as [[Users Groups and Service Principals|service principals]] with narrow rights. [[Row Filters and Column Masks]] narrow access further inside a table. Keep [[Admin Roles|admin roles]] to a few people, and use [[Compute Policies]] to limit what compute users can create.

Seen in: [[Privileges and Grants]], [[Users Groups and Service Principals]], [[Admin Roles]]

## Recall

Least Privilege::Give every user and program only the permissions its job needs, so a mistake or stolen account can do little harm.
