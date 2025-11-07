from fastmcp import FastMCP

mcp = FastMCP(name="calculator")

@mcp.tool
def multiply(a: float, b: float) -> float:
    return a * b

@mcp.tool(
    name = "add",
    description = "Add two numbers",
    tags = ["math", "addition"]
)
def add_numbers(a: float, b: float) -> float:
    return a + b

@mcp.tool
def subtract_numbers(a: float, b: float) -> float:
    return a - b

@mcp.tool
def multiply(a: float, b: float) -> float:
    return a * b

@mcp.tool
def divide(a: float, b: float) -> float:
    return a / b

if __name__ == "__main__":
    mcp.run()
    