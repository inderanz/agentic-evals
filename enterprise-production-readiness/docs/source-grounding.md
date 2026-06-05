# Source Grounding and Non-Hallucination Notes

This package avoids claiming private vendor implementation details. It maps only to publicly documented patterns:

1. MCP exposes capabilities as tools, resources, and prompts through a client/server protocol.
2. Official MCP SDKs and Inspector are used by the ecosystem to build/test servers.
3. Anthropic Skills are packaged capability folders centered on SKILL.md plus supporting files.
4. Agent evaluation patterns from Google-style ADK use golden datasets and regression checks.
5. AWS Bedrock Guardrails-style controls include sensitive information filtering, prompt attack protections, grounding/contextual checks, and policy guardrails.
6. GitHub enterprise delivery commonly uses Actions/Checks to gate PRs.
7. OPA is a common policy-as-code engine for Kubernetes and CI admission controls.

Anything not explicitly documented by a vendor is labeled as an enterprise implementation recommendation, not a vendor claim.
