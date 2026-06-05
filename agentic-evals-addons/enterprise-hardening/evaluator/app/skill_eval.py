import os
import re

UNSAFE_PATTERNS = [
    "ignore previous instructions",
    "bypass policy",
    "disable guardrails",
    "export all customer data",
    "send secrets",
    "exfiltrate",
    "do not tell the user"
]


def evaluate_skill(repo_path: str) -> list[dict]:
    findings = []
    path = os.path.join(repo_path, "SKILL.md")

    if not os.path.exists(path):
        return [{"severity": "critical", "category": "skill", "message": "SKILL.md is required for skill capabilities"}]

    content = open(path, encoding="utf-8").read()

    if "description:" not in content[:1000]:
        findings.append({"severity": "major", "category": "skill", "message": "SKILL.md should include frontmatter description for discovery"})

    for pattern in UNSAFE_PATTERNS:
        if pattern in content.lower():
            findings.append({"severity": "critical", "category": "skill-security", "message": f"Unsafe instruction pattern found: {pattern}"})

    if len(content.splitlines()) > 300:
        findings.append({"severity": "minor", "category": "skill-quality", "message": "SKILL.md is large; split reference material into separate files"})

    if "requires approval" not in content.lower() and any(x in content.lower() for x in ["delete", "replay", "transfer", "update record"]):
        findings.append({"severity": "major", "category": "skill-guardrail", "message": "State-changing instructions should explicitly require human approval"})

    return findings
