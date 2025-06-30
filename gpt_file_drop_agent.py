from ghost_env import INFURA_KEY, VAULT_ADDRESS
# === FILE: gpt_file_drop_agent.py ===

# 🚀 GPT File Drop Agent – Automatically moves files from GPT-gen folder to bridge
import os
import time
import shutil

BRIDGE_DROP_FOLDER = "bridge_drop"
GPT_GEN_FOLDER = "gpt_generated"

class GPTFileDropAgent:
    def __init__(self, watch_folder=GPT_GEN_FOLDER, drop_folder=BRIDGE_DROP_FOLDER, check_interval=5):
        self.watch_folder = watch_folder
        self.drop_folder = drop_folder
        self.check_interval = check_interval
        self.running = False

    def start(self):
        print("[GPT Drop Agent] 🚀 Starting GPT File Drop Agent...")
        self.running = True
        self._watch_loop()

    def stop(self):
        print("[GPT Drop Agent] 🛑 Stopping GPT File Drop Agent...")
        self.running = False

    def _watch_loop(self):
        while self.running:
            try:
                files = os.listdir(self.watch_folder)
                for file in files:
                    file_path = os.path.join(self.watch_folder, file)
                    if os.path.isfile(file_path):
                        target_path = os.path.join(self.drop_folder, file)
                        shutil.move(file_path, target_path)
                        print(f"[GPT Drop Agent] 📂 Dropped: {file} → {self.drop_folder}")
            except Exception as e:
                print(f"[GPT Drop Agent] ❌ Error during drop: {e}")
            time.sleep(self.check_interval)

def log_event():ef drop_files_to_bridge():