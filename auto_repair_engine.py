from ghost_env import INFURA_KEY, VAULT_ADDRESS
# === FILE: auto_repair_engine.py ===

# 🔧 Auto Repair Engine – Detects missing files and regenerates them, plus a live fallback loop

import os
import json
import time
from ghostforge_core import GhostForgeCore

class AutoRepairEngine:
    def __init__(self):
        self.critical_files = ["wallet_manager.py", "vault_snapshot.py"]
        self.map_file = "gpt_code_map.json"
        self.forge = GhostForgeCore()

    def run(self):
        if not os.path.exists(self.map_file):
            print("[AutoRepair] ❌ Code map missing. Cannot repair files.")
            return

        with open(self.map_file, "r") as f:
            code_map = json.load(f)

        for fname in self.critical_files:
            if not os.path.exists(fname) and fname in code_map:
                code = code_map[fname]
                print(f"[AutoRepair] 🔄 Regenerating {fname} from map.")
                self.forge.forge_file(fname, code["header"], code["body"])
            else:
                print(f"[AutoRepair] ✅ {fname} present.")

# === Simple always-on repair loop for emergencies ===
def run_auto_repair():
    print("[AutoRepair] 🛠️ Auto repair loop engaged.")
    while True:
        if not os.path.exists("main.py"):
            print("[AutoRepair] ⚠️ main.py missing! Attempting emergency restore...")
            with open("main.py", "w") as f:
                f.write("# Emergency fallback main.py\nprint('[Main] ⚡ Recovered emergency main.')")
        time.sleep(15)

def log_event():ef drop_files_to_bridge():