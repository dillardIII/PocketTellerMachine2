# === FILE: self_rebuilder.py ===
# 🔁 PTM Self-Rebuilder – Detects, Fixes, Deploys, and Learns
# ♻️ Also restores files from backup if missing

import os
import time
import traceback
from datetime import datetime
from pathlib import Path
import shutil

from error_parser import get_latest_error
from ai_code_generator import generate_code_fix_from_trace, suggest_improvements
from file_patcher import patch_file
from auto_deployer import deploy_fix
from diff_viewer import save_diff_report
from voice_repair_reporter import generate_voice_report
from file_auto_committer import auto_commit_file

# 🧠 Rebuilder State – Used for live UI or logging
rebuilder_status = {
    "last_run": None,
    "last_result": "Not started yet",
    "last_exception": None,
    "last_file": None,
    "mode": "idle"
}

ESSENTIAL_MODULES = [
    "core/ai_router.py",
    "core/ghost_sync.py",
    "logs",
    "state/init_report.json",
    "memory/ghostshade_core.json"
]

DEFAULT_BACKUP_DIR = "recovery_backups"

def log_status(result, file=None, exception=None):
    rebuilder_status["last_run"] = datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S UTC")
    rebuilder_status["last_result"] = result
    rebuilder_status["last_exception"] = str(exception) if exception else None
    rebuilder_status["last_file"] = file
    rebuilder_status["mode"] = "idle"

def is_system_file(file_path):
    return file_path.startswith("/nix/") or file_path.startswith("/usr/") or "site-packages" in file_path

# === Core Watchdog and Rebuild Loop ===
def self_rebuilder_loop():
    print("[SELF-BUILDER] 🧠 Self-Rebuild Loop started.")
    last_trace = None

    while True:
        try:
            rebuilder_status["mode"] = "auto"
            print("[SELF-BUILDER] 🔍 Scanning for errors...")

            # === Restore missing essential modules ===
            for module in ESSENTIAL_MODULES:
                if not os.path.exists(module):
                    print(f"[SelfRebuilder] 🧩 Missing: {module}")
                    attempt_restore(module)

            error = get_latest_error()
            if not error or not error.get("traceback"):
                log_status("No error to rebuild from.")
                time.sleep(300)
                continue

            file_path = error.get("file")
            trace = error["traceback"]

            if trace != last_trace and not is_system_file(file_path):
                print(f"[SELF-BUILDER] ⚙️ New error in {file_path}")
                fixed_code = generate_code_fix_from_trace(trace)
                if not fixed_code:
                    log_status("No code generated.", file=file_path)
                    continue

                with open(file_path, "r", encoding="utf-8") as f:
                    original_code = f.read()

                diff_path = save_diff_report(original_code, fixed_code, file_path)
                patch_result = patch_file(file_path, fixed_code)
                deploy_result = deploy_fix(file_path, fixed_code)

                generate_voice_report(file_path, "Auto-repair completed from traceback", deploy_result)
                auto_commit_file(file_path)

                with open("logs/self_rebuilder.log", "a") as log:
                    log.write(f"\n[{datetime.now()}] Rebuilt {file_path}:\n{trace}\nPatch: {patch_result}\nDeploy: {deploy_result}\nDiff: {diff_path}\n")

                log_status(f"Patch + Deploy OK", file=file_path)
                last_trace = trace
            else:
                log_status("Same error or system file, no new action.")
        except Exception as e:
            error_trace = traceback.format_exc()
            print(f"[SELF-BUILDER ERROR] ❌ {error_trace}")
            log_status("Rebuild failed", exception=error_trace)

        time.sleep(600)

def attempt_restore(filepath):
    backup_path = os.path.join(DEFAULT_BACKUP_DIR, filepath)
    if os.path.exists(backup_path):
        dest_dir = os.path.dirname(filepath)
        Path(dest_dir).mkdir(parents=True, exist_ok=True)
        shutil.copy2(backup_path, filepath)
        print(f"[SelfRebuilder] ✅ Restored: {filepath}")
    else:
        print(f"[SelfRebuilder] ⚠️ Backup missing for: {filepath}")

# === Manual Trigger ===
def manual_self_rebuild():
    try:
        rebuilder_status["mode"] = "manual"
        latest_error = get_latest_error()
        if not latest_error or not latest_error.get("traceback"):
            log_status("No error to repair.")
            return {"status": "no_error_found"}

        file_path = latest_error.get("file")
        trace = latest_error["traceback"]

        if is_system_file(file_path):
            print(f"[SELF-BUILDER] ⚠️ Skipping system file: {file_path}")
            return {"status": "skipped_system_file", "file": file_path}

        fix = generate_code_fix_from_trace(trace)

        with open(file_path, "r", encoding="utf-8") as f:
            original_code = f.read()

        diff_path = save_diff_report(original_code, fix, file_path)
        patch_result = patch_file(file_path, fix)
        deploy_result = deploy_fix(file_path, fix)

        generate_voice_report(file_path, "Manual rebuild triggered", deploy_result)
        auto_commit_file(file_path)

        log_status(f"Manual patch+deploy OK", file=file_path)
        return {
            "status": "fix_deployed",
            "patch": patch_result,
            "deploy": deploy_result,
            "diff": diff_path
        }
    except Exception as e:
        log_status("Manual rebuild failed", exception=traceback.format_exc())
        return {"status": "error", "message": str(e)}

# === Status Getter ===
def get_rebuilder_status():
    return rebuilder_status

# === Lightweight Repair Trigger ===
def rebuild_from_latest_error():
    print("[REBUILDER] 🛠 Starting self-repair cycle...")
    error = get_latest_error()

    if not error:
        return {"status": "no_error"}

    file_path = error.get("file")
    traceback_text = error.get("traceback") or error.get("error")

    if not file_path or not traceback_text or is_system_file(file_path):
        return {"status": "skipped"}

    fixed_code = generate_code_fix_from_trace(traceback_text)
    if not fixed_code:
        return {"status": "ai_failed"}

    patch_result = patch_file(file_path, fixed_code)
    if patch_result.get("status") != "success":
        return {"status": "patch_failed", "details": patch_result}

    commit_result = auto_commit_file(file_path)
    generate_voice_report(file_path, "AI repair applied", commit_result.get("status", "unknown"))

    return {
        "status": "repaired",
        "file": file_path,
        "commit": commit_result,
        "voice_report": True
    }