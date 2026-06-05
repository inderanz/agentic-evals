def evaluate_policy(manifest: dict) -> list[dict]:
    findings = []
    meta = manifest.get("metadata", {})
    spec = manifest.get("spec", {})

    for field in ["name", "version", "owner", "supportChannel"]:
        if not meta.get(field):
            findings.append({"severity": "critical", "category": "manifest", "message": f"metadata.{field} is required"})

    if spec.get("riskLevel") in ["high", "critical"] and not spec.get("runtime", {}).get("authRequired"):
        findings.append({"severity": "critical", "category": "auth", "message": "High/critical risk capability requires authentication"})

    if spec.get("dataClassification") in ["confidential", "restricted"]:
        if not spec.get("security", {}).get("requiresAuditLogging", False):
            findings.append({"severity": "critical", "category": "audit", "message": "Confidential/restricted capability requires audit logging"})

    return findings
