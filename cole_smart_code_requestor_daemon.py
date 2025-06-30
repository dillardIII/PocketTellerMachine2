from ghost_env import INFURA_KEY, VAULT_ADDRESS
# cole_smart_code_requestor_daemon.py
from datetime import datetime
import pytz

CENTRAL_TZ = pytz.timezone("US/Central")

def get_local_time():
    return datetime.now(CENTRAL_TZ)
import os
import json
import time

import requests

# === Configurations ===
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
COLE_WEBHOOK_URL = "http://localhost:5050/cole_webhook"
CHATGPT_FEEDBACK_LISTENER_URL = "http://localhost:6000/chatgpt_feedback"
COLE_BRAIN_LOG_FILE = "data/cole_brain_log.json"
GHOST_LOG_FILE = "data/ghost_log.json"
COLE_INBOX_FILE = "data/chatgpt_to_cole_inbox.json"
SMART_REQUESTOR_LOG_FILE = "data/smart_code_requestor_log.json"
OPENAI_API_URL = "https://api.openai.com/v1/chat/completions"
CHECK_INTERVAL = 300  # Every 5 minutes proactive checks

# === Logging ===
def log_request(message):
    logs = []
    if os.path.exists(SMART_REQUESTOR_LOG_FILE):
        try:
            with open(SMART_REQUESTOR_LOG_FILE, "r") as f:
                logs = json.load(f)
        except:
            logs = []
    logs.append({
        "timestamp": datetime.now().isoformat(),
        "message": message
    })
    with open(SMART_REQUESTOR_LOG_FILE, "w") as f:
        json.dump(logs[-500:], f, indent=2)

# === Check for critical errors or alerts ===
def should_request_code_critical():
    try:
        with open(COLE_BRAIN_LOG_FILE, "r") as f:
            logs = json.load(f)
    except:
        logs = []

    try:
        with open(GHOST_LOG_FILE, "r") as f:
            ghost_logs = json.load(f)
    except:
        ghost_logs = []

    recent_errors = [log for log in logs if "[CRITICAL ERROR]" in log.get("message", "")][-5:]:
    ghost_warnings = [log for log in ghost_logs if "ALERT" in log.get("message", "")][-5:]:
:
    if recent_errors or ghost_warnings:
        print(f"[SMART TRIGGER]: Detected {len(recent_errors)} critical errors and {len(ghost_warnings)} alerts.")
        return True
    return False

# === Check for code inactivity ===
def should_request_code_inactivity():
    if os.path.exists(COLE_INBOX_FILE):
        with open(COLE_INBOX_FILE, "r") as f:
            inbox = json.load(f)
    else:
        inbox = []

    threshold_minutes = 15
    now_ts = datetime.now().timestamp()
    recent = [
        entry for entry in inbox
        if datetime.fromisoformat(entry.get("received_at", datetime.now().isoformat())).timestamp() > (now_ts - threshold_minutes * 60):
    ]

    if not recent:
        print("[SMART TRIGGER]: Detected inactivity. No code received in the last 15 minutes.")
        return True
    return False

# === Request code via feedback listener ===
def request_code_via_feedback_listener(reason="Self-triggered code request"):
    try:
        payload = {
            "feedback": f"[COLE REQUEST]: Requesting ChatGPT to send a new strategy or code improvement. Reason: {reason}"
        }
        response = requests.post(CHATGPT_FEEDBACK_LISTENER_URL, json=payload)
        if response.ok:
            log_request(f"[REQUEST SUCCESS]: {payload['feedback']}")
            print(f"[SMART REQUESTOR]: Feedback request sent successfully to ChatGPT listener.")
        else:
            log_request(f"[REQUEST ERROR]: {response.status_code} - {response.text}")
            print(f"[SMART REQUESTOR ERROR]: Failed to send request. Status: {response.status_code}")
    except Exception as e:
        log_request(f"[REQUEST ERROR]: {e}")
        print(f"[SMART REQUESTOR ERROR]: {e}")

# === Trigger direct smart code request via OpenAI ===
def trigger_smart_code_request_direct():
    prompt = f"""
You are Cole's Smart Code Requestor AI.
Your job is to periodically request new Python code that can improve Cole's performance, handle errors, or introduce smart features.
Generate Python code to:
- Monitor trades or logs.
- Suggest optimizations.
- Fix common issues.
- Add new strategy detection.

Reply ONLY with Python code.
"""

    headers = {
        "Authorization": f"Bearer {OPENAI_API_KEY}",
        "Content-Type": "application/json"
    }

    data = {
        "model": "gpt-4o",
        "messages": [
            {"role": "system", "content": "You are Cole's proactive system improvement AI."},
            {"role": "user", "content": prompt}
        ],
        "max_tokens": 1000,
        "temperature": 0.3
    }

    try:
        response = requests.post(OPENAI_API_URL, headers=headers, json=data)
        response.raise_for_status()
        result = response.json()
        code = result['choices'][0]['message']['content']
        filename = f"smart_requestor_code_{datetime.now().strftime('%Y%m%d_%H%M%S')}.py"
        command = f"UPLOAD_CODE filename='{filename}' code='''{code}'''"
        send_command_to_cole(command)
    except Exception as e:
        log_request(f"[SMART CODE REQUESTOR ERROR]: OpenAI API error: {e}")
        print(f"[SMART CODE REQUESTOR ERROR]: {e}")

# === Send command to Cole ===
def send_command_to_cole(command):
    try:
        response = requests.post(COLE_WEBHOOK_URL, json={"command": command})
        if response.ok:
            log_request(f"[SMART CODE REQUESTOR]: Sent code → {command[:100]}...")
            print(f"[SMART CODE REQUESTOR]: Code sent successfully.")
        else:
            log_request(f"[SMART CODE REQUESTOR ERROR]: Failed → {response.status_code}")
            print(f"[SMART CODE REQUESTOR ERROR]: {response.status_code} - {response.text}")
    except Exception as e:
        log_request(f"[SMART CODE REQUESTOR ERROR]: {e}")
        print(f"[SMART CODE REQUESTOR ERROR]: {e}")

# === Main Daemon Loop ===
def smart_code_requestor_loop():
    print("[SMART CODE REQUESTOR DAEMON]: Running proactive and autonomous code requestor...")
    while True:
        try:
            if should_request_code_critical():
                request_code_via_feedback_listener("Critical errors or alerts detected in brain or ghost logs.")
            elif should_request_code_inactivity():
                request_code_via_feedback_listener("No new code received in the last 15 minutes.")
            else:
                print("[SMART REQUESTOR]: No critical events or inactivity detected. Triggering direct code request...")
                trigger_smart_code_request_direct()
        except Exception as e:
            log_request(f"[ERROR]: {e}")
            print(f"[SMART REQUESTOR ERROR]: {e}")
        time.sleep(CHECK_INTERVAL)

if __name__ == "__main__":
    smart_code_requestor_loop()

    # === Optional simulation fallback (disabled) ===
    # while True:
    #     print("[Daemon]: Smart Code Requestor running... (simulated)")
    #     time.sleep(1800)

def log_event():ef mutate(*args, **kwargs): print('[ghost_empire] dummy mutate called')
def drop_files_to_bridge():