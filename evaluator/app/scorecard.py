def build_scorecard(manifest: dict, findings: list[dict]) -> dict:
    score = 100
    for finding in findings:
        if finding["severity"] == "critical":
            score -= 30
        elif finding["severity"] == "major":
            score -= 10
        elif finding["severity"] == "minor":
            score -= 3

    score = max(score, 0)
    criticals = [f for f in findings if f["severity"] == "critical"]
    minimum = manifest.get("spec", {}).get("eval", {}).get("minimumScore", 85)
    status = "approved" if score >= minimum and not criticals else "rejected"

    return {
        "capability": manifest.get("metadata", {}).get("name"),
        "version": manifest.get("metadata", {}).get("version"),
        "owner": manifest.get("metadata", {}).get("owner"),
        "type": manifest.get("spec", {}).get("type"),
        "riskLevel": manifest.get("spec", {}).get("riskLevel"),
        "score": score,
        "status": status,
        "findings": findings,
        "certification": {
            "publishAllowed": status == "approved",
            "minimumScore": minimum,
        },
    }
