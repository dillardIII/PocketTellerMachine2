# cole_tools/cole_auto_feedback_sender.py

import requests
import json
import os
from datetime import datetime

FEEDBACK_LOG_FILE = "data/cole_auto_feedback_log.json"
FEEDBACK_ENDPOINT = "http://localhost:6000/chatgpt_feedback"  # Change to your ChatGPT or webhook listener endpoint

def log_feedback(message):
    logs = []
    if os.path.exists(FEEDBACK_LOG_FILE):
        try:
            with open(FEEDBACK_LOG_FILE, "r") as f:
                logs = json.load(f)
        except:
            logs = []
    logs.append({"timestamp": datetime.now().isoformat(), "message": message})
    with open(FEEDBACK_LOG_FILE, "w") as f:
        json.dump(logs[-500:], f, indent=2)

def send_feedback(status, content, extra=None):
    payload = {
        "status": status,
        "content": content,
        "timestamp": datetime.now().isoformat(),
    }
    if extra:
        payload["extra"] = extra

    try:
        response = requests.post(FEEDBACK_ENDPOINT, json=payload, timeout=5)
        if response.status_code == 200:
            log_feedback(f"[FEEDBACK]: Sent successfully → {payload}")
        else:
            log_feedback(f"[FEEDBACK ERROR]: HTTP {response.status_code} → {response.text}")
    except Exception as e:
        log_feedback(f"[FEEDBACK ERROR]: {e}")