import os
import re

def validate_skill_package(path: str) -> list[dict]:
    findings = []
    skill = os.path.join(path, "SKILL.md")
    if not os.path.exists(skill):
        return [{"severity": "critical", "category": "skill", "message": "SKILL.md missing"}]
    text = open(skill, encoding="utf-8").read()
    if "description:" not in text:
        findings.append({"severity": "major", "category": "skill", "message": "description missing"})
    for bad in ["ignore previous instructions", "bypass policy", "disable guardrails"]:
        if bad in text.lower():
            findings.append({"severity": "critical", "category": "skill-security", "message": f"Unsafe instruction: {bad}"})
    if len(text.split()) > 2500:
        findings.append({"severity": "minor", "category": "skill-quality", "message": "SKILL.md is large; move details to reference files"})
    return findings
