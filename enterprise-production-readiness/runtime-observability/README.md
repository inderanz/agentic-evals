# Runtime Observability

Purpose: certification is not enough. Certified capabilities must be monitored at runtime.

Signals:
- Tool invocation count
- User/team consuming capability
- Latency and error rate
- Rejected policy decisions
- Destructive action approval requests
- Prompt injection detections
- PII redaction events
- Cost per capability
- Model/tool drift over time

Recommended implementation:
- OpenTelemetry traces with run_id, capability_id, version, tool_name
- Structured audit logs
- BigQuery/warehouse export for governance dashboard
- Alerting on abnormal tool usage and policy denies
