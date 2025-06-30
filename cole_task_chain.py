from ghost_env import INFURA_KEY, VAULT_ADDRESS
import os
import json
import requests
from datetime import datetime

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")  # You can replace this with hardcoded key for now
GPT_ENDPOINT = "https://api.openai.com/v1/chat/completions"
INSTALL_ENDPOINT = "http://localhost:5000/install_code"

# === Send GPT a task and return the code ===
def send_task_to_gpt(task_desc):
    print(f"[Chain] Sending task to GPT: {task_desc}")

    headers = {
        "Authorization": f"Bearer {OPENAI_API_KEY}",
        "Content-Type": "application/json"
    }

    body = {
        "model": "gpt-4",
        "messages": [
            {"role": "system", "content": "You are a Python coding assistant. Respond only with clean, functional Python code for integration into a trading assistant bot."},
            {"role": "user", "content": f"Generate Python code for the following task:\n\n{task_desc}"}
        ],
        "temperature": 0.3
    }

    response = requests.post(GPT_ENDPOINT, headers=headers, json=body)
    result = response.json()

    if "choices" in result:
        code = result["choices"][0]["message"]["content"]
        return code
    else:
        print("[Chain] GPT failed:", result)
        return None

# === Install code directly into PTM ===
def install_code_file(filename, code):
    payload = {
        "filename": filename,
        "code": code
    }

    response = requests.post(INSTALL_ENDPOINT, json=payload)
    return response.json()

# === Run the full task chain ===
def run_task_chain(task_desc, filename):
    code = send_task_to_gpt(task_desc)
    if not code:
        return {"status": "error", "message": "GPT returned no code."}

    print("[Chain] Installing code...")
    result = install_code_file(filename, code)
    return result

def log_event():ef drop_files_to_bridge():