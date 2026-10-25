---
type: path
status: written
level: 80
section: Learning Paths
depth: 201
summary: LLMs, RAG, vector search, agents, Databricks Apps, and Lakebase.
personas:
  - ai-dev
chapter: "[[Chapter 80 - Learning Paths]]"
prev: "[[Path - Data Scientist and ML Engineer]]"
next: "[[Path - Platform Admin]]"
evolved_from: []
evolved_into: []
cloud_equivalent: []
related:
  - "[[Generative AI and LLMs]]"
  - "[[Foundation Model APIs]]"
  - "[[AI Functions in SQL]]"
  - "[[Vector Search]]"
  - "[[Retrieval-Augmented Generation]]"
  - "[[Agent Bricks]]"
  - "[[Mosaic AI Agent Framework]]"
  - "[[Agent Evaluation and Tracing]]"
  - "[[AI Gateway]]"
  - "[[Model Serving]]"
  - "[[Databricks Apps]]"
  - "[[Lakebase]]"
  - "[[Path - Data Scientist and ML Engineer]]"
  - "[[Path - Platform Admin]]"
  - "[[Path - Certification Prep]]"
aliases:
  - GenAI Path
  - Agent Developer Path
prereqs:
  - "[[Path - Absolute Beginner]]"
unlocks:
  - "[[Path - Certification Prep]]"
clouds:
  - aws
  - azure
  - gcp
mastery: new
last_verified: 2026-10-25
tags:
  - path
---

# Path - AI App Developer

> [!persona] Who this is for
> **Who:** an application or AI developer who wants to build chatbots, assistants, and agents on company data, and ship them as real apps.
> **Goal:** go from "call an LLM" to a governed, evaluated agent that retrieves from your documents, uses tools, and runs inside a web app with its own database.
> **Outcome:** you can build a RAG agent, measure its quality, put a gateway in front of it, and deploy it as a Databricks App backed by Lakebase.

## Before you start

You should write Python comfortably and know what a REST API is. Prior LLM experience helps but is not required. [[Databricks Free Edition and Trials|Free Edition]] is enough for the first two stages if its AI features are available in your region; Lakebase and production serving are best tried on a trial workspace.

## The route

### Stage 1: LLMs on Databricks (101 to 201)

**Goal:** call models, and know where your data and models are governed.

1. [[Generative AI and LLMs]]: what LLMs are and why your data makes them useful.
2. [[Foundation Model APIs]] (201): hosted open and partner models, billed per token.
3. [[AI Functions in SQL]] (201): `ai_query` and task functions straight from SQL.
4. [[Agent Bricks]]: the no-code route, so you know what you are competing with.
5. [[Unity Catalog]]: where models, functions, indexes, and data are all governed.
6. [[Volumes]] (201): where your PDFs and documents live.
7. [[MosaicML and Open Models]] (201): the open-model strategy behind the hosted models.

> [!check] Checkpoint
> Open the **Playground**, pick a hosted model, and ask it a question about your business; note what it gets wrong. Then run `ai_query()` from the SQL Editor over a table of short texts to summarize each row. Upload a handful of PDFs or text files to a Volume for Stage 2.

### Stage 2: Retrieval (201)

**Goal:** make the model answer from your documents instead of guessing.

1. [[Retrieval-Augmented Generation]] (201): the pattern, step by step.
2. [[Vector Search]] (201): indexes that find text by meaning.
3. [[Delta Lake]]: the chunk table that the index syncs from.
4. [[Change Data Feed]] (301): what keeps a Delta Sync index up to date.
5. [[Lakeflow Spark Declarative Pipelines]] (201): parsing and chunking documents on a schedule.
6. [[Embedding]]: the glossary entry for the vectors behind it all.

