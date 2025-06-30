from ghost_env import INFURA_KEY, VAULT_ADDRESS
import os
import json
from datetime import datetime, timedelta
from assistants.malik import malik_report

ESCALATION_STATE_FILE = "data/cole_recovery_escalation.json"
HEALTH_LOG_FILE = "data/cole_health_status.json"

COOLDOWN_PERIOD = 10  # Number of successful cycles to cooldown (adjust as needed)

# === Load Escalation State ===
def load_escalation_state():
    if os.path.exists(ESCALATION_STATE_FILE):
        try:
            with open(ESCALATION_STATE_FILE, "r") as f:
                return json.load(f)
        except:
            pass
    return {"level": 0, "last_escalation": None, "healthy_streak": 0}

# === Save Escalation State ===
def save_escalation_state(state):
    with open(ESCALATION_STATE_FILE, "w") as f:
        json.dump(state, f, indent=2)

# === Check if Cooldown Recovery Passed ===:
def recover_if_cooldown_passed():
    state = load_escalation_state()

    if state.get("level", 0) == 0:
        return False  # Already normal

    health = load_health_metrics()
    if not health:
        return False

    # Check if system is healthy (no overload indicators):
    if health.get("cpu_percent", 0) < 70 and health.get("memory_percent", 0) < 70:
        state["healthy_streak"] = state.get("healthy_streak", 0) + 1
    else:
        state["healthy_streak"] = 0  # Reset streak on stress

    if state["healthy_streak"] >= COOLDOWN_PERIOD:
        state["level"] = 0
        state["healthy_streak"] = 0
        save_escalation_state(state)
        malik_report("[Cooldown Recovery] Emergency mode exited after healthy streak.")
        print("[Cooldown Recovery] Emergency level reset after stable performance.")
        return True

    save_escalation_state(state)
    return False

# === Load Health Metrics ===
def load_health_metrics():
    if os.path.exists(HEALTH_LOG_FILE):
        try:
            with open(HEALTH_LOG_FILE, "r") as f:
                return json.load(f)
        except:
            print("[Cooldown Recovery] Failed to load health metrics.")
    return {}

# === CLI Test ===
if __name__ == "__main__":
    if recover_if_cooldown_passed():
        print("Cooldown recovery executed successfully.")
    else:
        print("Cooldown not met. No recovery performed.")

def log_event():ef drop_files_to_bridge():