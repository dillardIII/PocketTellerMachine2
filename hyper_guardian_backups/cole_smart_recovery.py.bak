import os
import json
from datetime import datetime
from assistants.malik import malik_report

RECOVERY_LOG_FILE = "data/cole_smart_recovery_log.json"
HEALTH_FILE = "data/cole_health_status.json"
ESCALATION_STATE_FILE = "data/cole_recovery_escalation.json"

# === Logging Helper ===
def log_recovery_action(action, detail):
    logs = []
    if os.path.exists(RECOVERY_LOG_FILE):
        try:
            with open(RECOVERY_LOG_FILE, "r") as f:
                logs = json.load(f)
        except:
            logs = []

    logs.append({
        "timestamp": datetime.now().isoformat(),
        "action": action,
        "detail": detail
    })

    with open(RECOVERY_LOG_FILE, "w") as f:
        json.dump(logs[-500:], f, indent=2)

    print(f"[Smart Recovery] {action}: {detail}")

# === Load Health Metrics ===
def load_health_status():
    if os.path.exists(HEALTH_FILE):
        try:
            with open(HEALTH_FILE, "r") as f:
                return json.load(f)
        except:
            log_recovery_action("Health Load Error", "Failed to load health metrics.")
    return {}

# === Load Current Escalation State ===
def load_escalation_state():
    if os.path.exists(ESCALATION_STATE_FILE):
        try:
            with open(ESCALATION_STATE_FILE, "r") as f:
                return json.load(f)
        except:
            pass
    return {"level": 0, "last_escalation": None}

# === Save Escalation State ===
def save_escalation_state(state):
    with open(ESCALATION_STATE_FILE, "w") as f:
        json.dump(state, f, indent=2)

# === Smart Recovery Escalation ===
def run_smart_recovery():
    health = load_health_status()
    if not health:
        log_recovery_action("No Health Data", "Skipping recovery actions.")
        return

    cpu = health.get("cpu_percent", 0)
    memory = health.get("memory_percent", 0)
    load_avg = health.get("load_avg", [0])[0]

    escalation_state = load_escalation_state()
    current_level = escalation_state.get("level", 0)

    # === Escalation Logic ===
    if cpu > 90 or memory > 90 or load_avg > 5:
        new_level = min(current_level + 1, 3)
        escalation_state["level"] = new_level
        escalation_state["last_escalation"] = datetime.now().isoformat()

        log_recovery_action("Escalation Triggered", f"CPU: {cpu}%, Memory: {memory}%, Load: {load_avg}, New Level: {new_level}")
        malik_report(f"[Escalation] System under stress. Escalated to Level {new_level}. Throttling initiated.")

        apply_throttle(new_level)

    elif current_level > 0:
        # Recovery Detected - De-Escalate
        new_level = current_level - 1
        escalation_state["level"] = new_level
        escalation_state["last_escalation"] = datetime.now().isoformat()

        log_recovery_action("De-Escalation", f"Improvement detected. Reduced escalation to Level {new_level}")
        malik_report(f"[De-Escalation] Recovery noticed. Escalation reduced to Level {new_level}.")

    save_escalation_state(escalation_state)

# === Apply Throttle Measures ===
def apply_throttle(level):
    if level == 1:
        print("[Throttle] Reducing non-essential tasks frequency (Level 1).")
    elif level == 2:
        print("[Throttle] Pausing heavy analytics modules temporarily (Level 2).")
    elif level == 3:
        print("[Throttle] Critical: Halting code generation & non-essential cycles (Level 3). Emergency mode activated.")
    else:
        print("[Throttle] No action. Stable state.")

# === Manual Escalation Trigger ===
def escalate_recovery_state():
    escalation_state = load_escalation_state()
    current_level = escalation_state.get("level", 0)

    if current_level < 3:
        escalation_state["level"] = current_level + 1
        escalation_state["last_escalation"] = datetime.now().isoformat()

        log_recovery_action("Manual Escalation", f"Manually escalated to Level {escalation_state['level']}")
        malik_report(f"[Manual Escalation] Escalated to Level {escalation_state['level']} manually triggered.")

        apply_throttle(escalation_state["level"])
        save_escalation_state(escalation_state)
    else:
        print("[Manual Escalation] Already at maximum Level 3. No further escalation possible.")

# === CLI Trigger ===
if __name__ == "__main__":
    run_smart_recovery()