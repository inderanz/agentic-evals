package ai.marketplace

deny[msg] {
  input.spec.riskLevel == "high"
  not input.spec.runtime.authRequired
  msg := "High-risk capability must require authentication"
}

deny[msg] {
  input.spec.dataClassification == "confidential"
  not input.spec.security.requiresAuditLogging
  msg := "Confidential capability must enable audit logging"
}

deny[msg] {
  tool := input.spec.capabilities.tools[_]
  tool.risk == "destructive"
  not tool.requiresHumanApproval
  msg := sprintf("Destructive tool %s requires human approval", [tool.name])
}
