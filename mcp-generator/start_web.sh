#!/bin/bash

# Quick launcher for Streamlit Web Interface

echo "🚀 Starting MCP Generator Web Interface..."
echo ""

# Check if streamlit is installed
if ! command -v streamlit &> /dev/null; then
    echo "📦 Installing Streamlit..."
    pip install -q streamlit
fi

echo "✅ Launching at http://localhost:8501"
echo "🌐 Browser will open automatically..."
echo "🛑 Press Ctrl+C to stop"
echo ""

streamlit run streamlit_app.py
