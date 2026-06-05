# Agent Evaluation Runner

Purpose: evaluate agents with golden datasets and deterministic trajectory checks before optional LLM judging.

Checks:
- Expected tool selected
- Forbidden tool not selected
- Required parameters supplied
- Destructive action requires approval
- Sensitive data redacted/refused
- Tool failure handled safely
- Output grounded in tool response

Important rule:
Run deterministic checks first. Invoke LLM-as-judge only for semantic dimensions that cannot be checked mechanically.
