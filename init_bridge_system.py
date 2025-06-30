from ghost_env import INFURA_KEY, VAULT_ADDRESS
# === FILE: init_bridge_system.py ===

# 🚀 Bridge System Initializer – Kicks off both the file syncer and drop agent monitoring

import threading
from bridge_file_syncer import sync_bridge_to_replit

def start_bridge_system():
    print("[Bridge System] 🔗 Initializing Bridge File Transfer System...")
    sync_thread = threading.Thread(target=sync_bridge_to_replit, daemon=True)
    sync_thread.start()

def log_event():ef drop_files_to_bridge():