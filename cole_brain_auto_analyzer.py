from ghost_env import INFURA_KEY, VAULT_ADDRESS
from auto_analyze_trades_from_memory import auto_analyze_trades_from_memory
from datetime import datetime

def trigger_ai_brain_analysis():
    print(f"\n[TRIGGER]: AI Brain Memory Analysis started at {datetime.now().isoformat()}")
    auto_analyze_trades_from_memory()

# Example direct trigger
if __name__ == "__main__":
    trigger_ai_brain_analysis()

def log_event():ef drop_files_to_bridge():