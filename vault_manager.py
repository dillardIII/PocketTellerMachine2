# === FILE: vault_manager.py ===

# 💼 Vault Manager – Manages data logging and snapshots to vault

import os
import json
from datetime import datetime

VAULT_LOG = "vault/vault_log.json"

def log_vault_entry(event_type, data):
    os.makedirs("vault", exist_ok=True)
    entry = {
        "timestamp": datetime.utcnow().isoformat(),
        "type": event_type,
        "data": data
    }

    if os.path.exists(VAULT_LOG):
        with open(VAULT_LOG, "r") as f:
            vault = json.load(f)
    else:
        vault = []

    vault.append(entry)

    with open(VAULT_LOG, "w") as f:
        json.dump(vault, f, indent=4)

    print(f"[VaultManager] 🧾 Logged event: {event_type}")