import requests

url = "http://localhost:5050/cole_webhook"  # Change 'localhost' to your actual server IP if remote
payload = {
    "command": "status check"
}

response = requests.post(url, json=payload)
print("[RESPONSE]:", response.status_code)
print(response.json())