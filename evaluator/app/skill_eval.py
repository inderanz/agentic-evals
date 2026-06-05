import os

UNSAFE_PATTERNS = [
    "ignore previous instructions",
    "bypass policy",
    "disable guardrails",
    "export all customer data",
]


def evaluate_skill(repo_path: str) -> list[dict]:
    findings = []
    path = os.path.join(repo_path, "SKILL.md")
    if not os.path.exists(path):
        return [{"severity": "critical", "category": "skill", "message": "SKILL.md missing"}]

    content = open(path, encoding="utf-8").read()
    lower = content.lower()

    if "description:" not in lower:
        findings.append({"severity": "major", "category": "skill", "message": "Skill description missing"})

    for pattern in UNSAFE_PATTERNS:
        if pattern in lower:
            findings.append({"severity": "critical", "category": "skill-security", "message": f"Unsafe instruction: {pattern}"})

    return findings
