#!/bin/bash

# MCP Generator Launcher
# Supports both MCP Server mode and Web Interface mode

echo "🔧 MCP Generator Launcher"
echo ""
echo "Select launch mode:"
echo "  1) Web Interface (Streamlit) - Recommended ⭐"
echo "  2) MCP Server (Python stdio)"
echo ""
read -p "Enter choice [1-2]: " choice

case $choice in
    1)
        echo ""
        echo "🚀 Launching Web Interface (Streamlit)..."
        echo ""

        # Check if streamlit is installed
        if ! command -v streamlit &> /dev/null; then
            echo "📦 Streamlit not found. Installing..."
            pip install -q streamlit
        fi

        echo "✅ Starting web interface at http://localhost:8501"
        echo "🌐 Browser will open automatically..."
        echo ""
        streamlit run streamlit_app.py
        ;;
    2)
        echo ""
        echo "🔧 Launching MCP Server..."
        echo "📡 Server will communicate via stdio"
        echo "💡 Use this with Claude Desktop or other MCP clients"
        echo ""
        python server.py
        ;;
    *)
        echo "❌ Invalid choice. Please run again and select 1 or 2."
        exit 1
        ;;
esac
