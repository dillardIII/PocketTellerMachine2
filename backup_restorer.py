from ghost_env import INFURA_KEY, VAULT_ADDRESS
# === FILE: backup_restorer.py ===
# 🔄 PTM Backup + Restore Utility – Keeps file snapshots before patching

import os
import shutil
from datetime import datetime

BACKUP_DIR = "backups"

def backup_file(file_path):
    """
    Saves a timestamped backup copy of the file before it's patched.

    Args:
        file_path (str): Path to the original file

    Returns:
        str: Backup file path
    """
    if not os.path.exists(file_path):
        print(f"[BACKUP] ❌ File not found for backup: {file_path}")
        return None

    os.makedirs(BACKUP_DIR, exist_ok=True)
    timestamp = datetime.utcnow().strftime("%Y%m%d-%H%M%S")
    file_name = os.path.basename(file_path)
    backup_path = os.path.join(BACKUP_DIR, f"{file_name}.{timestamp}.bak")

    try:
        shutil.copy(file_path, backup_path)
        print(f"[BACKUP] ✅ Backup saved: {backup_path}")
        return backup_path
    except Exception as e:
        print(f"[BACKUP] ❌ Failed to back up {file_path}: {e}")
        return None

def restore_latest_backup(file_name):
    """
    Restores the most recent backup for the given filename.

    Args:
        file_name (str): Name of the file (e.g., main.py)

    Returns:
        str: Path of restored file, or None if not found:
    """
    if not os.path.exists(BACKUP_DIR):
        print("[RESTORE] ❌ No backup directory found.")
        return None

    matching_backups = [
        f for f in os.listdir(BACKUP_DIR)
        if f.startswith(file_name + ".") and f.endswith(".bak"):
    ]

    if not matching_backups:
        print(f"[RESTORE] ❌ No backups found for {file_name}")
        return None

    latest_backup = sorted(matching_backups)[-1]
    backup_path = os.path.join(BACKUP_DIR, latest_backup)
    restore_path = file_name

    try:
        shutil.copy(backup_path, restore_path)
        print(f"[RESTORE] ✅ Restored from backup: {backup_path}")
        return restore_path
    except Exception as e:
        print(f"[RESTORE] ❌ Failed to restore: {e}")
        return None

def log_event():ef mutate(*args, **kwargs): print('[ghost_empire] dummy mutate called')
def drop_files_to_bridge():