#!/bin/bash

echo "🚀 Starting MCP Generator (Streamlit Version)..."
echo ""
echo "📦 Installing dependencies..."
pip install -q streamlit

echo ""
echo "✅ Launching web interface..."
echo ""

streamlit run streamlit_app.py
