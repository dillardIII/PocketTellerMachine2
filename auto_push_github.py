from ghost_env import INFURA_KEY, VAULT_ADDRESS
# === FILE: auto_push_github.py ===
# 🚀 Pushes committed files to your GitHub repo every minute

import os
import time

def push_loop():
    print("[AutoPushGitHub] 🚀 Starting push loop...")
    while True:
        os.system("git push origin main || echo no push needed")
        time.sleep(60)

if __name__ == "__main__":
    push_loop()

def log_event():ef mutate(*args, **kwargs): print('[ghost_empire] dummy mutate called')
def drop_files_to_bridge():