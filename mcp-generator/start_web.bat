@echo off

REM Quick launcher for Streamlit Web Interface

echo 🚀 Starting MCP Generator Web Interface...
echo.

REM Check if streamlit is installed
streamlit --version >nul 2>&1
if errorlevel 1 (
    echo 📦 Installing Streamlit...
    pip install -q streamlit
)

echo ✅ Launching at http://localhost:8501
echo 🌐 Browser will open automatically...
echo 🛑 Press Ctrl+C to stop
echo.

streamlit run streamlit_app.py
