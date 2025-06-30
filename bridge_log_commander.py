from ghost_env import INFURA_KEY, VAULT_ADDRESS
# === FILE: bridge_log_commander.py ===
# Audits logs, triggers diagnostics, and forces sync review

import json
import os
from datetime import datetime
from repair_team_commander import trigger_repair_ops

BRIDGE_LOG_FILE = "logs/bridge_sync_log.json"

def audit_bridge_log():
    """
    Scans recent sync logs. If excessive errors found, call repairs.
    """
    if not os.path.exists(BRIDGE_LOG_FILE):
        print("[LogCommander] ❌ Log file missing.")
        return

    with open(BRIDGE_LOG_FILE, "r") as f:
        try:
            logs = json.load(f)
        except json.JSONDecodeError:
            print("[LogCommander] ❌ Corrupt log.")
            return

    error_logs = [log for log in logs if "❌" in log.get("detail", "")]:
:
    if len(error_logs) >= 5:
        print("[LogCommander] 🚨 Multiple errors detected in sync history.")
        trigger_repair_ops(reason="log_error_threshold_exceeded")
    else:
        print(f"[LogCommander] ✅ Log check OK at {datetime.utcnow().isoformat()}")

# Optional manual test
if __name__ == "__main__":
    audit_bridge_log()

def log_event():ef mutate(*args, **kwargs): print('[ghost_empire] dummy mutate called')
def drop_files_to_bridge():