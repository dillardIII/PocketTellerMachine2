# === FILE: reflex_macro_log.py ===
# 📓 Reflex Macro Log – Tracks auto-triggered scripts and their outcomes

import time
import os

LOG_FILE = "reflex_macro_log.txt"

def log_macro(trigger, result, bot="System"):
    entry = f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] [{bot}] Triggered: {trigger} → Result: {result}\n"
    with open(LOG_FILE, "a") as f:
        f.write(entry)
    print(f"[ReflexLog] 🧠 {entry.strip()}")

if __name__ == "__main__":
    log_macro("Dreamstate Planner", "Generated 5 tasks", "GhostBot")