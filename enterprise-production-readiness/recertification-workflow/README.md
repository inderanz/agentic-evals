# Recertification Workflow

Purpose: a capability certified once should not remain trusted forever.

Triggers:
- Scheduled expiry reached
- Dependency update
- Base image update
- Model change
- Tool schema change
- Prompt/SKILL.md change
- Security scanner database update
- New policy pack version

Real outcome:
- Certified versions expire.
- Marketplace hides expired versions unless exception exists.
- Owners receive notifications before expiry.
