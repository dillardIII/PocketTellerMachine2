# === FILE: ghostmind_clone_engine.py ===
# 🧬 Clone Engine – Create synthetic twins of PTM with memory + mood + strategy settings

import json
import shutil
from datetime import datetime
from utils.logger import log_event

CLONE_DIR = "clones/"

class GhostMindCloneEngine:
    def __init__(self):
        self.destination = CLONE_DIR

    def create_clone(self, clone_name):
        timestamp = str(datetime.now())
        clone_path = f"{CLONE_DIR}{clone_name}_{timestamp.replace(' ', '_').replace(':', '-')}/"

        try:
            shutil.copytree("memory/", clone_path)
            log_event(f"🧪 GhostMind Clone created: {clone_name}")
            return {"clone": clone_name, "path": clone_path}
        except Exception as e:
            log_event(f"💥 Clone failed: {e}")
            return {"error": str(e)}

# Example clone
if __name__ == "__main__":
    cloner = GhostMindCloneEngine()
    cloner.create_clone("PTM_Shadow_Alpha")