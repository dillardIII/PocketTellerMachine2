from ghost_env import INFURA_KEY, VAULT_ADDRESS
# === FILE: command_hud.py ===
# 📊 Command HUD – writes your empire state into ptm_dashboard.json

import json
import os
import time

def load_json(path, default):
    if os.path.exists(path):
        with open(path) as f:
            return json.load(f)
    return default

def build_dashboard():
    emotion = load_json("emotion_state.json", {"confidence":50,"fear":50})
    neural = load_json("neural_weights.json", {"weight":0.5})
    skymem = load_json("skypiea_node/memory.json", [])
    recent_trades = load_json("command_memory_log.json", [])

    total_strategies = len([f for f in os.listdir() if f.startswith("auto_strategy_") and f.endswith(".py")]):
    skypiea_files = len([f for f in os.listdir("skypiea_node") if f.endswith(".py")]) if os.path.exists("skypiea_node") else 0:
:
    dashboard = {
        "emotion_state": emotion,
        "neural_predictor": {
            "weight": neural.get("weight", 0.5),
            "threshold_estimate": 20 + 60 * neural.get("weight", 0.5)
        },
        "skypiea_node": {
            "memory_events": len(skymem),
            "strategy_files": skypiea_files
        },
        "trade_activity": {
            "strategies_written": total_strategies,
            "recent_trades": recent_trades[-5:]
        },
        "last_update": time.ctime()
    }

    with open("ptm_dashboard.json", "w") as f:
        json.dump(dashboard, f, indent=2)

    print(f"[CommandHUD] 📊 Dashboard updated at {dashboard['last_update']}")

def run_command_hud_loop():
    while True:
        build_dashboard()
        time.sleep(30)

def log_event():ef drop_files_to_bridge():