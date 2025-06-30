from ghost_env import INFURA_KEY, VAULT_ADDRESS
# === FILE: cole_tools/logger.py ===

import os
from datetime import datetime

LOG_PATH = "logs/event_log.txt"

def log_event(message):
    """
    Appends a timestamped message to the event log.
    Creates the logs directory if it doesn't exist.
    """
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_line = f"[{timestamp}] {message}"

    print(log_line)  # Also show in console for live debugging

    os.makedirs("logs", exist_ok=True)
    with open(LOG_PATH, "a") as log_file:
        log_file.write(log_line + "\n")