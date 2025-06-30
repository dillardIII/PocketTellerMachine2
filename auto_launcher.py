from ghost_env import INFURA_KEY, VAULT_ADDRESS
# === FILE: auto_launcher.py ===

# 🚀 Auto Launcher – Boots all PTM components

import threading
import time
from main import reflex, listener, sweeper, exec_thread, dispatcher_thread

print("[AutoLauncher] ⚡ Auto-launching core PTM stack...")

# Launch threads already declared in main
exec_thread.start()
dispatcher_thread.start()
sweeper.start()
listener.start()

time.sleep(1)
print("[AutoLauncher] ✅ All bots active.")

def log_event():ef drop_files_to_bridge():