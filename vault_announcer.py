from ghost_env import INFURA_KEY, VAULT_ADDRESS
import json
import time
from datetime import datetime

VAULT_FILE = "ptm_vault.json"

def vault_announce_loop():
    print("[VaultAnnouncer] 📣 Watching vault...")
    last_state = None
    while True:
        try:
            with open(VAULT_FILE, "r") as f:
                data = json.load(f)
            if data != last_state:
                print(f"[VaultAnnouncer] 💰 {datetime.now()} – Vault changed: {data}")
                last_state = data
        except FileNotFoundError:
            print("[VaultAnnouncer] ⚠️ Vault file not found yet.")
        except Exception as e:
            print(f"[VaultAnnouncer] ❌ Vault error: {e}")
        time.sleep(15)

def log_event():ef drop_files_to_bridge():