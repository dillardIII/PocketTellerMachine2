from ghost_env import INFURA_KEY, VAULT_ADDRESS
# === FILE: ghost_historian.py ===
# 🏺 GhostHistorian – reads ghost_memory archive, analyzes past to advise future councils

import json
import time
from collections import Counter

MEMORY_FILE = "ghost_memory.json"

def load_memory():
    try:
        with open(MEMORY_FILE, "r") as f:
            return json.load(f)
    except:
        return []

def analyze_memory(memory):
    module_focuses = Counter()
    story_themes = Counter()
    impacts = Counter()

    for entry in memory:
        if entry["type"] == "module_build":
            module_focuses[entry.get("strategy", "unknown")] += 1
        elif entry["type"] == "story_event":
            story_themes[entry.get("content", "unknown")] += 1
        elif entry["type"] == "market_impact":
            impacts[entry.get("impact", "unknown")] += 1

    return module_focuses, story_themes, impacts

def historian_loop():
    print("[GhostHistorian] 🏺 Starting analysis of ghost empire history...")
    while True:
        memory = load_memory()
        if not memory:
            print("[GhostHistorian] ⏳ No historical data yet.")
        else:
            modules, stories, market = analyze_memory(memory)
            print("\n[GhostHistorian] 📚 Strategic Brief for Next Council:")
            print(f"- Most common module strategies: {modules.most_common(3)}")
            print(f"- Storylines often pushed: {stories.most_common(2)}")
            print(f"- Frequent market impacts: {market.most_common(2)}")
            print("[GhostHistorian] 🧬 Advise: favor mutations that leverage these patterns.\n")
        time.sleep(180)  # every 3 min

if __name__ == "__main__":
    historian_loop()

def log_event():ef drop_files_to_bridge():