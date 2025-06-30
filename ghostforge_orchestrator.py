from ghost_env import INFURA_KEY, VAULT_ADDRESS
# === FILE: ghostforge_orchestrator.py ===
# 🔁 GhostForge Orchestrator – Runs GhostForge loop and dispatches AI file generation

import json
import time
from ai_coder_engine import AICoder
from utils.logger import log_event
from utils.file_utils import save_file, list_missing_files

TASK_FILE = "ghostforge_tasks.json"
MEMORY_FILE = "ghostforge_memory.json"

class GhostForgeOrchestrator:
    def __init__(self):
        self.coder = AICoder()
        print("[GhostForge] 🔁 Orchestrator online.")

    def load_tasks(self):
        try:
            with open(TASK_FILE, "r") as f:
                return json.load(f)
        except:
            return []

    def save_memory(self, record):
        try:
            if not isinstance(record, dict):
                return
            memory = []
            if os.path.exists(MEMORY_FILE):
                with open(MEMORY_FILE, "r") as f:
                    memory = json.load(f)
            memory.append(record)
            with open(MEMORY_FILE, "w") as f:
                json.dump(memory, f, indent=2)
        except Exception as e:
            print(f"[GhostForge] ⚠️ Failed to save memory: {e}")

    def run(self):
        print("[GhostForge] ⚙️ Running self-coding loop...")
        while True:
            tasks = self.load_tasks()
            for task in tasks:
                filename = task.get("filename")
                purpose = task.get("purpose")
                seed = task.get("seed", "")
                print(f"[GhostForge] 🧠 Generating: {filename}")
                self.coder.generate_file(filename, purpose, seed)
                log_event("GhostForgeFileGenerated", {
                    "file": filename,
                    "purpose": purpose
                })
                self.save_memory({
                    "filename": filename,
                    "purpose": purpose,
                    "seed": seed,
                    "status": "written"
                })

            # Sweep for missing files and queue them
            missing = list_missing_files()
            for m in missing:
                filename = m["path"]
                purpose = m["purpose"]
                seed = m["base_code"]
                print(f"[GhostForge] 🛠️ Auto-task for missing: {filename}")
                self.coder.generate_file(filename, purpose, seed)
                log_event("GhostForgeAutoFix", {
                    "file": filename,
                    "purpose": purpose
                })
                self.save_memory({
                    "filename": filename,
                    "purpose": purpose,
                    "seed": seed,
                    "status": "auto-fixed"
                })

            time.sleep(60)