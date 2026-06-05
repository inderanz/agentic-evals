import os
import yaml


def evaluate_agent(repo_path: str, manifest: dict) -> list[dict]:
    findings = []
    cases_file = manifest.get("spec", {}).get("eval", {}).get("casesFile", "eval-cases.yaml")
    path = os.path.join(repo_path, cases_file)

    if not os.path.exists(path):
        return [{"severity": "critical", "category": "agent-eval", "message": "eval-cases.yaml is required for agent capabilities"}]

    cases = yaml.safe_load(open(path, encoding="utf-8")) or {}
    items = cases.get("cases", [])

    if len(items) < 3:
        findings.append({"severity": "major", "category": "agent-eval", "message": "At least 3 eval cases required: happy path, forbidden tool, safety/refusal"})

    required_types = {"tool_selection", "safety", "grounding"}
    present = {case.get("type") for case in items}
    missing = required_types - present
    for m in missing:
        findings.append({"severity": "major", "category": "agent-eval", "message": f"Missing agent eval type: {m}"})

    return findings
