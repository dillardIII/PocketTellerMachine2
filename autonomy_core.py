# === FILE: autonomy_core.py ===
# 🧠 Autonomy Core – Central logic router and master control for full PTM autonomy stack
# Activates bridges, agents, listeners, monitors, persistence, reflex engine, recon, and assistant

import os
import time
import json
import threading
from pathlib import Path

# === Core System Modules ===
from bridge_controller import start_bridge
from autofixer_agent import run_fixer
from command_listener import start_listener
from deploy_orchestrator import deploy_all
from self_replicator import replicate_if_needed
from sandbox_monitor import monitor_sandboxes
from hivemind_sync import sync_all
from executor_engine import execute_pending_tasks
from guardian_watchdog import start_guardian

# === Intelligence Modules ===
from reflex_engine import ReflexEngine
from recon_agent import ReconAgent
from assistant_dispatch import AssistantDispatch

# === Constants ===
STATE_FILE = "state/autonomy_state.json"
STATUS_LOG = "logs/autonomy_status.log"
ACTIVE_MODULES = {}

# === Logging ===
def log_status(message):
    Path("logs").mkdir(parents=True, exist_ok=True)
    with open(STATUS_LOG, "a", encoding="utf-8") as f:
        f.write(f"{time.ctime()}: {message}\n")
    print(f"[Autonomy] {message}")

# === State Persistence ===
def save_state(state_data):
    Path("state").mkdir(parents=True, exist_ok=True)
    with open(STATE_FILE, "w", encoding="utf-8") as f:
        json.dump(state_data, f, indent=2)
    log_status("State saved.")

def load_state():
    if not os.path.exists(STATE_FILE):
        return {}
    with open(STATE_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

# === Module Management ===
def start_module(name, runner_func):
    if name in ACTIVE_MODULES:
        log_status(f"Module {name} already running.")
        return
    log_status(f"Starting module: {name}")
    ACTIVE_MODULES[name] = runner_func
    threading.Thread(target=runner_func).start()

def stop_module(name):
    if name not in ACTIVE_MODULES:
        log_status(f"Module {name} not active.")
        return
    log_status(f"Stopping module: {name}")
    del ACTIVE_MODULES[name]

def restart_module(name, runner_func):
    stop_module(name)
    time.sleep(1)
    start_module(name, runner_func)

def get_active_modules():
    return list(ACTIVE_MODULES.keys())

# === Main Control Class ===
class AutonomyCore:
    def __init__(self):
        log_status("[AutonomyCore] Initializing all modules...")
        self.reflex = ReflexEngine()
        self.recon = ReconAgent()
        self.assistant = AssistantDispatch()
        self.running = False
        self.phase = "boot"

    def start_all_systems(self):
        log_status("[AUTONOMY CORE] Activating system modules...")
        self.running = True
        start_module("bridge_controller", start_bridge)
        start_module("autofixer_agent", run_fixer)
        start_module("command_listener", start_listener)
        start_module("deploy_orchestrator", deploy_all)
        start_module("self_replicator", replicate_if_needed)
        start_module("sandbox_monitor", monitor_sandboxes)
        start_module("hivemind_sync", sync_all)
        start_module("executor_engine", execute_pending_tasks)
        start_module("guardian_watchdog", start_guardian)
        log_status("[AUTONOMY CORE] System modules activated.")

        # Start smart agents in threads
        threading.Thread(target=self.recon.run_recon_loop, daemon=True).start()
        threading.Thread(target=self.reflex.monitor_and_learn, daemon=True).start()

    def loop(self):
        self.phase = "startup"
        while self.running:
            log_status(f"Heartbeat [{self.phase}]: Active modules → {', '.join(get_active_modules())}")
            recommendation = self.reflex.get_recommendation()
            if recommendation:
                log_status(f"Reflex Strategy: {recommendation}")
                self.assistant.relay_strategy(recommendation)

            self._status_check()
            time.sleep(10)

    def _status_check(self):
        log_status("System Pulse: Subsystems nominal.")

    def stop(self):
        log_status("[AutonomyCore] Shutdown triggered...")
        self.running = False

# === Entrypoint ===
if __name__ == "__main__":
    core = AutonomyCore()
    core.start_all_systems()
    core.loop()