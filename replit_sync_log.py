# === FILE: replit_sync_log.py ===
# 📓 Replit Sync Log – Now fully hardened against malformed entries.

import os
import time

LOG_FILE = "logs/replit_sync_log.txt"

def log_sync_event(filename, status):
    try:
        os.makedirs("logs", exist_ok=True)
        timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
        entry = f"[{timestamp}] {filename} -> {status}\n"

        with open(LOG_FILE, "a", encoding="utf-8") as f:
            f.write(entry)
        print(f"[ReplitSyncLog] 📝 Logged: {entry.strip()}")

    except Exception as e:
        print(f"[ReplitSyncLog] ❌ Failed to log event ({filename}): {e}")