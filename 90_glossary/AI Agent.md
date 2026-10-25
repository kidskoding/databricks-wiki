---
type: glossary
status: written
level: 90
section: Glossary
depth: 101
summary: "An AI system that uses a language model to plan steps and call tools, such as queries or APIs, to complete a task."
related:
  - "[[Agent Bricks]]"
  - "[[Mosaic AI Agent Framework]]"
  - "[[Agent Evaluation and Tracing]]"
  - "[[Generative AI and LLMs]]"
  - "[[Retrieval-Augmented Generation]]"
  - "[[Model Serving]]"
aliases:
  - "agent"
  - "agentic AI"
  - "LLM agent"
last_verified: 2026-10-25
tags:
  - glossary
  - flashcards
---

# AI Agent

> [!eli5] Summary
> An AI agent is software that completes a task rather than only answering a question. It decides which steps to take, looks up the information it needs, and returns a result.

**In data work:** An agent runs a [[LLM|large language model]] in a loop: the model reads the request, chooses a tool (a SQL query, a document search, an [[APIs|API]] call), reads the tool's output, and repeats until it can respond. A tool is any function the agent is permitted to call. Because agents take actions, they require scoped permissions, logging, and evaluation. Example: an online shop's support agent answers "Where is order 1182?" by querying the orders table and the carrier's tracking API.

**In Databricks:** [[Agent Bricks]] builds an agent from a natural-language description of the task and your data, generates evaluations and LLM judges, and optimizes for a chosen quality and cost trade-off. The [[Mosaic AI Agent Framework]] is for agents written in code, for example with LangGraph or LlamaIndex. [[MLflow]] tracing records each step, and its judges score quality ([[Agent Evaluation and Tracing]]). [[Unity Catalog]] governs the data and functions an agent can use, and [[Model Serving]] hosts it as an endpoint.

Seen in: [[Agent Bricks]], [[Mosaic AI Agent Framework]], [[Agent Evaluation and Tracing]], [[Retrieval-Augmented Generation]], [[Path - AI App Developer]]

## Recall

How does an AI agent differ from a chatbot?::An agent plans steps and calls tools such as queries and APIs to complete a task; a chatbot only produces text.
Which Databricks product builds an agent from a natural-language task description?::Agent Bricks.

> [!sources]- Sources (last verified: 2026-10-25)
> - [Introducing Agent Bricks (Databricks blog)](https://www.databricks.com/blog/introducing-agent-bricks)
> - [Use agents on Azure Databricks](https://learn.microsoft.com/en-us/azure/databricks/generative-ai/agent-bricks/)
> - [Built-in LLM judges (AWS)](https://docs.databricks.com/aws/en/mlflow3/genai/eval-monitor/concepts/judges)
