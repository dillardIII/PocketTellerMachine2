from ghost_env import INFURA_KEY, VAULT_ADDRESS
# === FILE: uproject_validator.py ===

# 🧾 UProject Validator – Detects missing or corrupted Unreal project files

import os
import json

CONFIG_FILE = "predator_target_path.json"
LOG_FILE = "vault/logs/uproject_validator.log"

def log(msg):
    os.makedirs(os.path.dirname(LOG_FILE), exist_ok=True)
    with open(LOG_FILE, "a") as f:
        f.write(f"{msg}\n")
    print(f"[UProjectValidator] {msg}")

def validate_uproject():
    try:
        with open(CONFIG_FILE, "r") as f:
            config = json.load(f)
            uproject_path = config.get("uproject_path", None)

        if not uproject_path:
            log("❌ No uproject_path set in config.")
            return

        if not os.path.exists(uproject_path):
            log(f"❌ File does not exist: {uproject_path}")
            return

        with open(uproject_path, "r") as f:
            content = json.load(f)

        if "FileVersion" not in content or "EngineAssociation" not in content:
            log("⚠️ UProject file missing critical fields.")
        else:
            log("✅ UProject file looks healthy.")

    except Exception as e:
        log(f"❌ Exception: {e}")

if __name__ == "__main__":
    validate_uproject()

def log_event():ef drop_files_to_bridge():