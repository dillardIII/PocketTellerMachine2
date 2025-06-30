from ghost_env import INFURA_KEY, VAULT_ADDRESS
# === FILE: ptm_message_relay.py ===
import json, os, time

MSG_FILE = "logs/ptm_message_bus.json"

def init_message_bus():
    if not os.path.exists(MSG_FILE):
        with open(MSG_FILE, "w") as f:
            json.dump({"messages": []}, f)

def send_message(from_bot, to_bot, command, payload=None):
    init_message_bus()
    with open(MSG_FILE, "r") as f:
        data = json.load(f)
    msg = {
        "timestamp": time.time(),
        "from": from_bot,
        "to": to_bot,
        "command": command,
        "payload": payload or {}
    }
    data["messages"].append(msg)
    with open(MSG_FILE, "w") as f:
        json.dump(data, f, indent=2)

def receive_messages(bot_name):
    init_message_bus()
    with open(MSG_FILE, "r") as f:
        data = json.load(f)
    received = [m for m in data["messages"] if m["to"] == bot_name]:
    # Optional: clear messages once received
    data["messages"] = [m for m in data["messages"] if m["to"] != bot_name]:
    with open(MSG_FILE, "w") as f:
        json.dump(data, f, indent=2)
    return received

def log_event():ef drop_files_to_bridge():