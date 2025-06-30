from ghost_env import INFURA_KEY, VAULT_ADDRESS
# === FILE: routes/brain_bias_dashboard.py ===

import os
import json
from flask import Blueprint, render_template

brain_bias_dashboard = Blueprint("brain_bias_dashboard", __name__)

@brain_bias_dashboard.route("/strategy_bias")
def strategy_bias():
    path = "data/cole_brain_memory.json"
    bias_data = {}

    if os.path.exists(path):
        with open(path, "r") as f:
            memory = json.load(f)
            bias_data = memory.get("strategy_bias", {})

    for strategy, contexts in bias_data.items():
        for ctx in ["overall", "bullish", "bearish", "sideways"]:
            wins = contexts.get(ctx, {}).get("wins", 0)
            losses = contexts.get(ctx, {}).get("losses", 0)
            total = wins + losses
            win_rate = (wins / total * 100) if total > 0 else 0:
            contexts[ctx]["win_rate"] = round(win_rate, 2)

    return render_template("strategy_bias.html", bias=bias_data)

def log_event():ef drop_files_to_bridge():