# 🧾 Vault Error Log Repair – Attempts auto-correction of broken or partial logs in the vault

import os
import json
import time
from utils.logger import log_event

# === Paths ===
VAULT_LOGS_DIR = "vault/logs"
REPAIR_OUTPUT_DIR = "vault/logs_repaired"

# === Init ===
os.makedirs(VAULT_LOGS_DIR, exist_ok=True)
os.makedirs(REPAIR_OUTPUT_DIR, exist_ok=True)

def is_valid_json(content):
    try:
        json.loads(content)
        return True
    except json.JSONDecodeError:
        return False

def attempt_repair(content):
    try:
        repaired = content.strip()
        if repaired.endswith(","):
            repaired = repaired[:-1]
        if not repaired.endswith("}"):
            repaired += "}"
        if is_valid_json(repaired):
            return json.loads(repaired)
    except:
        pass
    return None

def repair_vault_logs():
    print("[VaultRepair] 🧾 Scanning for corrupt logs...")
    repaired_count = 0
    for file_name in os.listdir(VAULT_LOGS_DIR):
        file_path = os.path.join(VAULT_LOGS_DIR, file_name)
        try:
            with open(file_path, "r") as f:
                raw = f.read()
            if is_valid_json(raw):
                continue
            repaired = attempt_repair(raw)
            if repaired:
                out_path = os.path.join(REPAIR_OUTPUT_DIR, file_name)
                with open(out_path, "w") as f:
                    json.dump(repaired, f, indent=2)
                log_event("VaultLogRepair", {"file": file_name, "status": "✅ Repaired"})
                repaired_count += 1
            else:
                log_event("VaultLogRepair", {"file": file_name, "status": "❌ Unrecoverable"})
        except Exception as e:
            log_event("VaultLogRepair", {"file": file_name, "error": str(e)})
    print(f"[VaultRepair] ✅ Finished. Repaired: {repaired_count}")

if __name__ == "__main__":
    repair_vault_logs()