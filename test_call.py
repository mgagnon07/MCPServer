import asyncio
from server import add, get_weather  # import the FunctionTool objects

async def main():
    # Call the 'add' tool
    add_result = await add.run({"a": 3, "b": 5})
    print("Add result:", add_result)  # <-- run() returns the value directly

    # Call the 'get_weather' tool
    weather_result = await get_weather.run({"city": "Boston"})
    print("Weather:", weather_result.content)  # <-- run() returns the value directly

asyncio.run(main())