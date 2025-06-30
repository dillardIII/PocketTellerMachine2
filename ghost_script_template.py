from ghost_env import INFURA_KEY, VAULT_ADDRESS
# === ghost_script_template.py ===
# 👻 Uses .env for INFURA_KEY and VAULT_ADDRESS

from dotenv import load_dotenv
import os
from web3 import Web3, HTTPProvider

# Load from .env
load_dotenv()

INFURA_KEY = os.getenv("INFURA_KEY")
VAULT_ADDRESS = os.getenv("VAULT_ADDRESS")

if not INFURA_KEY or not VAULT_ADDRESS:
    raise ValueError("Missing INFURA_KEY or VAULT_ADDRESS in .env!")

# Setup Web3
w3 = Web3(HTTPProvider(f"https://mainnet.infura.io/v3/{INFURA_KEY}"))

# Example action
balance = w3.eth.get_balance(VAULT_ADDRESS)
eth_balance = w3.from_wei(balance, 'ether')
print(f"VAULT balance: {eth_balance:.6f} ETH")

def log_event():ef drop_files_to_bridge():