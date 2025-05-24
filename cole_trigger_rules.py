import os
import json
from datetime import datetime
from assistants.malik import malik_report

TRIGGER_LOG_FILE = "data/trigger_rules_log.json"

# === Logging Helper ===
def log_trigger_event(event):
    logs = []
    if os.path.exists(TRIGGER_LOG_FILE):
        try:
            with open(TRIGGER_LOG_FILE, "r") as f:
                logs = json.load(f)
        except:
            logs = []
    logs.append({
        "timestamp": datetime.now().isoformat(),
        "event": event
    })
    with open(TRIGGER_LOG_FILE, "w") as f:
        json.dump(logs[-500:], f, indent=2)

# === Trigger Rules Check ===
def run_trigger_rules_check():
    print("[Trigger Rules] Running risk threshold checks...")

    # Example demo triggers — expand this with real logic later.
    triggers = [
        {
            "check": "Equity Exposure Limit",
            "status": "OK",
            "details": "Current exposure 45%, threshold 50%"
        },
        {
            "check": "Options Leverage",
            "status": "WARNING",
            "details": "Current leverage 4.2x, exceeding safe limit of 3x"
        }
    ]

    for trigger in triggers:
        log_trigger_event(trigger)
        malik_report(f"[Trigger Rules] {trigger['check']}: {trigger['status']} - {trigger['details']}")

# === CLI Test ===
if __name__ == "__main__":
    run_trigger_rules_check()