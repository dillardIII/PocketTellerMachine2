# === FILE: deeper_ghost_matrix.py ===
import os, json, time
from datetime import datetime

GHOST_FILE = "ghost_trade_log.json"

def deeper_ghost_loop():
    print("[DeeperGhost] 👻 Advanced memory weighting...")
    while True:
        if os.path.exists(GHOST_FILE):
            with open(GHOST_FILE, "r") as f:
                log = json.load(f)
            last = log[-10:]
            scores = {e["strategy"]: round(0.5 + 0.5 * i/10, 2) for i, e in enumerate(last)}
            print(f"[DeeperGhost] 🧮 Ranked weights: {scores}")
        else:
            print("[DeeperGhost] ⚠️ No ghost log yet.")
        time.sleep(50)