# === FILE: bridge_drop_bot.py ===
# 📝 Bridge Drop Bot – writes new files to the bridge for pickup

import os
import time

BRIDGE_DIR = "ptm_bridge_drop"

def write_file_to_bridge(filename, content):
    if not os.path.exists(BRIDGE_DIR):
        os.makedirs(BRIDGE_DIR)
    path = os.path.join(BRIDGE_DIR, filename)
    with open(path, "w") as f:
        f.write(content)
    print(f"[BridgeDropBot] ✅ Dropped file to bridge: {path}")

def run_bridge_drop_loop():
    counter = 0
    while True:
        # Example: auto-generate a dummy strategy
        filename = f"auto_strategy_{counter}.py"
        content = f"""
# Auto-generated strategy #{counter}
print("[AutoStrategy] Running strategy {counter}")
"""
        write_file_to_bridge(filename, content)
        counter += 1
        time.sleep(45)  # drop a new file every 45 sec

if __name__ == "__main__":
    run_bridge_drop_loop()