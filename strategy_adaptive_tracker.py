from ghost_env import INFURA_KEY, VAULT_ADDRESS
import json
import os
from datetime import datetime, timedelta
from cole_memory_brain import log_memory_event
from strategy_generator import generate_strategy_replacement
from strategy_optimizer import optimize_strategy_parameters  # Step 7 import

TRADE_LOG_FILE = "logs/trade_log.json"
COOLDOWN_FILE = "data/strategy_cooldowns.json"
MAX_MEMORY_PATTERNS = 50  # limit memory clutter

# === Load recent trades from log ===
def load_trades():
    if not os.path.exists(TRADE_LOG_FILE):
        return []
    with open(TRADE_LOG_FILE, "r") as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return []

# === Load active cooldowns ===
def load_cooldowns():
    if not os.path.exists(COOLDOWN_FILE):
        return {}
    with open(COOLDOWN_FILE, "r") as f:
        try:
            return json.load(f)
        except:
            return {}

# === Save cooldowns to file ===
def save_cooldowns(data):
    with open(COOLDOWN_FILE, "w") as f:
        json.dump(data, f, indent=2)

# === Analyze recent win/loss patterns ===
def detect_strategy_patterns(trades):
    recent_trends = {}
    max_lookback = 20  # only check last N trades

    for trade in trades[-max_lookback:]:
        strat = trade.get("strategy")
        result = trade.get("result")
        context = trade.get("context", "unknown")

        if strat not in recent_trends:
            recent_trends[strat] = {"wins": 0, "losses": 0, "context_counts": {}}

        if result == "win":
            recent_trends[strat]["wins"] += 1
        elif result == "loss":
            recent_trends[strat]["losses"] += 1

        if context:
            context_dict = recent_trends[strat]["context_counts"]
            context_dict[context] = context_dict.get(context, 0) + 1

    return recent_trends

# === Evaluate patterns, apply logic, and log ===
def evaluate_and_log_patterns(trends):
    cooldowns = load_cooldowns()
    now = datetime.now()

    for strategy, data in trends.items():
        total = data["wins"] + data["losses"]
        if total < 3:
            continue

        win_rate = data["wins"] / total

        # === Poor performance: Cooldown and replace ===
        if win_rate < 0.4 and data["losses"] >= 3:
            worst_context = max(data["context_counts"], key=data["context_counts"].get, default="unknown")
            summary = f"{strategy} is underperforming ({win_rate:.0%} win rate). Failing most in {worst_context} conditions."

            pattern_entry = {
                "strategy": strategy,
                "win_rate": round(win_rate, 2),
                "losses": data["losses"],
                "worst_context": worst_context,
                "observation": summary
            }

            print(f"[PATTERN OBSERVED]: {summary}")
            log_memory_event("strategy_patterns", pattern_entry)

            # Apply cooldown
            cooldown_until = (now + timedelta(days=1)).isoformat()
            cooldowns[strategy] = cooldown_until
            print(f"[STRATEGY COOLDOWN] Pausing {strategy} until {cooldown_until}")

            # Auto-generate replacement
            generate_strategy_replacement(strategy)

        # === Mid-performance range: Attempt optimization ===
        elif 0.45 <= win_rate <= 0.55:
            print(f"[OPTIMIZER] {strategy} flagged as mid-tier. Attempting optimization...")
            new_version = optimize_strategy_parameters(strategy)
            if new_version:
                print(f"[OPTIMIZER] Generated: {new_version}")

        # === High performance: Promote ===
        elif win_rate > 0.65 and data["wins"] >= 4:
            summary = f"{strategy} is a top performer ({win_rate:.0%} win rate). Promotion recommended."
            promotion_log = {
                "strategy": strategy,
                "win_rate": round(win_rate, 2),
                "wins": data["wins"],
                "observation": summary,
                "promoted_at": now.isoformat()
            }

            print(f"[STRATEGY PROMOTION] {summary}")
            log_memory_event("strategy_promotions", promotion_log)

    save_cooldowns(cooldowns)

# === Master function to run pattern logic ===
def run_strategy_brain_evolution():
    trades = load_trades()
    trends = detect_strategy_patterns(trades)
    evaluate_and_log_patterns(trends)

def log_event():ef drop_files_to_bridge():