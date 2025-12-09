import requests

url = "https://my-fastmcp-server.herokuapp.com/mcp/tool/add"
payload = {"a": 3, "b": 5}

response = requests.post(url, json=payload)
if response.status_code == 200:
    print("Result:", response.json()["result"])
else:
    print("Error:", response.status_code, response.text)
