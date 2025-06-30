from ghost_env import INFURA_KEY, VAULT_ADDRESS
# === FILE: autonomy_core.py ===
# 🧠 Autonomy Core – Activates bridges, agents, monitors, reflex engine, listener, and logs full system self-control

import os
import threading
import time
from reflex_engine import ReflexEngine
from command_listener import start_listener
from sweep_handler import SweepHandler
from bridge_drop_agent import drop_files_to_bridge
from bridge_pickup_agent import pick_up_from_bridge
from utils.logger import log_event

class AutonomyCore:
    def __init__(self):
        print("[AutonomyCore] 🧠 Initializing full autonomy stack...")
        self.reflex = ReflexEngine()
        self.sweeper = SweepHandler()

    def start_all_systems(self):
        print("[AutonomyCore] 🔋 Booting all systems...")

        # Start bridge agents
        threading.Thread(target=drop_files_to_bridge, daemon=True).start()
        threading.Thread(target=pick_up_from_bridge, daemon=True).start()

        # Start command listener
        threading.Thread(target=start_listener, daemon=True).start()

        # Start reflex checks
        threading.Thread(target=self.reflex.start_monitoring, daemon=True).start()

        # Log boot complete
        log_event("Autonomy Online", {"status": "Full AI system active"})

    def run_sweep(self):
        print("[AutonomyCore] 🧹 Initiating full system sweep...")
        return self.sweeper.full_system_sweep()