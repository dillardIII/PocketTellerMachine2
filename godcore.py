from ghost_env import INFURA_KEY, VAULT_ADDRESS
# === FILE: godcore.py ===
# 🧠 GodCore – Centralized orchestrator for all major PTM intelligence systems
# Manages mission control, module activation, AI harmony, and bridge coordination

import os
import time
from datetime import datetime
from utils.logger import log_event
from inspector_bot import InspectorBot
from ghostforge_core import GhostForge
from autonomy_core import start_autonomy_stack
from assistant_dispatch import AssistantDispatch

class GodCore:
    def __init__(self):
        self.inspector = InspectorBot()
        self.ghostforge = GhostForge()
        self.dispatch = AssistantDispatch()
        self.status = {
            "initialized_at": str(datetime.now()),
            "inspector_status": "pending",
            "ghostforge_status": "idle",
            "autonomy_status": "inactive",
            "logs": []
        }

    def initialize_system(self):
        print("[GodCore] 🧠 Initializing PTM Intelligence Core...")
        self.log("Boot sequence started.")
        self.run_inspection()
        self.activate_ghostforge()
        self.launch_autonomy_stack()
        self.greet()

    def run_inspection(self):
        print("[GodCore] 🔍 Running InspectorBot...")
        self.inspector.scan_project()
        self.status["inspector_status"] = "complete"
        self.log("InspectorBot completed scan.")

    def activate_ghostforge(self):
        print("[GodCore] ⚒️ Activating GhostForge Engine...")
        self.ghostforge.ensure_dir("generated_modules")
        self.status["ghostforge_status"] = "active"
        self.log("GhostForge initialized.")

    def launch_autonomy_stack(self):
        print("[GodCore] 🚀 Launching Autonomy Stack...")
        start_autonomy_stack()
        self.status["autonomy_status"] = "running"
        self.log("Autonomy Stack activated.")

    def greet(self):
        message = "Greetings, Commander. GodCore is fully online and operational."
        self.dispatch._speak(message, mood="proud")
        self.log("Greeting sent through Dispatch.")

    def log(self, message):
        timestamp = str(datetime.now())
        self.status["logs"].append({"timestamp": timestamp, "message": message})
        log_event("GodCore", message)

    def get_status(self):
        return self.status

# === Entry Point ===
if __name__ == "__main__":
    core = GodCore()
    core.initialize_system()