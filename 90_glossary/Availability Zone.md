---
type: glossary
status: written
level: 90
section: Glossary
depth: 101
summary: "One of several physically separate data centers within a cloud region, each with independent power and networking."
related:
  - "[[Region]]"
  - "[[Disaster Recovery]]"
  - "[[Servers and the Cloud]]"
  - "[[EC2 Instance Types and Graviton]]"
  - "[[Compute on Google Cloud]]"
  - "[[Customer-Managed VPC on AWS]]"
aliases:
  - "AZ"
  - "zone"
  - "availability zones"
  - "zone_id"
last_verified: 2026-10-25
tags:
  - glossary
  - flashcards
---

# Availability Zone

> [!eli5] Summary
> A cloud region is made up of several separate data centers called availability zones. If one zone fails, the others keep running.

**In data work:** Each cloud [[Region|region]] (for example AWS `us-east-1` or Google Cloud `us-central1`) contains several zones that are physically separate but connected by low-latency links. Placing copies of data and services in more than one zone protects against the failure of a single data center. Zones do not protect against the loss of a whole region; that is a [[Disaster Recovery]] concern.

**In Databricks:** Classic compute runs all of its nodes in one zone. On AWS, the zone setting (`zone_id`) defaults to `auto`: Databricks selects a zone at startup based on available IP addresses in the workspace subnets, and retries in another zone if AWS reports insufficient capacity for the [[EC2 Instance Types and Graviton|instance type]]. After launch, nodes stay in that zone until the compute restarts. The zone must be in the workspace's region. The deprecated `HA` setting resolves to `auto`.

Seen in: [[Region]], [[Disaster Recovery]], [[Servers and the Cloud]], [[Customer-Managed VPC on AWS]]

## Recall

What is an availability zone?::A physically separate data center, or group of data centers, within a cloud region.
What does the auto zone setting do for Databricks compute on AWS?::Databricks picks a zone at startup and retries in another zone if capacity is insufficient.

> [!sources]- Sources (last verified: 2026-10-25)
> - [Compute configuration reference (AWS)](https://docs.databricks.com/aws/en/compute/configure)
> - [Databricks clouds and regions (AWS)](https://docs.databricks.com/aws/en/resources/supported-regions)
