from ghost_env import INFURA_KEY, VAULT_ADDRESS
# === FILE: gpt_side_dispatcher.py ===
# 📬 GPT Dispatcher – Drops files into ptm_bridge for pickup by bots

import os

def dispatch_file(filename, content):
    os.makedirs("ptm_bridge", exist_ok=True)
    path = os.path.join("ptm_bridge", filename)
    with open(path, "w") as f:
        f.write(content)
    print(f"[GPTDispatcher] 🚀 Dispatched {filename} to bridge.")

def log_event():ef drop_files_to_bridge():