@echo off

REM MCP Generator Launcher
REM Supports both MCP Server mode and Web Interface mode

echo 🔧 MCP Generator Launcher
echo.
echo Select launch mode:
echo   1) Web Interface (Streamlit) - Recommended ⭐
echo   2) MCP Server (Python stdio)
echo.
set /p choice="Enter choice [1-2]: "

if "%choice%"=="1" (
    echo.
    echo 🚀 Launching Web Interface (Streamlit)...
    echo.

    REM Check if streamlit is installed
    streamlit --version >nul 2>&1
    if errorlevel 1 (
        echo 📦 Streamlit not found. Installing...
        pip install -q streamlit
    )

    echo ✅ Starting web interface at http://localhost:8501
    echo 🌐 Browser will open automatically...
    echo.
    streamlit run streamlit_app.py
) else if "%choice%"=="2" (
    echo.
    echo 🔧 Launching MCP Server...
    echo 📡 Server will communicate via stdio
    echo 💡 Use this with Claude Desktop or other MCP clients
    echo.
    python server.py
) else (
    echo ❌ Invalid choice. Please run again and select 1 or 2.
    exit /b 1
)
