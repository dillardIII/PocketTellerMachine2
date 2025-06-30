# === FILE: auto_strategy_generator.py ===
# 🧠 Generates new trading strategy files automatically

import os
import random
from datetime import datetime
from command_memory import log_command_event

STRATEGY_DIR = "ptm_inbox"

def generate_new_strategy():
    strategy_name = f"auto_strategy_{datetime.now().strftime('%Y%m%d_%H%M%S')}.py"
    filepath = os.path.join(STRATEGY_DIR, strategy_name)

    # Simple strategy generator for demonstration
    threshold = random.uniform(20, 80)
    content = f'''
def run_strategy():
    print("[{strategy_name}] Executing strategy with threshold {threshold:.2f}")

if __name__ == "__main__":
    run_strategy()
'''

    with open(filepath, "w") as f:
        f.write(content)
    print(f"[AutoStrategyGen] 🧠 Generated {strategy_name}")
    log_command_event("StrategyWritten", strategy_name)

if __name__ == "__main__":
    generate_new_strategy()