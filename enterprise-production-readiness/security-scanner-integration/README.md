# Security Scanner Integration

Purpose: replace simple regex scanning with standard enterprise scanners.

Recommended tools:
- Gitleaks for secrets
- Semgrep for static code analysis
- Trivy for container/dependency scan and SBOM
- OPA/Conftest for policy-as-code checks
- SLSA provenance verification where build provenance is available

Real outcome:
- Critical secret = reject
- Critical/high exploitable dependency = reject or require exception
- Missing SBOM for deployable server = reject
- License violation = reject or legal review
