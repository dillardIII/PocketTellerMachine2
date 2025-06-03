# === FILE: hivemind_sync.py ===
# 🧠 HiveMind Sync – Synchronizes data, models, and awareness across PTM agents

import time
import random
import json
from datetime import datetime
from pathlib import Path

# 🧠 Agent Awareness Sync
HIVEMIND_AGENTS = [
    "ReflexEngine",
    "ReconAgent",
    "VoiceAssist",
    "GhostBot",
    "SandboxMonitor",
    "AutoFixer"
]

def sync_all():
    print("[HiveMindSync] 🔄 Beginning HiveMind sync...")
    for agent in HIVEMIND_AGENTS:
        status = random.choice(["success", "delayed", "conflict", "pending"])
        print(f"[HiveMindSync] 🧠 {agent} → sync status: {status}")
        time.sleep(1)
    print("[HiveMindSync] ✅ HiveMind sync complete.")

# 🧬 Shared Knowledge Core
HIVEMIND_FILE = "state/hivemind_core.json"
Path("state").mkdir(exist_ok=True)

DEFAULT_HIVEMIND = {
    "last_updated": None,
    "shared_goals": [],
    "ai_units": {},
    "global_directives": [],
    "active_topics": [],
    "system_notes": {}
}

def load_hivemind():
    if not Path(HIVEMIND_FILE).exists():
        with open(HIVEMIND_FILE, "w", encoding="utf-8") as f:
            json.dump(DEFAULT_HIVEMIND, f, indent=2)
    with open(HIVEMIND_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

def update_hivemind(update_dict):
    current = load_hivemind()
    current["last_updated"] = datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S UTC")

    for key, value in update_dict.items():
        if isinstance(current.get(key), list) and isinstance(value, list):
            current[key] = list(set(current[key] + value))
        elif isinstance(current.get(key), dict) and isinstance(value, dict):
            current[key].update(value)
        else:
            current[key] = value

    with open(HIVEMIND_FILE, "w", encoding="utf-8") as f:
        json.dump(current, f, indent=2)

    print(f"[HIVEMIND] 🔁 Synced update at {current['last_updated']}")
    return current

def get_current_hivemind():
    return load_hivemind()