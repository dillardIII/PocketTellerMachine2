# === FILE: sandbox_monitor.py ===
# 🧪 Sandbox Monitor – Tracks file-based sandboxes & simulated agent activity

import os
import time
import random
from pathlib import Path

SANDBOX_DIR = "sandbox_envs"
MONITOR_LOG = "logs/sandbox_monitor.log"

SANDBOXES = [
    "TradeSim-A",
    "BotDev-Z",
    "ReflexTest",
    "OptionLab",
    "VoiceTrainer",
    "ChartRender-X"
]

# === Logger ===
def log_sandbox(message):
    Path("logs").mkdir(parents=True, exist_ok=True)
    with open(MONITOR_LOG, "a", encoding="utf-8") as f:
        f.write(f"{time.ctime()}: {message}\n")
    print(f"[Sandbox Monitor] {message}")

# === File-based sandbox watcher ===
def list_sandboxes():
    Path(SANDBOX_DIR).mkdir(parents=True, exist_ok=True)
    return [f for f in os.listdir(SANDBOX_DIR) if f.endswith(".py") or f.endswith(".json")]

# === Main Loop ===
def monitor_sandboxes():
    log_sandbox("🧪 Monitoring sandbox environments...")
    known_files = set(list_sandboxes())

    while True:
        # Check for file-level sandbox changes
        current_files = set(list_sandboxes())
        added = current_files - known_files
        removed = known_files - current_files

        for f in added:
            log_sandbox(f"📥 New sandbox file detected: {f}")
        for f in removed:
            log_sandbox(f"🗑️ Sandbox file removed: {f}")
        known_files = current_files

        # Simulated behavioral monitoring
        sandbox = random.choice(SANDBOXES)
        status = random.choice(["stable", "unstable", "crashed", "recovering"])
        log_sandbox(f"🔍 {sandbox} status: {status}")
        if status == "crashed":
            log_sandbox(f"⚠️ ALERT: {sandbox} has crashed. Recommend fix or restart.")

        time.sleep(15)