---
type: glossary
status: written
level: 90
section: Glossary
depth: 101
summary: "An automatic web message one system sends to another when something happens."
related:
  - "[[REST]]"
  - "[[APIs]]"
  - "[[Lakeflow Jobs]]"
  - "[[SQL Alerts]]"
  - "[[Tasks Triggers and Schedules]]"
  - "[[Event]]"
aliases:
  - "webhooks"
  - "HTTP callback"
  - "web callback"
  - "notification destination"
last_verified: 2026-10-25
tags:
  - glossary
  - flashcards
---

# Webhook

> [!eli5] Summary
> A webhook is an automatic web request that one system sends to another when an event happens, instead of the second system repeatedly checking for changes.

**In data work:** A webhook is an HTTP request (usually a `POST` with a JSON body) that a system sends to a URL you register whenever a specific [[Event|event]] occurs: an order is placed, a payment fails, a job finishes. It is the push opposite of polling an [[REST|API]] over and over. The receiver must be reachable, should verify the sender (often with a shared secret or signature), and should handle repeats safely because webhooks can be retried. A shop can register a Shopify webhook so every new order is posted instantly to its fulfillment service.

**In Databricks:** In Databricks, webhooks are mostly outbound notifications. [[Lakeflow Jobs]] and [[SQL Alerts]] can send to notification destinations such as email, Slack, Microsoft Teams, PagerDuty, or a generic webhook URL, which admins set up once in the workspace. Inbound, an external system can start a job by calling the [[Databricks SDKs and REST API|Jobs REST API]] instead of waiting for a schedule (see [[Tasks Triggers and Schedules]]).

Seen in: [[Lakeflow Jobs]], [[SQL Alerts]], [[Tasks Triggers and Schedules]]

## Recall

Webhook::An HTTP request one system pushes to a registered URL when an event happens; Databricks jobs and alerts can notify via webhooks.

> [!sources]- Sources (last verified: 2026-10-25)
> - [Manage notification destinations (AWS)](https://docs.databricks.com/aws/en/admin/workspace-settings/notification-destinations)
> - [Manage notification destinations (Azure Databricks)](https://learn.microsoft.com/en-us/azure/databricks/admin/workspace-settings/notification-destinations)
> - [Add notifications on a job (AWS)](https://docs.databricks.com/aws/en/jobs/notifications)
