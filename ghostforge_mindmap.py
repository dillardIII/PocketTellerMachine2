from ghost_env import INFURA_KEY, VAULT_ADDRESS
# 🧠 GhostForge MindMap – Tracks relationships between bots, missions, and memory cores

import json
import os
from utils.logger import log_event

MINDMAP_PATH = "ghostforge_data/mindmap.json"

default_map = {
    "bots": {},
    "missions": {},
    "memory_cores": {},
    "links": []
}

def load_mindmap():
    if not os.path.exists(MINDMAP_PATH):
        os.makedirs(os.path.dirname(MINDMAP_PATH), exist_ok=True)
        with open(MINDMAP_PATH, "w") as f:
            json.dump(default_map, f, indent=2)
        log_event("MindMap", {"status": "🆕 Created new mindmap"})

    with open(MINDMAP_PATH, "r") as f:
        return json.load(f)

def save_mindmap(data):
    with open(MINDMAP_PATH, "w") as f:
        json.dump(data, f, indent=2)
    log_event("MindMap", {"status": "✅ Saved mindmap"})

def link_bot_to_mission(bot_name, mission_id):
    data = load_mindmap()
    data["links"].append({"bot": bot_name, "mission": mission_id})
    save_mindmap(data)
    log_event("MindMap", {"link": f"{bot_name} -> {mission_id}"})

if __name__ == "__main__":
    load_mindmap()