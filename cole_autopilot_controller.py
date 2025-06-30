from ghost_env import INFURA_KEY, VAULT_ADDRESS
import json
from datetime import datetime
import os

LOG_FILE = "logs/autopilot_run_log.json"
os.makedirs("logs", exist_ok=True)

def log_autopilot_run(config):
    log_entry = {
        "timestamp": datetime.now().isoformat(),
        "phase": config.get("phase"),
        "tasks": config.get("tasks")
    }

    logs = []
    if os.path.exists(LOG_FILE):
        with open(LOG_FILE, "r") as f:
            logs = json.load(f)

    logs.append(log_entry)
    with open(LOG_FILE, "w") as f:
        json.dump(logs[-300:], f, indent=2)

def scheduled_autopilot_run():
    config = build_run_config()
    cole_auto_run(config)
    log_autopilot_run(config)

def log_event():ef drop_files_to_bridge():