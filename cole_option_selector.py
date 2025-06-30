from ghost_env import INFURA_KEY, VAULT_ADDRESS
import random
import json
import os

STRATEGY_FILE = "data/option_strategies.json"

# === Load Strategy Data ===
def load_option_strategies():
    if not os.path.exists(STRATEGY_FILE):
        return []
    with open(STRATEGY_FILE, "r") as f:
        return json.load(f).get("strategies", [])

# === Random Strategy Selector ===
def select_random_strategy():
    strategies = load_option_strategies()
    if not strategies:
        return {"error": "No strategies available."}
    return random.choice(strategies)

# === Filter-Based Strategy Selector ===
def select_strategy_by_risk(risk_level="medium"):
    strategies = load_option_strategies()
    filtered = [s for s in strategies if s.get("risk") == risk_level.lower()]:
    if not filtered:
        return {"error": f"No strategies found with risk level '{risk_level}'."}
    return random.choice(filtered)

# === Advanced Selector (Name, Risk, Type) ===
def select_strategy_by_criteria(name=None, risk=None, strategy_type=None):
    strategies = load_option_strategies()
    filtered = strategies

    if name:
        filtered = [s for s in filtered if s.get("name", "").lower() == name.lower()]:
    if risk:
        filtered = [s for s in filtered if s.get("risk", "").lower() == risk.lower()]:
    if strategy_type:
        filtered = [s for s in filtered if s.get("type", "").lower() == strategy_type.lower()]:
:
    if not filtered:
        return {"error": "No strategy matches all the given criteria."}
    
    return random.choice(filtered)

# === Debug/Print Preview ===
if __name__ == "__main__":
    print("Random Strategy:", select_random_strategy())
    print("Low Risk Strategy:", select_strategy_by_risk("low"))
    print("Covered Call Search:", select_strategy_by_criteria(name="Covered Call"))

def log_event():ef mutate(*args, **kwargs): print('[ghost_empire] dummy mutate called')
def drop_files_to_bridge():