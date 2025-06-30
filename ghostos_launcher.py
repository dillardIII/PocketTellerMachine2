from ghost_env import INFURA_KEY, VAULT_ADDRESS
# 🚀 GhostOS Launcher – Boots up GhostOS modules, starts error handling and monitoring

import subprocess
import json
import time
import os
from utils.logger import log_event

CONFIG_PATH = "config/ghostos_config.json"
STATE_PATH = "config/ghostos_state.json"

def load_config():
    with open(CONFIG_PATH, "r") as f:
        return json.load(f)

def update_boot_state():
    state = {}
    if os.path.exists(STATE_PATH):
        with open(STATE_PATH, "r") as f:
            state = json.load(f)

    state["boot_count"] = state.get("boot_count", 0) + 1
    state["last_boot"] = time.strftime("%Y-%m-%d %H:%M:%S")

    with open(STATE_PATH, "w") as f:
        json.dump(state, f, indent=2)

    log_event("GhostOS", {"boot_count": state["boot_count"]})

def launch_modules(modules):
    for module in modules:
        try:
            subprocess.Popen(["python", module])
            log_event("GhostOS", {"launched": module})
        except Exception as e:
            log_event("GhostOS", {"error": str(e), "module": module})

def ghostos_launch():
    print("[GhostOS] 🚀 Launching system...")
    config = load_config()
    update_boot_state()

    if config.get("autobuilder_on_boot", False):
        try:
            subprocess.Popen(["python", "ghostforge_autobuilder.py"])
            log_event("GhostOS", {"autobuilder": "✅ Started"})
        except Exception as e:
            log_event("GhostOS", {"autobuilder": "❌ Failed", "error": str(e)})

    launch_modules(config.get("autostart_modules", []))

if __name__ == "__main__":
    ghostos_launch()