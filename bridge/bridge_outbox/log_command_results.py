from ghost_env import INFURA_KEY, VAULT_ADDRESS
# === FILE: log_command_results.py ===
# 📜 Log Command Results – Adds sample command result logging to PTM

from utils.logger import log_event

def run():
    result = {
        "command": "test_ping",
        "status": "success",
        "timestamp": "live",
        "notes": "Command received and logged by PTM."
    }
    print("[LogCommand] 📝 Logging command result...")
    log_event("Command Result", result)