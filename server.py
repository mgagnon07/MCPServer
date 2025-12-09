'''
from fastmcp import FastMCP

mcp = FastMCP("My Server")

@mcp.tool
def add(a: int, b: int) -> int:
    return a + b

@mcp.tool
def get_weather(city: str, units: str = "celsius") -> dict:
    return {"temp": 22, "city": city, "units": units}

if __name__ == "__main__":
    mcp.run(transport="http", host="127.0.0.1", port=8000)
'''

import os
from fastmcp import FastMCP

# Use PORT environment variable if set, otherwise default to 8000
port = int(os.environ.get("PORT", 8000))

# Create MCP server
mcp = FastMCP("My Server")

# Tool 1: add two numbers
@mcp.tool
def add(a: int, b: int) -> int:
    return a + b

# Tool 2: get dummy weather
@mcp.tool
def get_weather(city: str, units: str = "celsius") -> dict:
    return {"temp": 22, "city": city, "units": units}

if __name__ == "__main__":
    # Run server on all interfaces
    # transport="http" is fine for EC2
    mcp.run(host="0.0.0.0", port=port, transport="http")
