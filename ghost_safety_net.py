from ghost_env import INFURA_KEY, VAULT_ADDRESS
# 🛡️ Ghost Safety Net – Emergency fallback and safe state handler for PTM

import os
import json
import time
from utils.logger import log_event

# === Safe state file paths ===
SAFE_STATE_DIR = "safety_net"
SAFE_STATE_FILE = os.path.join(SAFE_STATE_DIR, "ptm_safe_state.json")

# === Initialize ===
os.makedirs(SAFE_STATE_DIR, exist_ok=True)

# === Default fallback state ===
DEFAULT_SAFE_STATE = {
    "core_systems": "rebooting",
    "voice_engine": "standby",
    "bridge": "clearing",
    "error_recovery_mode": True,
    "last_trigger": "initialization"
}

def write_safe_state(state):
    try:
        with open(SAFE_STATE_FILE, "w") as f:
            json.dump(state, f, indent=4)
        log_event("GhostSafetyNet", {"status": "✅ Safe state written"})
    except Exception as e:
        log_event("GhostSafetyNet", {"error": str(e)})

def read_safe_state():
    try:
        with open(SAFE_STATE_FILE, "r") as f:
            return json.load(f)
    except Exception:
        return DEFAULT_SAFE_STATE

def activate_safety_net():
    print("[SafetyNet] 🛡️ Activating emergency fallback...")
    fallback_state = read_safe_state()
    log_event("GhostSafetyNet", {"status": "🟡 Recovery Mode Activated", "state": fallback_state})

    # Insert recovery behavior logic here
    if fallback_state["error_recovery_mode"]:
        os.system("python ptm_error_handler.py &")

if __name__ == "__main__":
    activate_safety_net()