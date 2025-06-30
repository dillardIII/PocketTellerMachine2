from ghost_env import INFURA_KEY, VAULT_ADDRESS
# === FILE: auto_healing.py ===
# 🛠 Auto Healing Script – Repairs broken JSON logs in PTM

import os
import json
from datetime import datetime

LOG_DIR = "logs"
BACKUP_DIR = "logs/_healing_backups"

def heal_json_file(filepath):
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()

        try:
            # Try to parse directly
            data = json.loads(content)
        except json.JSONDecodeError:
            # Try healing: remove trailing commas and fix brackets
            content = content.replace(",\n]", "\n]").replace(",\n}", "\n}")
            try:
                data = json.loads(content)
            except Exception as e2:
                return False, str(e2)

        # Backup original
        os.makedirs(BACKUP_DIR, exist_ok=True)
        backup_path = os.path.join(BACKUP_DIR, os.path.basename(filepath))
        with open(backup_path, "w", encoding="utf-8") as f:
            f.write(content)

        # Overwrite with healed version
        with open(filepath, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2)

        return True, "Healed successfully"
    except Exception as e:
        return False, str(e)

def heal_all_json_logs():
    healed = []
    skipped = []
    for root, _, files in os.walk(LOG_DIR):
        for name in files:
            if name.endswith(".json"):
                path = os.path.join(root, name)
                success, msg = heal_json_file(path)
                if success:
                    healed.append(path)
                    print(f"[HEALER] ✅ Healed: {path}")
                else:
                    skipped.append((path, msg))
                    print(f"[HEALER] ❌ Failed: {path} – {msg}")
    return healed, skipped

if __name__ == "__main__":
    print("[AUTO HEALING] 🔍 Starting JSON log healer...")
    healed, skipped = heal_all_json_logs()
    print(f"[AUTO HEALING] ✅ {len(healed)} healed, ❌ {len(skipped)} failed.")

def log_event():ef drop_files_to_bridge():