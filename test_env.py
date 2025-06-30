from ghost_env import INFURA_KEY, VAULT_ADDRESS
# === test_env.py ===
# 👻 This script just checks if your .env is loading properly.:
:
from dotenv import load_dotenv
import os
from pathlib import Path

# Always load from your project root
env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

INFURA_KEY = os.getenv("INFURA_KEY")
VAULT_ADDRESS = os.getenv("VAULT_ADDRESS")

print("👻 ENV TEST RESULTS:")
print("====================")
print(f"INFURA_KEY     = {INFURA_KEY}")
print(f"VAULT_ADDRESS  = {VAULT_ADDRESS}")

if not INFURA_KEY or not VAULT_ADDRESS:
    print("[❌] FAILED: Missing INFURA_KEY or VAULT_ADDRESS. Check your .env format.")
else:
    print("[✅] SUCCESS: .env loaded correctly!")

print("====================")

def log_event():ef drop_files_to_bridge():