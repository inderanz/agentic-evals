import os
import subprocess
import tempfile
import yaml
from skill_eval import evaluate_skill
from mcp_eval import evaluate_mcp
from scorecard import build_scorecard


def clone_repo(repo_url: str, sha: str) -> str:
    tmp = tempfile.mkdtemp()
    subprocess.run(["git", "clone", repo_url, tmp], check=True)
    subprocess.run(["git", "checkout", sha], cwd=tmp, check=True)
    return tmp


def load_manifest(repo_path: str) -> dict:
    path = os.path.join(repo_path, "marketplace.yaml")
    if not os.path.exists(path):
        raise Exception("marketplace.yaml missing")
    with open(path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)


def evaluate_repo(repo_url: str, sha: str) -> dict:
    repo_path = clone_repo(repo_url, sha)
    manifest = load_manifest(repo_path)
    findings = []

    spec = manifest.get("spec", {})
    if not manifest.get("metadata", {}).get("owner"):
        findings.append({"severity": "critical", "category": "manifest", "message": "Owner missing"})

    if not os.path.exists(os.path.join(repo_path, spec.get("eval", {}).get("casesFile", "eval-cases.yaml"))):
        findings.append({"severity": "critical", "category": "eval", "message": "eval-cases.yaml missing"})

    if spec.get("type") == "skill":
        findings += evaluate_skill(repo_path)
    elif spec.get("type") == "mcp-server":
        findings += evaluate_mcp(repo_path, manifest)
    else:
        findings.append({"severity": "critical", "category": "manifest", "message": "Unsupported capability type"})

    return build_scorecard(manifest, findings)
