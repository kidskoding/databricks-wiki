---
type: glossary
status: written
level: 90
section: Glossary
depth: 101
summary: "An identity layer on top of OAuth 2.0 that lets an application confirm who a user or workload is through a signed ID token."
related:
  - "[[OAuth]]"
  - "[[SAML]]"
  - "[[Single Sign-On]]"
  - "[[Identity Provider]]"
  - "[[Authentication - Tokens and OAuth]]"
  - "[[Token]]"
aliases:
  - "OIDC"
  - "OpenID Connect (OIDC)"
  - "workload identity federation"
last_verified: 2026-10-26
tags:
  - glossary
  - flashcards
---

# OpenID Connect

> [!eli5] Summary
> OpenID Connect is a standard way for a sign-in service to tell an app who you are. It builds on OAuth, which handles what the app is allowed to do.

**In data work:** [[OAuth]] 2.0 grants access but does not say who the user is. OIDC adds that: after sign-in, the [[Identity Provider|identity provider]] issues a signed ID token (a JSON Web Token) that carries claims such as the subject, issuer, and audience. The application verifies the signature and trusts the claims. OIDC is the modern, JSON-based alternative to [[SAML]] for [[Single Sign-On|single sign-on]], and it also identifies machines: CI systems such as GitHub Actions issue OIDC tokens to each pipeline run.

**In Databricks:** OIDC appears in two places.
- **Single sign-on:** Account SSO can be configured with OIDC or SAML against your identity provider.
- **Workload identity federation:** Databricks OAuth token federation (OIDC) lets automated workloads, such as GitHub Actions, GitLab CI/CD, CircleCI, Jenkins, and AWS IAM workloads, exchange their own OIDC tokens for Databricks OAuth tokens. An account admin creates a federation policy that names the token issuer, audiences, and subject, and the workload authenticates as a [[Users Groups and Service Principals|service principal]]. No Databricks secret is stored in the pipeline, which is why Databricks recommends this method whenever possible.

For a small team deploying with GitHub Actions, federation removes the need to store and rotate a [[Personal Access Token|personal access token]].

Seen in: [[Authentication - Tokens and OAuth]], [[Single Sign-On]], [[CI-CD for Data Pipelines]]

## Recall

OpenID Connect (OIDC)::An identity layer on OAuth 2.0 in which the identity provider issues a signed ID token that proves who the user or workload is.
What does Databricks workload identity federation remove from CI/CD pipelines?::Stored Databricks secrets; the pipeline exchanges its own OIDC token for a Databricks OAuth token.

> [!sources]- Sources (last verified: 2026-10-26)
> - [Configure SSO using OIDC (GCP)](https://docs.databricks.com/gcp/en/security/auth/single-sign-on/oidc)
> - [Enable workload identity federation in CI/CD (AWS)](https://docs.databricks.com/aws/en/dev-tools/auth/oauth-federation-provider)
> - [Enable workload identity federation for GitHub Actions (AWS)](https://docs.databricks.com/aws/en/dev-tools/auth/provider-github)
> - [Configure a federation policy (AWS)](https://docs.databricks.com/aws/en/dev-tools/auth/oauth-federation-policy)
