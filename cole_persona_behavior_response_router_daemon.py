from ghost_env import INFURA_KEY, VAULT_ADDRESS
# cole_persona_behavior_response_router_daemon.py

import os
import json
import time
from datetime import datetime

# === Configurations ===
BEHAVIOR_MODEL_FILE = "data/persona_behavior_model.json"
ROUTER_LOG_FILE = "data/persona_behavior_router_log.json"
COMMAND_FILE = "data/pending_user_commands.json"
ROUTED_COMMANDS_FILE = "data/routed_user_commands.json"
CHECK_INTERVAL = 300  # Every 5 minutes

# === Ensure data folder exists ===
os.makedirs("data", exist_ok=True)

# === Logging ===
def log_event(message):
    logs = []
    if os.path.exists(ROUTER_LOG_FILE):
        try:
            with open(ROUTER_LOG_FILE, "r") as f:
                logs = json.load(f)
        except:
            logs = []
    logs.append({"timestamp": datetime.now().isoformat(), "message": message})
    with open(ROUTER_LOG_FILE, "w") as f:
        json.dump(logs[-500:], f, indent=2)

# === Load Files ===
def load_behavior_model():
    if os.path.exists(BEHAVIOR_MODEL_FILE):
        try:
            with open(BEHAVIOR_MODEL_FILE, "r") as f:
                return json.load(f)
        except:
            return {}
    return {}

def load_pending_commands():
    if os.path.exists(COMMAND_FILE):
        try:
            with open(COMMAND_FILE, "r") as f:
                return json.load(f)
        except:
            return []
    return []

# === Save Routed Commands ===
def save_routed_commands(commands):
    with open(ROUTED_COMMANDS_FILE, "w") as f:
        json.dump(commands, f, indent=2)

# === Route Command Based on Persona Behavior ===
def route_command(persona, command, behavior_model):
    behavior = behavior_model.get(persona, {}).get("current_behavior", "Neutral and Balanced")
    return {
        "persona": persona,
        "behavior": behavior,
        "command": command,
        "routed_at": datetime.now().isoformat()
    }

# === Main Routing Logic ===
def route_pending_commands():
    behavior_model = load_behavior_model()
    pending_commands = load_pending_commands()
    routed_commands = []

    if not pending_commands:
        return

    for cmd in pending_commands:
        persona = cmd.get("persona", "DefaultPersona")
        routed = route_command(persona, cmd.get("command"), behavior_model)
        routed_commands.append(routed)
        log_event(f"[ROUTER]: Routed command '{cmd.get('command')}' to {persona} using behavior {routed['behavior']}")

    save_routed_commands(routed_commands)

# === Main Daemon Loop ===
def persona_behavior_router_loop():
    print("[BEHAVIOR ROUTER]: Running persona behavior router daemon...")
    while True:
        try:
            route_pending_commands()
        except Exception as e:
            log_event(f"[ROUTER ERROR]: {e}")
        time.sleep(CHECK_INTERVAL)

if __name__ == "__main__":
    persona_behavior_router_loop()