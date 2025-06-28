# === FILE: ghostforge_writer.py ===
# 👻 GhostForge Writer – Creates new files on its own, beyond just strategies

import os
import random
from datetime import datetime
from command_memory import log_command_event

GEN_DIR = "ptm_inbox"

def generate_new_strategy():
    strategy_name = f"auto_strategy_{datetime.now().strftime('%Y%m%d_%H%M%S')}.py"
    filepath = os.path.join(GEN_DIR, strategy_name)
    threshold = random.uniform(20, 80)
    with open(filepath, "w") as f:
        f.write(f'''
def run_strategy():
    print("[{strategy_name}] Running strategy with threshold {threshold:.2f}")
if __name__ == "__main__":
    run_strategy()
''')
    print(f"[GhostForge] 🧠 Generated {strategy_name}")
    log_command_event("StrategyWritten", strategy_name)

def ghostforge_loop():
    while True:
        generate_new_strategy()
        time.sleep(60)