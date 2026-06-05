# Vendor Patterns and Practical Evaluation Requirements

## 1. What vendors are doing in real products

### MCP ecosystem

MCP standardizes how AI applications connect to external tools, data, prompts and resources through a client-server protocol. In practice, an MCP server is not just code; it is a capability boundary. It exposes:

- Tools: actions the model can request.
- Resources: contextual data the model can read.
- Prompts: reusable templates/workflows provided by the server.

For enterprise evaluation, each MCP server must be tested for protocol behavior, tool schema quality, authorization, prompt injection resistance, destructive-action protection, and auditability.

### Anthropic-style Skills

A Skill is a folder-based capability package. The key file is `SKILL.md`, which normally contains metadata, description, usage instructions and references to scripts/resources. The important production lesson is that `SKILL.md` is operational text, not passive documentation. The description influences discovery and selection, so registries must scan it for overbroad triggers, unsafe instructions, semantic poisoning and hidden policy override language.

### Google ADK-style agent evaluation

The practical pattern is agent code plus golden evaluation datasets. Each agent must be regression tested for:

- Task success
- Tool selection accuracy
- Tool parameter correctness
- Safety behavior
- Grounding
- Refusal behavior
- Multi-turn behavior

### AWS-style guardrails

Guardrails should cover content safety, prompt attacks, sensitive information, grounding, contextual relevance and policy violations. For banking use cases, guardrails must also include approval requirements for state-changing actions and strict PII handling.

## 2. Required enterprise gates

A capability cannot be published unless all hard gates pass:

- `marketplace.yaml` exists and validates.
- Owner, support channel, version, risk level and data classification are defined.
- High/critical risk tools require authentication.
- Destructive tools require human approval.
- Skill instructions do not contain jailbreak or bypass language.
- MCP server passes protocol smoke checks.
- Eval cases exist.
- Secret scan passes.
- Audit logging is required for confidential/restricted data.

## 3. What the evaluator must output

The evaluator must produce both a machine-readable JSON scorecard and a human-readable Markdown report:

```json
{
  "capability": "payment-investigation-mcp",
  "score": 92,
  "status": "approved",
  "criticalFindings": 0,
  "publishAllowed": true
}
```

## 4. Recommended score dimensions

| Dimension | Weight |
|---|---:|
| Manifest and ownership | 10 |
| MCP protocol conformance | 15 |
| Skill quality | 10 |
| Agent behavior | 15 |
| Security and policy | 20 |
| Memory safety | 10 |
| Observability | 10 |
| Documentation | 10 |
