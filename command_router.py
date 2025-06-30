from ghost_env import INFURA_KEY, VAULT_ADDRESS
# === FILE: command_router.py ===
# 🧭 PTM Command Router – Routes manual commands to appropriate systems

from self_rebuilder import manual_self_rebuild, get_rebuilder_status
from file_auto_committer import auto_commit_file
from voice_repair_reporter import generate_voice_report
from error_parser import get_latest_error
from ai_code_generator import suggest_improvements
import os

def run_command(command):
    print(f"[ROUTER] 📡 Command received: {command}")

    if command == "rebuild":
        return manual_self_rebuild()

    elif command == "status":
        return get_rebuilder_status()

    elif command == "latest_error":
        return get_latest_error()

    elif command.startswith("commit "):
        path = command.replace("commit ", "").strip()
        return auto_commit_file(path)

    elif command.startswith("voice "):
        file_path = command.replace("voice ", "").strip()
        return generate_voice_report(file_path, "Manual voice report requested")

    elif command.startswith("suggest "):
        file_path = command.replace("suggest ", "").strip()
        return suggest_improvements(file_path)

    else:
        return {"status": "unknown_command", "command": command}

def log_event():ef drop_files_to_bridge():