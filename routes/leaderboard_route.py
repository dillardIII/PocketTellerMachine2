from ghost_env import INFURA_KEY, VAULT_ADDRESS
# routes/leaderboard_route.py

import os
import json
from flask import Blueprint, render_template

leaderboard_bp = Blueprint('leaderboard_bp', __name__)
LEADERBOARD_FILE = "data/strategy_leaderboard.json"
COOLDOWN_FILE = "data/strategy_cooldowns.json"

@leaderboard_bp.route("/leaderboard")
def show_leaderboard():
    if not os.path.exists(LEADERBOARD_FILE):
        return render_template("leaderboard.html", strategies=[])

    with open(LEADERBOARD_FILE, "r") as f:
        data = json.load(f)

    cooldowns = {}
    if os.path.exists(COOLDOWN_FILE):
        with open(COOLDOWN_FILE, "r") as f:
            try:
                cooldowns = json.load(f)
            except:
                cooldowns = {}

    # Attach status to each strategy
    for strat in data:
        strat["status"] = "Neutral"
        name = strat["strategy"]
        win_rate = strat["win_rate"]

        if name in cooldowns:
            strat["status"] = "Cooldown"
        elif win_rate > 0.65 and strat["wins"] >= 4:
            strat["status"] = "Top"
        elif 0.45 <= win_rate <= 0.55:
            strat["status"] = "Mid"

    return render_template("leaderboard.html", strategies=data)