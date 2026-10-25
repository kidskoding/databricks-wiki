---
type: glossary
status: written
level: 90
section: Glossary
depth: 101
summary: "An open standard for handing out short-lived access tokens instead of sharing passwords."
related:
  - "[[Authentication - Tokens and OAuth]]"
  - "[[Users Groups and Service Principals]]"
  - "[[Single Sign-On]]"
  - "[[Identity Provider]]"
  - "[[Databricks CLI]]"
  - "[[Token]]"
aliases:
  - "OAuth 2.0"
  - "OAuth2"
  - "OAuth M2M"
  - "OAuth U2M"
last_verified: 2026-10-25
tags:
  - glossary
  - flashcards
---

# OAuth

> [!eli5] Summary
> OAuth is a standard way for an application to get limited, temporary access on behalf of a user or program without handling a password.

**In data work:** OAuth 2.0 is a standard way for an app to get permission to act on a user's or a program's behalf. The app is sent to an authorization server (often the company's [[Identity Provider|identity provider]]), which issues a short-lived access [[Token|token]] with limited scope. The app never sees the password, and the token expires on its own, so a leak does less damage. User-to-machine (U2M) flows involve a person logging in through a browser; machine-to-machine (M2M) flows use a client ID and secret for automated jobs. When a reporting tool says Sign in with Microsoft, that is OAuth.

**In Databricks:** Databricks supports OAuth U2M for people using the [[Databricks CLI]], SDKs, and BI tools, and OAuth M2M for [[Users Groups and Service Principals|service principals]] running automation. For automated tools, scripts, and apps, Databricks recommends OAuth tokens over personal access tokens, and calls OAuth 2.0 its preferred protocol for service principals. Details and setup are in [[Authentication - Tokens and OAuth]]; on Azure, Microsoft Entra ID tokens are also accepted (see [[Microsoft Entra ID Integration]]).

Seen in: [[Authentication - Tokens and OAuth]], [[Users Groups and Service Principals]], [[Connecting Power BI]]

## Recall

OAuth::A standard for issuing short-lived, scoped access tokens so apps never handle passwords; Databricks recommends it over personal access tokens.

> [!sources]- Sources (last verified: 2026-10-25)
> - [Authorize service principal access with OAuth (AWS)](https://docs.databricks.com/aws/en/dev-tools/auth/oauth-m2m)
