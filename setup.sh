#!/bin/bash
# VPS Agent Auto-Setup Script
# এই স্ক্রিপ্ট চালালে সবকিছু স্বয়ংক্রিয়ভাবে সেটআপ হবে

set -e

echo "🚀 Qwen3 AI Agent VPS Setup শুরু হচ্ছে..."
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"

# Step 1: Directory সেটআপ
echo "📁 Directory তৈরি করছি..."
AGENT_DIR="/root/qwen3-ai-agent"
if [ ! -d "$AGENT_DIR" ]; then
    mkdir -p "$AGENT_DIR"
    cd "$AGENT_DIR"
    git init
    git remote add origin https://github.com/umd81568-lab/qwen3-ai-agent.git
else
    cd "$AGENT_DIR"
fi

# Step 2: Repository থেকে pull করুন
echo "📥 GitHub থেকে ফাইল pull করছি..."
git fetch origin main
git reset --hard origin/main

# Step 3: Permission সেট করুন
echo "🔐 Permission সেট করছি..."
chmod +x *.py
chmod +x setup.sh 2>/dev/null || true

# Step 4: Python dependencies চেক করুন
echo "🐍 Python dependencies চেক করছি..."
if ! command -v python3 &> /dev/null; then
    echo "❌ Python3 ইনস্টল করা নেই"
    exit 1
fi

# Step 5: Test করুন
echo "✅ ফাইল সেটআপ সম্পন্ন!"
echo ""
echo "📋 এখন যোগ করা হয়েছে:"
ls -lah | grep -E "\.py$|\.md$"

echo ""
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "🎯 এখন চালান:"
echo ""
echo "1️⃣  Queen Model Agent:"
echo "   python3 queen_model_agent.py"
echo ""
echo "2️⃣  Secondary Agent Control:"
echo "   python3 secondary_agent_control.py"
echo ""
echo "3️⃣  System Status:"
echo "   python3 -c \"from queen_model_agent import QueenModelAgent; QueenModelAgent().get_system_status()\""
echo ""
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "✨ সেটআপ সম্পন্ন!"
