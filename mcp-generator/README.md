# MCP Generator

A **Model Context Protocol (MCP) server that generates other MCP servers**. This meta-MCP tool helps developers quickly scaffold new MCP servers with best practices and proper structure.

## 🌟 NEW: Web Interface Available!

Now with a **beautiful web interface** for creating MCP servers without writing any code! 🎉

![Web Interface](https://img.shields.io/badge/Web-Interface-brightgreen) ![Python](https://img.shields.io/badge/Python-3.10+-blue) ![FastAPI](https://img.shields.io/badge/FastAPI-Modern-orange)

## What is MCP Generator?

MCP Generator is a code generation tool that creates complete, production-ready MCP servers from simple configurations. Instead of manually writing boilerplate code, you describe what you want and MCP Generator creates the entire server structure for you.

## Features

- ✨ **Beautiful Web Interface**: Step-by-step wizard for easy server creation (NEW!)
- 🚀 **Multiple Server Types**: Generate tool-based, resource-based, or full-featured MCP servers
- 📝 **Template-Based Generation**: Uses best practices and proven patterns
- 📁 **Automatic File Structure**: Creates all necessary files (server.py, README.md, requirements.txt)
- ✅ **Configuration Validation**: Validates your configuration before generation
- 📚 **Example Configs**: Provides example configurations to get started quickly
- 🤖 **AI Assistant Integration**: Works with Cursor, Claude Code, and other MCP-compatible tools
- 🎨 **Modern UI**: Responsive design with smooth animations and Tailwind CSS

## Installation & Usage

### Prerequisites

- Python 3.10 or higher
- pip package manager

### 🚀 Quick Start

Choose your preferred method:

---

### Method 1: Web Interface (Easiest!) ⭐ RECOMMENDED

**Perfect for:** Everyone! No coding needed.

```bash
cd mcp-generator

# Quick start - Interactive launcher
./start.sh          # Mac/Linux
start.bat           # Windows

# OR directly launch web interface
./start_web.sh      # Mac/Linux
start_web.bat       # Windows

# OR manual launch
pip install streamlit
streamlit run streamlit_app.py
```

**Features:**
- ✅ Opens automatically in your browser at `http://localhost:8501`
- ✅ No port conflicts - Streamlit handles it!
- ✅ Beautiful step-by-step wizard
- ✅ Download generated servers as ZIP

👉 **See [STREAMLIT_GUIDE.md](STREAMLIT_GUIDE.md) for detailed guide**

---

### Method 2: MCP Server Mode (For Claude Desktop)

**Perfect for:** Using with Claude Desktop, Cursor, or other MCP clients

```bash
cd mcp-generator

# Quick start
./start_mcp.sh      # Mac/Linux
start_mcp.bat       # Windows

# OR manual launch
python server.py
```

**Configuration:**

Add to your Claude Desktop config (`~/Library/Application Support/Claude/claude_desktop_config.json` on Mac):

```json
{
  "mcpServers": {
    "mcp-generator": {
      "command": "python",
      "args": ["/absolute/path/to/mcp-generator/server.py"]
    }
  }
}
```

**Features:**
- 🤖 Generate servers by talking to Claude
- 🔧 Access via MCP tools
- 📝 Example configurations included

👉 **See [DETAILED_README.md](DETAILED_README.md) for comprehensive documentation**

---

### Method 3: FastAPI (Advanced)

**Perfect for:** Developers who need REST API access

```bash
cd mcp-generator
pip install -r web_requirements.txt

# Start server (auto-finds available port)
python web_app.py

# Custom port
python web_app.py --port 8080
```

Open browser at `http://localhost:5000` (or check terminal for actual port)

👉 **See [WEB_APP_GUIDE.md](WEB_APP_GUIDE.md) for detailed guide**

---

### 💡 Which Method Should I Use?

| Method | Use When | Difficulty |
|--------|----------|-----------|
| **Web Interface (Streamlit)** ⭐ | You want a simple UI | 🟢 Easy |
| **MCP Server Mode** | Using with Claude Desktop | 🟡 Medium |
| **FastAPI** | Need REST API | 🔴 Advanced |

**Recommendation:** Start with the **Web Interface (Streamlit)**! It's the easiest and most user-friendly.

## Available Tools

### 1. generate_mcp_server

Generate a complete MCP server from a template.

**Parameters:**
- `name` (string, required): Name of the server (e.g., "weather-server")
- `description` (string, required): What the server does
- `server_type` (enum, required): Type of server ("tool", "resource", or "full")
- `output_dir` (string, required): Where to create the server
- `config` (object, optional): Configuration with tools, resources, and prompts

**Example:**
```json
{
  "name": "calculator-server",
  "description": "A calculator MCP server with math operations",
  "server_type": "tool",
  "output_dir": "./my-servers",
  "config": {
    "tools": [
      {
        "name": "add",
        "description": "Add two numbers",
        "parameters": [
          {"name": "a", "type": "number", "description": "First number", "required": true},
          {"name": "b", "type": "number", "description": "Second number", "required": true}
        ]
      }
    ]
  }
}
```

### 2. list_templates

List all available MCP server templates with descriptions.

**Parameters:** None

### 3. validate_mcp_config

Validate a configuration before generating a server.

**Parameters:**
- `config` (object, required): The configuration to validate

### 4. generate_example_config

Get an example configuration for a specific server type.

**Parameters:**
- `server_type` (enum, required): Server type ("tool", "resource", or "full")

## Server Types

### Tool Server (`"tool"`)

Creates a server that provides tools/functions for AI assistants to use.

**Use cases:**
- API integrations (weather, databases, etc.)
- Calculations and data processing
- External service calls
- File operations

**Configuration:**
```json
{
  "tools": [
    {
      "name": "tool_name",
      "description": "What the tool does",
      "parameters": [
        {
          "name": "param_name",
          "type": "string|number|boolean|object|array",
          "description": "Parameter description",
          "required": true|false
        }
      ]
    }
  ]
}
```

### Resource Server (`"resource"`)

Creates a server that exposes data resources via URIs.

**Use cases:**
- Database access
- File system navigation
- Configuration data
- Real-time data feeds

**Configuration:**
```json
{
  "resources": [
    {
      "uri": "data://resource-name",
      "name": "Resource Display Name",
      "description": "What this resource provides",
      "type": "text|json"
    }
  ]
}
```

### Full Server (`"full"`)

Creates a complete server with tools, resources, and prompts.

**Use cases:**
- Complex integrations
- Multi-feature servers
- Advanced AI workflows
- Custom prompt templates

**Configuration:**
```json
{
  "tools": [...],
  "resources": [...],
  "prompts": [
    {
      "name": "prompt_name",
      "description": "What this prompt does"
    }
  ]
}
```

## Quick Start Examples

### Example 1: Simple Calculator

Ask your AI assistant:
```
Use the mcp-generator to create a calculator server with add and multiply tools
```

### Example 2: Weather Data Resource

Ask your AI assistant:
```
Generate a resource-based MCP server that provides weather data
```

### Example 3: Full-Featured Server

Ask your AI assistant:
```
Create a full MCP server with a search tool, results resource, and analysis prompt
```

## Usage in AI Tools

Once configured, you can interact with the generator through your AI assistant:

### Generating a Server

**User:** "Create a new MCP server for managing todos with add and list tools"

**AI Assistant will:**
1. Call `generate_example_config` to understand the structure
2. Call `generate_mcp_server` with your specifications
3. Create all necessary files
4. Provide instructions for using the new server

### Validating Configuration

**User:** "Validate this MCP config before generating: {...}"

**AI Assistant will:**
1. Call `validate_mcp_config` with your configuration
2. Report any errors or warnings
3. Suggest corrections if needed

## Generated Server Structure

When you generate a server, you get:

```
my-server/
├── server.py          # Main MCP server implementation
├── README.md          # Documentation
└── requirements.txt   # Python dependencies
```

## Tips and Best Practices

1. **Start Simple**: Begin with a basic tool server, then add complexity
2. **Validate First**: Use `validate_mcp_config` before generating
3. **Check Examples**: Use `generate_example_config` to see proper structure
4. **Test Locally**: Run `python server.py` to test your generated server
5. **Iterate**: Generate, test, modify, and regenerate as needed

## Troubleshooting

### Server not showing in AI tool
- Verify the path in your MCP configuration is absolute
- Check that Python is in your PATH
- Restart your AI tool completely

### Generation fails
- Validate your configuration first
- Check that output directory is writable
- Ensure all required fields are provided

### Generated server doesn't work
- Install requirements: `pip install -r requirements.txt`
- Check Python version (3.10+)
- Look for syntax errors in generated code

## Advanced Usage

### Custom Tool Types

You can specify various parameter types:
- `string`: Text data
- `number`: Numeric values
- `boolean`: True/False
- `object`: Nested structures
- `array`: Lists of items

### URI Patterns for Resources

Resources use URI patterns:
- `data://name` - Data resources
- `file://path` - File resources
- `api://endpoint` - API resources
- Custom patterns supported

### Multiple Tools in One Server

You can define multiple tools, resources, and prompts in a single server:

```json
{
  "tools": [
    {"name": "tool1", ...},
    {"name": "tool2", ...},
    {"name": "tool3", ...}
  ]
}
```

## Contributing

Ideas for improvement:
- Additional server templates
- More example configurations
- Code generation optimizations
- Documentation improvements

## License

MIT License - Feel free to use and modify

## Support

For issues or questions:
- Check the troubleshooting section
- Review example configurations
- Test with simple configurations first

---

**Made with MCP - A tool that generates MCP tools!**
