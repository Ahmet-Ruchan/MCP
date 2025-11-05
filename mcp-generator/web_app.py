#!/usr/bin/env python3
"""
MCP Generator Web Application
A user-friendly web interface for generating MCP servers
"""

import asyncio
import json
import shutil
import sys
import tempfile
import zipfile
from pathlib import Path
from typing import Dict, Any, List

from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import HTMLResponse, JSONResponse, FileResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

# Mock MCP imports for web usage
class MockServer:
    def __init__(self, name): pass
    def list_tools(self): return lambda f: f
    def call_tool(self): return lambda f: f
    def list_resources(self): return lambda f: f
    def read_resource(self): return lambda f: f
    def list_prompts(self): return lambda f: f
    def get_prompt(self): return lambda f: f

sys.modules['mcp'] = type(sys)('mcp')
sys.modules['mcp.server'] = type(sys)('mcp.server')
sys.modules['mcp.server'].Server = MockServer
sys.modules['mcp.server.stdio'] = type(sys)('mcp.server.stdio')
sys.modules['mcp.server.stdio'].stdio_server = lambda: None
sys.modules['mcp.types'] = type(sys)('mcp.types')
sys.modules['mcp.types'].Tool = object
sys.modules['mcp.types'].TextContent = object
sys.modules['mcp.types'].ImageContent = object
sys.modules['mcp.types'].EmbeddedResource = object
sys.modules['mcp.types'].LoggingLevel = object

from server import MCPTemplate

# Initialize FastAPI app
app = FastAPI(title="MCP Generator Web UI", version="1.0.0")

# Mount static files and templates
static_path = Path(__file__).parent / "static"
templates_path = Path(__file__).parent / "templates"
static_path.mkdir(exist_ok=True)
templates_path.mkdir(exist_ok=True)

app.mount("/static", StaticFiles(directory=str(static_path)), name="static")
templates = Jinja2Templates(directory=str(templates_path))


@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    """Render the main page"""
    return templates.TemplateResponse("index.html", {"request": request})


@app.get("/api/examples/{server_type}")
async def get_example(server_type: str):
    """Get example configuration for a server type"""
    examples = {
        "tool": {
            "tools": [
                {
                    "name": "example_tool",
                    "description": "An example tool",
                    "parameters": [
                        {
                            "name": "input",
                            "type": "string",
                            "description": "Input parameter",
                            "required": True
                        }
                    ]
                }
            ]
        },
        "resource": {
            "resources": [
                {
                    "uri": "data://example",
                    "name": "Example Resource",
                    "description": "An example resource",
                    "type": "json"
                }
            ]
        },
        "full": {
            "tools": [
                {
                    "name": "example_tool",
                    "description": "An example tool",
                    "parameters": [
                        {
                            "name": "input",
                            "type": "string",
                            "description": "Input parameter",
                            "required": True
                        }
                    ]
                }
            ],
            "resources": [
                {
                    "uri": "data://example",
                    "name": "Example Resource",
                    "description": "An example resource",
                    "type": "json"
                }
            ],
            "prompts": [
                {
                    "name": "example_prompt",
                    "description": "An example prompt"
                }
            ]
        }
    }

    if server_type not in examples:
        raise HTTPException(status_code=404, detail="Server type not found")

    return JSONResponse(examples[server_type])


@app.post("/api/validate")
async def validate_config(config: Dict[str, Any]):
    """Validate a configuration"""
    errors = []
    warnings = []

    # Validate tools
    if "tools" in config:
        for i, tool in enumerate(config["tools"]):
            if not tool.get("name"):
                errors.append(f"Tool {i + 1}: Missing 'name' field")
            if not tool.get("description"):
                warnings.append(f"Tool {i + 1}: Missing 'description' field")

            if "parameters" in tool:
                for j, param in enumerate(tool["parameters"]):
                    if not param.get("name"):
                        errors.append(f"Tool {i + 1}, Parameter {j + 1}: Missing 'name' field")

    # Validate resources
    if "resources" in config:
        for i, resource in enumerate(config["resources"]):
            if not resource.get("uri"):
                errors.append(f"Resource {i + 1}: Missing 'uri' field")
            if not resource.get("name"):
                errors.append(f"Resource {i + 1}: Missing 'name' field")

    # Validate prompts
    if "prompts" in config:
        for i, prompt in enumerate(config["prompts"]):
            if not prompt.get("name"):
                errors.append(f"Prompt {i + 1}: Missing 'name' field")

    return JSONResponse({
        "valid": len(errors) == 0,
        "errors": errors,
        "warnings": warnings
    })


@app.post("/api/generate")
async def generate_server(request: Dict[str, Any]):
    """Generate MCP server files"""
    try:
        name = request.get("name")
        description = request.get("description")
        server_type = request.get("server_type")
        config = request.get("config", {})

        # Validation
        if not name:
            raise HTTPException(status_code=400, detail="Server name is required")
        if not description:
            raise HTTPException(status_code=400, detail="Description is required")
        if not server_type:
            raise HTTPException(status_code=400, detail="Server type is required")

        # Generate files based on server type
        if server_type == "tool":
            tools = config.get("tools", [])
            files = MCPTemplate.basic_tool_server(name, description, tools)
        elif server_type == "resource":
            resources = config.get("resources", [])
            files = MCPTemplate.resource_server(name, description, resources)
        elif server_type == "full":
            files = MCPTemplate.full_server(name, description, config)
        else:
            raise HTTPException(status_code=400, detail=f"Unknown server type: {server_type}")

        # Create temporary directory
        temp_dir = Path(tempfile.mkdtemp())
        server_dir = temp_dir / name
        server_dir.mkdir(parents=True, exist_ok=True)

        # Write files
        for filename, content in files.items():
            (server_dir / filename).write_text(content)

        # Create zip file
        zip_path = temp_dir / f"{name}.zip"
        with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
            for file_path in server_dir.rglob('*'):
                if file_path.is_file():
                    zipf.write(file_path, file_path.relative_to(temp_dir))

        return JSONResponse({
            "success": True,
            "message": f"Server '{name}' generated successfully!",
            "download_url": f"/api/download/{zip_path.name}",
            "files": list(files.keys()),
            "temp_path": str(zip_path)
        })

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# Store temp files for download
temp_files = {}

