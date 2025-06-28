# === FILE: auto_repair_engine.py ===

# 🔧 Auto Repair Engine – Detects missing files and regenerates them

import os
import json
from ghostforge_core import GhostForgeCore

class AutoRepairEngine:
    def __init__(self):
        self.critical_files = ["wallet_manager.py", "vault_snapshot.py"]
        self.map_file = "gpt_code_map.json"
        self.forge = GhostForgeCore()

    def run(self):
        if not os.path.exists(self.map_file):
            print("[AutoRepair] ❌ Code map missing.")
            return

        with open(self.map_file, "r") as f:
            code_map = json.load(f)

        for fname in self.critical_files:
            if not os.path.exists(fname) and fname in code_map:
                code = code_map[fname]
                self.forge.forge_file(fname, code["header"], code["body"])