# 💰 Vault Manager – Handles MetaMask vault triggers & payouts

import json
import os

WALLET_FILE = "vault/wallet_state.json"

def load_wallet():
    if not os.path.exists(WALLET_FILE):
        print("[VaultManager] 🚫 No wallet state found.")
        return {}
    with open(WALLET_FILE, "r") as f:
        return json.load(f)

def payout(amount, to_address):
    print(f"[VaultManager] 💸 Payout of {amount} ETH initiated to {to_address}")
    # Normally you'd trigger Web3 call here
    # Example: web3.eth.send_transaction({...})
    print("[VaultManager] ✅ Payout completed.")

if __name__ == "__main__":
    wallet = load_wallet()
    print("[VaultManager] 📝 Current wallet state:", wallet)
    payout(0.01, "0xExampleETHAddress123")