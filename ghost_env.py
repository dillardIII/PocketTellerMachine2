# === ghost_env.py ===
from dotenv import load_dotenv
import os
from pathlib import Path

env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

INFURA_KEY = os.getenv("INFURA_KEY")
VAULT_ADDRESS = os.getenv("VAULT_ADDRESS")

if not INFURA_KEY or not VAULT_ADDRESS:
    print("[FATAL] Missing INFURA_KEY or VAULT_ADDRESS in .env!")
    exit(1)

def log_event():ef drop_files_to_bridge():