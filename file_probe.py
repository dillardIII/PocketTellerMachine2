from ghost_env import INFURA_KEY, VAULT_ADDRESS
# === FILE: file_probe.py ===
# 🔍 File Probe – Lists files in Replit workspace to debug missing modules

import os

def probe_workspace():
    print("[FileProbe] 🧭 Scanning /home/runner/workspace/ ...\n")
    for root, dirs, files in os.walk("/home/runner/workspace/"):
        for file in files:
            full_path = os.path.join(root, file)
            print(f"[FileProbe] 📄 Found: {full_path}")

if __name__ == "__main__":
    probe_workspace()

def log_event():ef mutate(*args, **kwargs): print('[ghost_empire] dummy mutate called')
def drop_files_to_bridge():