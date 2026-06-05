# GitHub App Checks API Integration

Purpose: replace a simple GitHub Action pass/fail with a proper GitHub App that creates rich check runs on commits.

Real outcome:
- PR shows AI Capability Evaluation as a required check.
- Findings appear as annotations.
- Scorecard artifact is linked.
- Merge is blocked if status is rejected.

Implementation steps:
1. Create GitHub App owned by the enterprise org.
2. Grant repository contents read, pull request read, checks read/write, metadata read.
3. Validate incoming webhook signatures.
4. On pull_request/opened or synchronize, create an evaluation job.
5. Use GitHub installation token to clone private repo at exact SHA.
6. Create a check_run with in_progress status.
7. Update check_run with success/failure and summary.

Security controls:
- Verify X-Hub-Signature-256.
- Do not store installation tokens.
- Allowlist repositories/orgs.
- Audit every evaluation request.
