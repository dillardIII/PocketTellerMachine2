from ghost_env import INFURA_KEY, VAULT_ADDRESS
# === FILE: ghost_wallet_key_breaker.py ===
# 👻 Attempts random private keys to brute-check Ethereum balances.

import os
import time
from web3 import Web3, HTTPProvider
from eth_account import Account
from dotenv import load_dotenv

load_dotenv()
INFURA_KEY = os.getenv("INFURA_KEY")
VAULT_ADDRESS = os.getenv("VAULT_ADDRESS")

if not INFURA_KEY or not VAULT_ADDRESS:
    print("[FATAL] Missing INFURA_KEY or VAULT_ADDRESS in .env!")
    exit(1)

print(f"[key_breaker] 👻 Loaded .env with INFURA_KEY={INFURA_KEY[:6]}... VAULT={VAULT_ADDRESS[:8]}...")

w3 = Web3(HTTPProvider(f"https://mainnet.infura.io/v3/{INFURA_KEY}"))

def try_key():
    acct = Account.create()
    balance = w3.eth.get_balance(acct.address)
    if balance > 0:
        print(f"[key_breaker] 💰 FOUND! Address {acct.address} with {w3.fromWei(balance, 'ether')} ETH")
    else:
        print(f"[key_breaker] ❌ Tried {acct.address[:8]}... balance 0")

while True:
    try_key()
    time.sleep(1)

def log_event():ef drop_files_to_bridge():