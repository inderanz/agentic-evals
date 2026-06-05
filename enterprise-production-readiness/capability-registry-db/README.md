# Capability Registry Database

Purpose: persist certified capability metadata, versions, evidence, approvals, and expiry.

Real outcome:
- Marketplace only reads from certified registry.
- Every capability version is tied to repo, commit SHA, scorecard, and evidence artifacts.
- Recertification is possible because expiry and source commit are stored.
