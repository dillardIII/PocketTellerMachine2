# === FILE: wallet_data_syncer.py ===
# 🛠️ PTM Wallet Data Syncer – Fetches live native & ERC‑20 balances

import os
import json
from web3 import Web3
from decimal import Decimal
from utils.logger import log_event

# ⚠️ Set your Alchemy/Infura RPC URL in env: ALCHEMY_RPC
RPC_URL = os.getenv("ALCHEMY_RPC", "")
if not RPC_URL:
    raise RuntimeError("🔌 Missing ALCHEMY_RPC env var for Web3 provider")
w3 = Web3(Web3.HTTPProvider(RPC_URL))

# ERC‑20 ABI (minimal)
ERC20_ABI = [{
    "constant": True,
    "inputs": [{"name": "_owner", "type": "address"}],
    "name": "balanceOf",
    "outputs": [{"name": "balance", "type": "uint256"}],
    "type": "function"
},
{
    "constant": True,
    "name": "decimals",
    "outputs": [{"name": "", "type": "uint8"}],
    "type": "function",
    "inputs": []
}]

# Define wallets and tokens to monitor
WALLETS = {
    "MetaMask": os.getenv("METAMASK_ADDR", ""),
    "Trust Wallet": os.getenv("TRUST_WALLET_ADDR", "")
}

TOKENS = {
    "USDC": os.getenv("USDC_ADDR", ""),
    "APE": os.getenv("APE_ADDR", "")
    # add more: e.g. "USDT": "0xdAC17F9..."
}

VAULT_WALLETS_PATH = "vault/wallets.json"
VAULT_COINS_PATH = "vault/coins.json"

def load_json(path):
    if os.path.exists(path):
        with open(path) as f:
            return json.load(f)
    return {}

def save_json(path, data):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w") as f:
        json.dump(data, f, indent=2)

def sync_wallet_and_coins():
    wallets_out = {}
    coins_out = {}

    now = w3.eth.get_block('latest').timestamp

    for name, addr in WALLETS.items():
        if not Web3.isAddress(addr):
            log_event("WalletSync", {"error": f"Invalid address for {name}"})
            continue
        addr = Web3.toChecksumAddress(addr)
        bal_wei = w3.eth.get_balance(addr)
        bal_eth = w3.fromWei(bal_wei, 'ether')
        wallets_out[name] = {
            "native": float(f"{bal_eth:.6f}"),
            "network": "Ethereum",
            "updated": now
        }

        for symbol, tok_addr in TOKENS.items():
            try:
                tok_addr = Web3.toChecksumAddress(tok_addr)
                token = w3.eth.contract(address=tok_addr, abi=ERC20_ABI)
                raw = token.functions.balanceOf(addr).call()
                decs = token.functions.decimals().call()
                amount = Decimal(raw) / Decimal(10 ** decs)
                coins_out[symbol] = {
                    "amount": float(f"{amount:.4f}"),
                    "chain": "Ethereum",
                    "last_seen": now
                }
            except Exception as e:
                log_event("WalletSync", {"token_error": f"{symbol}@{name}: {e}"})

    save_json(VAULT_WALLETS_PATH, wallets_out)
    save_json(VAULT_COINS_PATH, coins_out)
    log_event("WalletSync", {"wallets_synced": list(wallets_out.keys()),
                             "coins_synced": list(coins_out.keys())})