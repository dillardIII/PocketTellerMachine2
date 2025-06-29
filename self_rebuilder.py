# 🔁 PTM Self-Rebuilder – Hardened
import os
import time
import traceback
from datetime import datetime
from pathlib import Path
import shutil
from error_parser import get_latest_error
from ai_code_generator import generate_code_fix_from_trace
from file_patcher import patch_file
from auto_deployer import deploy_fix
from diff_viewer import save_diff_report
from voice_repair_reporter import generate_voice_report
from file_auto_committer import auto_commit_file

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
    return not file_path or file_path == "unknown" or \
           file_path.startswith("/nix/") or file_path.startswith("/usr/") or "site-packages" in file_path

def attempt_restore(filepath):
    backup_path = os.path.join(DEFAULT_BACKUP_DIR, filepath)
    if os.path.exists(backup_path):
        dest_dir = os.path.dirname(filepath)
        Path(dest_dir).mkdir(parents=True, exist_ok=True)
        shutil.copy2(backup_path, filepath)
        print(f"[SelfRebuilder] ✅ Restored: {filepath}")
    else:
        print(f"[SelfRebuilder] ⚠️ Backup missing for: {filepath}")

def self_rebuilder_loop():
    print("[SELF-BUILDER] 🧠 Hardened self-rebuild loop running.")
    last_trace = None
    while True:
        try:
            rebuilder_status["mode"] = "auto"
            for module in ESSENTIAL_MODULES:
                if not os.path.exists(module):
                    print(f"[SelfRebuilder] 🧩 Missing: {module}")
                    attempt_restore(module)
            error = get_latest_error()
            if not error or not error.get("traceback"):
                log_status("No error found.")
                time.sleep(300)
                continue
            file_path = error.get("file")
            trace = error["traceback"]
            if is_system_file(file_path):
                print(f"[SelfRebuilder] ⚠️ Skipping file: {file_path}")
                time.sleep(60)
                continue
            if trace != last_trace:
                print(f"[SELF-BUILDER] ⚙️ Repairing: {file_path}")
                fix = generate_code_fix_from_trace(trace)
                original = open(file_path).read()
                diff = save_diff_report(original, fix, file_path)
                patch_result = patch_file(file_path, fix)
                deploy_result = deploy_fix(file_path, fix)
                generate_voice_report(file_path, "AI Repair Complete", deploy_result)
                auto_commit_file(file_path)
                log_status(f"Patched + deployed", file=file_path)
                last_trace = trace
            else:
                log_status("Same error, idle.")
        except Exception as e:
            log_status("Rebuild failed", exception=traceback.format_exc())
        time.sleep(600)