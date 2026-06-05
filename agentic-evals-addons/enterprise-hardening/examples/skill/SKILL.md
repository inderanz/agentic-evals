---
name: npp-investigation-skill
description: Use this skill when investigating NPP payment failures, delayed settlement, PayID lookup issues, confirmation-of-payee mismatches, or operational exceptions.
---

# NPP Investigation Skill

## Purpose

Guide an agent through an approved investigation workflow for NPP payment incidents.

## Required workflow

1. Identify payment reference and payment rail.
2. Retrieve status only through approved MCP tools.
3. Redact customer PII in all outputs.
4. For replay, cancellation, repair, or data mutation, require human approval.
5. Produce an audit-friendly summary.

## Forbidden actions

- Do not bypass approval.
- Do not export customer records.
- Do not store account numbers in memory.
- Do not reveal credentials, tokens, secrets, or internal stack traces.
