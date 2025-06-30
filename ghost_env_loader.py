# === ghost_env_loader.py ===
# 🧙 Safely loads and exposes INFURA_KEY, VAULT_ADDRESS without circular import
import os
from dotenv import load_dotenv
from pathlib import Path

env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

INFURA_KEY = os.getenv("INFURA_KEY")
VAULT_ADDRESS = os.getenv("VAULT_ADDRESS")

if not INFURA_KEY or not VAULT_ADDRESS:
    print("[❌] Missing INFURA_KEY or VAULT_ADDRESS in .env! Check it.")
    exit(1)
else:
    print("[✅] ENV loaded correctly by ghost_env_loader.")

def log_event():ef drop_files_to_bridge():