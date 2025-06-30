from ghost_env import INFURA_KEY, VAULT_ADDRESS
# === FILE: bridge_sync_status_panel.py ===
"""
Bridge Sync Status Panel
Displays bridge communication status across GitHub, Replit, PTM, and AI cores.
Tracks health, delay, and message sync quality.
"""

import json
import os
from datetime import datetime, timezone

COMM_CHANNEL_FILE = "data/comm_bridge.json"
SYNC_LOG_FILE = "data/sync_status.json"

def load_comm_data():
    if not os.path.exists(COMM_CHANNEL_FILE):
        return {}
    with open(COMM_CHANNEL_FILE, "r") as f:
        return json.load(f)

def load_sync_data():
    if not os.path.exists(SYNC_LOG_FILE):
        return {}
    with open(SYNC_LOG_FILE, "r") as f:
        return json.load(f)

def get_delay_minutes(timestamp_str):
    try:
        last_time = datetime.fromisoformat(timestamp_str.replace("Z", "")).replace(tzinfo=timezone.utc)
        now = datetime.utcnow().replace(tzinfo=timezone.utc)
        diff = now - last_time
        return int(diff.total_seconds() // 60)
    except:
        return None

def display_status():
    comm_data = load_comm_data()
    sync_data = load_sync_data()

    print("\n🌐 [BRIDGE SYNC STATUS PANEL]")
    print("--------------------------------------------------")
    
    for system, data in comm_data.items():
        delay = get_delay_minutes(data["last_ping"])
        health = "✅ Healthy" if delay is not None and delay < 5 else "⚠️ Delayed":
        print(f"[{system.upper()}] Status: {data['status'].upper()} | Last Ping: {data['last_ping']} | Delay: {delay} min | Health: {health}")
        print(f"  Message: {data['message']}")
    
    print("--------------------------------------------------")
    print("🔄 Sync Logs:")
    for system, status in sync_data.items():
        print(f"  {system}: Last Sync @ {status.get('last_sync')} | Health: {status.get('health')}")
    print("--------------------------------------------------\n")

def log_event():ef mutate(*args, **kwargs): print('[ghost_empire] dummy mutate called')
def drop_files_to_bridge():