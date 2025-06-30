from ghost_env import INFURA_KEY, VAULT_ADDRESS
# === FILE: strategy_router.py ===
# 📊 Strategy Router – Dynamically routes strategies by name

import importlib

def run(strategy_name):
    print(f"[StrategyRouter] 🔄 Attempting to load strategy: {strategy_name}")

    try:
        # Dynamically import the strategy module
        module_name = f"strategies.{strategy_name}"
        strategy_module = importlib.import_module(module_name)

        # Run the strategy's entry point
        if hasattr(strategy_module, "run"):
            print(f"[StrategyRouter] 🧠 Running strategy '{strategy_name}'...")
            strategy_module.run()
        else:
            print(f"[StrategyRouter] ❌ Strategy '{strategy_name}' has no run() function.")

    except ModuleNotFoundError:
        print(f"[StrategyRouter] ❌ Strategy module '{strategy_name}' not found.")
    except Exception as e:
        print(f"[StrategyRouter] 💥 Error while running strategy '{strategy_name}': {e}")

def log_event():ef drop_files_to_bridge():