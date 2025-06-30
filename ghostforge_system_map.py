from ghost_env import INFURA_KEY, VAULT_ADDRESS
# 🗺️ GhostForge System Map – Blueprint(of all core services, files, and AI functions)

import json
from utils.logger import log_event

SYSTEM_MAP_PATH = "ghostforge_data/system_map.json"

SYSTEM_STRUCTURE = {
    "modules": [
        "ghostforge_core",
        "reflex_engine",
        "command_listener",
        "vault_profit_trigger",
        "bridge_pickup_agent",
        "bridge_drop_agent",
        "ghostforge_heartbeat",
        "ghostforge_memory_core",
        "ghostforge_autobuilder",
        "ptm_error_handler"
    ],
    "bots": {
        "inspectors": ["InspectorBot"],
        "builders": ["GhostForge"],
        "engineers": ["ReflexEngine"],
        "commanders": ["CommandListener"],
        "defenders": ["PTMErrorHandler"],
        "traders": ["MoCash", "Mentor", "Strategist"]
    },
    "folders": [
        "core", "bots", "routes", "scripts", "voices", "config", "vault", "ui", "bridge"
    ]
}

def write_system_map():
    try:
        with open(SYSTEM_MAP_PATH, "w") as f:
            json.dump(SYSTEM_STRUCTURE, f, indent=2)
        log_event("SystemMap", {"status": "✅ Map written to file"})
    except Exception as e:
        log_event("SystemMap", {"status": "❌ Error", "error": str(e)})

if __name__ == "__main__":
    write_system_map()