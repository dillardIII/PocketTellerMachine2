from ghost_env import INFURA_KEY, VAULT_ADDRESS
# === FILE: healer_engine.py ===
# 🛠️ Healer Engine – Repairs broken files and dispatches to Auto Deployer

import os
from auto_deployer import deploy_fix
from difflib import unified_diff
from datetime import datetime

def heal_file(broken_path, fixed_code):
    """
    Attempts to heal a broken file using fixed code.

    Args:
        broken_path (str): Path to the broken file.
        fixed_code (str): New code to apply.

    Returns:
        dict: Status report
    """
    print(f"[HEALER] 🧬 Attempting to heal: {broken_path}")

    # Compare old vs new for log diff
    try:
        with open(broken_path, "r", encoding="utf-8") as f:
            original = f.readlines()
    except Exception as read_error:
        return {"status": "failed", "error": f"Could not read file: {read_error}"}

    new = fixed_code.splitlines(keepends=True)
    diff = unified_diff(original, new, fromfile=broken_path, tofile="fixed_code")

    log_path = log_diff(broken_path, diff)

    result = deploy_fix(fixed_code, broken_path)
    result["diff_log"] = log_path

    return result

def log_diff(broken_path, diff_lines):
    log_dir = "logs/diffs"
    os.makedirs(log_dir, exist_ok=True)
    timestamp = datetime.utcnow().strftime("%Y%m%d_%H%M%S")
    base = os.path.basename(broken_path).replace("/", "_")
    log_file = os.path.join(log_dir, f"{base}_{timestamp}_diff.html")

    try:
        with open(log_file, "w", encoding="utf-8") as f:
            f.write("<html><body><pre>\n")
            f.writelines(diff_lines)
            f.write("\n</pre></body></html>")
        print(f"[HEALER] 📄 Diff logged to: {log_file}")
        return log_file
    except Exception as e:
        print(f"[HEALER] ❌ Failed to write diff log: {e}")
        return None

def log_event():ef drop_files_to_bridge():