@app.post("/api/generate-and-prepare")
async def generate_and_prepare(request: Dict[str, Any]):
    """Generate server and prepare for download"""
    try:
        name = request.get("name")
        description = request.get("description")
        server_type = request.get("server_type")
        config = request.get("config", {})

        # Validation
        if not name:
            raise HTTPException(status_code=400, detail="Server name is required")
        if not description:
            raise HTTPException(status_code=400, detail="Description is required")
        if not server_type:
            raise HTTPException(status_code=400, detail="Server type is required")

        # Generate files
        if server_type == "tool":
            tools = config.get("tools", [])
            files = MCPTemplate.basic_tool_server(name, description, tools)
        elif server_type == "resource":
            resources = config.get("resources", [])
            files = MCPTemplate.resource_server(name, description, resources)
        elif server_type == "full":
            files = MCPTemplate.full_server(name, description, config)
        else:
            raise HTTPException(status_code=400, detail=f"Unknown server type: {server_type}")

        # Create temporary directory
        temp_dir = Path(tempfile.mkdtemp())
        server_dir = temp_dir / name
        server_dir.mkdir(parents=True, exist_ok=True)

        # Write files
        for filename, content in files.items():
            (server_dir / filename).write_text(content)

        # Create zip file
        zip_filename = f"{name}.zip"
        zip_path = temp_dir / zip_filename
        with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
            for file_path in server_dir.rglob('*'):
                if file_path.is_file():
                    zipf.write(file_path, file_path.relative_to(temp_dir))

        # Store for download
        temp_files[zip_filename] = str(zip_path)

        return JSONResponse({
            "success": True,
            "message": f"✅ Server '{name}' generated successfully!",
            "filename": zip_filename,
            "files": list(files.keys())
        })

    except Exception as e:
        return JSONResponse({
            "success": False,
            "message": f"❌ Error: {str(e)}"
        }, status_code=500)


@app.get("/api/download/{filename}")
async def download_file(filename: str):
    """Download generated server zip file"""
    if filename not in temp_files:
        raise HTTPException(status_code=404, detail="File not found")

    file_path = temp_files[filename]

    if not Path(file_path).exists():
        raise HTTPException(status_code=404, detail="File not found")

    return FileResponse(
        file_path,
        media_type="application/zip",
        filename=filename
    )


@app.get("/health")
async def health():
    """Health check endpoint"""
    return {"status": "healthy", "service": "MCP Generator Web UI"}


def find_available_port(start_port: int = 5000, max_attempts: int = 10) -> int:
    """Find an available port starting from start_port"""
    import socket

    for port in range(start_port, start_port + max_attempts):
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.bind(("0.0.0.0", port))
                return port
        except OSError:
            continue

    raise RuntimeError(f"Could not find available port in range {start_port}-{start_port + max_attempts}")


def is_port_available(host: str, port: int) -> bool:
    """Check if a port is available"""
    import socket

    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind((host, port))
            return True
    except OSError:
        return False


if __name__ == "__main__":
    import uvicorn
    import argparse

    # Parse command line arguments
    parser = argparse.ArgumentParser(description="MCP Generator Web UI")
    parser.add_argument(
        "--port",
        type=int,
        default=5000,
        help="Port to run the server on (default: 5000)"
    )
    parser.add_argument(
        "--host",
        type=str,
        default="0.0.0.0",
        help="Host to bind to (default: 0.0.0.0)"
    )
    parser.add_argument(
        "--auto-port",
        action="store_true",
        help="Automatically find an available port if the specified port is in use"
    )

    args = parser.parse_args()

    port = args.port

    # Check if port is available BEFORE trying to start uvicorn
    if not is_port_available(args.host, port):
        if args.auto_port:
            try:
                port = find_available_port(port)
                print(f"⚠️  Port {args.port} is already in use")
                print(f"✅ Using available port {port} instead\n")
            except RuntimeError as e:
                print(f"❌ Error: {e}")
                sys.exit(1)
        else:
            # Port is in use and auto-port is not enabled
            print()
            print(f"❌ Error: Port {port} is already in use!")
            print()
            print("💡 Solutions:")
            print(f"   1. Use a different port: python web_app.py --port 8080")
            print(f"   2. Use auto-port mode: python web_app.py --auto-port")
            print(f"   3. Kill the process using port {port}:")
            print(f"      - macOS/Linux: lsof -i :{port} | grep LISTEN")
            print(f"      - Windows: netstat -ano | findstr :{port}")
            print()
            sys.exit(1)

    print("🚀 Starting MCP Generator Web UI...")
    print(f"📍 Open your browser at: http://localhost:{port}")
    print("🛑 Press Ctrl+C to stop")
    print()

    uvicorn.run(app, host=args.host, port=port)
