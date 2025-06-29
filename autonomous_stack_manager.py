# === FILE: autonomous_stack_manager.py ===
# 🛠 Autonomous Stack Manager – Ensures empire modules always exist and self-heal

import os
import json
import time
from ghost_self_coder import generate_file

REQUIRED_MODULES = {
    "dashboard": "ptm_modules/auto_dashboard.py",
    "trader": "ptm_modules/auto_trader.py",
    "data_scraper": "ptm_modules/auto_scraper.py"
}

def check_and_repair():
    for mtype, path in REQUIRED_MODULES.items():
        if not os.path.exists(path):
            print(f"[StackManager] ⚠️ Missing {mtype}. Rebuilding...")
            generate_file(mtype, filename=path)

while True:
    check_and_repair()
    print("[StackManager] ✅ Stack integrity verified.")
    time.sleep(120)