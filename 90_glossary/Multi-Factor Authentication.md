---
type: glossary
status: written
level: 90
section: Glossary
depth: 101
summary: "Sign-in that requires a second proof of identity, such as a code from an authenticator app, in addition to a password."
related:
  - "[[Single Sign-On]]"
  - "[[Identity Provider]]"
  - "[[Authentication - Tokens and OAuth]]"
  - "[[Microsoft Entra ID Integration]]"
  - "[[Account Console]]"
  - "[[Compliance Security Profile]]"
aliases:
  - "MFA"
  - "two-factor authentication"
  - "2FA"
last_verified: 2026-10-26
tags:
  - glossary
  - flashcards
---

# Multi-Factor Authentication

> [!eli5] Summary
> Multi-factor authentication asks for something besides your password, such as a code from your phone. A stolen password alone is then not enough to sign in.

**In data work:** MFA combines two or more kinds of evidence: something you know (a password), something you have (a phone or security key), or something you are (a fingerprint). It is one of the most effective controls against account takeover, and most compliance frameworks expect it for access to sensitive data. In a five-person shop where everyone signs in to the same reporting tools, turning on MFA in the company's identity provider protects every connected app at once.

**In Databricks:** Account admins configure sign-in for the whole account in the [[Account Console|account console]].
- **With single sign-on:** MFA is enforced by your [[Identity Provider|identity provider]] (Okta, Microsoft Entra ID, and others). When [[Single Sign-On|SSO]] is enabled, Databricks-managed MFA is disabled and cannot be changed.
- **Without single sign-on:** Databricks-managed MFA can be set to recommended, required, or disabled.
- **Emergency access:** Admins can grant emergency access to up to 20 users, who sign in with a password and MFA if the identity provider is unavailable.

On Azure Databricks, MFA is configured in Microsoft Entra ID (see [[Microsoft Entra ID Integration]]). MFA protects interactive sign-in; automated jobs should use [[OAuth]] with [[Users Groups and Service Principals|service principals]] instead.

Seen in: [[Single Sign-On]], [[Authentication - Tokens and OAuth]], [[Account Console]]

## Recall

Multi-factor authentication::Sign-in that requires a second factor (such as a phone code) in addition to a password.
Where is MFA enforced when a Databricks account uses SSO?::In the identity provider; Databricks-managed MFA is disabled.

> [!sources]- Sources (last verified: 2026-10-26)
> - [Configure multi-factor authentication (AWS)](https://docs.databricks.com/aws/en/security/auth/mfa)
> - [Emergency access to prevent lockouts (AWS)](https://docs.databricks.com/aws/en/security/auth/single-sign-on/emergency-access)
> - [Authentication and access control (AWS)](https://docs.databricks.com/aws/en/security/auth/)
> - [Authentication and access control (Azure Databricks)](https://learn.microsoft.com/en-us/azure/databricks/security/auth/)
