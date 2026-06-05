import os
import json
import subprocess


def evaluate_mcp(repo_path: str, manifest: dict) -> list[dict]:
    findings = []

    if not os.path.exists(os.path.join(repo_path, "package.json")):
        findings.append({"severity": "major", "category": "mcp", "message": "package.json missing; Node/TypeScript MCP conformance test cannot run"})
        return findings

    try:
        subprocess.run(["npm", "install"], cwd=repo_path, timeout=180, check=True, capture_output=True, text=True)
        subprocess.run(["npm", "run", "build"], cwd=repo_path, timeout=120, check=True, capture_output=True, text=True)
    except Exception as exc:
        findings.append({"severity": "critical", "category": "mcp-build", "message": f"MCP build failed: {str(exc)}"})

    tools = manifest.get("spec", {}).get("capabilities", {}).get("tools", [])
    for tool in tools:
        if not tool.get("name"):
            findings.append({"severity": "critical", "category": "mcp-schema", "message": "Tool missing name"})
        if tool.get("risk") == "destructive" and not tool.get("requiresHumanApproval"):
            findings.append({"severity": "critical", "category": "tool-safety", "message": f"Destructive tool {tool.get('name')} requires human approval"})

    return findings
