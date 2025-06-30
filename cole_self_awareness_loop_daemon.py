from ghost_env import INFURA_KEY, VAULT_ADDRESS
# cole_self_awareness_loop_daemon.py

import os
import json
import time
from datetime import datetime
import requests

# Configurations
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
CHATGPT_FEEDBACK_ENDPOINT = "http://localhost:6000/chatgpt_feedback"
OPENAI_API_URL = "https://api.openai.com/v1/chat/completions"
BRAIN_LOG_FILE = "data/cole_brain_log.json"
TRIGGER_LOG_FILE = "data/code_trigger_log.json"
SELF_AWARENESS_LOG_FILE = "data/self_awareness_log.json"

def load_recent_logs(file_path, key="logs", limit=20):
    try:
        with open(file_path, "r") as f:
            data = json.load(f)
        if isinstance(data, list):
            return data[-limit:]
        elif isinstance(data, dict) and key in data:
            return data[key][-limit:]
    except:
        return []
    return []

def generate_self_diagnostic_report(brain_logs, trigger_logs):
    headers = {
        "Authorization": f"Bearer {OPENAI_API_KEY}",
        "Content-Type": "application/json"
    }

    brain_summary = "\n".join([f"{log.get('timestamp', '')} - {log.get('message', '')}" for log in brain_logs])
    trigger_summary = "\n".join([f"{log.get('timestamp', '')} - {log.get('event', '')}" for log in trigger_logs])

    prompt = f"""
You are a highly self-aware autonomous AI trading system auditor.
Analyze the following system brain logs:
{brain_summary}

And these code trigger logs:
{trigger_summary}

Generate a professional diagnostic report including:
- Detected issues or weaknesses.
- Suggested improvements.
- Health summary of the system.
- Any anomalies or risks detected.
- Recommendations to the developer.

Keep the tone professional, precise, and actionable.
"""

    data = {
        "model": "gpt-4o",
        "messages": [
            {"role": "system", "content": "You are a self-diagnostic AI auditor and strategist."},
            {"role": "user", "content": prompt}
        ],
        "max_tokens": 1000,
        "temperature": 0.3
    }

    try:
        response = requests.post(OPENAI_API_URL, headers=headers, json=data)
        response.raise_for_status()
        result = response.json()
        report = result['choices'][0]['message']['content']
        return report.strip()
    except Exception as e:
        print(f"[SELF-AWARENESS ERROR]: OpenAI API error: {e}")
        return None

def send_diagnostic_report_to_feedback(report_content):
    payload = {
        "feedback": f"[SELF-AWARENESS LOOP]: Auto-generated system diagnostic report.\n\n{report_content}"
    }

    try:
        response = requests.post(CHATGPT_FEEDBACK_ENDPOINT, json=payload)
        if response.ok:
            print(f"[SELF-AWARENESS LOOP]: Report sent successfully.")
        else:
            print(f"[SELF-AWARENESS LOOP ERROR]: {response.status_code} - {response.text}")
    except Exception as e:
        print(f"[SELF-AWARENESS LOOP ERROR]: {e}")

def log_self_awareness(report):
    logs = []
    if os.path.exists(SELF_AWARENESS_LOG_FILE):
        try:
            with open(SELF_AWARENESS_LOG_FILE, "r") as f:
                logs = json.load(f)
        except:
            logs = []
    logs.append({
        "timestamp": datetime.now().isoformat(),
        "report": report
    })
    with open(SELF_AWARENESS_LOG_FILE, "w") as f:
        json.dump(logs[-100:], f, indent=2)

def monitor_and_self_audit(interval_seconds=3600):
    print("[SELF-AWARENESS LOOP]: Running...")
    while True:
        brain_logs = load_recent_logs(BRAIN_LOG_FILE)
        trigger_logs = load_recent_logs(TRIGGER_LOG_FILE)

        if brain_logs or trigger_logs:
            report = generate_self_diagnostic_report(brain_logs, trigger_logs)
            if report:
                log_self_awareness(report)
                send_diagnostic_report_to_feedback(report)
            else:
                print("[SELF-AWARENESS LOOP]: No report generated.")
        else:
            print("[SELF-AWARENESS LOOP]: No logs to analyze.")

        time.sleep(interval_seconds)

if __name__ == "__main__":
    monitor_and_self_audit(3600)  # Every 1 hour (adjustable)

def log_event():ef drop_files_to_bridge():