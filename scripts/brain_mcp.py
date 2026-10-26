#!/usr/bin/env python3
"""MCP server for the Databricks Brain vault (stdio transport, standard library only).

Exposes the scripts/brain.py queries as MCP tools so any MCP-capable harness
(Claude Code, Claude Desktop, Cursor, and others) can ask the knowledge graph
directly. The index stays in memory, so calls after the first are near-instant.

Register it with the repo's .mcp.json, or run:
  claude mcp add databricks-brain -- python3 /path/to/databricks-wiki/scripts/brain_mcp.py
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import brain  # noqa: E402

PROTOCOL = "2025-06-18"
INSTRUCTIONS = (
    "Databricks Brain: a verified knowledge graph of the Databricks platform (October 2026), "
    "from beginner to expert, across Azure, AWS, and Google Cloud. Start a Databricks task with "
    "`databricks_primer` once, then use `databricks_context` for each question. Use "
    "`databricks_resolve` before writing any product name: Databricks renames products often. "
    "Cite the note titles you used."
)


def _schema(props: dict, required: list[str]) -> dict:
    return {"type": "object", "properties": props, "required": required, "additionalProperties": False}


TOOLS = [
    {
        "name": "databricks_primer",
        "description": "Load the dense Databricks briefing: current product names, platform map, decision guides, "
                       "defaults and limits, cloud differences, snippets, gotchas, and the preview watchlist. "
                       "Call once at the start of a Databricks task.",
        "inputSchema": _schema({}, []),
        "run": lambda a: brain.run("primer", {}),
    },
    {
        "name": "databricks_context",
        "description": "Answer bundle for a natural-language question: translates renamed product names, pulls the "
                       "summaries of notes the question names, then the best-matching sections, within a word budget. "
                       "The default tool for any Databricks question.",
        "inputSchema": _schema({
            "question": {"type": "string", "description": "The question or task, in plain words."},
            "budget": {"type": "integer", "description": "Approximate word budget (default 1800).", "minimum": 200},
        }, ["question"]),
        "run": lambda a: brain.render("context", brain.run("context", a)),
    },
    {
        "name": "databricks_search",
        "description": "Ranked search over every section of every note (BM25 with title and alias boosts). "
                       "Filter by note type or by cloud.",
        "inputSchema": _schema({
            "query": {"type": "string"},
            "k": {"type": "integer", "minimum": 1, "maximum": 30},
            "type": {"type": "string", "enum": ["concept", "glossary", "chapter", "path", "hub"]},
            "cloud": {"type": "string", "enum": ["azure", "aws", "gcp"]},
        }, ["query"]),
        "run": lambda a: brain.render("search", brain.run("search", a)),
    },
    {
        "name": "databricks_note",
        "description": "Read one note by title, alias, or old product name. level=summary (definition only), "
                       "standard (main sections, default), or full; or pass section to read one heading.",
        "inputSchema": _schema({
            "title": {"type": "string"},
            "level": {"type": "string", "enum": ["summary", "standard", "full"]},
            "section": {"type": "string", "description": "Heading prefix, for example 'How it works'."},
        }, ["title"]),
        "run": lambda a: brain.render("note", brain.run("note", a)),
    },
    {
        "name": "databricks_resolve",
        "description": "Translate any product name, including old names (Delta Live Tables, Workflows, Vector Search, "
                       "Databricks Assistant), into the current note title and summary.",
        "inputSchema": _schema({"name": {"type": "string"}}, ["name"]),
        "run": lambda a: json.dumps(brain.run("resolve", a), indent=1, ensure_ascii=False),
    },
    {
        "name": "databricks_neighbors",
        "description": "Graph neighbors of a note, grouped by edge type: related, prereqs, unlocks, evolved_from, "
                       "evolved_into, cloud_equivalent, chapter, prev, next.",
        "inputSchema": _schema({
            "title": {"type": "string"},
            "edge": {"type": "string", "enum": ["related", "prereqs", "unlocks", "evolved_from", "evolved_into",
                                                 "cloud_equivalent", "chapter", "prev", "next"]},
        }, ["title"]),
        "run": lambda a: json.dumps(brain.run("neighbors", a), indent=1, ensure_ascii=False),
    },
    {
        "name": "databricks_history",
        "description": "Lineage of a concept: what it evolved from and what replaced it, across chapters.",
        "inputSchema": _schema({"title": {"type": "string"}}, ["title"]),
        "run": lambda a: json.dumps(brain.run("history", a), indent=1, ensure_ascii=False),
    },
    {
        "name": "databricks_cloud",
        "description": "How a concept differs on Azure, AWS, and Google Cloud, plus its equivalent notes on the other clouds.",
        "inputSchema": _schema({"title": {"type": "string"}}, ["title"]),
        "run": lambda a: json.dumps(brain.run("cloud", a), indent=1, ensure_ascii=False),
    },
    {
        "name": "databricks_path",
        "description": "The learning path for a persona: everyone, owner, analyst, engineer, scientist, ai-dev, admin, "
                       "security, finance, solo.",
        "inputSchema": _schema({"persona": {"type": "string"}}, ["persona"]),
        "run": lambda a: json.dumps(brain.run("path", a), indent=1, ensure_ascii=False),
    },
]
BY_NAME = {t["name"]: t for t in TOOLS}


def reply(msg_id, result=None, error=None):
    out = {"jsonrpc": "2.0", "id": msg_id}
    if error:
        out["error"] = error
    else:
        out["result"] = result
    sys.stdout.write(json.dumps(out, ensure_ascii=False) + "\n")
    sys.stdout.flush()


def handle(msg: dict):
    method, msg_id, params = msg.get("method"), msg.get("id"), msg.get("params") or {}
    if msg_id is None:  # notifications (initialized, cancelled) need no answer
        return
    if method == "initialize":
        reply(msg_id, {
            "protocolVersion": params.get("protocolVersion", PROTOCOL),
            "capabilities": {"tools": {"listChanged": False}},
            "serverInfo": {"name": "databricks-brain", "version": "1.0.0"},
            "instructions": INSTRUCTIONS,
        })
    elif method == "ping":
        reply(msg_id, {})
    elif method == "tools/list":
        reply(msg_id, {"tools": [{k: v for k, v in t.items() if k != "run"} for t in TOOLS]})
    elif method == "tools/call":
        tool = BY_NAME.get(params.get("name"))
        if not tool:
            reply(msg_id, error={"code": -32602, "message": f"unknown tool {params.get('name')!r}"})
            return
        try:
            text = tool["run"](params.get("arguments") or {})
            reply(msg_id, {"content": [{"type": "text", "text": text}], "isError": False})
        except Exception as e:  # report tool failures to the model instead of crashing the server
            reply(msg_id, {"content": [{"type": "text", "text": f"error: {e}"}], "isError": True})
    else:
        reply(msg_id, error={"code": -32601, "message": f"method not found: {method}"})


def main():
    brain.search_index()  # warm the index before the first request
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        try:
            msg = json.loads(line)
        except json.JSONDecodeError:
            reply(None, error={"code": -32700, "message": "parse error"})
            continue
        for m in msg if isinstance(msg, list) else [msg]:
            handle(m)


if __name__ == "__main__":
    main()
