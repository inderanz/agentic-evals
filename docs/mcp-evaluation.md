# MCP Evaluation

## What to Test

- `initialize`
- `tools/list`
- `tools/call`
- `resources/list`
- `prompts/list`
- invalid input handling
- timeout handling
- safe error messages
- no stack trace leakage
- no hidden dangerous tools

## CI Pattern

Each MCP repo contains:

- `marketplace.yaml`
- `eval-cases.yaml`
- `package.json`
- MCP server implementation

The central evaluator clones the repo, builds it, validates metadata, and runs protocol and safety tests.
