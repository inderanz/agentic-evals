import os
import subprocess


def evaluate_mcp(repo_path: str, manifest: dict) -> list[dict]:
    findings = []

    if not os.path.exists(os.path.join(repo_path, "package.json")):
        return [{"severity": "critical", "category": "mcp", "message": "package.json missing"}]

    try:
        subprocess.run(["npm", "install"], cwd=repo_path, check=True, timeout=180, capture_output=True, text=True)
        subprocess.run(["npm", "run", "build"], cwd=repo_path, check=True, timeout=120, capture_output=True, text=True)
    except Exception as e:
        findings.append({"severity": "critical", "category": "mcp-build", "message": str(e)})

    spec = manifest.get("spec", {})
    if spec.get("riskLevel") in ["high", "critical"] and not spec.get("runtime", {}).get("authRequired"):
        findings.append({"severity": "critical", "category": "auth", "message": "High-risk MCP server requires auth"})

    for tool in spec.get("capabilities", {}).get("tools", []):
        if tool.get("risk") == "destructive" and not tool.get("requiresHumanApproval"):
            findings.append({"severity": "critical", "category": "tool-safety", "message": f"Destructive tool {tool.get('name')} requires human approval"})

    return findings
