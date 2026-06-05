# Evaluation Framework

## Layered Evaluation Strategy

Run cheap deterministic checks before semantic or LLM-based judging.

1. Manifest validation
2. Schema validation
3. Policy-as-code validation
4. Protocol conformance validation
5. Static security validation
6. Runtime behaviour validation
7. Agent golden dataset evaluation
8. Optional LLM-as-judge semantic evaluation

## Scorecard Dimensions

```yaml
weights:
  protocol_conformance: 15
  deterministic_validation: 10
  security_guardrails: 20
  tool_safety: 15
  agent_behaviour: 15
  memory_safety: 10
  observability: 5
  runtime_readiness: 5
  documentation: 5

publish_gate:
  minimum_score: 85
  critical_findings_allowed: 0
```

## Hard Reject Examples

- No owner
- No version
- No support channel
- Hardcoded secrets
- High-risk tool without auth
- Destructive tool without human approval
- MCP server fails initialize/list/call checks
- Skill contains jailbreak or policy override instructions
- Capability has no eval cases
