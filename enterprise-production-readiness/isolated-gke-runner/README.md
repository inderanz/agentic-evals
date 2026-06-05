# Isolated GKE Evaluation Runner

Purpose: every evaluation runs in an isolated Kubernetes Job, not inside the API pod.

Real outcome:
- No shared state across evaluations.
- Network egress can be restricted.
- Resource limits prevent abuse.
- Logs and artifacts are collected per run.

Recommended controls:
- Namespace: ai-evaluation-runs
- One Job per evaluation
- Non-root container
- No privilege escalation
- Read-only root filesystem where possible
- Deny-all NetworkPolicy by default
- Only allow egress to GitHub, Artifact Registry, package mirrors approved by enterprise, and internal evaluator APIs
- Workload Identity with least privilege
