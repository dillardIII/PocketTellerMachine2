# 🧬 GhostOS Init – Initializes core settings, state memory, and boot sequences

import os
import json
from utils.logger import log_event

GHOSTOS_CONFIG_PATH = "config/ghostos_config.json"
GHOSTOS_STATE_PATH = "config/ghostos_state.json"

DEFAULT_CONFIG = {
    "autostart_modules": [
        "ghostforge_core.py",
        "reflex_engine.py",
        "command_listener.py",
        "vault_profit_trigger.py",
        "bridge_pickup_agent.py",
        "bridge_drop_agent.py",
        "ptm_error_handler.py"
    ],
    "voice_enabled": True,
    "mood_sync_enabled": True,
    "autobuilder_on_boot": True
}

DEFAULT_STATE = {
    "boot_count": 0,
    "last_boot": None,
    "active_bots": [],
    "errors_detected": [],
    "last_repair": None
}

def init_ghostos():
    os.makedirs("config", exist_ok=True)

    if not os.path.exists(GHOSTOS_CONFIG_PATH):
        with open(GHOSTOS_CONFIG_PATH, "w") as f:
            json.dump(DEFAULT_CONFIG, f, indent=2)
        log_event("GhostOS", {"config": "✅ Created default config"})

    if not os.path.exists(GHOSTOS_STATE_PATH):
        with open(GHOSTOS_STATE_PATH, "w") as f:
            json.dump(DEFAULT_STATE, f, indent=2)
        log_event("GhostOS", {"state": "✅ Created default state"})

    print("[GhostOS] ⚙️ Init complete.")

if __name__ == "__main__":
    init_ghostos()