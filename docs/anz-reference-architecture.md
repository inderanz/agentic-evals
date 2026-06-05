# ANZ-Style Reference Architecture

## Target Environment

- GitHub Enterprise for source control and pull requests
- GKE for evaluation API and runners
- Workload Identity for cloud access
- OPA for policy-as-code
- GCS for scorecard/evidence retention
- BigQuery/Looker for evaluation analytics
- Internal marketplace UI after governance is proven

## Flow

```text
Developer PR
  -> GitHub workflow
  -> Internal HTTPS endpoint
  -> Evaluation API
  -> Isolated runner pod
  -> Scorecard
  -> GitHub required check
  -> Certified registry
```

## Banking Controls

- No direct publishing
- Human approval for destructive/payment-impacting tools
- Audit logging for confidential data
- PII redaction and leakage tests
- Cross-user memory isolation tests
- Periodic recertification
- Runtime monitoring after publication
