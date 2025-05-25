import os
import json
from datetime import datetime
import pytz

CENTRAL_TZ = pytz.timezone("US/Central")

def get_local_time():
    return datetime.now(CENTRAL_TZ)

from cole_tools.cole_auto_runner import cole_auto_run
from cole_phase_manager import auto_detect_phase

LOG_FILE = "data/cole_auto_system_log.json"
os.makedirs("data", exist_ok=True)

# === Helper: Log System Events ===
def log_auto_event(event, detail):
    entry = {
        "timestamp": datetime.now().isoformat(),
        "event": event,
        "detail": detail
    }

    logs = []
    if os.path.exists(LOG_FILE):
        try:
            with open(LOG_FILE, "r") as f:
                logs = json.load(f)
        except:
            logs = []

    logs.append(entry)
    with open(LOG_FILE, "w") as f:
        json.dump(logs[-300:], f, indent=2)

    print(f"[AutoSystem] {event}: {detail}")

# === Run Auto System ===
def run_auto_system():
    try:
        phase = auto_detect_phase()
        config = {
            "phase": phase,
            "tasks": ["auto_system_init", "status_check"]
        }

        cole_auto_run(config)
        log_auto_event("Auto System Run", f"Phase: {phase}, Config: {config}")
    except Exception as e:
        log_auto_event("Auto System Error", str(e))

# === CLI Trigger ===
if __name__ == "__main__":
    run_auto_system()

# === Export cole_autopilot_cycle for app.py ===
from cole_autopilot_loop import cole_autopilot_cycle

__all__ = ["cole_autopilot_cycle"]