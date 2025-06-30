from ghost_env import INFURA_KEY, VAULT_ADDRESS
import os
import json
from datetime import datetime
from assistants.malik import malik_report

# === Config ===
LOG_FILE = "data/cole_event_log.json"
os.makedirs("data", exist_ok=True)

# === Core Logger ===
def log_event(event_type, source, message, notify=True):
    log_entry = {
        "timestamp": datetime.now().isoformat(),
        "type": event_type.upper(),
        "source": source,
        "message": message
    }

    # Append to JSON log file
    logs = []
    if os.path.exists(LOG_FILE):
        try:
            with open(LOG_FILE, "r") as f:
                logs = json.load(f)
        except:
            logs = []

    logs.append(log_entry)
    with open(LOG_FILE, "w") as f:
        json.dump(logs[-1000:], f, indent=2)

    # Console Output
    print(f"[{log_entry['type']}] {source}: {message}")

    # Optional Malik Report
    if notify and event_type.lower() in ["warning", "error", "critical", "recovery"]:
        malik_report(f"[{log_entry['type']}] {source}: {message}")

# === Quick Helpers ===
def log_info(source, message, notify=False):
    log_event("info", source, message, notify)

def log_warning(source, message, notify=True):
    log_event("warning", source, message, notify)

def log_error(source, message, notify=True):
    log_event("error", source, message, notify)

def log_critical(source, message, notify=True):
    log_event("critical", source, message, notify)

def log_recovery(source, message, notify=True):
    log_event("recovery", source, message, notify)

# === CLI Test ===
if __name__ == "__main__":
    log_info("TestModule", "This is an informational message.")
    log_warning("TestModule", "This is a warning message.")
    log_error("TestModule", "This is an error message.")
    log_critical("TestModule", "This is a critical alert!")
    log_recovery("TestModule", "System has recovered from error state.")