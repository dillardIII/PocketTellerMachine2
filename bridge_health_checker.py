from ghost_env import INFURA_KEY, VAULT_ADDRESS
# === FILE: bridge_health_checker.py ===
# 🔍 Bridge Health Checker – Scans bridge folder integrity and prints status.

import os

def check_bridge_health():
    drop_folder = "bridge/inbox"
    pickup_folder = "bridge/outbox"
    status = []

    if not os.path.isdir(drop_folder):
        status.append("❌ Missing: bridge/inbox (Drop Folder)")
    else:
        status.append("✅ Found: bridge/inbox")

    if not os.path.isdir(pickup_folder):
        status.append("❌ Missing: bridge/outbox (Pickup Folder)")
    else:
        status.append("✅ Found: bridge/outbox")

    print("[Bridge Health Check] -------------------------")
    for line in status:
        print(f"[Bridge Health] {line}")
    print("[Bridge Health Check] -------------------------\n")

def log_event():ef drop_files_to_bridge():