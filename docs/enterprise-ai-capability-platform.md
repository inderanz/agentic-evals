# Enterprise AI Capability Platform

## Purpose

Build an internal governed marketplace for AI capabilities:

- MCP servers
- Skills
- Agents
- Prompt packages
- Workflow packages
- Knowledge packs

The marketplace is not just a UI. It is an AI supply-chain control plane.

## Core Architecture

```mermaid
flowchart LR
  TeamRepo[Team Capability Repo] --> PR[Pull Request]
  PR --> GHA[GitHub Workflow]
  GHA --> EvalAPI[Evaluation API on GKE]
  EvalAPI --> Runner[Evaluation Runner]
  Runner --> Static[Static Validation]
  Runner --> MCP[MCP Protocol Evals]
  Runner --> Skill[Skill Evals]
  Runner --> Agent[Agent Behaviour Evals]
  Runner --> Policy[OPA Policy]
  Runner --> Score[Scorecard]
  Score --> Check[GitHub Required Check]
  Score --> Registry[Certified Capability Registry]
  Registry --> Marketplace[Internal Marketplace]
```

## Enterprise Rule

No AI capability is publishable unless:

- `marketplace.yaml` is valid
- ownership is clear
- risk and data classification are declared
- eval cases exist
- security checks pass
- destructive actions require human approval
- score is above threshold
- zero critical findings exist

