#!/bin/bash

# Verification script for CLI Coding Agents Lab
# Checks all prerequisites and installations

echo "============================================"
echo "🔍 CLI Coding Agents Lab - Setup Verification"
echo "============================================"
echo ""

# Track overall status
ALL_GOOD=true

# Initialize status variables
PYTHON_STATUS="❌ Not installed"
NODE_STATUS="❌ Not installed"
TOKEN_STATUS="❌ Not set"
COPILOT_STATUS="❌ Not installed"
GEMINI_STATUS="❌ Not installed"
EXTENSION_STATUS="❌ Not installed"
AUTH_STATUS="❌ Not configured"

# Check 1: Python & pip
if command -v python3 &> /dev/null && command -v pip3 &> /dev/null; then
    PYTHON_VERSION=$(python3 --version)
    PIP_VERSION=$(pip3 --version | cut -d' ' -f2)
    PYTHON_STATUS="✅ $PYTHON_VERSION, pip $PIP_VERSION"
else
    ALL_GOOD=false
fi

# Check 2: Node.js & npm
if command -v node &> /dev/null && command -v npm &> /dev/null; then
    NODE_VERSION=$(node --version)
    NPM_VERSION=$(npm --version)
    NODE_MAJOR=$(node --version | cut -d'.' -f1 | tr -d 'v')
    if [ "$NODE_MAJOR" -lt 22 ]; then
        NODE_STATUS="⚠️  $NODE_VERSION (v22+ recommended), npm $NPM_VERSION"
    else
        NODE_STATUS="✅ $NODE_VERSION, npm $NPM_VERSION"
    fi
else
    ALL_GOOD=false
fi

# Check 3: GitHub Token
if [ -n "$GITHUB_TOKEN" ] || [ -n "$GH_TOKEN" ]; then
    if [ -n "$GITHUB_TOKEN" ]; then
        TOKEN_PREVIEW="${GITHUB_TOKEN:0:12}..."
    else
        TOKEN_PREVIEW="${GH_TOKEN:0:12}..."
    fi
    TOKEN_STATUS="✅ Set ($TOKEN_PREVIEW)"
else
    TOKEN_STATUS="❌ Not set"
    ALL_GOOD=false
fi

# Check 4: GitHub Copilot CLI
if command -v copilot &> /dev/null; then
    COPILOT_VERSION=$(timeout 3 copilot --version 2>/dev/null | head -1 || echo "installed")
    COPILOT_STATUS="✅ $COPILOT_VERSION"
else
    COPILOT_STATUS="❌ Not installed"
    ALL_GOOD=false
fi

# Check 5: Google Gemini CLI
if command -v gemini &> /dev/null; then
    GEMINI_VERSION=$(timeout 3 gemini --version 2>/dev/null || echo "installed")
    GEMINI_STATUS="✅ $GEMINI_VERSION"
else
    GEMINI_STATUS="❌ Not installed"
    ALL_GOOD=false
fi

# Check 6: Gemini CLI Companion Extension
if [ -d "$HOME/.vscode-remote/extensions" ] && ls "$HOME/.vscode-remote/extensions" | grep -q "google.gemini-cli-vscode-ide-companion"; then
    EXTENSION_VERSION=$(ls "$HOME/.vscode-remote/extensions" | grep "google.gemini-cli-vscode-ide-companion" | head -1 | sed 's/.*ide-companion-//')
    EXTENSION_STATUS="✅ v$EXTENSION_VERSION"
else
    EXTENSION_STATUS="❌ Not installed"
    ALL_GOOD=false
fi

# Check Gemini Authentication (only if CLI is installed)
if command -v gemini &> /dev/null; then
    if [ -n "$GEMINI_API_KEY" ]; then
        AUTH_STATUS="✅ API key set"
    else
        AUTH_STATUS="⚠️  API key not set"
    fi
fi

# Output compact table
printf "| %-22s | %-29s |\n" "Component" "Status"
printf "|%-23s|%-30s|\n" "------------------------" "-------------------------------"
printf "| %-24s | %-30s |\n" "🐍 Python & pip" "$PYTHON_STATUS"
printf "| %-24s | %-30s |\n" "📦 Node.js & npm" "$NODE_STATUS"
printf "| %-24s | %-30s |\n" "🔑 GitHub Token" "$TOKEN_STATUS"
printf "| %-24s | %-30s |\n" "🤖 GitHub Copilot CLI" "$COPILOT_STATUS"
printf "| %-24s | %-30s |\n" "🌟 Google Gemini CLI" "$GEMINI_STATUS"
printf "| %-24s | %-30s |\n" "🔌 Gemini Extension" "$EXTENSION_STATUS"
printf "| %-24s | %-30s |\n" "🔐 Gemini Auth" "$AUTH_STATUS"
echo ""

# Final status
echo "============================================"
if [ "$ALL_GOOD" = true ]; then
    echo "🎉 All systems ready!"
    echo ""
    echo "🚀 Quick start:"
    echo "   copilot    # GitHub Copilot CLI"
    echo "   gemini     # Google Gemini CLI"
else
    echo "⚠️  Fix issues above, then run: ./verify_setup.sh"
fi
echo "============================================"
