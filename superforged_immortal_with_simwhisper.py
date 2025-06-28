# === FILE: superforged_immortal_with_simwhisper.py ===
# 💀 PTM Empire – Superforged Immortal Combined with Simulated Whisper Voice Commands

import threading
import time
import os
import json
import random

# === Vault ===
VAULT_FILE = "vault_data.json"
COMMAND_FILE = "whisper_commands.txt"

def load_vault():
    if not os.path.exists(VAULT_FILE):
        return {"metamask_balance": "0.0 ETH", "latest_tokens": [], "payouts": []}
    with open(VAULT_FILE, "r") as f:
        return json.load(f)

def save_vault(data):
    with open(VAULT_FILE, "w") as f:
        json.dump(data, f, indent=2)

# === GuardianForge Self-Repair ===
def guardian_forge_self_repair():
    CORE_FILES = [
        "main.py", "file_exec_engine.py", "autonomous_trade_executor.py",
        "emotion_engine.py", "ghostforge_writer.py", "meta_dispatcher.py",
        "skypiea_node.py", "neural_predictor.py", "high_risk_manager.py"
    ]
    while True:
        for f in CORE_FILES:
            if not os.path.exists(f):
                print(f"[GuardianForge] 🚨 {f} missing – rebuilding...")
                with open(f, "w") as rebuilt:
                    rebuilt.write(f"# {f} auto-rebuilt by GuardianForge\n")
                    rebuilt.write("print('[GuardianForge] ✅ Placeholder rebuild.')\n")
                print(f"[GuardianForge] ✅ {f} restored.")
        time.sleep(60)

# === Vault Restore Sync ===
def vault_restore_sync():
    while True:
        vault_data = {
            "metamask_balance": f"{round(random.uniform(0.1, 2.0), 3)} ETH",
            "latest_tokens": ["$GHOST", "$PTM", "$SKYPIEA"],
            "last_sync": time.ctime()
        }
        save_vault(vault_data)
        print(f"[VaultRestore] 🔄 Synced vault data at {time.ctime()}")
        time.sleep(60)

# === Simulated Whisper Command Engine ===
def simulated_whisper_loop():
    print("[SimWhisper] 🎧 Watching 'whisper_commands.txt' for simulated voice commands...")
    while True:
        if os.path.exists(COMMAND_FILE):
            with open(COMMAND_FILE, "r") as f:
                command = f.read().strip().lower()
            if command:
                print(f"[SimWhisper] 🗣️ Command: '{command}'")
                if "trigger payout" in command:
                    payout_engine()
                elif "run vault scan" in command:
                    vault_scan()
                else:
                    print("[SimWhisper] 🤔 Unrecognized command.")
                open(COMMAND_FILE, "w").close()
        time.sleep(5)

def payout_engine():
    vault = load_vault()
    amount = round(random.uniform(0.01, 0.05), 4)
    vault.setdefault("payouts", []).append({
        "timestamp": time.ctime(),
        "amount": f"{amount} ETH",
        "to": "0xExternalWallet..."
    })
    save_vault(vault)
    print(f"[PayoutEngine] 💸 Simulated sending {amount} ETH to 0xExternalWallet...")

def vault_scan():
    vault = load_vault()
    print("[VaultScan] 🔍 Vault Contents:")
    print(json.dumps(vault, indent=2))

# === Inline MetaDispatcher ===
class MetaDispatcher:
    def __init__(self):
        self.active_tasks = {}
        self.loop_running = False

    def register_task(self, task_name, func):
        self.active_tasks[task_name] = func
        print(f"[MetaDispatcher] 📘 Registered: {task_name}")

    def start_task_monitor(self, interval=30):
        if self.loop_running:
            print("[MetaDispatcher] 🔁 Already running.")
            return
        self.loop_running = True
        print("[MetaDispatcher] 🧭 Task monitor started.")
        while self.loop_running:
            print("\n[MetaDispatcher] 📋 Current Tasks:")
            for name in self.active_tasks:
                print(f" - {name}")
            time.sleep(interval)

# === IMPORT THE CORE EMPIRE SYSTEMS ===
from reflex_engine import ReflexEngine
from command_listener import CommandListener
from sweep_handler import SweepHandler
from agents.bridge_team_launcher import start_bridge_team
from file_exec_engine import start_exec_engine
from loop_monitor import monitor_loop_health
from ghostforge_writer import ghostforge_loop
from autonomous_trade_executor import run_autonomous_trading
from skypiea_node import run_skypiea_loop
from neural_predictor import neural_predictor_loop
from high_risk_manager import run_high_risk_loop

threads = []
print("[PTM] 🚀 Launching FULL IMMORTAL EMPIRE STACK...")

# === Launch everything ===
reflex = ReflexEngine()
print("[ReflexEngine] 🧠 Initialized Reflex AI Engine")

listener = CommandListener()
listener.start(); threads.append(listener)
print("[CommandListener] 🎧 Listening...")

sweeper = SweepHandler()
sweeper.start(); threads.append(sweeper)
print("[SweepHandler] 🧹 Monitoring system...")

print("[BridgeTeam] 🔗 Deploying bridge bots...")
start_bridge_team()

def start_thread(target, name):
    t = threading.Thread(target=target, name=name)
    t.start()
    threads.append(t)

start_thread(start_exec_engine, "FileExecEngine")
start_thread(monitor_loop_health, "LoopMonitor")
start_thread(ghostforge_loop, "GhostForgeWriter")
start_thread(run_autonomous_trading, "AutoTrader")
start_thread(run_skypiea_loop, "SkypieaNode")
start_thread(neural_predictor_loop, "NeuralPredictor")
start_thread(run_high_risk_loop, "HighRiskManager")
start_thread(guardian_forge_self_repair, "GuardianForge")
start_thread(vault_restore_sync, "VaultRestore")
start_thread(simulated_whisper_loop, "SimWhisper")

dispatcher = MetaDispatcher()
t = threading.Thread(target=dispatcher.start_task_monitor, name="MetaDispatcher", args=(30,))
t.start(); threads.append(t)

# === Forever heartbeat ===
try:
    while True:
        time.sleep(10)
        print("[PTM] 💓 Immortal Empire heartbeat...")
except KeyboardInterrupt:
    print("\n[PTM] ⛔ Shutting down Immortal Empire Stack...")