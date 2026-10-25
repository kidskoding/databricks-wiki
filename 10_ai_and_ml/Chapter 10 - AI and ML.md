---
type: chapter
status: written
part: 1
level: 10
section: AI & ML
summary: From classic machine learning to agents, covering MLflow, Model Serving, Unity Gateway, AI Search, and Agent Bricks.
prev: "[[Genie One]]"
next: "[[Machine Learning Basics]]"
notes:
  - "[[Machine Learning Basics]]"
  - "[[Generative AI and LLMs]]"
  - "[[Feature Engineering and Feature Store]]"
  - "[[MLflow]]"
  - "[[Experiment Tracking]]"
  - "[[Models in Unity Catalog]]"
  - "[[AutoML]]"
  - "[[Model Serving]]"
  - "[[Foundation Model APIs]]"
  - "[[Unity Gateway]]"
  - "[[AI Search]]"
  - "[[Retrieval-Augmented Generation]]"
  - "[[Agent Bricks]]"
  - "[[Mosaic AI Agent Framework]]"
  - "[[Agent Evaluation and Tracing]]"
  - "[[Fine-Tuning]]"
  - "[[Data Quality Monitoring]]"
  - "[[AI Runtime]]"
  - "[[MosaicML and Open Models]]"
last_verified: 2026-10-25
tags:
  - chapter
---

# Chapter 10 - AI and ML

> [!story] Previously
> [[Chapter 09 - SQL BI and Apps|Chapter 09]] put governed tables in front of business users through Databricks SQL, dashboards, Genie, apps, and [[Genie One]]. Those tools describe what already happened. This chapter covers the tools that predict, generate, and act on the same data.

**From classic machine learning to agents, covering MLflow, Model Serving, Unity Gateway, AI Search, and Agent Bricks.**

## The story of this chapter

This chapter covers machine learning and generative AI on Databricks, in the order a team usually adopts them. Every tool reads the same [[Delta Lake]] tables and is governed by [[Unity Catalog]], so models, agents, and their data share one set of permissions and one audit trail.

**Classic machine learning.** [[Machine Learning Basics]] defines the vocabulary: features, labels, training, inference, and drift. [[Generative AI and LLMs]] explains how large language models differ: they arrive pre-trained, so the work shifts from training to connecting a model to business data. [[Feature Engineering and Feature Store]] keeps model inputs consistent between training and serving, with online lookups backed by [[Lakebase]].

**The model lifecycle.** [[MLflow]], which Databricks open-sourced in 2018, records every training run ([[Experiment Tracking]]). Version 3, released in June 2025, adds tracing and evaluation for GenAI apps. Trained models are registered as versioned, governed objects with movable aliases such as `@Champion` ([[Models in Unity Catalog]]). [[AutoML]] runs baseline trials automatically, although the Databricks Runtime 18.0 ML release notes list it as removed. [[Model Serving]] exposes registered models as autoscaling REST endpoints.

**Hosted LLMs and governance.** [[Foundation Model APIs]] provide Databricks-hosted open and partner models, billed per token or by provisioned throughput, through an OpenAI-compatible API. [[Unity Gateway|Unity Gateway]] (formerly AI Gateway, renamed April 2026, generally available August 2026) applies permissions, rate limits, guardrails, and usage logging to every model and MCP call, including calls to external providers.

**Grounding answers in company data.** Databricks AI Search ([[AI Search]], renamed June 1, 2026) finds documents by meaning, using indexes kept in sync with Delta tables. [[Retrieval-Augmented Generation]] combines retrieved passages with an LLM so answers come from company documents rather than from the model's training data.

**Agents.** [[Agent Bricks]] launched in 2025 as a way to build agents from a task description. In October 2026 Databricks refocused it on code-first development with the Agent Bricks CLI and Agent Runtime, and moved its no-code role to Genie Agents. The earlier [[Mosaic AI Agent Framework]] tooling is now legacy and maps to Agent Bricks. [[Agent Evaluation and Tracing]] measures quality with MLflow traces, LLM judges, and human review.

**Specialized and operational topics.** [[Fine-Tuning]] adapts a model's behavior with your own examples; the managed Foundation Model Fine-tuning service is end of life, and fine-tuning now runs on AI Runtime. [[Data Quality Monitoring]] (formerly Lakehouse Monitoring) watches tables and model predictions for freshness, completeness, and drift. [[AI Runtime]] covers classic GPU clusters and AI Runtime serverless GPUs. [[MosaicML and Open Models]] closes the chapter with the 2023 acquisition, the MPT and DBRX models, and Databricks' shift to hosting many models.

**Two small-business examples run through the chapter.** A garden center builds a **demand forecast**: features from daily sales, a model tracked in MLflow and registered with a `Champion` alias, a nightly batch job, and drift monitoring on the predictions. An online plant shop builds a **support assistant over its help documents**: documents parsed and indexed in AI Search, a RAG chain calling a hosted model through Unity Gateway, an evaluation set of real customer questions, and traces reviewed by the support lead.

