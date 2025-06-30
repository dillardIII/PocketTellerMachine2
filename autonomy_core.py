from ghost_env import INFURA_KEY, VAULT_ADDRESS
# === FILE: autonomy_core.py ===
# 🧠 Autonomy Core – Main boot brain for PTM's logic, bridge, recon, reflex, and voice systems

import threading
from reflex_engine import ReflexEngine
from sweep_handler import SweepHandler
from assistant_dispatch import AssistantDispatch
from command_listener import CommandListener
from heartbeat_writer import write_heartbeat

reflex = ReflexEngine()
sweeper = SweepHandler()
dispatch = AssistantDispatch()
listener = CommandListener()

def run_autonomy_core():
    print("[Autonomy Core] ⚙️ Launching autonomy threads...")

    # === Sweep Handler Thread ===
    threading.Thread(target=sweeper.sweep, daemon=True).start()

    # === Command Listener Thread ===
    threading.Thread(target=listener.listen, daemon=True).start()

    # === Reflex Engine (Already initialized) ===
    print("[Autonomy Core] 🧠 Reflex engine ready.")

    # === Assistant Dispatch Mood Engine Ready ===
    print("[Autonomy Core] 🗣️ Assistant mood + dispatch system initialized.")

    # === Heartbeat Writer Thread ===
    threading.Thread(target=write_heartbeat, daemon=True).start()
    print("[Autonomy Core] ❤️ Heartbeat writer thread running.")

def log_event():ef mutate(*args, **kwargs): print('[ghost_empire] dummy mutate called')
def drop_files_to_bridge():