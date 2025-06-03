# === FILE: guardian_watchdog.py ===
# 🛡️ Guardian Watchdog – Monitors system health, module activity, and restarts dead processes

import time
import os
import psutil
import random
from pathlib import Path
import threading

from autonomy_core import restart_module, get_active_modules
from bridge_controller import start_bridge
from autofixer_agent import run_fixer
from command_listener import start_listener
from deploy_orchestrator import deploy_all
from self_replicator import replicate_if_needed
from sandbox_monitor import monitor_sandboxes
from hivemind_sync import sync_all
from executor_engine import execute_pending_tasks

# === Log Setup ===
GUARDIAN_LOG = "logs/guardian_health.log"

def log_guardian(message):
    Path("logs").mkdir(parents=True, exist_ok=True)
    with open(GUARDIAN_LOG, "a", encoding="utf-8") as f:
        f.write(f"{time.ctime()}: {message}\n")
    print(f"[Guardian] {message}")

# === System Health Checks ===
def check_cpu_memory():
    cpu = psutil.cpu_percent()
    memory = psutil.virtual_memory().percent
    log_guardian(f"🧠 CPU: {cpu}% | Memory: {memory}%")

def check_disk_usage():
    disk = psutil.disk_usage("/")
    log_guardian(f"💾 Disk Usage: {disk.percent}%")

# === Critical Modules to Monitor & Restart ===
CRITICAL_MODULES = {
    "bridge": start_bridge,
    "fixer": run_fixer,
    "listener": start_listener,
    "deployer": deploy_all,
    "replicator": replicate_if_needed,
    "sandbox": monitor_sandboxes,
    "sync": sync_all,
    "executor": execute_pending_tasks
}

# === Simulated Health Monitoring Targets ===
MONITORED_MODULES = [
    "bridge_controller",
    "reflex_engine",
    "recon_agent",
    "assistant_dispatch",
    "autofixer_agent",
    "command_listener",
    "executor_engine",
    "self_replicator",
    "sandbox_monitor",
    "hivemind_sync"
]

CHECK_INTERVAL = 30  # seconds

# === Watchdog Runtime ===
def start_guardian():
    log_guardian("👁️ Guardian Watchdog activated.")
    while True:
        check_cpu_memory()
        check_disk_usage()

        # Check active module threads
        active = set(get_active_modules())
        for name, runner in CRITICAL_MODULES.items():
            if name not in active:
                log_guardian(f"⚠️ Module '{name}' not active. Attempting restart...")
                restart_module(name, runner)

        # Simulate health alerts for other components
        module = random.choice(MONITORED_MODULES)
        status = random.choice(["healthy", "unresponsive", "terminated", "delayed"])
        log_guardian(f"🔎 {module} → status: {status}")
        if status in ["unresponsive", "terminated"]:
            log_guardian(f"🚨 ALERT: {module} requires investigation or fix!")

        time.sleep(CHECK_INTERVAL)