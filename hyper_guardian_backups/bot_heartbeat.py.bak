# === FILE: bot_heartbeat.py ===

import time
import json
import os

# Shared file used by all bots to register their presence
GHOSTNET_STATE_FILE = "ghostnet_state.json"

# How often to check the status of each bot (seconds)
HEARTBEAT_INTERVAL = 10
BOT_TIMEOUT = 30  # If no ping within 30s, mark as "inactive"


def load_ghostnet_state():
    """Load the current ghostnet state from shared file."""
    if not os.path.exists(GHOSTNET_STATE_FILE):
        return {}
    with open(GHOSTNET_STATE_FILE, "r") as file:
        return json.load(file)


def save_ghostnet_state(state):
    """Save updated state to file."""
    with open(GHOSTNET_STATE_FILE, "w") as file:
        json.dump(state, file, indent=2)


def check_heartbeats():
    """Check each bot's last seen time and mark inactive if too long."""
    while True:
        print("[Heartbeat] Checking bot statuses...")
        state = load_ghostnet_state()
        now = time.time()
        updated = False

        for bot_id, data in state.items():
            last_seen = data.get("last_seen", 0)
            if now - last_seen > BOT_TIMEOUT:
                if data.get("status") != "inactive":
                    print(f"[Heartbeat] ⚠️ Bot {bot_id} is now INACTIVE.")
                    state[bot_id]["status"] = "inactive"
                    updated = True
            else:
                if data.get("status") != "alive":
                    print(f"[Heartbeat] ✅ Bot {bot_id} is back ONLINE.")
                    state[bot_id]["status"] = "alive"
                    updated = True

        if updated:
            save_ghostnet_state(state)

        time.sleep(HEARTBEAT_INTERVAL)


# Start monitoring immediately if run directly
if __name__ == "__main__":
    check_heartbeats()