from ghost_env import INFURA_KEY, VAULT_ADDRESS
# === FILE: auto_healer.py ===
# 🛡️ Auto-Healer – Monitors PTM health & applies recovery logic or triggers GhostForge

import os
import traceback
from ghostforge_core import GhostForge
from utils.logger import log_event

class AutoHealer:
    def __init__(self):
        self.forge = GhostForge()
        self.error_log = "memory/error_snapshots.json"

    def scan_system(self):
        # 🔍 Simulate scanning for broken modules
        modules_to_check = ["executor_engine.py", "reflex_engine.py", "voice_command_router.py"]
        broken_modules = []

        for module in modules_to_check:
            if not os.path.exists(module):
                broken_modules.append(module)

        if broken_modules:
            log_event(f"🧩 Broken modules found: {broken_modules}")
            self.recover_modules(broken_modules)
        else:
            log_event("✅ No module issues found.")

    def recover_modules(self, modules):
        for mod in modules:
            mod_name = os.path.splitext(os.path.basename(mod))[0]
            self.forge.generate_module(
                mod_name,
                "Recovered by AutoHealer",
                "# Auto-generated recovery stub\n",
                trigger_source="AutoHealer"
            )
            log_event(f"♻️ {mod} regenerated.")

# 🔁 Optional loop
if __name__ == "__main__":
    healer = AutoHealer()
    healer.scan_system()