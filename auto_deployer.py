# === FILE: auto_deployer.py ===
# 🚀 Auto Deployer – Pushes fixed code into production environment

import os
import shutil
from datetime import datetime

# === Deploy AI-Generated Fix Safely ===
def deploy_fix(fixed_code, target_file):
    try:
        if not target_file or not fixed_code:
            print("[AutoDeployer] ❌ Missing file path or new code.")
            return {"status": "failed", "error": "Missing file path or code."}

        if not os.path.exists(target_file):
            print(f"[AutoDeployer] ❌ File not found: {target_file}")
            return {"status": "failed", "error": "Target file not found."}

        # === Backup Original File with Timestamp ===
        backup_folder = "backups"
        os.makedirs(backup_folder, exist_ok=True)
        timestamp = datetime.utcnow().strftime("%Y%m%d_%H%M%S")
        backup_path = os.path.join(
            backup_folder,
            f"{os.path.basename(target_file)}.{timestamp}.bak"
        )
        shutil.copy2(target_file, backup_path)
        print(f"[AutoDeployer] 🔒 Backup created: {backup_path}")

        # === Write New Fixed Code ===
        with open(target_file, "w", encoding="utf-8") as f:
            f.write(fixed_code)

        print(f"[AutoDeployer] ✅ Fix deployed to {target_file}")
        return {
            "status": "success",
            "deployed_to": target_file,
            "backup": backup_path
        }

    except Exception as e:
        print(f"[AutoDeployer] ❌ Deployment failed: {e}")
        print("[AutoDeployer] 🛠️ Attempting rollback...")

        # === Rollback if something goes wrong ===
        try:
            if os.path.exists(backup_path):
                shutil.copy2(backup_path, target_file)
                print("[AutoDeployer] 🔄 Rollback complete.")
            else:
                print("[AutoDeployer] ⚠️ No backup found. Cannot rollback.")
        except Exception as rollback_error:
            print(f"[AutoDeployer] 🚨 Rollback failed: {rollback_error}")

        return {"status": "failed", "error": str(e)}