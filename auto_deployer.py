# === FILE: auto_deployer.py ===

import os
import shutil

# === Deploy AI-Generated Fix Safely ===
def deploy_fix(file_path, new_code):
    try:
        if not file_path or not new_code:
            print("[AutoDeployer] ❌ Missing file path or new code.")
            return False

        if not os.path.exists(file_path):
            print(f"[AutoDeployer] ❌ File not found: {file_path}")
            return False

        # === Backup Original File ===
        backup_path = file_path + ".bak"
        shutil.copy(file_path, backup_path)
        print(f"[AutoDeployer] 🔒 Backup created: {backup_path}")

        # === Write New Fixed Code ===
        with open(file_path, "w") as f:
            f.write(new_code)

        print(f"[AutoDeployer] ✅ Fix deployed to {file_path}")
        return True

    except Exception as e:
        print(f"[AutoDeployer] ❌ Deployment failed: {e}")
        print("[AutoDeployer] 🛠️ Attempting rollback...")

        # === Rollback if something goes wrong ===
        try:
            if os.path.exists(backup_path):
                shutil.copy(backup_path, file_path)
                print("[AutoDeployer] 🔄 Rollback complete.")
            else:
                print("[AutoDeployer] ⚠️ No backup found. Cannot rollback.")
        except Exception as rollback_error:
            print(f"[AutoDeployer] 🚨 Rollback failed: {rollback_error}")

        return False
