# === FILE: vault_manager.py ===
# 💼 Vault Manager – Handles all vault operations, logging, snapshots, and partial key recombining

import os
import json
from datetime import datetime

# === FILE LOCATIONS ===
VAULT_LOG = "vault/vault_log.json"
VAULT_FILE = "vault.json"

# === LOG A NEW VAULT EVENT ===
def log_vault_entry(event_type, data):
    os.makedirs("vault", exist_ok=True)
    entry = {
        "timestamp": datetime.utcnow().isoformat(),
        "type": event_type,
        "data": data
    }

    if os.path.exists(VAULT_LOG):
        try:
            with open(VAULT_LOG, "r") as f:
                vault = json.load(f)
        except json.JSONDecodeError:
            print("[VaultManager] ⚠️ Corrupt log file, resetting.")
            vault = []
    else:
        vault = []

    vault.append(entry)

    with open(VAULT_LOG, "w") as f:
        json.dump(vault, f, indent=4)

    print(f"[VaultManager] 🧾 Logged event: {event_type}")

# === LOAD FULL VAULT STRUCTURE SAFELY ===
def load_vault():
    try:
        if not os.path.exists(VAULT_FILE):
            print("[VaultManager] 🗃️ No vault found, creating new.")
            with open(VAULT_FILE, "w") as f:
                json.dump({"assets": [], "partial_keys": []}, f)
        with open(VAULT_FILE) as f:
            return json.load(f)
    except json.JSONDecodeError:
        print("[VaultManager] ❌ Corrupt vault file detected, resetting.")
        with open(VAULT_FILE, "w") as f:
            json.dump({"assets": [], "partial_keys": []}, f)
        return {"assets": [], "partial_keys": []}

# === SAVE ENTIRE VAULT STRUCTURE ===
def save_vault(data):
    try:
        with open(VAULT_FILE, "w") as f:
            json.dump(data, f, indent=2)
        print("[VaultManager] 💾 Vault saved.")
    except Exception as e:
        print(f"[VaultManager] ❌ Failed to save vault: {e}")

# === FORCE RECOMBINE PARTIAL KEYS LOGGED & SAVE ===
def force_recombine_partials():
    vault = load_vault()
    if vault.get("partial_keys"):
        print("[VaultManager] 🔑 Attempting recombine of partial keys...")
        vault["partial_keys"] = []
        new_asset = {
            "type": "key",
            "status": "recombined",
            "timestamp": datetime.utcnow().isoformat()
        }
        vault["assets"].append(new_asset)
        save_vault(vault)
        log_vault_entry("recombine", {"status": "success", "new_asset": new_asset})
    else:
        print("[VaultManager] 💤 No partial keys to recombine.")

# === SIMPLE FORCE RECOMBINE WITHOUT LOGGING FOR INLINE CALLS ===
def simple_force_recombine():
    vault = load_vault()
    if vault.get("partial_keys"):
        print("[VaultManager] 🔑 Combining partial keys...")
        vault["partial_keys"] = []
        vault["assets"].append({"type": "key", "status": "recombined"})
        save_vault(vault)
    else:
        print("[VaultManager] 💤 Nothing to combine.")