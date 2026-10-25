---
type: glossary
status: written
level: 90
section: Glossary
depth: 101
summary: "Two meanings: a digital pass that proves who you are, or a small chunk of text that a language model reads and writes."
related:
  - "[[Authentication - Tokens and OAuth]]"
  - "[[OAuth]]"
  - "[[Secrets Management]]"
  - "[[LLM]]"
  - "[[Foundation Model APIs]]"
  - "[[Prompt]]"
aliases:
  - "tokens"
  - "access token"
  - "personal access token"
  - "PAT"
  - "LLM token"
  - "bearer token"
last_verified: 2026-10-25
tags:
  - glossary
  - flashcards
---

# Token

> [!eli5] Summary
> Token has two meanings. In security, it is a digital pass that proves identity; in AI, it is a small piece of text that a language model reads or writes.

**In data work:** In security, an access token is a string a program sends with each request (often in an `Authorization: Bearer` header) to prove identity. It replaces a password, can be scoped, and should expire; long-lived tokens are risky if leaked, so they belong in a secret store, never in code. In AI, a token is the unit an [[LLM]] processes: a word, part of a word, or a punctuation mark. Token counts set model limits (the context window) and usage metering.

**In Databricks:** Databricks uses both. For authentication, personal access tokens (PATs) and short-lived [[OAuth]] tokens let the [[Databricks CLI]], SDKs, and BI tools call the platform; Databricks recommends OAuth for automated tools and, where PATs are used, PATs that belong to service principals rather than people (see [[Authentication - Tokens and OAuth]] and [[Secrets Management]]). For AI, [[Foundation Model APIs]] in pay-per-token mode are metered separately for input and output tokens and have token-per-minute rate limits; see [[How Databricks Pricing Works]] for how that meter works.

Seen in: [[Authentication - Tokens and OAuth]], [[Foundation Model APIs]], [[Generative AI and LLMs]]

## Recall

Token (security)::A string sent with each request to prove identity, replacing a password; prefer short-lived OAuth tokens over long-lived PATs.
Token (AI)::The chunk of text an LLM reads or writes, roughly three-quarters of a word; model limits and usage are counted in tokens.

> [!sources]- Sources (last verified: 2026-10-25)
> - [Authorize service principal access with OAuth (AWS)](https://docs.databricks.com/aws/en/dev-tools/auth/oauth-m2m)
> - [Foundation Model APIs limits and quotas (AWS)](https://docs.databricks.com/aws/en/machine-learning/foundation-model-apis/limits)
> - [Foundation Model Serving pricing](https://www.databricks.com/product/pricing/foundation-model-serving)
