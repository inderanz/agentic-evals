#!/usr/bin/env bash
set -euo pipefail

REPO_PATH="${1:-.}"
mkdir -p security-results

gitleaks detect --source "$REPO_PATH" --report-format json --report-path security-results/gitleaks.json || true
semgrep scan --config auto --json --output security-results/semgrep.json "$REPO_PATH" || true
trivy fs --format json --output security-results/trivy-fs.json "$REPO_PATH" || true
trivy fs --format cyclonedx --output security-results/sbom.cdx.json "$REPO_PATH" || true

echo "Security scan artifacts written to security-results/"
