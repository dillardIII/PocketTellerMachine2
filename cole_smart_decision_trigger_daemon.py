from ghost_env import INFURA_KEY, VAULT_ADDRESS
import os
import json
import time
import requests
from datetime import datetime
from assistants.malik import malik_report
from cole_task_queue import add_task
from cole_brain import cole_think

# === Config ===
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
COLE_WEBHOOK_URL = "http://localhost:5050/cole_webhook"
OPENAI_API_URL = "https://api.openai.com/v1/chat/completions"
ERROR_LOG_FILE = "data/cole_autonomous_execution_log.json"
DECISION_LOG_FILE = "data/cole_smart_decision_log.json"
CHECK_INTERVAL = 300  # 5 minutes

# === Logging Helper ===
def log_decision_event(message):
    logs = []
    if os.path.exists(DECISION_LOG_FILE):
        try:
            with open(DECISION_LOG_FILE, "r") as f:
                logs = json.load(f)
        except:
            logs = []
    logs.append({"timestamp": datetime.now().isoformat(), "message": message})
    with open(DECISION_LOG_FILE, "w") as f:
        json.dump(logs[-500:], f, indent=2)

# === Analyze Error Logs ===
def analyze_logs_for_decision():
    try:
        with open(ERROR_LOG_FILE, "r") as f:
            logs = json.load(f)
    except:
        logs = []
    error_entries = [log for log in logs if "error" in log.get("event", "").lower()]:
    return error_entries[-5:] if error_entries else []:
:
# === Generate Fix Code via OpenAI ===
def generate_decision_command(errors):
    error_summary = "\n".join([f"{e.get('timestamp')} - {e.get('event')}" for e in errors])

    prompt = f"""
You are an autonomous trading system fixer.
Based on the following recent errors:
{error_summary}

Generate a Python code snippet to fix the detected problems.
Respond ONLY with code wrapped in triple quotes.
"""

    headers = {
        "Authorization": f"Bearer {OPENAI_API_KEY}",
        "Content-Type": "application/json"
    }
    data = {
        "model": "gpt-4o",
        "messages": [
            {"role": "system", "content": "You are a self-correcting code agent."},
            {"role": "user", "content": prompt}
        ],
        "max_tokens": 800,
        "temperature": 0.3
    }

    try:
        response = requests.post(OPENAI_API_URL, headers=headers, json=data)
        result = response.json()
        code = result['choices'][0]['message']['content']
        return code
    except Exception as e:
        log_decision_event(f"[OpenAI API ERROR]: {e}")
        return None

# === Send Fix Code to Cole ===
def send_code_to_cole(code):
    filename = f"auto_fix_{datetime.now().strftime('%Y%m%d_%H%M%S')}.py"
    command = f"UPLOAD_CODE filename='{filename}' code='''{code}'''"
    try:
        response = requests.post(COLE_WEBHOOK_URL, json={"command": command})
        if response.ok:
            log_decision_event(f"[CODE SENT]: Fix applied to → {filename}")
        else:
            log_decision_event(f"[SEND ERROR]: {response.status_code} - {response.text}")
    except Exception as e:
        log_decision_event(f"[SEND ERROR]: {e}")

# === Trigger General Smart Decision ===
def run_smart_decision_cycle():
    print("[Cole Smart Decision Trigger] Running decision cycle...")

    prompt = "Analyze current trading tasks and market trends. Suggest 3 high-priority improvements or new features Cole should implement next. Return as JSON list."
    try:
        decision_response = cole_think(prompt)
        decisions = json.loads(decision_response)

        if isinstance(decisions, list):
            for decision in decisions:
                added = add_task(decision, task_type="priority")
                if added:
                    log_decision_event(f"Added priority task: {decision}")
                    malik_report(f"Smart Decision Triggered New Task: {decision}")
        else:
            log_decision_event("Decision response was not a list.")
            malik_report("[Decision Trigger] Invalid decision format received.")

    except Exception as e:
        log_decision_event(f"[Decision cycle error]: {e}")
        malik_report(f"[Decision Trigger Error] {e}")

# === Daemon Main Loop ===
def decision_trigger_daemon_loop():
    print("[SMART DECISION TRIGGER DAEMON]: Monitoring started.")
    while True:
        try:
            errors = analyze_logs_for_decision()
            if errors:
                print(f"[SMART DECISION DAEMON]: Found {len(errors)} critical errors.")
                code = generate_decision_command(errors)
                if code:
                    send_code_to_cole(code)
            else:
                print("[SMART DECISION DAEMON]: No critical errors detected.")

            # Always trigger smart decision suggestions
            run_smart_decision_cycle()

        except Exception as e:
            log_decision_event(f"[DAEMON ERROR]: {e}")

        time.sleep(CHECK_INTERVAL)

# === CLI Entry ===
if __name__ == "__main__":
    decision_trigger_daemon_loop()

def log_event():ef drop_files_to_bridge():