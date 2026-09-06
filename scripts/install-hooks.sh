#!/usr/bin/env bash
# FLL Team 76265 - Git Pre-commit Hook Installer
# Installs local git pre-commit security checks into .git/hooks/pre-commit

set -e

REPO_ROOT="$(git rev-parse --show-toplevel 2>/dev/null || pwd)"
HOOK_FILE="$REPO_ROOT/.git/hooks/pre-commit"

echo " Installing FLL #76265 Security & Privacy Pre-commit Hooks..."

mkdir -p "$REPO_ROOT/.git/hooks"

cat << 'EOF' > "$HOOK_FILE"
#!/usr/bin/env bash
# Git Pre-commit Hook for FLL Team 76265 BIOGLOW
set -e

echo "🔍 Running FLL #76265 Pre-commit Security & Privacy Checks..."

# 1. PII Leak Scanner
if command -v python3 >/dev/null 2>&1; then
    python3 scripts/pii_leak_scanner.py
else
    echo "⚠️ Python3 not found; skipping local PII scan."
fi

# 2. Credential & Secret Scanner (Gitleaks if installed)
if command -v gitleaks >/dev/null 2>&1; then
    echo "🔒 Running Gitleaks credential scanner..."
    gitleaks protect --staged --verbose
else
    echo "💡 Note: Gitleaks is not installed locally. Secret scan will run in GitHub Actions CI."
fi

echo "✅ All local pre-commit security checks passed!"
EOF

chmod +x "$HOOK_FILE"

echo "✅ Pre-commit hook successfully installed at: $HOOK_FILE"
