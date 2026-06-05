# Agentic Evals: Enterprise AI Capability Evaluation Platform

A practical starter repository for an internal enterprise marketplace/governance platform for MCP servers, Skills, and Agents.

## Outcome

Teams publish AI capabilities as code. Pull requests call a central evaluator running on GKE. The evaluator returns a scorecard and blocks unsafe capabilities before they are published.

```text
Team Repo PR -> GitHub Action -> Evaluation API on GKE -> Policy + Protocol + Security + Behaviour Evals -> Scorecard -> Marketplace Registry
```

## Contents

- `docs/` architecture and implementation documentation
- `evaluator/` FastAPI evaluation service
- `examples/sample-mcp-server/` TypeScript MCP server example
- `examples/sample-skill/` Claude-style Skill package example
- `examples/sample-agent/` minimal agent + eval cases example
- `.github/workflows/` workflow template for calling the evaluator
