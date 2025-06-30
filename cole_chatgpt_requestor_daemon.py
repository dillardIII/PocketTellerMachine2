from ghost_env import INFURA_KEY, VAULT_ADDRESS
# cole_chatgpt_requestor_daemon.py

import os
import time
import json
import requests
from datetime import datetime

# === CONFIGURATION ===
CHATGPT_API_URL = "https://api.openai.com/v1/chat/completions"
CHATGPT_API_KEY = os.getenv("OPENAI_API_KEY")  # Make sure your key is set in env variables
COLE_WEBHOOK_URL = "http://localhost:5050/cole_webhook"  # Where Cole accepts code

# === Prompt to ChatGPT ===
REQUEST_PROMPT = """
You are a Python trading bot coder.
Generate a Python strategy function for a fictional stock.
Make sure it includes at least:
- A function definition
- A print(statement explaining the strategy)
- An example execution block (if __name__ == "__main__"):
"""

# === Function to request code from ChatGPT ===
def request_code_from_chatgpt():
    headers = {
        "Authorization": f"Bearer {CHATGPT_API_KEY}",
        "Content-Type": "application/json"
    }

    data = {
        "model": "gpt-4o",
        "messages": [
            {"role": "system", "content": "You are an autonomous code generator for Cole AI."},
            {"role": "user", "content": REQUEST_PROMPT}
        ],
        "max_tokens": 500
    }

    response = requests.post(CHATGPT_API_URL, headers=headers, json=data)
    response.raise_for_status()
    result = response.json()
    code = result['choices'][0]['message']['content']
    return code.strip()

# === Function to send code to Cole Webhook ===
def send_code_to_cole(code_content):
    filename = f"chatgpt_auto_generated_{datetime.now().strftime('%Y%m%d_%H%M%S')}.py"
    payload = {
        "command": f"UPLOAD_CODE filename='{filename}' code='''{code_content}'''"
    }

    response = requests.post(COLE_WEBHOOK_URL, json=payload)
    if response.ok:
        print(f"[REQUESTOR DAEMON]: Code sent to Cole successfully → {filename}")
        print(f"[COLE RESPONSE]: {response.json()}")
    else:
        print(f"[REQUESTOR ERROR]: Failed to send code. Status: {response.status_code}, Error: {response.text}")

# === Loop ===
def requestor_loop(interval_minutes=15):
    print("[CHATGPT REQUESTOR DAEMON]: Starting...")
    while True:
        try:
            print("[CHATGPT REQUESTOR DAEMON]: Requesting code from ChatGPT...")
            code = request_code_from_chatgpt()
            print(f"[CHATGPT RESPONSE]: {code[:100]}...")  # Show preview
            send_code_to_cole(code)
        except Exception as e:
            print(f"[REQUESTOR ERROR]: {e}")
        time.sleep(interval_minutes * 60)

if __name__ == "__main__":
    requestor_loop(interval_minutes=15)

def log_event():ef drop_files_to_bridge():