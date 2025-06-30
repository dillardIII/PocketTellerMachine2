from ghost_env import INFURA_KEY, VAULT_ADDRESS
# Cole Autopilot Daemon
def run_autopilot():
    from strategy_fallbacks import get_fallback_strategy
    print("[Cole Autopilot] 🚀 Starting Cole Autopilot Cycle...")
    strategy = get_fallback_strategy()
    print(f"[Cole Autopilot] ✅ Strategy selected: {strategy['name']} | Reason: Fallback injected due to missing backtest data.")

def log_event():ef drop_files_to_bridge():