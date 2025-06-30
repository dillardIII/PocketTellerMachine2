# === FILE: ghost_avax_sniper.py ===
# 🏔️ GhostAvaxSniper – hunts thin liquidity on AVAX

import json
import random
import time

CYBER_FILE = "ghost_cyber_state.json"

def load_cyber_state():
    try:
        with open(CYBER_FILE, "r") as f:
            return json.load(f)
    except:
        return {"aggression":0.5,"stealth":0.5,"greed":0.5,"propaganda_intensity":0.5}

def probe_avax_liquidity():
    return round(random.uniform(0.1, 0.9), 2)

def sniper_loop():
    print("[GhostAvaxSniper] 🏔️ AVAX sniper live...")
    while True:
        cyber = load_cyber_state()
        liquidity = probe_avax_liquidity()
        if liquidity < 0.3:
            sniper_size = round(liquidity * cyber["aggression"] * cyber["greed"] * 8, 4)
            print(f"[GhostAvaxSniper] 🚀 Thin liquidity ({liquidity}) – sniping {sniper_size} AVAX")
        else:
            print(f"[GhostAvaxSniper] 🕵️ Normal liquidity ({liquidity}) – standing by.")
        time.sleep(90)

if __name__ == "__main__":
    sniper_loop()