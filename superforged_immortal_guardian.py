from ghost_env import INFURA_KEY, VAULT_ADDRESS
# 🚀 Superforged Immortal Empire with Self-Repair Guardian Loop

import threading
import time
from reflex_engine import ReflexEngine
from command_listener import CommandListener
from sweep_handler import SweepHandler
from meta_dispatcher import MetaDispatcher
from ghostforge_writer import ghostforge_loop
from vault_announcer import vault_announce_loop
from simulated_whisper import whisper_loop
from gpt_auto_seed_bot import auto_seed_loop
from self_forge_guardian import guardian_loop
from bridge_team_launcher import start_bridge_team

threads = []

print("[PTM] 🚀 Launching FULL SUPERFORGED IMMORTAL EMPIRE STACK...")

# === Reflex
reflex = ReflexEngine()
print("[ReflexEngine] 🧠 Initialized Reflex AI Engine")

# === Command Listener
listener = CommandListener()
listener.start()
threads.append(listener)
print("[CommandListener] 🎧 Listening for commands...")

# === Sweep
sweeper = SweepHandler()
sweeper.start()
threads.append(sweeper)
print("[SweepHandler] 🧹 Monitoring system...")

# === Bridge Bots
print("[BridgeTeam] 🔗 Deploying bridge drop & pickup bots...")
start_bridge_team()

# === Utility to spawn all loops
def start_loop(target, name):
    t = threading.Thread(target=target, name=name, daemon=True)
    t.start()
    threads.append(t)

# === Core Autonomous Loops
start_loop(ghostforge_loop, "GhostForge")
start_loop(vault_announce_loop, "VaultAnnouncer")
start_loop(whisper_loop, "SimWhisper")
start_loop(auto_seed_loop, "GPTAutoSeeder")
start_loop(guardian_loop, "SelfForgeGuardian")

# === MetaDispatcher
dispatcher = MetaDispatcher()
t = threading.Thread(target=dispatcher.start_task_monitor, name="MetaDispatcher", args=(30,), daemon=True)
t.start()
threads.append(t)

# === Keep alive
try:
    while True:
        time.sleep(10)
        print("[PTM] 💓 Empire Heartbeat – all systems nominal.")
except KeyboardInterrupt:
    print("\n[PTM] ⛔ Shutting down empire...")

def log_event():ef drop_files_to_bridge():