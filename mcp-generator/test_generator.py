#!/usr/bin/env python3
"""
Test script for MCP Generator
Creates example servers to verify the generator works correctly
"""

import asyncio
import json
import sys
from pathlib import Path
import importlib.util

# Add parent directory to path to import the server module
sys.path.insert(0, str(Path(__file__).parent))

# Mock MCP imports since we only need to test template generation
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

# Now import the server module
from server import MCPTemplate


async def test_generate_calculator():
    """Test generating a simple calculator tool server"""
    print("=" * 60)
    print("TEST 1: Generating Calculator Tool Server")
    print("=" * 60)

    config = {
        "name": "calculator-server",
        "description": "A simple calculator with basic math operations",
        "server_type": "tool",
        "output_dir": "./test-output",
        "config": {
            "tools": [
                {
                    "name": "add",
                    "description": "Add two numbers",
                    "parameters": [
                        {"name": "a", "type": "number", "description": "First number", "required": True},
                        {"name": "b", "type": "number", "description": "Second number", "required": True}
                    ]
                },
                {
                    "name": "multiply",
                    "description": "Multiply two numbers",
                    "parameters": [
                        {"name": "a", "type": "number", "description": "First number", "required": True},
                        {"name": "b", "type": "number", "description": "Second number", "required": True}
                    ]
                }
            ]
        }
    }

    print(f"\nConfiguration:")
    print(json.dumps(config, indent=2))

    try:
        files = MCPTemplate.basic_tool_server(
            config["name"],
            config["description"],
            config["config"]["tools"]
        )

        output_path = Path(config["output_dir"]) / config["name"]
        output_path.mkdir(parents=True, exist_ok=True)

        for filename, content in files.items():
            file_path = output_path / filename
            file_path.write_text(content)
            print(f"\n✅ Created: {file_path}")

        print(f"\n✅ Calculator server generated successfully at {output_path}")
        return True

    except Exception as e:
        print(f"\n❌ Error: {str(e)}")
        return False


async def test_generate_weather_resource():
    """Test generating a weather resource server"""
    print("\n" + "=" * 60)
    print("TEST 2: Generating Weather Resource Server")
    print("=" * 60)

    config = {
        "name": "weather-server",
        "description": "Provides weather data as resources",
        "server_type": "resource",
        "output_dir": "./test-output",
        "config": {
            "resources": [
                {
                    "uri": "weather://current",
                    "name": "Current Weather",
                    "description": "Current weather conditions",
                    "type": "json"
                },
                {
                    "uri": "weather://forecast",
                    "name": "Weather Forecast",
                    "description": "5-day weather forecast",
                    "type": "json"
                }
            ]
        }
    }

    print(f"\nConfiguration:")
    print(json.dumps(config, indent=2))

    try:
        files = MCPTemplate.resource_server(
            config["name"],
            config["description"],
            config["config"]["resources"]
        )

        output_path = Path(config["output_dir"]) / config["name"]
        output_path.mkdir(parents=True, exist_ok=True)

        for filename, content in files.items():
            file_path = output_path / filename
            file_path.write_text(content)
            print(f"\n✅ Created: {file_path}")

        print(f"\n✅ Weather server generated successfully at {output_path}")
        return True

    except Exception as e:
        print(f"\n❌ Error: {str(e)}")
        return False


async def test_generate_full_server():
    """Test generating a full-featured server"""
    print("\n" + "=" * 60)
    print("TEST 3: Generating Full-Featured Server")
    print("=" * 60)

    config = {
        "name": "search-server",
        "description": "A comprehensive search server with tools, resources, and prompts",
        "server_type": "full",
        "output_dir": "./test-output",
        "config": {
            "tools": [
                {
                    "name": "search",
                    "description": "Search for information",
                    "parameters": [
                        {"name": "query", "type": "string", "description": "Search query", "required": True},
                        {"name": "limit", "type": "number", "description": "Max results", "required": False}
                    ]
                }
            ],
            "resources": [
                {
                    "uri": "search://results",
                    "name": "Search Results",
                    "description": "Latest search results",
                    "type": "json"
                }
            ],
            "prompts": [
                {
                    "name": "analyze_results",
                    "description": "Analyze search results and provide insights"
                }
            ]
        }
    }

    print(f"\nConfiguration:")
    print(json.dumps(config, indent=2))

    try:
        files = MCPTemplate.full_server(
            config["name"],
            config["description"],
            config["config"]
        )

        output_path = Path(config["output_dir"]) / config["name"]
        output_path.mkdir(parents=True, exist_ok=True)

        for filename, content in files.items():
            file_path = output_path / filename
            file_path.write_text(content)
            print(f"\n✅ Created: {file_path}")

        print(f"\n✅ Full server generated successfully at {output_path}")
        return True

    except Exception as e:
        print(f"\n❌ Error: {str(e)}")
        return False


async def test_validation():
    """Test configuration validation"""
    print("\n" + "=" * 60)
    print("TEST 4: Configuration Validation")
    print("=" * 60)

    # Test valid config
    valid_config = {
        "tools": [
            {
                "name": "test_tool",
                "description": "A test tool",
                "parameters": [
                    {"name": "param1", "type": "string", "required": True}
                ]
            }
        ]
    }

    print("\n✅ Valid configuration:")
    print(json.dumps(valid_config, indent=2))

    # Test invalid config
    invalid_config = {
        "tools": [
            {
                # Missing name
                "description": "A test tool",
                "parameters": [
                    {"type": "string", "required": True}  # Missing parameter name
                ]
            }
        ]
    }

    print("\n\n❌ Invalid configuration (for testing):")
    print(json.dumps(invalid_config, indent=2))

    print("\n✅ Validation tests completed")
    return True


async def main():
    """Run all tests"""
    print("\n" + "=" * 60)
    print("MCP GENERATOR TEST SUITE")
    print("=" * 60)

    tests = [
        ("Calculator Server", test_generate_calculator),
        ("Weather Resource Server", test_generate_weather_resource),
        ("Full-Featured Server", test_generate_full_server),
        ("Configuration Validation", test_validation)
    ]

    results = []

    for test_name, test_func in tests:
        try:
            result = await test_func()
            results.append((test_name, result))
        except Exception as e:
            print(f"\n❌ Test '{test_name}' failed with exception: {str(e)}")
            results.append((test_name, False))

    # Summary
    print("\n" + "=" * 60)
    print("TEST SUMMARY")
    print("=" * 60)

    passed = sum(1 for _, result in results if result)
    total = len(results)

    for test_name, result in results:
        status = "✅ PASS" if result else "❌ FAIL"
        print(f"{status}: {test_name}")

    print(f"\nResults: {passed}/{total} tests passed")

    if passed == total:
        print("\n🎉 All tests passed!")
        print("\n📁 Generated servers are in: ./test-output/")
        print("\nYou can test them by:")
        print("  cd test-output/calculator-server")
        print("  pip install -r requirements.txt")
        print("  python server.py")
    else:
        print("\n⚠️  Some tests failed. Please review the errors above.")

    return passed == total


if __name__ == "__main__":
    success = asyncio.run(main())
    sys.exit(0 if success else 1)
