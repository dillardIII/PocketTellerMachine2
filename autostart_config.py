from ghost_env import INFURA_KEY, VAULT_ADDRESS
# === FILE: autostart_config.py ===

# 🚀 AutoStart Config – Initializes core modules when PTM boots

import threading
from reflex_engine import ReflexEngine
from command_listener import CommandListener
from sweep_handler import SweepHandler
from bridge_team_launcher import start_bridge_team
from file_exec_engine import start_exec_engine
from whisper_listener import start_whisper_listener
from net_recovery_loop import recovery_sweep
from reflex_feedback_loop import monitor_and_adapt

def boot_all_systems():
    print("[AutoStart] 🚀 Launching full PTM stack...")

    recovery_sweep()
    reflex = ReflexEngine()
    whisper_thread = threading.Thread(target=start_whisper_listener, daemon=True)
    listener = CommandListener()
    sweeper = SweepHandler()

    whisper_thread.start()
    listener.start()
    sweeper.start()

    start_bridge_team()
    start_exec_engine()

    monitor_and_adapt()

def log_event():ef drop_files_to_bridge():