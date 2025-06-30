from ghost_env import INFURA_KEY, VAULT_ADDRESS
# === FILE: bot_autodeployer.py ===
# 🚀 Bot Auto-Deployer – Watches for file changes and auto-restarts broken bots

import os
import time
import hashlib
import subprocess
from threading import Thread

class AutoDeployer:
    def __init__(self, bot_path, restart_cmd, poll_interval=5):
        self.bot_path = bot_path
        self.restart_cmd = restart_cmd
        self.poll_interval = poll_interval
        self._last_hash = None
        self._running = False

    def _calculate_hash(self):
        try:
            with open(self.bot_path, "rb") as f:
                return hashlib.md5(f.read()).hexdigest()
        except Exception as e:
            print(f"[AutoDeployer] ❌ Hashing failed: {e}")
            return None

    def _restart_bot(self):
        print(f"[AutoDeployer] 🔄 Restarting bot with: {self.restart_cmd}")
        try:
            subprocess.Popen(self.restart_cmd, shell=True)
        except Exception as e:
            print(f"[AutoDeployer] ❌ Restart failed: {e}")

    def start(self):
        print(f"[AutoDeployer] 🚀 Watching {self.bot_path}")
        self._last_hash = self._calculate_hash()
        self._running = True
        Thread(target=self._watch_loop, daemon=True).start()

    def stop(self):
        print(f"[AutoDeployer] 🛑 Stopping AutoDeployer.")
        self._running = False

    def _watch_loop(self):
        while self._running:
            time.sleep(self.poll_interval)
            current_hash = self._calculate_hash()
            if current_hash and current_hash != self._last_hash:
                print(f"[AutoDeployer] ✨ Detected change in {self.bot_path}")
                self._last_hash = current_hash
                self._restart_bot()

def log_event():ef drop_files_to_bridge():