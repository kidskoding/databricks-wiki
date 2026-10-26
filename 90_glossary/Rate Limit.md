---
type: glossary
status: written
level: 90
section: Glossary
depth: 101
summary: "A cap on how many requests or tokens a client can send to a service in a time window; requests over the cap receive HTTP 429."
related:
  - "[[APIs]]"
  - "[[REST]]"
  - "[[Foundation Model APIs]]"
  - "[[Unity Gateway]]"
  - "[[Model Serving]]"
  - "[[Pagination]]"
aliases:
  - "throttling"
  - "HTTP 429"
  - "rate limiting"
  - "quota"
last_verified: 2026-10-26
tags:
  - glossary
  - flashcards
---

# Rate Limit

> [!eli5] Summary
> A rate limit is a speed limit on how often you can call a service. Go over it and the service tells you to slow down and try again later.

**In data work:** Services cap request rates to protect shared capacity and control cost. Limits are expressed per time unit, such as requests per second or tokens per minute. When a client exceeds one, the service returns HTTP `429 Too Many Requests`, often with a `Retry-After` header. Well-behaved clients retry with exponential backoff (wait longer after each failure) and jitter (a random offset so many clients do not retry in sync).

**In Databricks:**
- **REST APIs:** Limits apply per endpoint and per workspace. Retry 429 responses with exponential backoff and jitter, and wait at least the `Retry-After` value when present. The Databricks SDKs and CLI can retry for you.
- **[[Foundation Model APIs]] (pay-per-token):** Limits are set on input tokens per minute (ITPM), output tokens per minute (OTPM), and queries per hour (QPH); the most restrictive one applies. A 503 means the service is temporarily at capacity, which is different from your own limit.
- **[[Unity Gateway]]:** Service owners can set rate limits per service, user, or group on model and MCP services. Exceeding the service-level limit blocks all requests to that service.

For a small team calling an LLM from a nightly job, add backoff to the client and spread requests over time rather than sending them all at once.

Seen in: [[Foundation Model APIs]], [[Unity Gateway]], [[Databricks SDKs and REST API]]

## Recall

Rate limit::A cap on requests or tokens per time window; exceeding it returns HTTP 429.
How should a client handle HTTP 429 from Databricks?::Retry with exponential backoff and jitter, waiting at least the Retry-After value.

> [!sources]- Sources (last verified: 2026-10-26)
> - [Databricks REST API (AWS)](https://docs.databricks.com/aws/en/dev-tools/rest-api)
> - [Foundation Model APIs limits and quotas (AWS)](https://docs.databricks.com/aws/en/machine-learning/foundation-model-apis/limits)
> - [Apply rate limits to model and MCP services (AWS)](https://docs.databricks.com/aws/en/ai-gateway/rate-limits)
> - [Unity Catalog best practices (Azure Databricks)](https://learn.microsoft.com/en-us/azure/databricks/data-governance/unity-catalog/best-practices)
