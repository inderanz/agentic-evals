# Skill Package Validator

Purpose: validate Anthropic-style Skill package hygiene without claiming private Anthropic internals.

Checks:
- SKILL.md exists.
- Frontmatter includes name and description.
- Description is specific enough to support invocation.
- Instructions are not overloaded; large content should move to reference files.
- Dangerous actions require confirmation.
- Scripts are declared and reviewed.
- Reference files do not contain secrets.
- Skill does not ask the model to bypass policy or ignore higher-priority instructions.
