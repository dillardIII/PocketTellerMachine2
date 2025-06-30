import uuid
import json
from datetime import datetime

HYBRID_FILE = "data/cole_hybrid_strategies.json"

# === Hybrid Creator ===
def create_hybrid_strategy(strat_a, strat_b):
    hybrid_key = f"{strat_a['key']}_{strat_b['key']}_Hybrid"
    hybrid_desc = f"Hybrid Strategy combining {strat_a['description']} and {strat_b['description']}"

    hybrid = {
        "id": str(uuid.uuid4()),
        "key": hybrid_key,
        "description": hybrid_desc,
        "parent_strategies": [strat_a['key'], strat_b['key']],
        "creation_date": datetime.now().isoformat()
    }

    try:
        with open(HYBRID_FILE, "a") as f:
            json.dump(hybrid, f)
            f.write("\n")
        print("[HYBRID STRATEGY CREATED]:", hybrid)
    except Exception as e:
        print("[ERROR]: Could not save hybrid strategy.", e)

# Example usage
sma = {"key": "sma_cross", "description": "SMA Crossover Strategy"}
rsi = {"key": "rsi_reversal", "description": "RSI Reversal Strategy"}

create_hybrid_strategy(sma, rsi)