# 🚀 MCP Generator - Comprehensive Guide

A revolutionary **Model Context Protocol (MCP)** server that generates other MCP servers automatically. This meta-tool allows developers to create production-ready MCP servers through simple configurations, eliminating boilerplate code and following best practices.

## 📑 Table of Contents

- [What is MCP Generator?](#what-is-mcp-generator)
- [Why Use MCP Generator?](#why-use-mcp-generator)
- [Features](#features)
- [Installation](#installation)
  - [Prerequisites](#prerequisites)
  - [Quick Install](#quick-install)
  - [Detailed Setup](#detailed-setup)
- [Configuration](#configuration)
  - [Cursor Setup](#cursor-setup)
  - [Claude Code Setup](#claude-code-setup)
  - [Standalone Usage](#standalone-usage)
- [Usage Guide](#usage-guide)
  - [Through AI Assistant](#through-ai-assistant)
  - [Through Web Interface](#through-web-interface)
  - [Programmatic Usage](#programmatic-usage)
- [Server Types](#server-types)
- [Examples](#examples)
- [Advanced Usage](#advanced-usage)
- [Troubleshooting](#troubleshooting)
- [FAQ](#faq)

---

## 🤔 What is MCP Generator?

MCP Generator is a **meta-MCP server** - it's an MCP server that creates other MCP servers for you. Instead of manually writing hundreds of lines of boilerplate code, you simply describe what you want, and MCP Generator creates a complete, production-ready server.

**Think of it as:**
- A scaffolding tool for MCP servers
- A code generator following MCP best practices
- A learning tool for understanding MCP protocol
- A productivity booster for developers

## 💡 Why Use MCP Generator?

### Before MCP Generator:
```python
# You need to write 200+ lines of boilerplate code
# Understanding MCP protocol intricacies
# Setting up proper async handlers
# Creating correct JSON schemas
# Writing documentation
# Testing everything manually
```

### With MCP Generator:
```javascript
// Simply tell your AI assistant:
"Create a weather MCP server with get_current and get_forecast tools"

// Or use the web interface and click through a wizard
// Generator creates everything for you in seconds!
```

### Benefits:
- ⚡ **10x Faster Development**: Create servers in minutes, not hours
- 📚 **Best Practices Built-in**: Follows MCP protocol standards
- 🎓 **Learning Tool**: Generated code is clean and well-documented
- 🔄 **Iterative Development**: Quickly regenerate and modify
- ✅ **Validated Output**: Built-in validation ensures correctness
- 📝 **Complete Documentation**: Generates README for each server

---

## ✨ Features

### Core Capabilities

1. **Three Server Types**
   - **Tool Servers**: For API integrations, calculations, external services
   - **Resource Servers**: For data access, file systems, databases
   - **Full Servers**: Complete servers with tools, resources, and prompts

2. **Automatic Generation**
   - Complete Python server code
   - JSON schema generation
   - README documentation
   - Requirements.txt with dependencies

3. **Interactive Tools**
   - `generate_mcp_server`: Create a new server
   - `list_templates`: View available templates
   - `validate_mcp_config`: Validate before generation
   - `generate_example_config`: Get example configurations

4. **Multiple Interfaces**
   - AI Assistant integration (Cursor, Claude Code)
   - Web-based wizard interface (NEW!)
   - Command-line programmatic usage
   - Python API for advanced users

---

## 📦 Installation

### Prerequisites

Before installing, ensure you have:

- **Python 3.10 or higher**
  ```bash
  python --version  # Should show 3.10+
  ```

- **pip** (Python package manager)
  ```bash
  pip --version
  ```

- **Git** (for cloning the repository)
  ```bash
  git --version
  ```

- **An MCP-compatible AI tool** (optional, for AI assistant integration)
  - Cursor IDE
  - Claude Code
  - Any MCP-compatible environment

### Quick Install

```bash
# 1. Clone the repository
git clone https://github.com/Ahmet-Ruchan/MCP.git
cd MCP/mcp-generator

# 2. Install dependencies
pip install -r requirements.txt

# 3. Verify installation
python test_generator.py
```

If you see "🎉 All tests passed!" - you're ready to go!

### Detailed Setup

#### Step 1: Clone Repository

```bash
# Using HTTPS
git clone https://github.com/Ahmet-Ruchan/MCP.git

# Or using SSH
git clone git@github.com:Ahmet-Ruchan/MCP.git

# Navigate to generator directory
cd MCP/mcp-generator
```

#### Step 2: Create Virtual Environment (Recommended)

```bash
# Create virtual environment
python -m venv venv

# Activate on macOS/Linux
source venv/bin/activate

# Activate on Windows
venv\Scripts\activate
```

#### Step 3: Install Dependencies

```bash
# Install from requirements.txt
pip install -r requirements.txt

# Verify installation
pip list | grep mcp
```

#### Step 4: Test Installation

```bash
# Run test suite
python test_generator.py

# Expected output:
# ============================================================
# TEST SUMMARY
# ============================================================
# ✅ PASS: Calculator Server
# ✅ PASS: Weather Resource Server
# ✅ PASS: Full-Featured Server
# ✅ PASS: Configuration Validation
#
# Results: 4/4 tests passed
# 🎉 All tests passed!
```

---

## ⚙️ Configuration

### Cursor Setup

1. **Find your Cursor MCP config file:**
   ```bash
   # macOS/Linux
   ~/.cursor/mcp.json

   # Windows
   %USERPROFILE%\.cursor\mcp.json
   ```

2. **Edit or create the file:**
   ```json
   {
     "mcpServers": {
       "mcp-generator": {
         "command": "python",
         "args": [
           "/absolute/path/to/MCP/mcp-generator/server.py"
         ]
       }
     }
   }
   ```

3. **Replace the path:**
   - On macOS/Linux: `/Users/yourusername/MCP/mcp-generator/server.py`
   - On Windows: `C:\\Users\\yourusername\\MCP\\mcp-generator\\server.py`

4. **Restart Cursor**

5. **Verify it's working:**
   - Open Cursor
   - Start a chat
   - Ask: "List available MCP tools"
   - You should see mcp-generator tools listed

### Claude Code Setup

1. **Find your Claude Code config:**
   ```bash
   # macOS/Linux
   ~/.config/claude-code/mcp.json

   # Windows
   %APPDATA%\claude-code\mcp.json
   ```

2. **Add configuration:**
   ```json
   {
     "mcpServers": {
       "mcp-generator": {
         "command": "python",
         "args": [
           "/absolute/path/to/MCP/mcp-generator/server.py"
         ]
       }
     }
   }
   ```

3. **Restart Claude Code**

### Standalone Usage

You can also use MCP Generator without an AI assistant:

```bash
# Option 1: Web Interface (NEW!)
cd /path/to/MCP/mcp-generator
python web_app.py
# Auto-finds available port (5000, 5001, 5002, etc.)
# Open the URL shown in terminal

# Specify custom port:
python web_app.py --port 8080

# Option 2: Command Line
python -c "from server import MCPTemplate; print(MCPTemplate.basic_tool_server(...))"

# Option 3: Python Script
# See "Programmatic Usage" section below
```

---

## 📖 Usage Guide

### Through AI Assistant

This is the easiest way to use MCP Generator!

#### Basic Example:

```
You: "Use the mcp-generator to create a calculator server with add and multiply tools"

AI: Let me create that for you...
    ✅ Successfully generated MCP server 'calculator-server'!

    📁 Location: ./my-servers/calculator-server
    📄 Files created:
      - server.py
      - README.md
      - requirements.txt

    🚀 Next steps:
    1. cd ./my-servers/calculator-server
    2. pip install -r requirements.txt
    3. python server.py
```

#### Advanced Example:

```
You: "Generate a full MCP server for a task manager with:
      - Tools: create_task, update_task, delete_task, list_tasks
      - Resources: tasks://all, tasks://completed
      - Prompts: summarize_tasks, prioritize_tasks"

AI: [Generates complete server with all components]
```

#### Validation Example:

```
You: "First validate this config, then generate if valid: {
       tools: [
         { name: 'search', description: 'Search data' }
       ]
     }"

AI: ✅ Configuration is valid!
    Now generating the server...
```

### Through Web Interface

1. **Start the web server:**
   ```bash
   cd mcp-generator
   python web_app.py
   # Auto-finds available port (default starts at 5000)

   # Custom port:
   python web_app.py --port 8080
   ```

2. **Open your browser:**
   ```
   Check the terminal output for the actual port
   ```
   Usually http://localhost:5000 (or 5001, 5002 if 5000 is busy)

3. **Follow the wizard:**

   **Step 1: Basic Information**
   - Server Name: `my-weather-server`
   - Description: `Weather data MCP server`
   - Server Type: `Full Server`

   **Step 2: Define Tools**
   - Tool Name: `get_weather`
   - Description: `Get current weather`
   - Parameters:
     - city (string, required)
     - units (string, optional)

   **Step 3: Define Resources** (if applicable)
   - URI: `weather://current`
   - Name: `Current Weather`
   - Type: `json`

   **Step 4: Review & Generate**
   - Preview your configuration
   - Click "Generate Server"
   - Download the generated files

### Programmatic Usage

For advanced users who want to integrate MCP Generator into their own tools:

```python
from server import MCPTemplate

# Example 1: Generate a tool server
config = {
    "name": "my-calculator",
    "description": "Simple calculator",
    "server_type": "tool",
    "output_dir": "./output",
    "config": {
        "tools": [
            {
                "name": "add",
                "description": "Add two numbers",
                "parameters": [
                    {
                        "name": "a",
                        "type": "number",
                        "description": "First number",
                        "required": True
                    },
                    {
                        "name": "b",
                        "type": "number",
                        "description": "Second number",
                        "required": True
                    }
                ]
            }
        ]
    }
}

# Generate the server
from pathlib import Path
files = MCPTemplate.basic_tool_server(
    config["name"],
    config["description"],
    config["config"]["tools"]
)

# Save files
output_path = Path(config["output_dir"]) / config["name"]
output_path.mkdir(parents=True, exist_ok=True)

for filename, content in files.items():
    (output_path / filename).write_text(content)

print(f"Server generated at: {output_path}")
```

---

## 🏗️ Server Types

### 1. Tool Server

**Purpose:** Create servers that provide executable tools/functions.

**Use Cases:**
- API integrations (weather, maps, databases)
- Mathematical calculations
- Data processing
- External service calls
- File operations

**Example Configuration:**
```json
{
  "tools": [
    {
      "name": "calculate_distance",
      "description": "Calculate distance between two points",
      "parameters": [
        {
          "name": "lat1",
          "type": "number",
          "description": "Latitude of first point",
          "required": true
        },
        {
          "name": "lon1",
          "type": "number",
          "description": "Longitude of first point",
          "required": true
        },
        {
          "name": "lat2",
          "type": "number",
          "description": "Latitude of second point",
          "required": true
        },
        {
          "name": "lon2",
          "type": "number",
          "description": "Longitude of second point",
          "required": true
        }
      ]
    }
  ]
}
```

### 2. Resource Server

**Purpose:** Expose data resources via URIs.

**Use Cases:**
- Database access
- File system navigation
- Configuration data
- Real-time data feeds
- Document storage

**Example Configuration:**
```json
{
  "resources": [
    {
      "uri": "db://users",
      "name": "User Database",
      "description": "Access user records",
      "type": "json"
    },
    {
      "uri": "db://products",
      "name": "Product Catalog",
      "description": "Product information",
      "type": "json"
    },
    {
      "uri": "config://settings",
      "name": "Application Settings",
      "description": "Configuration data",
      "type": "text"
    }
  ]
}
```

### 3. Full Server

**Purpose:** Complete servers with tools, resources, and prompts.

**Use Cases:**
- Complex integrations
- Multi-feature servers
- Advanced AI workflows
- Custom prompt templates
- Complete application backends

**Example Configuration:**
```json
{
  "tools": [
    {
      "name": "analyze_data",
      "description": "Analyze dataset",
      "parameters": [
        {
          "name": "data_id",
          "type": "string",
          "description": "Dataset identifier",
          "required": true
        }
      ]
    }
  ],
  "resources": [
    {
      "uri": "data://raw",
      "name": "Raw Data",
      "description": "Unprocessed data",
      "type": "json"
    },
    {
      "uri": "data://processed",
      "name": "Processed Data",
      "description": "Analyzed data",
      "type": "json"
    }
  ],
  "prompts": [
    {
      "name": "summarize_analysis",
      "description": "Create analysis summary"
    },
    {
      "name": "generate_report",
      "description": "Generate full report"
    }
  ]
}
```

---

## 💼 Examples

### Example 1: Weather Service

```javascript
// Ask AI:
"Create a weather MCP server with these tools:
 - get_current_weather (parameters: city, units)
 - get_forecast (parameters: city, days)
And these resources:
 - weather://alerts
 - weather://historical"
```

### Example 2: Database Manager

```javascript
// Ask AI:
"Generate a database MCP server with:
 - Tools: query, insert, update, delete
 - Resources: db://tables, db://schema
 - Prompts: optimize_query, explain_schema"
```

### Example 3: File System Navigator

```javascript
// Ask AI:
"Create a filesystem server with:
 - Tools: list_files, read_file, write_file, delete_file
 - Resources: fs://home, fs://documents"
```

### Example 4: E-commerce Server

```json
{
  "name": "ecommerce-server",
  "description": "E-commerce backend MCP server",
  "server_type": "full",
  "config": {
    "tools": [
      {
        "name": "search_products",
        "description": "Search product catalog",
        "parameters": [
          {
            "name": "query",
            "type": "string",
            "description": "Search query",
            "required": true
          },
          {
            "name": "category",
            "type": "string",
            "description": "Product category",
            "required": false
          }
        ]
      },
      {
        "name": "add_to_cart",
        "description": "Add product to cart",
        "parameters": [
          {
            "name": "product_id",
            "type": "string",
            "description": "Product ID",
            "required": true
          },
          {
            "name": "quantity",
            "type": "number",
            "description": "Quantity",
            "required": true
          }
        ]
      }
    ],
    "resources": [
      {
        "uri": "shop://products",
        "name": "Product Catalog",
        "description": "All products",
        "type": "json"
      },
      {
        "uri": "shop://cart",
        "name": "Shopping Cart",
        "description": "Current cart",
        "type": "json"
      }
    ],
    "prompts": [
      {
        "name": "recommend_products",
        "description": "Product recommendations"
      }
    ]
  }
}
```

---

## 🔧 Advanced Usage

### Custom Templates

Create your own templates by modifying the `MCPTemplate` class:

```python
@staticmethod
def custom_server(name: str, description: str, custom_config: dict) -> dict:
    """Your custom template logic"""
    # Implement your template
    return {
        "server.py": generated_code,
        "README.md": documentation,
        "requirements.txt": dependencies
    }
```

### Validation Rules

Add custom validation:

```python
def validate_custom_config(config: dict) -> tuple[bool, list[str]]:
    """Custom validation logic"""
    errors = []

    # Your validation rules
    if "required_field" not in config:
        errors.append("Missing required_field")

    return len(errors) == 0, errors
```

### Batch Generation

Generate multiple servers at once:

```python
servers = [
    {"name": "server1", "type": "tool", ...},
    {"name": "server2", "type": "resource", ...},
    {"name": "server3", "type": "full", ...}
]

for server_config in servers:
    # Generate each server
    generate_server(server_config)
```

---

## 🐛 Troubleshooting

### Issue: "No module named 'mcp'"

**Solution:**
```bash
pip install mcp
# or
pip install -r requirements.txt
```

### Issue: "Server not showing in AI assistant"

**Checklist:**
1. ✅ Is the path absolute in mcp.json?
2. ✅ Did you restart your AI tool?
3. ✅ Is Python in your PATH?
4. ✅ Can you run `python server.py` manually?

**Debug:**
```bash
# Test manually
python /absolute/path/to/server.py

# Check Python path
which python  # macOS/Linux
where python  # Windows
```

### Issue: "Generation fails"

**Steps:**
1. Validate your config first:
   ```javascript
   "Validate this config: {your config}"
   ```

2. Check for common issues:
   - Missing required fields
   - Invalid JSON structure
   - Typos in parameter types

3. Start with a simple example:
   ```javascript
   "Generate example config for tool server"
   ```

### Issue: "Web interface won't start"

**Note:** Auto-port is now enabled by default, so this should rarely happen!

**Solution:**
```bash
# Just run normally - it will auto-find a port
python web_app.py

# Or specify a different port
python web_app.py --port 8080

# Check what's using ports (if needed)
lsof -i :5000  # macOS/Linux
netstat -ano | findstr :5000  # Windows
```

---

## ❓ FAQ

### Q: Do I need to know MCP protocol to use this?
**A:** No! That's the whole point. MCP Generator handles all protocol details for you.

### Q: Can I modify generated servers?
**A:** Absolutely! Generated code is clean, well-documented, and meant to be customized.

### Q: Is it production-ready?
**A:** Generated servers follow best practices and are production-ready, but always test thoroughly.

### Q: Can I generate servers in other languages?
**A:** Currently only Python. Other languages coming soon!

### Q: How do I add my own templates?
**A:** See "Advanced Usage" → "Custom Templates" section.

### Q: Is there a limit to the number of tools/resources?
**A:** No hard limit, but keep it reasonable for maintainability.

### Q: Can I use this commercially?
**A:** Yes! MIT licensed.

### Q: Where can I get help?
**A:**
- GitHub Issues: https://github.com/Ahmet-Ruchan/MCP/issues
- Email: aruchanavci01@gmail.com

---

## 🚀 Next Steps

1. **Try the examples** in this guide
2. **Generate your first server** through AI or web interface
3. **Customize** the generated code for your needs
4. **Share** your creations with the community!

---

## 📝 License

MIT License - See LICENSE file for details

---

## 🙏 Acknowledgments

- Built with MCP (Model Context Protocol)
- Inspired by the need for rapid MCP server development
- Community-driven development

---

**Happy Generating! 🎉**

For more information, visit: https://github.com/Ahmet-Ruchan/MCP
