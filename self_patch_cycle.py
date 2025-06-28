"""
Self-Patch Cycle – PTM Auto-Healing + Bot Recovery System

Monitors critical modules, trade outcomes, error logs,
and triggers self-repair routines. Supports auto-restart,
fallback persona switching, or full system alert escalation.
"""

import os
import json
import time
from datetime import datetime
from fix_logger import GhostLogger  # ✅ Fixed: replaced ghost_logger with fix_logger
from command_dispatcher import dispatch

ERROR_LOG_FILE = "logs/error_watch.json"
MAX_FAILURES = 3
RETRY_WINDOW = 300  # seconds (5 minutes)

logger = GhostLogger()

def monitor_for_failures():
    if not os.path.exists(ERROR_LOG_FILE):
        with open(ERROR_LOG_FILE, "w") as f:
            json.dump([], f)

    with open(ERROR_LOG_FILE, "r") as f:
        errors = json.load(f)

    now = time.time()
    recent = [e for e in errors if now - e.get("timestamp", 0) < RETRY_WINDOW]
    return recent

def attempt_auto_patch():
    print("[🛠️ Self-Patch] Scanning error logs...")

    recent_errors = monitor_for_failures()
    persona_failures = {}

    for err in recent_errors:
        source = err.get("source", "Unknown")
        persona_failures[source] = persona_failures.get(source, 0) + 1

    for bot, count in persona_failures.items():
        if count >= MAX_FAILURES:
            logger.log(f"[AUTO-PATCH] Restarting module: {bot} ({count} failures)")
            restart_cmd = f"restart {bot.lower()}"
            dispatch(restart_cmd)
        else:
            logger.log(f"[AUTO-MONITOR] {bot} has {count} error(s), below threshold.")

def self_patch_loop():
    print("[♻️ Self-Healing Loop] Active. Watching logs and behavior...")
    while True:
        attempt_auto_patch()
        time.sleep(30)  # Check every 30 seconds

# Manual run
if __name__ == "__main__":
    self_patch_loop()