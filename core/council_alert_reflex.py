"""
Council Alert Reflex
Watches for repeated instability or unresolved drift in ghost_status.json.
Notifies assistant personas to intervene, vote, or enter council mode.
"""

import os
import json
from datetime import datetime
import time

STATUS_FILE = "memory/ghost_status.json"
ALERT_LOG = "memory/council_alert_log.json"
TRIGGER_LIMIT = 3
CHECK_INTERVAL = 15  # seconds

def load_status():
    if not os.path.exists(STATUS_FILE):
        return {"drift_detected": False}
    with open(STATUS_FILE, "r") as f:
        return json.load(f)

def load_alert_log():
    if not os.path.exists(ALERT_LOG):
        return []
    with open(ALERT_LOG, "r") as f:
        return json.load(f)

def save_alert_log(log):
    with open(ALERT_LOG, "w") as f:
        json.dump(log[-100:], f, indent=2)

def trigger_council_alert(reason="unknown_drift"):
    now = datetime.utcnow().isoformat()
    log = load_alert_log()
    entry = {
        "timestamp": now,
        "trigger": reason,
        "action": "council_vote_required"
    }
    log.append(entry)
    save_alert_log(log)
    print(f"[CouncilReflex] 🛑 Drift crisis! Triggered council alert: {reason}")

    # OPTIONAL: Insert speech, screen notification, or persona summon
    try:
        from assistants.spectra import alert_personas
        alert_personas(reason)
    except:
        print("[CouncilReflex] ⚠️ Could not notify assistants directly.")

def monitor_drift():
    print("[CouncilReflex] 👁️ Watching ghost_status.json for repeated instability...")
    failure_count = 0

    while True:
        status = load_status()
        if status.get("drift_detected", False):
            failure_count += 1
            print(f"[CouncilReflex] ⚠️ Drift still unresolved ({failure_count})")
            if failure_count >= TRIGGER_LIMIT:
                trigger_council_alert(status.get("drift_reason", "unknown"))
                failure_count = 0  # reset after triggering
        else:
            failure_count = 0  # reset if stable
        time.sleep(CHECK_INTERVAL)

if __name__ == "__main__":
    monitor_drift()