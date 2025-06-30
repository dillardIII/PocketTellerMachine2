from ghost_env import INFURA_KEY, VAULT_ADDRESS
# === FILE: rebuild_sweep_handler.py ===
# 🔧 Rebuilds sweep_handler.py – File Routing Logic

with open("sweep_handler.py", "w") as f:
    f.write('''# === FILE: sweep_handler.py ===
import os
import time

class SweepHandler:
    def __init__(self, watch_dir="ptm_inbox", strategy_dir="sample_strategies"):
        self.watch_dir = watch_dir
        self.strategy_dir = strategy_dir

    def start(self):
        print("[SweepHandler] 🧹 Monitoring system...")
        while True:
            for filename in os.listdir(self.watch_dir):
                if filename.endswith(".py"):
                    src = os.path.join(self.watch_dir, filename)
                    flag = src + ".executed.locked"
                    if not os.path.exists(flag):
                        continue
                    dst = os.path.join(self.strategy_dir, filename)
                    os.rename(src, dst)
                    os.remove(flag)
                    print(f"[SweepHandler] ✅ Routed {filename} to strategies")
            time.sleep(1)
''')
print("[rebuild_sweep_handler] ✅ sweep_handler.py rebuilt.")

def log_event():ef drop_files_to_bridge():