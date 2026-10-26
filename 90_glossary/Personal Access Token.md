---
type: glossary
status: written
level: 90
section: Glossary
depth: 101
summary: "A long-lived secret tied to one user that authenticates scripts and tools to Databricks APIs; Databricks treats it as legacy and recommends OAuth."
related:
  - "[[Token]]"
  - "[[OAuth]]"
  - "[[Authentication - Tokens and OAuth]]"
  - "[[Secrets Management]]"
  - "[[Users Groups and Service Principals]]"
  - "[[Databricks CLI]]"
aliases:
  - "PAT"
  - "PATs"
  - "personal access tokens"
  - "Databricks token"
last_verified: 2026-10-26
tags:
  - glossary
  - flashcards
---

# Personal Access Token

> [!eli5] Summary
> A personal access token is a long password-like string that lets a program act as you. Anyone who has it can use your access until it expires or is revoked.

**In data work:** A personal access token (PAT) is a bearer credential: the client sends it in an `Authorization: Bearer <token>` header, and the service grants the owner's permissions. PATs are easy to create, which is why they end up pasted into notebooks, `.env` files, and BI tool settings. They are risky for the same reason: they live long, are tied to a person, and still work after that person changes roles.

**In Databricks:** Databricks documents PATs as a legacy method and recommends [[OAuth]] for users and [[Users Groups and Service Principals|service principals]].
- **Lifetime:** The default maximum lifetime for new PATs is 730 days. Admins can set a lower maximum.
- **Control:** Workspace admins can monitor and revoke tokens and control who may create them.
- **Ownership:** Prefer tokens owned by a service principal over a person, so automation does not break when someone leaves.
- **Storage:** Keep tokens in a secret store, not in code (see [[Secrets Management]]).

For a small business, the most common PAT is the one in a BI connection. Replace it with OAuth where the tool supports it, or at least give it an expiry and an owner. For CI/CD, [[OpenID Connect|workload identity federation]] removes stored tokens entirely. Details are in [[Authentication - Tokens and OAuth]].

Seen in: [[Authentication - Tokens and OAuth]], [[Databricks CLI]], [[Connecting Power BI]]

## Recall

Personal access token (PAT)::A long-lived bearer secret that lets a tool act as its owner; legacy in Databricks, which recommends OAuth.
What is the default maximum lifetime for new Databricks PATs?::730 days.

> [!sources]- Sources (last verified: 2026-10-26)
> - [Authenticate with personal access tokens, legacy (AWS)](https://docs.databricks.com/aws/en/dev-tools/auth/pat)
> - [Monitor and revoke personal access tokens (AWS)](https://docs.databricks.com/aws/en/admin/access-control/tokens)
> - [Monitor and revoke personal access tokens (Azure)](https://learn.microsoft.com/en-us/azure/databricks/admin/access-control/tokens)
> - [Manage personal access token permissions (AWS)](https://docs.databricks.com/aws/en/security/auth/api-access-permissions)
