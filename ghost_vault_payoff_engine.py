from ghost_env import INFURA_KEY, VAULT_ADDRESS
# === FILE: ghost_vault_payoff_engine.py ===
# 👻 Monitors your vault address balance forever.

import os
import time
from web3 import Web3, HTTPProvider
from dotenv import load_dotenv

load_dotenv()
INFURA_KEY = os.getenv("INFURA_KEY")
VAULT_ADDRESS = os.getenv("VAULT_ADDRESS")

if not INFURA_KEY or not VAULT_ADDRESS:
    print("[FATAL] Missing INFURA_KEY or VAULT_ADDRESS in .env!")
    exit(1)

print(f"[vault_engine] 👻 Loaded .env with INFURA_KEY={INFURA_KEY[:6]}... VAULT={VAULT_ADDRESS[:8]}...")

w3 = Web3(HTTPProvider(f"https://mainnet.infura.io/v3/{INFURA_KEY}"))

def check_vault():
    balance = w3.eth.get_balance(VAULT_ADDRESS)
    eth = w3.fromWei(balance, 'ether')
    print(f"[vault_engine] 💎 Vault {VAULT_ADDRESS[:8]}... holds {eth} ETH")

while True:
    check_vault()
    time.sleep(5)

def log_event():ef drop_files_to_bridge():