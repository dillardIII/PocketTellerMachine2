from ghost_env import INFURA_KEY, VAULT_ADDRESS
# assistants/malik.py

import datetime
import os

LOG_FILE = "data/malik_log.txt"

# === Basic Reporting with Console and File Logging ===
def malik_report(message, level="INFO"):
    """
    Malik reports a message to the console and logs it to malik_log.txt.
    Level can be 'INFO', 'WARNING', or 'ERROR'.
    """
    timestamp = str(datetime.datetime.now())
    formatted_message = f"[{timestamp}] [Malik - {level.upper()}]: {message}"

    # Print to console
    print(formatted_message)

    # Ensure log directory exists
    os.makedirs("data", exist_ok=True)

    # Append to log file
    with open(LOG_FILE, "a") as f:
        f.write(formatted_message + "\n")

# === Advanced Reporting (Placeholder for future hooks) ===
def malik_advanced_report(message, level="INFO"):
    """
    Advanced reporting with logging and optional future hooks:
    - UI notification center
    - Voice assistant alert
    """
    malik_report(message, level)
    # Future enhancements here:
    # trigger_ui_alert(formatted_message)
    # trigger_voice_assistant(formatted_message)