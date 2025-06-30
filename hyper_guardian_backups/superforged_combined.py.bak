# === FILE: superforged_combined.py ===
# 🚀 PTM Empire – Superforged Combined Launcher + MetaDispatcher bound inside

import threading
import time

# === INLINE MetaDispatcher CLASS ===
class MetaDispatcher:
    def __init__(self):
        self.active_tasks = {}
        self.loop_running = False

    def register_task(self, task_name, func):
        self.active_tasks[task_name] = func
        print(f"[MetaDispatcher] 📘 Registered: {task_name}")

    def list_status(self):
        print("\n[MetaDispatcher] 📋 Current Tasks:")
        for name in self.active_tasks:
            print(f" - {name}")
        print("")

    def start_task_monitor(self, interval=30):
        if self.loop_running:
            print("[MetaDispatcher] 🔁 Already running.")
            return
        self.loop_running = True
        print("[MetaDispatcher] 🧭 Task monitor started.")
        while self.loop_running:
            self.list_status()
            time.sleep(interval)

    def stop(self):
        self.loop_running = False
        print("[MetaDispatcher] 🛑 Stopped.")

# === IMPORT PTM SYSTEMS ===
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

print("[PTM] 🚀 Launching Superforged Combined Empire Stack...")

# === Start Reflex Engine ===
reflex = ReflexEngine()
print("[ReflexEngine] 🧠 Initialized Reflex AI Engine")

# === Start Command Listener ===
listener = CommandListener()
listener.start()
threads.append(listener)
print("[CommandListener] 🎧 Listening for commands...")

# === Start Sweep Handler ===
sweeper = SweepHandler()
sweeper.start()
threads.append(sweeper)
print("[SweepHandler] 🧹 Monitoring system...")

# === Start Bridge Bots ===
print("[BridgeTeam] 🔗 Deploying bridge bots...")
start_bridge_team()

# === Start critical AI systems as non-daemon threads ===
def start_thread(target, name, *args):
    t = threading.Thread(target=target, name=name, args=args)
    t.start()
    threads.append(t)

start_thread(start_exec_engine, "FileExecEngine")
start_thread(monitor_loop_health, "LoopMonitor")
start_thread(ghostforge_loop, "GhostForgeWriter")
start_thread(run_autonomous_trading, "AutoTrader")
start_thread(run_skypiea_loop, "SkypieaNode")
start_thread(neural_predictor_loop, "NeuralPredictor")
start_thread(run_high_risk_loop, "HighRiskManager")

# === Start embedded MetaDispatcher ===
dispatcher = MetaDispatcher()
t = threading.Thread(target=dispatcher.start_task_monitor, name="MetaDispatcher", args=(30,))
t.start()
threads.append(t)

# === Heartbeat loop ===
try:
    while True:
        time.sleep(10)
        print("[PTM] 💓 Main heartbeat – ALL SYSTEMS IMMORTAL & ONLINE.")
except KeyboardInterrupt:
    print("\n[PTM] ⛔ Shutting down Superforged Empire...")