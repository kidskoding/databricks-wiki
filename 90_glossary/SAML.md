---
type: glossary
status: written
level: 90
section: Glossary
depth: 101
summary: "Security Assertion Markup Language: an XML-based standard an identity provider uses to tell an application that a user has signed in."
related:
  - "[[Single Sign-On]]"
  - "[[Identity Provider]]"
  - "[[OpenID Connect]]"
  - "[[SCIM]]"
  - "[[Microsoft Entra ID Integration]]"
  - "[[Multi-Factor Authentication]]"
aliases:
  - "SAML 2.0"
  - "Security Assertion Markup Language"
  - "SAML assertion"
last_verified: 2026-10-26
tags:
  - glossary
  - flashcards
---

# SAML

> [!eli5] Summary
> SAML is a standard that lets you sign in once with your company account and then open other apps without new passwords. The sign-in service vouches for you to each app.

**In data work:** SAML 2.0 defines two parties. The **identity provider** (IdP), such as Okta or Microsoft Entra ID, authenticates the user. The **service provider** (SP), such as Databricks, trusts the IdP. When a user opens the SP, the browser is redirected to the IdP, which signs the user in (often with [[Multi-Factor Authentication|MFA]]) and returns a digitally signed XML **assertion** that names the user. The SP checks the signature against the IdP's certificate and starts a session. SAML is older and XML-based; [[OpenID Connect]] is the newer JSON-based alternative, and both deliver [[Single Sign-On|single sign-on]].

**In Databricks:** Account admins configure SSO in the [[Account Console|account console]] under **Security**, **Identity provider setup**, choosing SAML 2.0 or OIDC.
- **Unified login:** One SSO configuration applies to the account console and all workspaces; it is enabled by default for most accounts.
- **Emergency access:** Admins can name up to 20 users who can sign in with a password and MFA if the IdP fails.
- **Azure:** Azure Databricks signs users in through Microsoft Entra ID natively (see [[Microsoft Entra ID Integration]]).

SAML only signs users in. Creating and removing their accounts is a separate job handled by [[SCIM]].

Seen in: [[Single Sign-On]], [[Identity Provider]], [[SCIM Provisioning]]

## Recall

SAML::An XML-based standard in which an identity provider sends a signed assertion to an application to sign a user in.
Which standard provisions users, as opposed to signing them in?::SCIM.

> [!sources]- Sources (last verified: 2026-10-26)
> - [Configure SSO using SAML (AWS)](https://docs.databricks.com/aws/en/admin/account-settings-e2/single-sign-on/saml)
> - [Configure SSO using SAML (GCP)](https://docs.databricks.com/gcp/en/security/auth/single-sign-on/saml)
> - [Configure SSO in Databricks (AWS)](https://docs.databricks.com/aws/en/security/auth/single-sign-on/)
> - [Emergency access to prevent lockouts (AWS)](https://docs.databricks.com/aws/en/security/auth/single-sign-on/emergency-access)