> [!check] Checkpoint
> Parse your Volume files into a Delta table of chunks (`id`, `text`, `source`), enable change data feed on it (`ALTER TABLE ... SET TBLPROPERTIES (delta.enableChangeDataFeed = true)`), and create a Vector Search endpoint and a Delta Sync index with a hosted embedding model. Query it with `similarity_search` and check that the right chunk comes back for three questions.

### Stage 3: Agents, evaluation, and governance (301)

**Goal:** turn retrieval into an agent you can measure and control.

1. [[Mosaic AI Agent Framework]] (301): agents in code, with tools and deployment.
2. [[MLflow]]: tracing, logging, and versioning agents.
3. [[Agent Evaluation and Tracing]] (301): LLM judges, evaluation sets, and traces.
4. [[Model Serving]] (201): the endpoint your agent runs on.
5. [[Models in Unity Catalog]] (201): versioning and aliasing the agent like any model.
6. [[AI Gateway]] (301): rate limits, logging, guardrails, and external providers.

> [!check] Checkpoint
> Write a tool-calling agent that uses your Vector Search index as a retrieval tool and a Unity Catalog SQL function as a second tool. Log it with MLflow, run it on ten test questions with tracing on, and run an evaluation with built-in judges. Fix one failure and re-run the evaluation to show the score moved.

### Stage 4: Apps and state (301 to 401)

**Goal:** ship the agent inside a real app with its own fast database.

1. [[Databricks Apps]] (201): host a Streamlit, Dash, or React app next to your data.
2. [[Lakebase]] (301): managed Postgres for app state, chat history, and agent memory.
3. [[Databricks SDKs and REST API]] (301): calling the platform from app code.
4. [[Authentication - Tokens and OAuth]] (301): how the app and its users authenticate.
5. [[Databricks Connect]] (301): developing against Databricks from your IDE.
6. [[Declarative Automation Bundles]] (301): deploy the app, endpoint, and jobs from Git.
7. [[Fine-Tuning]] (401): the last resort when prompts and retrieval are not enough.

> [!check] Checkpoint
> Create a Databricks App from a chatbot template, point it at your agent's serving endpoint, and share it with one colleague. On a workspace with Lakebase, create a database instance, store each conversation turn in a Postgres table from the app, and confirm a colleague's chat history persists after the app restarts.

## Rabbit holes

- **The models themselves:** [[Machine Learning Basics]], [[GPU Compute]], [[Hallucination]], [[Prompt]], [[Token]].
- **Data plumbing for agents:** [[Lakeflow Jobs]], [[Lakeflow Connect]], [[Lakehouse Federation]].
- **Business-user front ends:** [[Genie]] and [[Databricks One]].
- **Security for AI:** [[Serverless Network Security]], [[Secrets Management]], [[Row Filters and Column Masks]].
- **Your cloud:** network and identity specifics in [[Path - Azure Deep Dive]], [[Path - AWS Deep Dive]], and [[Path - Google Cloud Deep Dive]].
- **Exams:** the Generative AI Engineer track in [[Path - Certification Prep]].

## You are done when

- You can call a hosted model from SQL and Python and know how it is billed.
- You can build and query a Vector Search index that stays in sync with a Delta table.
- You have an agent with at least two tools, traced and evaluated in MLflow.
- You can put a gateway with rate limits and logging in front of model calls.
- You have deployed an app that talks to your agent and keeps state in Lakebase.
- You can explain when fine-tuning is worth it, and when it is not.

> [!nextup] Up next
> Someone has to set up the workspaces, identities, and networks all of this runs on. That is [[Path - Platform Admin]].

> [!sources]- Sources (last verified: 2026-10-25)
> - Route assembled on 2026-10-25 from the vault index (`llms.txt`) and the `ai-dev` persona tags in `_meta/manifest.yaml`. Product facts and official documentation links live in each linked note's `[!sources]` callout.
> - Free Edition and regional availability of Foundation Model APIs, Vector Search, Model Serving, Apps, and Lakebase was not re-checked for this path; see [[Databricks Free Edition and Trials]] and use a trial workspace where a feature is missing.
