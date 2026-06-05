# Enterprise Production Readiness Add-on

This folder is intentionally separate from the earlier generated content. It adds production-readiness modules for an enterprise AI capability platform covering Skills, MCP servers, and Agents.

The content is grounded in public vendor/standards patterns:

- MCP: client/server protocol for tools, resources, prompts; official SDK/Inspector ecosystem.
- Anthropic Skills: SKILL.md based capability packages with instructions, scripts, and resources.
- Google ADK style agent evaluation: golden datasets, automated regression evaluation.
- AWS Bedrock Guardrails style controls: sensitive information, prompt attack, grounding, and policy checks.
- GitHub Checks / Actions style PR gating.
- OPA policy-as-code and Kubernetes/GKE isolated runner patterns.

This is still a reference implementation scaffold. Before bank production use, security, platform, architecture, and risk teams must review and approve controls.
