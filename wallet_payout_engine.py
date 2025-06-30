from ghost_env import INFURA_KEY, VAULT_ADDRESS
# === FILE: wallet_payout_engine.py ===
# 💸 PTM Wallet Payout Engine – Sends real crypto to user wallet after trade profits

from web3 import Web3
import json
import os
from dotenv import load_dotenv

load_dotenv()

# === Load Environment Config ===
PRIVATE_KEY = os.getenv("METAMASK_PRIVATE_KEY")
WALLET_ADDRESS = os.getenv("METAMASK_PUBLIC_ADDRESS")  # Receiving address
INFURA_URL = os.getenv("WEB3_PROVIDER_URL")  # Mainnet/Chain endpoint

# === Set Up Web3 ===
web3 = Web3(Web3.HTTPProvider(INFURA_URL))
assert web3.isConnected(), "[PayoutEngine] ❌ Web3 connection failed!"

# === Coin Info ===
GAS_LIMIT = 21000  # Standard ETH transfer
CHAIN_ID = 1       # Ethereum mainnet

def send_eth_payout(amount_eth: float):
    try:
        print(f"[PayoutEngine] 🔄 Preparing payout of {amount_eth} ETH...")
        nonce = web3.eth.getTransactionCount(WALLET_ADDRESS)

        tx = {
            'nonce': nonce,
            'to': WALLET_ADDRESS,
            'value': web3.toWei(amount_eth, 'ether'),
            'gas': GAS_LIMIT,
            'gasPrice': web3.toWei('50', 'gwei'),
            'chainId': CHAIN_ID
        }

        signed_tx = web3.eth.account.sign_transaction(tx, PRIVATE_KEY)
        tx_hash = web3.eth.sendRawTransaction(signed_tx.rawTransaction)

        print(f"[PayoutEngine] ✅ Sent! TX Hash: {web3.toHex(tx_hash)}")
        return web3.toHex(tx_hash)
    
    except Exception as e:
        print(f"[PayoutEngine] ❌ Failed to send payout: {e}")
        return None

def payout_from_profit_log(log_path="vault/profit_log.json"):
    try:
        with open(log_path, "r") as f:
            data = json.load(f)
            profit_eth = data.get("eth_profit", 0.0)

        if profit_eth > 0:
            return send_eth_payout(profit_eth)
        else:
            print("[PayoutEngine] ⚠️ No ETH profit to send.")
            return None

    except Exception as e:
        print(f"[PayoutEngine] ❌ Error reading profit log: {e}")
        return None

def log_event():ef drop_files_to_bridge():