**Renames to know.** Databricks renamed many AI products in 2026: Vector Search is AI Search, AI Gateway is Unity Gateway, serverless GPU compute is AI Runtime, Lakehouse Monitoring is data profiling, Databricks Assistant is Genie Code, and Genie spaces are Genie Agents. Note titles in this chapter keep some older names; each note lists the current name in a `[!renamed]` callout.

This chapter ends Part 1, the story of the platform. Part 2 covers the clouds, starting with [[Chapter 11 - Azure Databricks]], a first-party Microsoft service with its own identity, networking, billing, and integrations.

## Notes in reading order

<!-- GENERATED:reading-order START (scripts/scaffold.py) -->

| # | Note | Depth | What it covers |
|---|---|---|---|
| 1 | [[Machine Learning Basics]] | 101 Beginner | Teaching software from examples, covering training, models, features, labels, and predictions, and where each step lives in Databricks. |
| 2 | [[Generative AI and LLMs]] | 101 Beginner | What large language models are, why they need your business data to be useful, and the Databricks tools for each way of using them. |
| 3 | [[Feature Engineering and Feature Store]] | 301 Advanced | Reusable, governed model inputs in Unity Catalog, kept consistent between training and serving, with Lakebase-backed online stores. |
| 4 | [[MLflow]] | 101 Beginner | The open-source platform for tracking, packaging, evaluating, tracing, and deploying ML models and GenAI agents, managed on Databricks. |
| 5 | [[Experiment Tracking]] | 201 Practitioner | Logging every training run's parameters, metrics, and artifacts in MLflow experiments, so results can be compared and reproduced. |
| 6 | [[Models in Unity Catalog]] | 201 Practitioner | Versioning, aliasing, and governing ML models as Unity Catalog objects, the default MLflow registry since MLflow 3. |
| 7 | [[AutoML]] | 101 Beginner | Letting Databricks train and compare models for you and hand back notebooks, now removed from Databricks Runtime 18.0 ML onward. |
| 8 | [[Model Serving]] | 201 Practitioner | Turning a registered model into a live, autoscaling REST endpoint on serverless CPU or GPU compute. |
| 9 | [[Foundation Model APIs]] | 201 Practitioner | Pay-per-token and provisioned-throughput access to Databricks-hosted open and partner LLMs, through an OpenAI-compatible API. |
| 10 | [[Unity Gateway]] | 301 Advanced | Unity Gateway (formerly AI Gateway) governs, rate-limits, logs, and guards every model and MCP call, including calls to external providers. |
| 11 | [[AI Search]] | 201 Practitioner | Databricks AI Search (formerly Vector Search) finds text or images by meaning, the retrieval half of RAG, with indexes synced from Delta tables. |
| 12 | [[Retrieval-Augmented Generation]] | 201 Practitioner | Giving an LLM your documents at question time so it answers from facts, built on Databricks with document parsing, AI Search, and MLflow evaluation. |
| 13 | [[Agent Bricks]] | 101 Beginner | Databricks' agent platform, launched in 2025 for building agents from a task description and refocused in 2026 on code-first agents with the Agent Bricks CLI and Agent Runtime. |
| 14 | [[Mosaic AI Agent Framework]] | 301 Advanced | The earlier code-first agent tooling (ResponsesAgent, MLflow AgentServer on Databricks Apps, Model Serving deployment), now legacy and mapped to Agent Bricks. |
| 15 | [[Agent Evaluation and Tracing]] | 301 Advanced | Measuring agent and RAG quality in MLflow 3 with traces, LLM judges, custom scorers, human feedback, and production monitoring. |
| 16 | [[Fine-Tuning]] | 401 Expert | Further training a foundation model on your own examples, when not to bother, and how to do it on AI Runtime now that Foundation Model Fine-tuning is end of life. |
| 17 | [[Data Quality Monitoring]] | 301 Advanced | Watching tables and model inputs for freshness, completeness, and drift with anomaly detection and data profiling (formerly Lakehouse Monitoring). |
| 18 | [[AI Runtime]] | 301 Advanced | GPU clusters on Databricks Runtime ML and AI Runtime serverless GPUs (A10 and H100) for deep learning, fine-tuning, and LLM work. |
| 19 | [[MosaicML and Open Models]] | 201 Practitioner | Databricks' 2023 MosaicML acquisition, the MPT and DBRX open models, and how that technology lives on in hosted models, serving, and AI Runtime. |

<!-- GENERATED:reading-order END -->

> [!nextup] Up next
> Start with [[Machine Learning Basics]]. After the last note, the story continues in [[Chapter 11 - Azure Databricks]].
