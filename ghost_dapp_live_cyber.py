# === FILE: ghost_dapp_live_cyber.py ===
import json
import time

CYBER_FILE = "ghost_cyber_state.json"

def load_cyber_state():
    try:
        with open(CYBER_FILE, "r") as f:
            return json.load(f)
    except:
        return {"aggression":0.5,"stealth":0.5,"greed":0.5,"propaganda_intensity":0.5}

def dapp_loop():
    print("[GhostDAppLive] 🖥️ Displaying ghost empire cyber state...")
    while True:
        cyber = load_cyber_state()
        print(f"[GhostDAppLive] AGG:{cyber['aggression']:.2f} STL:{cyber['stealth']:.2f} GRD:{cyber['greed']:.2f} PROP:{cyber['propaganda_intensity']:.2f}")
        time.sleep(30)

if __name__ == "__main__":
    dapp_loop()