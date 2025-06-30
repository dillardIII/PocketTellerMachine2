from ghost_env import INFURA_KEY, VAULT_ADDRESS
# === FILE: macro_daemon.py ===
# ⚙️ MacroDaemon – Core for autonomous macro generation, management, and execution

import os
import json
import time
import subprocess
from datetime import datetime
from utils.logger import log_event
from utils.file_utils import save_json_file, load_json_file

MACRO_DIR = "macros"
MACRO_LOG = "memory/macro_activity_log.json"

class MacroDaemon:
    def __init__(self):
        os.makedirs(MACRO_DIR, exist_ok=True)
        self.macro_registry = self._load_registry()
        print("[MacroDaemon] ⚙️ Initialized Macro Core.")

    def _load_registry(self):
        registry_path = os.path.join(MACRO_DIR, "macro_registry.json")
        if os.path.exists(registry_path):
            return load_json_file(registry_path)
        else:
            default = {}
            save_json_file(registry_path, default)
            return default

    def create_macro(self, name, actions, description="", author="PTM"):
        macro_file = os.path.join(MACRO_DIR, f"{name}.json")
        macro = {
            "name": name,
            "description": description,
            "author": author,
            "created_at": str(datetime.utcnow()),
            "actions": actions
        }
        save_json_file(macro_file, macro)
        self.macro_registry[name] = macro_file
        self._save_registry()
        log_event("Macro Created", macro)
        print(f"[MacroDaemon] ✅ Macro created: {name}")
        return True

    def execute_macro(self, name):
        if name not in self.macro_registry:
            print(f"[MacroDaemon] ❌ Macro not found: {name}")
            return False

        macro_path = self.macro_registry[name]
        macro = load_json_file(macro_path)
        print(f"[MacroDaemon] 🚀 Executing macro: {name}")

        for step in macro["actions"]:
            command = step.get("command")
            if command:
                try:
                    print(f"  🔸 Running: {command}")
                    subprocess.run(command, shell=True)
                    time.sleep(step.get("delay", 1))
                except Exception as e:
                    print(f"[MacroDaemon] ⚠️ Error in macro step: {e}")
        
        log_event("Macro Executed", {"name": name})
        return True

    def _save_registry(self):
        save_json_file(os.path.join(MACRO_DIR, "macro_registry.json"), self.macro_registry)

# === Test Hook ===
if __name__ == "__main__":
    daemon = MacroDaemon()
    test_actions = [
        {"command": "echo Hello, world", "delay": 1},
        {"command": "echo Macro Execution Complete", "delay": 1}
    ]
    daemon.create_macro("test_macro", test_actions, "Simple test macro")
    daemon.execute_macro("test_macro")