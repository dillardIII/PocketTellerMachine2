"""
Cole Logger:
Unified event logging system for PTM bots and assistants.
Supports log tagging, severity levels, and routing outputs.
"""

import os
from datetime import datetime

LOG_DIR = "logs"
LOG_FILE = os.path.join(LOG_DIR, "event_log.txt")

# Make sure log directory exists
os.makedirs(LOG_DIR, exist_ok=True)

def get_timestamp():
    return datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S UTC")

def log_event(source, message, level="info"):
    """
    Logs an event to the log file with timestamp, source, and severity.
    """
    timestamp = get_timestamp()
    log_line = f"[{timestamp}] [{level.upper()}] [{source}] {message}"

    try:
        with open(LOG_FILE, "a") as f:
            f.write(log_line + "\n")
    except Exception as e:
        print(f"❌ Failed to write to log: {e}")

    # Optional: also print to terminal
    print(log_line)

def log_info(message):
    log_event("System", message, level="info")

def log_warning(message):
    log_event("System", message, level="warn")

def log_error(message):
    log_event("System", message, level="error")

# Manual test
if __name__ == "__main__":
    log_info("✅ Cole Logger test: info")
    log_warning("⚠️ Cole Logger test: warning")
    log_error("❌ Cole Logger test: error")