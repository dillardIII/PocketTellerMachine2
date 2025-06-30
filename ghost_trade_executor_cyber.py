# === FILE: ghost_trade_executor_cyber.py ===
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

def fetch_fusion_scores():
    return [{"ghost": f"Ghost_{i}", "score": random.uniform(0, 1)} for i in range(5)]

def executor_loop():
    print("[GhostTradeExecutor] 💰 Executor w/ cyber mesh live...")
    while True:
        cyber = load_cyber_state()
        threshold = 0.6 * cyber["aggression"]
        fusion_data = fetch_fusion_scores()
        for entry in fusion_data:
            if entry["score"] > threshold:
                trade_size = round(entry["score"] * cyber["greed"] * 0.01, 5)
                print(f"[GhostTradeExecutor] 🚀 {entry['ghost']} placing trade: {trade_size} ETH @ score {entry['score']:.2f}")
            else:
                print(f"[GhostTradeExecutor] 🛡️ {entry['ghost']} holding @ score {entry['score']:.2f}")
        time.sleep(60)

if __name__ == "__main__":
    executor_loop()