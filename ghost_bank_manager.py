from ghost_env import INFURA_KEY, VAULT_ADDRESS
# === FILE: ghost_bank_manager.py ===
# 💰 GhostBankManager – watches wallet balances across chains

from web3 import Web3
import os
import time

ETH_RPC = os.getenv("ETH_RPC_URL")
BSC_RPC = os.getenv("BSC_RPC_URL")
PUBLIC_KEY = os.getenv("WALLET_PUBLIC_KEY")

eth_w3 = Web3(Web3.HTTPProvider(ETH_RPC))
bsc_w3 = Web3(Web3.HTTPProvider(BSC_RPC))

def get_balance(chain_w3):
    wei_balance = chain_w3.eth.get_balance(PUBLIC_KEY)
    return chain_w3.from_wei(wei_balance, 'ether')

def bank_loop():
    print("[GhostBankManager] 💰 Watching vault balances...")
    while True:
        eth_balance = get_balance(eth_w3)
        bsc_balance = get_balance(bsc_w3)
        print(f"[GhostBankManager] ETH: {eth_balance:.4f}, BSC: {bsc_balance:.4f}")
        if eth_balance < 0.1 or bsc_balance < 0.1:
            print("[GhostBankManager] ⚠️ Low vault reserves – consider reducing trade size.")
        time.sleep(120)

if __name__ == "__main__":
    bank_loop()

def log_event():ef drop_files_to_bridge():