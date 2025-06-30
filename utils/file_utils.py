from ghost_env import INFURA_KEY, VAULT_ADDRESS
# === FILE: utils/file_utils.py ===
# 🛠️ File Utilities – Scans for missing files, manages directories, repairs module gaps, and writes generated files

import os
import json

# === PTM Folder Structure (Required Directories) ===
PTM_DIRECTORIES = [
    "core",
    "agents",
    "bridge",
    "utils",
    "memory",
    "vault",
    "ghost_modules",
    "recon",
    "sandbox",
]

# === Essential Files for Auto-Repair Scan ===
ESSENTIAL_FILES = {
    "core": ["godcore.py", "inspector_bot.py", "sweep_handler.py"],
    "agents": ["bridge_drop_agent.py", "bridge_pickup_agent.py"],
    "bridge": ["bridge_controller.py", "bridge_file_syncer.py"],
    "utils": ["logger.py", "file_utils.py"],
    "memory": ["ghostforge_activity_log.json"],
    "vault": ["wallet_snapshot.json"],
    "ghost_modules": ["reflex_engine.py"],
    "recon": ["recon_agent.py"],
    "sandbox": ["sandbox_monitor.py"],
}

# === List All Missing Critical Files ===
def list_missing_files():
    missing = []
    for folder, required_files in ESSENTIAL_FILES.items():
        for file in required_files:
            file_path = os.path.join(folder, file)
            if not os.path.exists(file_path):
                missing.append({
                    "folder": folder,
                    "filename": file,
                    "path": file_path,
                    "purpose": "Auto repair required",
                    "base_code": "# Auto-generated placeholder file"
                })
    return missing

# === Repair a Missing File (Used by Inspector, Sweep, or GhostForge) ===
def repair_file(file_info):
    folder = file_info["folder"]
    file_path = file_info["path"]
    try:
        os.makedirs(folder, exist_ok=True)
        with open(file_path, "w") as f:
            f.write(file_info.get("base_code", "# Placeholder\n"))
        return {"filename": file_info["filename"], "success": True}
    except Exception as e:
        return {"filename": file_info["filename"], "success": False, "error": str(e)}

# === Save a File to Disk (Used by GhostForge + AI Coder) ===
def save_file(path, code):
    dir_path = os.path.dirname(path)
    if dir_path and not os.path.exists(dir_path):
        os.makedirs(dir_path)

    with open(path, "w") as f:
        f.write(code)
    print(f"[FileSaver] 💾 File written: {path}")