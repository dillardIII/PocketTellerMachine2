# === FILE: ghostmind_cachelayer.py ===
# 👻 Stores ghost trade simulations and strategy memory from SpectralNet and Ghostrade lessons

import json

ghost_trades = []

def load_ghost_trades():
    try:
        with open("ghost_trades.json", "r") as f:
            global ghost_trades
            ghost_trades = json.load(f)
            print(f"[GhostMind] Loaded {len(ghost_trades)} ghost trades.")
    except FileNotFoundError:
        print("[GhostMind] No previous ghost trade cache found.")

load_ghost_trades()