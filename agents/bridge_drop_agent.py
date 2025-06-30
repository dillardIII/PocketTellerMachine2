from ghost_env import INFURA_KEY, VAULT_ADDRESS
# === FILE: agents/bridge_drop_agent.py ===

import os
import time

def run_drop_agent():
    print("[BridgeDrop] 📤 Managing bridge_drop...")
    os.makedirs("bridge_drop", exist_ok=True)

    counter = 0
    while True:
        filename = f"heartbeat_{counter}.txt"
        with open(os.path.join("bridge_drop", filename), "w") as f:
            f.write("Bridge drop heartbeat\n")
        print(f"[BridgeDrop] ❤️ Dropped {filename}")
        counter += 1
        time.sleep(10)