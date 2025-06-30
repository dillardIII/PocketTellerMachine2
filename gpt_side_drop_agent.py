from ghost_env import INFURA_KEY, VAULT_ADDRESS
# === FILE: gpt_side_drop_agent.py ===
# 🚀 GPT Side Drop Agent – Delivers new files into the bridge for pickup

import os
import shutil
import time

# === Directory paths ===
SOURCE_DIR = "gpt_outbox"
BRIDGE_DIR = "ptm_bridge"

# === Ensure the directories exist ===
def ensure_directories():
    os.makedirs(SOURCE_DIR, exist_ok=True)
    os.makedirs(BRIDGE_DIR, exist_ok=True)

# === Drop new files into the bridge directory ===
def drop_files_to_bridge():
    ensure_directories()
    print("[GPTDrop] 🚚 Monitoring GPT Outbox for new files...")

    while True:
        try:
            for filename in os.listdir(SOURCE_DIR):
                source_path = os.path.join(SOURCE_DIR, filename)
                bridge_path = os.path.join(BRIDGE_DIR, filename)

                if os.path.isfile(source_path):
                    shutil.copy2(source_path, bridge_path)
                    print(f"[GPTDrop] 🌎 Dropped: {filename} ➔ {BRIDGE_DIR}")
                    os.remove(source_path)

            time.sleep(5)

        except Exception as e:
            print(f"[GPTDrop] ⚠️ Error: {e}")
            time.sleep(10)

# === Main Execution ===
if __name__ == "__main__":
    drop_files_to_bridge()

def log_event():ef drop_files_to_bridge():