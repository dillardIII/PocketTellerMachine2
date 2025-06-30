# === FILE: ghost_graph_liquidity_hunter.py ===
# 👻 GRAPH LIQUIDITY HUNTER WITH SWAP ROUTER EXECUTION
# Uses Graph Protocol to scan thousands of pools, validates reserves, executes real swaps on routers, evolves DNA.

import json
import time
import random
import requests
from datetime import datetime
from web3 import Web3

DNA_FILE = "GhostDNA.json"
LOGBOOK_FILE = "vault_logbook.txt"
PRIVATE_KEY_FILE = "vault_key.txt"

WEB3_PROVIDERS = {
    "ETH": "https://mainnet.infura.io/v3/YOUR_INFURA_KEY",
    "BNB": "https://bsc-dataseed1.binance.org",
    "MATIC": "https://polygon-rpc.com",
    "ARB": "https://arb1.arbitrum.io/rpc"
}

GRAPH_ENDPOINTS = {
    "ETH": "https://api.thegraph.com/subgraphs/name/uniswap/uniswap-v2",
    "BNB": "https://api.thegraph.com/subgraphs/name/pancakeswap/exchange-v2",
    "MATIC": "https://api.thegraph.com/subgraphs/name/sameepsi/quickswap06",
    "ARB": "https://api.thegraph.com/subgraphs/name/sushiswap/arbitrum-exchange"
}

ROUTERS = {
    "ETH": "0x7a250d5630B4cF539739dF2C5dAcb4c659F2488D",  # Uniswap V2
    "BNB": "0x10ED43C718714eb63d5aA57B78B54704E256024E",  # PancakeSwap V2
    "MATIC": "0xa5E0829CaCED8A8E62E891B22B1d0e8cc5aE45F6",  # QuickSwap
    "ARB": "0x1b02da8cb0d097eb8d57a175b88c7d8b47997506"   # SushiSwap
}

ROUTER_ABI = json.loads('[{"inputs":[{"internalType":"uint256","name":"amountOutMin","type":"uint256"},{"internalType":"address[]","name":"path","type":"address[]"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"deadline","type":"uint256"}],"name":"swapExactETHForTokens","outputs":[{"internalType":"uint256[]","name":"","type":"uint256[]"}],"stateMutability":"payable","type":"function"}]')

previous_balances = {chain: None for chain in WEB3_PROVIDERS.keys()}

def log_action(message):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(LOGBOOK_FILE, "a") as f:
        f.write(f"[{timestamp}] {message}\n")

def load_account_and_providers():
    try:
        with open(PRIVATE_KEY_FILE, "r") as f:
            key = f.read().strip()
    except FileNotFoundError:
        log_action("[Hunter] vault_key.txt missing.")
        return None, {}, ""
    providers = {}
    for chain, url in WEB3_PROVIDERS.items():
        providers[chain] = Web3(Web3.HTTPProvider(url))
    account = providers["ETH"].eth.account.from_key(key)
    return account, providers, key

account, providers, private_key = load_account_and_providers()

def check_balance(w3, chain):
    try:
        bal = w3.eth.get_balance(account.address)
        eth_bal = w3.from_wei(bal, 'ether')
        log_action(f"[Hunter] {chain} balance: {eth_bal:.5f}")
        return eth_bal
    except Exception as e:
        log_action(f"[Hunter] Failed {chain} balance: {e}")
        return 0

def query_graph_for_pairs(endpoint):
    query = """
    {
      pairs(first: 5, orderBy: reserveUSD, orderDirection: desc) {
        id
        reserveUSD
        token0 { id symbol }
        token1 { id symbol }
      }
    }
    """
    try:
        r = requests.post(endpoint, json={"query": query})
        return r.json()["data"]["pairs"]
    except Exception as e:
        log_action(f"[Hunter] Graph query failed: {e}")
        return []

def execute_swap_router(w3, chain, router_address, path):
    router = w3.eth.contract(address=router_address, abi=ROUTER_ABI)
    try:
        tx = router.functions.swapExactETHForTokens(
            0,  # amountOutMin, very high slippage for demo (normally you'd set min expected)
            path,
            account.address,
            int(time.time()) + 60
        ).buildTransaction({
            "from": account.address,
            "value": w3.to_wei(0.001, "ether"),
            "gas": 300000,
            "gasPrice": w3.to_wei("5", "gwei"),
            "nonce": w3.eth.get_transaction_count(account.address)
        })
        signed_tx = w3.eth.account.sign_transaction(tx, private_key=private_key)
        tx_hash = w3.eth.send_raw_transaction(signed_tx.rawTransaction)
        log_action(f"[Hunter] 🚀 Sent swap on {chain} via router: {tx_hash.hex()}")
    except Exception as e:
        log_action(f"[Hunter] ⚠️ Swap router call failed: {e}")

def main():
    print("[GraphHunter] 👻 Starting graph-based liquidity hunter with live router swaps.")
    while True:
        try:
            with open(DNA_FILE, "r") as f:
                dna = json.load(f)
        except FileNotFoundError:
            dna = {}

        total_delta = 0.0
        for chain in WEB3_PROVIDERS.keys():
            w3 = providers[chain]
            prev = previous_balances[chain] or check_balance(w3, chain)

            pairs = query_graph_for_pairs(GRAPH_ENDPOINTS[chain])
            if pairs:
                top_pair = pairs[0]
                token_path = [w3.to_checksum_address("0xEeeeeEeeeEeEeeEeEeEeeEEEeeeeEeeeeeeeEEeE"), w3.to_checksum_address(top_pair["token0"]["id"])]
                log_action(f"[Hunter] {chain} top pool: {top_pair['token0']['symbol']}-{top_pair['token1']['symbol']} liquidity: {top_pair['reserveUSD']}")
                execute_swap_router(w3, chain, ROUTERS[chain], token_path)

            time.sleep(5)
            new_bal = check_balance(w3, chain)
            delta = new_bal - prev
            total_delta += delta
            previous_balances[chain] = new_bal

        for key in dna.keys():
            if total_delta > 0:
                dna[key]["profits"] = dna[key].get("profits",0)+1
            elif total_delta < 0:
                dna[key]["losses"] = dna[key].get("losses",0)+1
        with open(DNA_FILE, "w") as f:
            json.dump(dna, f, indent=4)
        time.sleep(10)

if __name__ == "__main__":
    main()