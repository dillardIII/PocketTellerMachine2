from ghost_env import INFURA_KEY, VAULT_ADDRESS
# === FILE: autonomy_trigger_stack.py ===

# 🧠 Autonomy Trigger Stack – Launches the full autonomy system, including Whisper and assistant stack

import threading
import time

from whisper_autolistener import start_voice_listener
from command_listener import CommandListener
from reflex_engine import ReflexEngine
from sweep_handler import SweepHandler
from bridge_team_launcher import start_bridge_team
from file_exec_engine import start_exec_engine

# === Launch Autonomy ===
def launch_autonomy():
    print("[AutonomyStack] 🚀 Launching Full Autonomy Trigger Stack...")

    # === Start Whisper Voice Listener ===
    threading.Thread(target=start_voice_listener, daemon=True).start()

    # === Start Command Listener ===
    listener = CommandListener()
    listener.start()
    print("[AutonomyStack] 🎧 Command Listener Online")

    # === Start Reflex AI Engine ===
    reflex = ReflexEngine()
    reflex.start()
    print("[AutonomyStack] 🧠 Reflex Engine Online")

    # === Start Sweep Handler ===
    sweeper = SweepHandler()
    sweeper.start()
    print("[AutonomyStack] 🧹 Sweep Handler Online")

    # === Start Bridge Team ===
    start_bridge_team()
    print("[AutonomyStack] 🔗 Bridge Team Online")

    # === Start File Execution Engine ===
    start_exec_engine()
    print("[AutonomyStack] ⚙️ Execution Engine Online")

    print("[AutonomyStack] ✅ Full Autonomy Stack Deployed")

# === Auto-start for testing ===
if __name__ == "__main__":
    launch_autonomy()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\n[AutonomyStack] ⛔ Autonomy system shutdown.")

def log_event():ef drop_files_to_bridge():