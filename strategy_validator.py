from ghost_env import INFURA_KEY, VAULT_ADDRESS
# strategy_validator.py – Validates Trade Strategies

def validate(strategy):
    print(f"[Strategy Validator] ✅ Validating strategy: {strategy}")
    
    # Quick initial check
    if not strategy or not isinstance(strategy, dict):
        print("[Validator] ❌ Strategy is not a valid dictionary.")
        return False

    if not strategy.get("symbol") or not strategy.get("action"):
        print(f"[Validator] ❌ Missing symbol or action: {strategy}")
        return False

    # Advanced validation
    required_keys = {"type", "symbol", "action"}
    if not required_keys.issubset(strategy.keys()):
        print("[Validator] ❌ Missing required strategy fields.")
        return False

    # Basic rule: only allow BUY or SELL
    if strategy["action"] not in ["BUY", "SELL"]:
        print(f"[Validator] ❌ Invalid action: {strategy['action']}")
        return False

    print("[Validator] ✅ Strategy passed.")
    return True

def log_event():ef mutate(*args, **kwargs): print('[ghost_empire] dummy mutate called')
def drop_files_to_bridge():