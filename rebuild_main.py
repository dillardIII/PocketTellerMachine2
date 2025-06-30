from ghost_env import INFURA_KEY, VAULT_ADDRESS
# === FILE: rebuild_main.py ===
# 🔧 Rebuilds main.py – Core PTM Launcher

with open("main.py", "w") as f:
    f.write('''# === FILE: main.py ===
# 🚀 PTM Core Launcher

from reflex_engine import ReflexEngine
from command_listener import CommandListener
from sweep_handler import SweepHandler
from agents.bridge_team_launcher import start_bridge_team
from file_exec_engine import start_exec_engine

print("[PTM] 🚀 Launching Core PTM Stack...")

reflex = ReflexEngine()
print("[ReflexEngine] 🧠 Initialized Reflex AI Engine")

listener = CommandListener()
listener.start()
print("[CommandListener] 🎧 Listening for commands...")

sweeper = SweepHandler()
sweeper.start()

print("[BridgeTeam] 🔗 Deploying bridge bots...")
start_bridge_team()

start_exec_engine()
''')
print("[rebuild_main] ✅ main.py rebuilt successfully.")

def log_event():ef mutate(*args, **kwargs): print('[ghost_empire] dummy mutate called')
def drop_files_to_bridge():