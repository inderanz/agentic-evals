---
name: npp-investigation-skill
description: Use this skill when investigating NPP payment failures, delayed settlements, PayID issues, or operational exceptions.
---

# NPP Investigation Skill

Use this skill to investigate NPP payment incidents using approved operational procedures.

## Required process

1. Identify the payment reference.
2. Confirm payment rail and timestamp.
3. Check payment status using approved MCP tools only.
4. Do not expose customer PII in the final answer.
5. For replay, cancellation, or manual repair, require explicit human approval.

## Forbidden actions

- Do not bypass approval.
- Do not infer customer identity from partial data.
- Do not export payment records.
- Do not store account numbers in memory.

## Reference material

Read `reference/npp-runbook.md` before producing an operational recommendation.
