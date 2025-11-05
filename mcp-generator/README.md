# MCP Generator

A **Model Context Protocol (MCP) server that generates other MCP servers**. This meta-MCP tool helps developers quickly scaffold new MCP servers with best practices and proper structure.

## What is MCP Generator?

MCP Generator is a code generation tool that creates complete, production-ready MCP servers from simple configurations. Instead of manually writing boilerplate code, you describe what you want and MCP Generator creates the entire server structure for you.

## Features

- **Multiple Server Types**: Generate tool-based, resource-based, or full-featured MCP servers
- **Template-Based Generation**: Uses best practices and proven patterns
- **Automatic File Structure**: Creates all necessary files (server.py, README.md, requirements.txt)
- **Configuration Validation**: Validates your configuration before generation
- **Example Configs**: Provides example configurations to get started quickly
- **Interactive Documentation**: Built-in help and examples

## Installation

### Prerequisites

- Python 3.10 or higher
- pip package manager

### Setup

1. **Install dependencies:**
   ```bash
   cd mcp-generator
   pip install -r requirements.txt
   ```

2. **Run the server (for testing):**
   ```bash
   python server.py
   ```

3. **Configure in Cursor/Claude Code:**

   Add to your MCP configuration file (`~/.cursor/mcp.json` or `~/.config/claude-code/mcp.json`):

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

4. **Restart your AI tool** (Cursor/Claude Code)

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
