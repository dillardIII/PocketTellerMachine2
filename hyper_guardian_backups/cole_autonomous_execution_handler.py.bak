import os
import json
import time
import requests
from datetime import datetime
from threading import Thread
from cole_command_interpreter import cole_interpret_command
from cole_trade_decision_engine import evaluate_trade_decision
from assistants.malik import malik_report

# === Config ===
INBOX_FILE = "data/chatgpt_to_cole_inbox.json"
AUTONOMOUS_LOG_FILE = "data/cole_autonomous_execution_log.json"
EXECUTION_LOG_FILE = "data/cole_execution_log.json"
WATCHLIST_FILE = "data/cole_watchlist.json"
COLE_WEBHOOK_URL = "http://localhost:5050/cole_webhook"
CHECK_INTERVAL = 600  # 10 minutes

os.makedirs("data", exist_ok=True)

# === Logging ===
def log_autonomous_execution(entry):
    logs = []
    if os.path.exists(AUTONOMOUS_LOG_FILE):
        try:
            with open(AUTONOMOUS_LOG_FILE, "r") as f:
                logs = json.load(f)
        except:
            logs = []
    logs.append(entry)
    with open(AUTONOMOUS_LOG_FILE, "w") as f:
        json.dump(logs[-500:], f, indent=2)

def log_execution(result):
    logs = []
    if os.path.exists(EXECUTION_LOG_FILE):
        try:
            with open(EXECUTION_LOG_FILE, "r") as f:
                logs = json.load(f)
        except:
            logs = []
    logs.append(result)
    with open(EXECUTION_LOG_FILE, "w") as f:
        json.dump(logs[-500:], f, indent=2)

# === Extract code from command ===
def extract_code_from_command(command_text):
    if "UPLOAD_CODE" in command_text:
        try:
            filename_part = command_text.split("filename='")[1].split("'")[0]
            code_part = command_text.split("code='''")[1].split("'''")[0]
            return filename_part, code_part
        except:
            return None, None
    return None, None

# === Execute received code ===
def execute_code(code, filename):
    try:
        exec_globals = {}
        exec(code, exec_globals)
        log_autonomous_execution({
            "timestamp": datetime.now().isoformat(),
            "type": "code_execution",
            "filename": filename,
            "result": "success"
        })
        print(f"[EXECUTION]: Successfully executed {filename}")
    except Exception as e:
        log_autonomous_execution({
            "timestamp": datetime.now().isoformat(),
            "type": "code_execution",
            "filename": filename,
            "error": str(e)
        })
        print(f"[EXECUTION ERROR]: {e}")

# === Process incoming commands ===
def process_inbox():
    print("[AUTONOMOUS EXECUTION HANDLER]: Running inbox handler loop...")
    while True:
        try:
            if os.path.exists(INBOX_FILE):
                with open(INBOX_FILE, "r") as f:
                    inbox = json.load(f)
            else:
                inbox = []

            for entry in inbox:
                if entry.get("executed", False):
                    continue

                command_text = entry.get("command")
                if not command_text:
                    continue

                filename, code = extract_code_from_command(command_text)
                if filename and code:
                    print(f"[HANDLER]: Executing received code file → {filename}")
                    execute_code(code, filename)
                else:
                    print(f"[HANDLER]: Executing general command → {command_text}")
                    try:
                        result = cole_interpret_command(command_text)
                        log_autonomous_execution({
                            "timestamp": datetime.now().isoformat(),
                            "type": "command_execution",
                            "command": command_text,
                            "result": result
                        })
                        print(f"[EXECUTION RESULT]: {result}")
                    except Exception as e:
                        log_autonomous_execution({
                            "timestamp": datetime.now().isoformat(),
                            "type": "command_execution",
                            "command": command_text,
                            "error": str(e)
                        })
                        print(f"[EXECUTION ERROR]: {e}")

                entry["executed"] = True
                entry["executed_at"] = datetime.now().isoformat()

            with open(INBOX_FILE, "w") as f:
                json.dump(inbox, f, indent=2)

        except Exception as e:
            log_autonomous_execution({
                "timestamp": datetime.now().isoformat(),
                "type": "system_error",
                "error": str(e)
            })
            print(f"[HANDLER ERROR]: {e}")

        time.sleep(30)

# === Periodic trigger autonomous task ===
def trigger_autonomous_execution_task():
    command = "EXECUTE_AUTONOMOUS_TASK"
    try:
        response = requests.post(COLE_WEBHOOK_URL, json={"command": command})
        if response.ok:
            log_autonomous_execution({
                "timestamp": datetime.now().isoformat(),
                "type": "autonomous_task_trigger",
                "message": f"Sent execution command → {command}"
            })
            print(f"[AUTONOMOUS HANDLER]: Command executed → {command}")
        else:
            log_autonomous_execution({
                "timestamp": datetime.now().isoformat(),
                "type": "autonomous_task_trigger",
                "message": f"Failed → {response.status_code}"
            })
            print(f"[AUTONOMOUS HANDLER ERROR]: Failed with status {response.status_code}")
    except Exception as e:
        log_autonomous_execution({
            "timestamp": datetime.now().isoformat(),
            "type": "autonomous_task_trigger",
            "error": str(e)
        })
        print(f"[AUTONOMOUS HANDLER ERROR]: {e}")

# === Watchlist Trade Decision Evaluation ===
def load_watchlist():
    if os.path.exists(WATCHLIST_FILE):
        try:
            with open(WATCHLIST_FILE, "r") as f:
                return json.load(f)
        except:
            print("[Execution Handler] Failed to load watchlist.")
    return []

def cole_autonomous_execution_cycle():
    print("[Execution Handler] Running autonomous trade evaluation...")

    watchlist = load_watchlist()
    if not watchlist:
        print("[Execution Handler] Watchlist is empty.")
        return

    for ticker in watchlist:
        decision = evaluate_trade_decision(ticker)
        log_execution(decision)

    malik_report(f"Execution cycle completed for {len(watchlist)} tickers.")

# === Main Loop ===
def autonomous_execution_loop():
    print("[AUTONOMOUS EXECUTION HANDLER]: Running task trigger loop...")
    while True:
        try:
            trigger_autonomous_execution_task()
            cole_autonomous_execution_cycle()
        except Exception as e:
            log_autonomous_execution({
                "timestamp": datetime.now().isoformat(),
                "type": "autonomous_task_trigger_error",
                "error": str(e)
            })
        time.sleep(CHECK_INTERVAL)

if __name__ == "__main__":
    Thread(target=process_inbox).start()
    Thread(target=autonomous_execution_loop).start()