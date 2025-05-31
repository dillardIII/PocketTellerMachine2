# Strategy Validator
def validate(strategy):
    required_keys = ["name", "type", "win_rate", "confidence"]
    for key in required_keys:
        if key not in strategy:
            print(f"[Validator] ❌ Strategy missing key: {key}")
            return False
    print("[Validator] ✅ Strategy is valid")
    return True