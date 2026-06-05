# MCP JSON-RPC Conformance Harness

Purpose: evaluate MCP servers as protocol endpoints, not just source code.

Tests:
- Server starts from manifest startCommand.
- initialize succeeds.
- tools/list returns declared tools with schemas.
- tools/call validates required input.
- invalid input returns safe error.
- destructive tools require approval parameter or policy gate.
- resources/list does not expose restricted data unexpectedly.
- prompts/list returns approved prompts only.
- All JSON-RPC transcripts are stored as evidence.

This aligns to MCP's public model of servers exposing tools, resources, and prompts through a client/server protocol.
