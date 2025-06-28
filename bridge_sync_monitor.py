# === FILE: bridge_sync_monitor.py ===

# 🔗 Bridge Sync Monitor – Validates file handoffs between GPT and execution side

import os

def verify_bridge_sync():
    try:
        bridge_files = os.listdir("ptm_bridge")
        inbox_files = os.listdir("ptm_inbox")
        missing = [f for f in bridge_files if f not in inbox_files]
        if missing:
            print(f"[BridgeMonitor] ⚠️ Files not synced to inbox: {missing}")
        else:
            print("[BridgeMonitor] ✅ Bridge sync looks clean.")
    except Exception as e:
        print(f"[BridgeMonitor] ❌ Error: {e}")