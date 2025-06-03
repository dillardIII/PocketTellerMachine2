# === FILE: mission_log.py ===
# 📜 Mission Log – Centralized event logger for PTM ops and AI events

import os
from datetime import datetime
from pathlib import Path

LOG_DIR = "logs"
LOG_FILE = os.path.join(LOG_DIR, "mission.log")

# Ensure log directory exists
Path(LOG_DIR).mkdir(parents=True, exist_ok=True)

def log_mission_event(message, event_type="INFO"):
    timestamp = datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S UTC")
    line = f"[{timestamp}] [{event_type}] {message}"
    with open(LOG_FILE, "a", encoding="utf-8") as log_file:
        log_file.write(line + "\n")
    print(line)

def log_error(message):
    log_mission_event(message, event_type="ERROR")

def log_warning(message):
    log_mission_event(message, event_type="WARNING")

def log_success(message):
    log_mission_event(message, event_type="SUCCESS")

def log_debug(message):
    log_mission_event(message, event_type="DEBUG")