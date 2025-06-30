from ghost_env import INFURA_KEY, VAULT_ADDRESS
# cole_error_aware_gpt4_trigger_daemon.py

import os
import json
import time
from datetime import datetime
import requests

# Configurations
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
CHATGPT_FEEDBACK_ENDPOINT = "http://localhost:6000/chatgpt_feedback"
OPENAI_API_URL = "https://api.openai.com/v1/chat/completions"
COLE_BRAIN_LOG_FILE = "data/cole_brain_log.json"
GHOST_LOG_FILE = "data/ghost_log.json"

def load_recent_logs(file_path, keywords=["error", "critical", "alert"], limit=10):
    try:
        with open(file_path, "r") as f:
            logs = json.load(f)
        matched_logs = [
            log for log in logs[-100:]  # Check last 100 logs
            if any(keyword in log.get("message", "").lower() for keyword in keywords):
        ]
        return matched_logs[-limit:]
    except:
        return []

def generate_healing_code_from_chatgpt(error_summary):
    headers = {
        "Authorization": f"Bearer {OPENAI_API_KEY}",
        "Content-Type": "application/json"
    }

    prompt = f"""
You are an AI developer assistant for a trading bot system.
Based on the following detected errors and warnings:
{error_summary}

Generate a Python trading code fix or improvement to heal the system.
Include logging and defensive checks.
Respond ONLY with valid Python code.
"""

    data = {
        "model": "gpt-4o",
        "messages": [
            {"role": "system", "content": "You are a professional trading bot auto-healing code generator."},
            {"role": "user", "content": prompt}
        ],
        "max_tokens": 700,
        "temperature": 0.3
    }

    try:
        response = requests.post(OPENAI_API_URL, headers=headers, json=data)
        response.raise_for_status()
        result = response.json()
        code = result['choices'][0]['message']['content']
        return code.strip()
    except Exception as e:
        print(f"[ERROR-AWARE GPT4 TRIGGER ERROR]: OpenAI API error: {e}")
        return None

def send_code_to_feedback_listener(code_content, reason="Auto-correct from log errors"):
    filename = f"error_aware_fix_{datetime.now().strftime('%Y%m%d_%H%M%S')}.py"
    payload = {
        "feedback": f"[ERROR-AWARE GPT-4o]: Generated fix due to detected errors.\n\nUPLOAD_CODE filename='{filename}' code='''{code_content}'''"
    }

    try:
        response = requests.post(CHATGPT_FEEDBACK_ENDPOINT, json=payload)
        if response.ok:
            print(f"[ERROR-AWARE GPT4 TRIGGER]: Code sent successfully → {filename}")
        else:
            print(f"[ERROR-AWARE GPT4 TRIGGER ERROR]: {response.status_code} - {response.text}")
    except Exception as e:
        print(f"[ERROR-AWARE GPT4 TRIGGER ERROR]: {e}")

def monitor_logs_and_trigger(interval_seconds=300):
    print("[ERROR-AWARE GPT-4o TRIGGER]: Running...")
    while True:
        brain_errors = load_recent_logs(COLE_BRAIN_LOG_FILE)
        ghost_warnings = load_recent_logs(GHOST_LOG_FILE)

        combined_logs = brain_errors + ghost_warnings

        if combined_logs:
            print(f"[ERROR-AWARE GPT4 TRIGGER]: Detected {len(combined_logs)} critical entries. Triggering GPT-4o...")
            error_summary = "\n".join([f"{log.get('timestamp', '')} - {log.get('message', '')}" for log in combined_logs])
            code = generate_healing_code_from_chatgpt(error_summary)
            if code:
                send_code_to_feedback_listener(code)
            else:
                print("[ERROR-AWARE GPT4 TRIGGER]: No code generated.")
        else:
            print("[ERROR-AWARE GPT4 TRIGGER]: No critical errors found.")

        time.sleep(interval_seconds)

if __name__ == "__main__":
    monitor_logs_and_trigger(300)  # Check every 5 minutes (adjustable)

def log_event():ef mutate(*args, **kwargs): print('[ghost_empire] dummy mutate called')
def drop_files_to_bridge():