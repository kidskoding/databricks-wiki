#!/usr/bin/env python3
"""Regression checks for scripts/brain.py and scripts/brain_mcp.py.

Usage: python3 scripts/test_brain.py
"""
import json
import subprocess
import sys
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))
import brain  # noqa: E402

FAILS = []


def check(name, cond, detail=""):
    print(("ok   " if cond else "FAIL ") + name + ("" if cond else f": {detail}"))
    if not cond:
        FAILS.append(name)


# Old product names must resolve to the current note.
for old, new in [("Delta Live Tables", "Lakeflow Spark Declarative Pipelines"), ("Workflows", "Lakeflow Jobs"),
                 ("Vector Search", "AI Search"), ("Databricks Assistant", "Genie Code"),
                 ("Databricks Asset Bundles", "Declarative Automation Bundles"), ("Delta Sharing", "OpenSharing"),
                 ("cluster policies", "Compute Policies"), ("unity catalg", "Unity Catalog")]:
    got = brain.resolve(old)["title"]
    check(f"resolve {old!r}", got == new, got)

# Search should surface the obvious note near the top.
for query, expect in [("private connectivity aws", "AWS PrivateLink"), ("incremental file ingestion cloud storage", "Auto Loader"),
                      ("row level security mask column", "Row Filters and Column Masks"),
                      ("vnet injection subnets", "VNet Injection")]:
    titles = [h["title"] for h in brain.search(query, k=5)]
    check(f"search {query!r}", expect in titles, titles)

check("history lineage", any(a["to"] == "Hive Metastore" for a in brain.history("Unity Catalog")["ancestors"]))
check("cloud equivalents", len(brain.cloud("VNet Injection")["equivalents"]) >= 2)
check("path reading order", brain.path("solo")["route"][:1] != [], brain.path("solo"))
ctx = brain.context("Can I still use Delta Live Tables for CDC?", budget=600)
check("context translates renames", any(r["current"] == "Lakeflow Spark Declarative Pipelines" for r in ctx["renamed_terms"]), ctx["renamed_terms"])
check("context respects budget", ctx["words"] <= 600, ctx["words"])
check("note levels", len(brain.note("Unity Catalog", "summary")["sections"]) < len(brain.note("Unity Catalog", "full")["sections"]))

# The MCP server must complete a handshake and run a tool.
msgs = [
    {"jsonrpc": "2.0", "id": 1, "method": "initialize", "params": {"protocolVersion": "2025-06-18", "capabilities": {}, "clientInfo": {"name": "test", "version": "0"}}},
    {"jsonrpc": "2.0", "method": "notifications/initialized"},
    {"jsonrpc": "2.0", "id": 2, "method": "tools/list"},
    {"jsonrpc": "2.0", "id": 3, "method": "tools/call", "params": {"name": "databricks_context", "arguments": {"question": "liquid clustering vs partitioning"}}},
]
start = time.time()
proc = subprocess.run([sys.executable, str(ROOT / "scripts" / "brain_mcp.py")], input="\n".join(json.dumps(m) for m in msgs) + "\n",
                      capture_output=True, text=True, timeout=30)
replies = {r["id"]: r for r in map(json.loads, proc.stdout.splitlines())}
check("mcp initialize", replies.get(1, {}).get("result", {}).get("serverInfo", {}).get("name") == "databricks-brain", proc.stderr)
check("mcp tools/list", len(replies.get(2, {}).get("result", {}).get("tools", [])) >= 9)
check("mcp tools/call", "Liquid Clustering" in replies.get(3, {}).get("result", {}).get("content", [{}])[0].get("text", ""))
check("mcp session under 3s", time.time() - start < 3, round(time.time() - start, 2))

print(f"\n{len(FAILS)} failure(s)")
sys.exit(1 if FAILS else 0)
