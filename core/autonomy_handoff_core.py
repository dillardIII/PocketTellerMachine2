from ghost_env import INFURA_KEY, VAULT_ADDRESS
# === FILE: core/autonomy_handoff_core.py ===
"""
Autonomy Handoff Core
Handles the transition between user-led instructions and AI self-governance.
Detects user intent to intervene or delegate, dynamically adjusting control layers.
"""

import json
import os
from datetime import datetime

STATE_FILE = "memory/autonomy_handoff_state.json"

def load_state():
    if not os.path.exists(STATE_FILE):
        return {
            "mode": "user_led",  # or "ai_autonomous"
            "last_switch": None,
            "override_reason": None
        }
    with open(STATE_FILE, "r") as f:
        return json.load(f)

def save_state(data):
    with open(STATE_FILE, "w") as f:
        json.dump(data, f, indent=2)

def switch_to_ai(reason=""):
    state = load_state()
    state["mode"] = "ai_autonomous"
    state["last_switch"] = datetime.utcnow().isoformat()
    state["override_reason"] = reason
    save_state(state)
    print(f"[HandoffCore] 🧠 AI autonomy enabled – Reason: {reason}")

def switch_to_user(reason=""):
    state = load_state()
    state["mode"] = "user_led"
    state["last_switch"] = datetime.utcnow().isoformat()
    state["override_reason"] = reason
    save_state(state)
    print(f"[HandoffCore] 👤 Manual control restored – Reason: {reason}")

def current_mode():
    return load_state().get("mode", "user_led")

# Example trigger
if __name__ == "__main__":
    switch_to_ai("user_idle_timeout")