def build_scorecard(manifest: dict, findings: list[dict]) -> dict:
    score = 100
    for finding in findings:
        sev = finding.get("severity")
        if sev == "critical":
            score -= 30
        elif sev == "major":
            score -= 10
        elif sev == "minor":
            score -= 3
    score = max(score, 0)
    critical_count = sum(1 for f in findings if f.get("severity") == "critical")
    minimum = manifest.get("spec", {}).get("eval", {}).get("minimumScore", 85)
    status = "approved" if score >= minimum and critical_count == 0 else "rejected"
    return {
        "capability": manifest.get("metadata", {}).get("name"),
        "version": manifest.get("metadata", {}).get("version"),
        "owner": manifest.get("metadata", {}).get("owner"),
        "type": manifest.get("spec", {}).get("type"),
        "riskLevel": manifest.get("spec", {}).get("riskLevel"),
        "score": score,
        "minimumScore": minimum,
        "status": status,
        "criticalFindings": critical_count,
        "publishAllowed": status == "approved",
        "findings": findings,
    }
