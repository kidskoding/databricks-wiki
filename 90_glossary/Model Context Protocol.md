---
type: glossary
status: written
level: 90
section: Glossary
depth: 101
summary: "An open protocol that lets AI applications connect to external tools and data through a standard client-server interface."
related:
  - "[[Managed MCP Servers]]"
  - "[[AI Agent]]"
  - "[[Mosaic AI Agent Framework]]"
  - "[[Unity Gateway]]"
  - "[[Genie Code]]"
  - "[[Unity Catalog Functions]]"
aliases:
  - "MCP"
  - "MCP server"
  - "MCP client"
last_verified: 2026-10-26
tags:
  - glossary
  - flashcards
---

# Model Context Protocol

> [!eli5] Summary
> The Model Context Protocol is a shared standard for plugging AI assistants into tools and data. A tool built once for MCP works with any assistant that supports it.

**In data work:** MCP defines three roles. A **host** is the AI application (for example, a chat app or coding agent). The host runs one **client** per connection, and each client talks to one **server**. Servers expose **tools** (functions the model can call), **resources** (data that adds context), and **prompts** (reusable templates). All messages use JSON-RPC 2.0. The specification requires hosts to get explicit user consent before invoking a tool, because a tool call can run arbitrary code. The spec is versioned by date; the 2026-07-28 revision makes the protocol stateless, while earlier revisions such as 2025-06-18 use an initialization handshake.

**In Databricks:** [[Managed MCP Servers|Databricks managed MCP servers]] (Public Preview as of October 2026) give [[AI Agent|agents]] access to [[Genie One]], [[Genie Agents]], [[AI Search]] indexes, Databricks SQL, and [[Unity Catalog Functions]] with no server to run. [[Unity Catalog]] permissions decide which tools and data each user or [[Users Groups and Service Principals|service principal]] can reach, and OAuth is the recommended authentication. External clients such as Claude, Claude Code, Cursor, and ChatGPT connect over Streamable HTTP. [[Genie Code]] can also connect to MCP servers. A small team can point an assistant at a Genie Agent through MCP to answer sales questions from governed tables.

Seen in: [[Managed MCP Servers]], [[AI Agent]], [[Genie Code]], [[Unity Gateway]]

## Recall

Model Context Protocol (MCP)::An open standard, built on JSON-RPC 2.0, for connecting AI applications (hosts and clients) to servers that expose tools, resources, and prompts.
What controls access to data through Databricks managed MCP servers?::Unity Catalog permissions of the calling user or service principal.

> [!sources]- Sources (last verified: 2026-10-26)
> - [Specification, 2025-06-18 (Model Context Protocol)](https://modelcontextprotocol.io/specification/2025-06-18)
> - [Architecture overview (Model Context Protocol)](https://modelcontextprotocol.io/docs/learn/architecture)
> - [The 2026-07-28 Specification (MCP blog)](https://blog.modelcontextprotocol.io/posts/2026-07-28/)
> - [Databricks managed MCP servers (AWS)](https://docs.databricks.com/aws/en/agents/mcp-tools/managed-mcp)
> - [Model Context Protocol (MCP) on Azure Databricks](https://learn.microsoft.com/en-us/azure/databricks/agents/mcp/)
> - [Connect Genie Code to MCP servers (AWS)](https://docs.databricks.com/aws/en/genie-code/mcp)
