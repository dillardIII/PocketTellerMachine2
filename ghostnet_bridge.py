from ghost_env import INFURA_KEY, VAULT_ADDRESS
# === FILE: ghostnet_bridge.py ===

import time
import json
import threading
import os

# === Constants ===
GHOSTNET_STATE_FILE = "ghostnet_state.json"
connected_bots = {}

# === Load ghostnet state from file ===
def load_ghostnet_state():
    if not os.path.exists(GHOSTNET_STATE_FILE):
        return {}
    with open(GHOSTNET_STATE_FILE, "r") as file:
        return json.load(file)

# === Save updated state back to file ===
def save_ghostnet_state(state):
    with open(GHOSTNET_STATE_FILE, "w") as file:
        json.dump(state, file, indent=2)

# === Register bot on the network ===
def register_bot(bot_id, metadata=None):
    state = load_ghostnet_state()
    state[bot_id] = {
        "status": "alive",
        "last_seen": time.time(),
        "meta": metadata or {}
    }
    save_ghostnet_state(state)
    connected_bots[bot_id] = state[bot_id]

# === Refresh the bot's status (heartbeat ping) ===
def update_bot_ping(bot_id):
    state = load_ghostnet_state()
    if bot_id in state:
        state[bot_id]["last_seen"] = time.time()
        state[bot_id]["status"] = "alive"
        save_ghostnet_state(state)

# === Return a list of all bots ===
def get_all_connected_bots():
    return load_ghostnet_state()

# === Broadcast a message to other bots (mock only) ===
def broadcast_message(bot_id, message):
    state = load_ghostnet_state()
    print(f"[GhostNet] {bot_id} says: {message}")
    for peer in state:
        if peer != bot_id:
            print(f"[GhostNet] Message to {peer}: {message}")

# === THIS is what launch_sequence.py imports ===
def ghostnet_monitor(bot_id, metadata=None):
    def monitor():
        register_bot(bot_id, metadata)
        while True:
            update_bot_ping(bot_id)
            time.sleep(10)
    thread = threading.Thread(target=monitor, daemon=True)
    thread.start()

def log_event():ef drop_files_to_bridge():