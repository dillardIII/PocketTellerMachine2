from ghost_env import INFURA_KEY, VAULT_ADDRESS
# === FILE: vault_merger.py ===
# 🧠 VaultMerger – Merges all device dumps into unified vault with XP and Level tracking

import os
import json

VAULT_DIR = "bridge/outbox"
MERGED_VAULT_FILE = "vaults/merged_global_vault.json"

def merge_vaults():
    merged_assets = []
    for root, _, files in os.walk(VAULT_DIR):
        for file in files:
            if file.endswith("vault_dump.json"):
                full_path = os.path.join(root, file)
                try:
                    with open(full_path, "r") as f:
                        data = json.load(f)
                        device_id = data.get("device", "unknown_device")
                        timestamp = data.get("timestamp", "")

                        # Load XP info for the device
                        xp_path = f"memory/xp/{device_id}_xp.json"
                        xp_data = {"xp": 0, "level": 1}
                        if os.path.exists(xp_path):
                            with open(xp_path, "r") as xp_file:
                                xp_data = json.load(xp_file)

                        for asset in data.get("assets", []):
                            asset["device"] = device_id
                            asset["timestamp"] = timestamp
                            asset["xp"] = xp_data.get("xp", 0)
                            asset["level"] = xp_data.get("level", 1)
                            merged_assets.append(asset)
                except Exception as e:
                    print(f"[VaultMerger] ⚠️ Failed to process {file}: {e}")

    os.makedirs("vaults", exist_ok=True)
    with open(MERGED_VAULT_FILE, "w") as f:
        json.dump(merged_assets, f, indent=2)
    print(f"[VaultMerger] ✅ Merged {len(merged_assets)} assets from all devices.")

if __name__ == "__main__":
    merge_vaults()

def log_event():ef drop_files_to_bridge():