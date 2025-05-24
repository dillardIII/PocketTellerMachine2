import os
import shutil

def deploy_fix(file_path, new_code):
    try:
        if not os.path.exists(file_path):
            print(f"[AutoDeployer] File not found: {file_path}")
            return False

        # === Backup original ===
        backup_path = file_path + ".bak"
        shutil.copy(file_path, backup_path)

        # === Write the fix ===
        with open(file_path, "w") as f:
            f.write(new_code)

        print(f"[AutoDeployer] Fix deployed to {file_path}")
        return True

    except Exception as e:
        print("[AutoDeployer] Failed. Rolling back...")

        # === Rollback ===
        if os.path.exists(backup_path):
            shutil.copy(backup_path, file_path)
            print("[AutoDeployer] Rollback complete.")
        else:
            print("[AutoDeployer] No backup found. Cannot rollback.")
        return False