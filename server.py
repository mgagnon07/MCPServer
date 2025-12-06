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

# Get the port from Heroku, default to 8000 for local testing
port = int(os.environ.get("PORT", 8000))

mcp = FastMCP("My Server")

@mcp.tool
def add(a: int, b: int) -> int:
    return a + b

@mcp.tool
def get_weather(city: str, units: str = "celsius") -> dict:
    return {"temp": 22, "city": city, "units": units}

if __name__ == "__main__":
    # Run the server on all interfaces for Heroku, with the correct port
    mcp.run(host="0.0.0.0", port=port, transport="http")
