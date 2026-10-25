---
type: glossary
status: written
level: 90
section: Glossary
depth: 101
summary: "A service level agreement: a written promise about uptime, speed, or delivery time, often with penalties if missed."
related:
  - "[[Lakeflow Jobs]]"
  - "[[Disaster Recovery]]"
  - "[[Fault Tolerance]]"
  - "[[SQL Alerts]]"
  - "[[Latency]]"
aliases:
  - "Service Level Agreement"
  - "SLO"
  - "service level objective"
  - "uptime guarantee"
last_verified: 2026-10-25
tags:
  - glossary
  - flashcards
---

# SLA

> [!eli5] Summary
> An SLA (service level agreement) is a written commitment about service quality, such as uptime or delivery time, often with remedies if it is missed.

**In data work:** An SLA is a commitment between a provider and a customer, such as 99.9 percent monthly uptime or the sales dashboard refreshed by 7 a.m. Cloud vendors publish SLAs with service credits if they miss them. Internal teams use the same idea, often as service level objectives (SLOs) without penalties. For data teams, SLAs usually cover freshness (how old the data may be) and completion time for pipelines. An online store might promise its warehouse team an orders-to-ship report every morning by 6 a.m.

**In Databricks:** Databricks and each cloud publish their own service SLAs; check the official pages for your cloud and tier. Inside your workspace, you meet your own data SLAs with [[Lakeflow Jobs]] features such as schedules, retries, duration thresholds, and failure notifications (see [[Tasks Triggers and Schedules]]). [[SQL Alerts]] can warn when data goes stale, and [[Disaster Recovery]] planning covers SLAs for regional outages.

Seen in: [[Lakeflow Jobs]], [[Disaster Recovery]], [[Tasks Triggers and Schedules]]

## Recall

SLA::A service level agreement, a written promise about uptime, speed, or delivery time; data teams use them for pipeline freshness.
