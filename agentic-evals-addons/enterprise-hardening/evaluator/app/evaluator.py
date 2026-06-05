import os
import yaml
from skill_eval import evaluate_skill
from mcp_eval import evaluate_mcp
from agent_eval import evaluate_agent
from policy_eval import evaluate_policy
from scorecard import build_scorecard


def load_manifest(repo_path: str) -> dict:
    path = os.path.join(repo_path, "marketplace.yaml")
    if not os.path.exists(path):
        return {}
    with open(path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)


def evaluate_local_repo(repo_path: str) -> dict:
    manifest = load_manifest(repo_path)
    findings = []

    if not manifest:
        findings.append({"severity": "critical", "category": "manifest", "message": "marketplace.yaml missing"})
        return build_scorecard({"metadata": {"name": "unknown", "version": "unknown", "owner": "unknown"}, "spec": {"type": "unknown", "riskLevel": "unknown", "eval": {"minimumScore": 85}}}, findings)

    findings.extend(evaluate_policy(manifest))
    cap_type = manifest.get("spec", {}).get("type")

    if cap_type == "skill":
        findings.extend(evaluate_skill(repo_path))
    elif cap_type == "mcp-server":
        findings.extend(evaluate_mcp(repo_path, manifest))
    elif cap_type == "agent":
        findings.extend(evaluate_agent(repo_path, manifest))
    else:
        findings.append({"severity": "critical", "category": "manifest", "message": f"Unsupported capability type: {cap_type}"})

    return build_scorecard(manifest, findings)
