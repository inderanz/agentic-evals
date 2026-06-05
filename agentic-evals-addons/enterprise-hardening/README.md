# Enterprise Hardening Add-on: Agent, Skill and MCP Evaluation

This folder is designed to be copied into the existing `agentic-evals` repository without changing the earlier content. It adds the missing production-hardening layer for:

- Agent evaluation
- Skill evaluation
- MCP server evaluation
- GitHub PR gates
- GKE isolated runner pattern
- OPA policy-as-code
- Scorecard and certification output

The design follows current public vendor patterns: MCP client/server capability exposure, Claude-style Skills as folder packages with `SKILL.md`, Google ADK-style golden eval datasets, AWS-style guardrails, and GitHub Checks/Actions as CI gates.
