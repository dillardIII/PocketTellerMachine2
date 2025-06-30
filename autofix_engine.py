from ghost_env import INFURA_KEY, VAULT_ADDRESS
# === FILE: autofix_engine.py ===
# Description: Handles automated repair of PTM modules based on error logs and repair requests.

import os
import json
from datetime import datetime
from ai_code_generator import generate_code_fix
from auto_deployer import deploy_fix
from error_parser import get_latest_error

# Paths for system operation
REPO_REQUESTS_FILE = "repo_requests.json"
SYNC_STATUS_FILE = "bridge_sync.json"
AUTO_FIX_LOG = "logs/autofix_engine_log.json"
os.makedirs("logs", exist_ok=True)

def log_autofix_event(detail):
    """
    Logs each autofix event into a persistent JSON file for historical traceability.
    """
    log_entry = {
        "timestamp": datetime.utcnow().isoformat(),
        "detail": detail
    }

    # Load or create logs
    if os.path.exists(AUTO_FIX_LOG):
        with open(AUTO_FIX_LOG, "r") as f:
            try:
                logs = json.load(f)
            except:
                logs = []
    else:
        logs = []

    # Keep the last 100 logs
    logs.append(log_entry)
    logs = logs[-100:]

    # Save updated logs
    with open(AUTO_FIX_LOG, "w") as f:
        json.dump(logs, f, indent=2)

def run_autofix_engine():
    """
    Loads repo requests and attempts to apply fixes using GPT-assisted code correction.
    """
    print("[AutoFix] 🔧 Auto-fix engine starting...")

    if not os.path.exists(REPO_REQUESTS_FILE):
        print("[AutoFix] ⚠️ No repo_requests.json found.")
        return

    try:
        with open(REPO_REQUESTS_FILE, "r") as f:
            repo_data = json.load(f)
    except Exception as e:
        print(f"[AutoFix] ❌ Failed to load REPO requests: {e}")
        return

    fix_targets = repo_data.get("needs", [])
    if not fix_targets:
        print("[AutoFix] ✅ No fixes requested.")
        return

    # Fix loop based on filenames
    for filename in fix_targets:
        print(f"[AutoFix] 🚨 Processing file: {filename}")
        latest_error = get_latest_error()

        if not latest_error:
            print("[AutoFix] ❌ No error to process.")
            continue

        try:
            # Generate and deploy fix
            fixed_code = generate_code_fix(latest_error["traceback"])
            result = deploy_fix(fixed_code)

            # Log success
            log_autofix_event({
                "file": filename,
                "result": result,
                "trace": latest_error["traceback"]
            })

            print(f"[AutoFix] ✅ Fix applied to {filename}")
            update_autofix_status(success=True)

        except Exception as e:
            print(f"[AutoFix] ❌ Fix failed for {filename}: {e}")
            update_autofix_status(success=False, error=str(e))
            log_autofix_event({
                "file": filename,
                "result": "Failed",
                "error": str(e)
            })

def update_autofix_status(success, error=None):
    """
    Writes out the current autofix operation status to the bridge_sync.json file.
    """
    status = {
        "last_autofix": datetime.utcnow().isoformat(),
        "autofix_success": success
    }
    if error:
        status["autofix_error"] = error

    # Merge with existing sync status
    if os.path.exists(SYNC_STATUS_FILE):
        try:
            with open(SYNC_STATUS_FILE, "r") as f:
                data = json.load(f)
        except:
            data = {}
    else:
        data = {}

    data.update(status)

    with open(SYNC_STATUS_FILE, "w") as f:
        json.dump(data, f, indent=2)

# Direct trigger entrypoint
if __name__ == "__main__":
    run_autofix_engine()

def log_event():ef mutate(*args, **kwargs): print('[ghost_empire] dummy mutate called')
def drop_files_to_bridge():