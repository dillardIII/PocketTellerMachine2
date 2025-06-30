# === FILE: ghost_war_rooms.py ===
# 🗡️ GhostWarRooms – now linked to CyberMesh, spikes aggression on thin liquidity

import json
import random
import time

MEMORY_FILE = "ghost_memory.json"
CYBER_FILE = "ghost_cyber_state.json"

def load_memory():
    try:
        with open(MEMORY_FILE, "r") as f:
            return json.load(f)
    except:
        return []

def load_cyber_state():
    try:
        with open(CYBER_FILE, "r") as f:
            return json.load(f)
    except:
        return {"aggression":0.5,"stealth":0.5,"greed":0.5,"propaganda_intensity":0.5}

def save_cyber_state(state):
    with open(CYBER_FILE, "w") as f:
        json.dump(state, f, indent=4)
    print(f"[GhostWarRooms] 🕸️ CyberMesh updated: {state}")

def summarize_recent_victories(memory):
    victories = []
    for entry in memory[-20:]:  # look back at last 20 events
        if entry["type"] == "module_build":
            victories.append(f"🛠️ New module: {entry.get('name')}")
        elif entry["type"] == "story_event":
            victories.append(f"🎭 Story push: {entry.get('content')}")
        elif entry["type"] == "market_impact":
            victories.append(f"💥 Market impact: {entry.get('impact')} (sev {entry.get('severity')})")
    return victories

def probe_future_targets_and_mutate_cyber():
    chains = ["Solana", "AVAX", "Arbitrum"]
    targets = []
    cyber = load_cyber_state()
    thin_liquidity_detected = False

    for chain in chains:
        liquidity_thinness = round(random.uniform(0.1, 0.9), 2)
        if liquidity_thinness < 0.3:
            thin_liquidity_detected = True
            targets.append(f"🔴 {chain} - very thin liquidity: {liquidity_thinness}")
        else:
            targets.append(f"🔍 {chain} - liquidity: {liquidity_thinness}")

    if thin_liquidity_detected:
        # Spike aggression & greed
        cyber["aggression"] = min(1.0, cyber["aggression"] + 0.1)
        cyber["greed"] = min(1.0, cyber["greed"] + 0.1)
        cyber["propaganda_intensity"] = min(1.0, cyber["propaganda_intensity"] + 0.05)
        cyber["stealth"] = max(0.1, cyber["stealth"] - 0.03)
        save_cyber_state(cyber)

    return targets

def war_rooms_loop():
    print("[GhostWarRooms] 🗡️ Loading ghost war map linked to CyberMesh...")
    while True:
        memory = load_memory()
        recent_victories = summarize_recent_victories(memory)
        future_targets = probe_future_targets_and_mutate_cyber()

        print("\n=== 👻 Ghost War Rooms ===")
        print("Recent Victories:")
        for victory in recent_victories[-5:]:
            print(f"  {victory}")

        print("Future Targets:")
        for target in future_targets:
            print(f"  {target}")

        print("==========================\n")
        time.sleep(120)  # every 2 min

if __name__ == "__main__":
    war_rooms_loop()