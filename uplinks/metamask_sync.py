# === FILE: uplinks/metamask_sync.py ===
# 👛 MetaMask Sync – Reads live wallet balances from connected MetaMask vault

from web3 import Web3
from utils.logger import log_event

INFURA_URL = "https://mainnet.infura.io/v3/your-infura-key"
VAULT_ADDRESS = "0xYourWalletAddressHere"

def pull_wallet_balances():
    print("[MetaMask] 👛 Connecting to Ethereum...")
    try:
        web3 = Web3(Web3.HTTPProvider(INFURA_URL))
        balance = web3.eth.get_balance(VAULT_ADDRESS)
        eth_balance = web3.fromWei(balance, "ether")
        print(f"[MetaMask] 💰 Balance: {eth_balance} ETH")
        log_event("WalletSync", {"balance_eth": float(eth_balance)})
    except Exception as e:
        print(f"[MetaMask] ⚠️ Error: {e}")
        log_event("MetaMaskError", {"error": str(e)})