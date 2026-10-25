---
type: glossary
status: written
level: 90
section: Glossary
depth: 101
summary: "The text instructions and context you give a language model to get an answer."
related:
  - "[[LLM]]"
  - "[[Generative AI and LLMs]]"
  - "[[AI Functions in SQL]]"
  - "[[Retrieval-Augmented Generation]]"
  - "[[Mosaic AI Agent Framework]]"
  - "[[Token]]"
aliases:
  - "prompts"
  - "prompt engineering"
  - "system prompt"
  - "prompt template"
last_verified: 2026-10-25
tags:
  - glossary
  - flashcards
---

# Prompt

> [!eli5] Summary
> A prompt is the text instructions and context given to an AI language model. The model's answer depends heavily on how clear and specific the prompt is.

**In data work:** A prompt is the input to an [[LLM]]: instructions, examples, and any context such as a document to summarize. A system prompt sets standing rules (you are a polite support agent, answer only from the policy text), and a user prompt carries the question. Prompt engineering is the craft of writing prompts that give reliable results, for example by stating the output format and giving one or two examples. A cleaning company might use a prompt like: classify this email as quote, complaint, or scheduling, and reply with one word. Prompts are measured in [[Token|tokens]], which is how usage is metered.

**In Databricks:** You write prompts in the AI Playground, in [[AI Functions in SQL]] such as `ai_query`, and in agent code built with the [[Mosaic AI Agent Framework]]. [[Retrieval-Augmented Generation]] adds retrieved company documents into the prompt. [[Unity Gateway]] can log prompts and responses for review, and [[Agent Evaluation and Tracing]] shows exactly which prompt produced which answer.

Seen in: [[Generative AI and LLMs]], [[AI Functions in SQL]], [[Retrieval-Augmented Generation]]

## Recall

Prompt::The instructions and context sent to an LLM; clear format rules and examples make answers more reliable.
