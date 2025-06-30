from ghost_env import INFURA_KEY, VAULT_ADDRESS
# === FILE: live_liquidity_hunter.py ===
# 👻 LIVE LIQUIDITY HUNTER WITH GETRESERVES & NEW PAIR CHASING
# Watches PairCreated logs, calls getReserves(), hunts optimal pools across ETH, BNB, MATIC, ARB.

import json
import time
import random
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

FACTORIES = {
    "ETH": "0x5C69bEe701ef814a2B6a3EDD4B1652CB9cc5aA6f",  # UniswapV2
    "BNB": "0xCA143Ce32Fe78f1f7019d7d551a6402fC5350c73", # PancakeSwap
    "MATIC": "0x5757371414417b8c6caad45baef941abc7d3ab32", # QuickSwap
    "ARB": "0xc35DADB65012eC5796536bD9864eD8773aBc74C4", # SushiSwap
}

PAIR_CREATED_TOPIC = "0x0d3648bd0f6ba80134a33ba9275ac585d9d315f0ad8355cddefde31afa28d0e9"
previous_balances = {chain: None for chain in WEB3_PROVIDERS.keys()}

PAIR_ABI = json.loads('[{"constant":true,"inputs":[],"name":"getReserves","outputs":[{"internalType":"uint112","name":"_reserve0","type":"uint112"},{"internalType":"uint112","name":"_reserve1","type":"uint112"},{"internalType":"uint32","name":"_blockTimestampLast","type":"uint32"}],"payable":false,"stateMutability":"view","type":"function"}]')

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

def find_new_pairs_and_liquidity(w3, factory_address):
    best_pool = None
    best_liquidity = 0
    try:
        logs = w3.eth.get_logs({
            "fromBlock": "latest",
            "address": factory_address,
            "topics": [PAIR_CREATED_TOPIC]
        })
        for log in logs:
            pair_address = "0x" + log["data"][-40:]
            pair_contract = w3.eth.contract(address=pair_address, abi=PAIR_ABI)
            reserves = pair_contract.functions.getReserves().call()
            total_liquidity = reserves[0] + reserves[1]
            if total_liquidity > best_liquidity:
                best_liquidity = total_liquidity
                best_pool = (pair_address, reserves)
    except Exception as e:
        log_action(f"[Hunter] No new pairs or getReserves failed: {e}")
    return best_pool, best_liquidity

def execute_optimal_swap(w3, pair_address):
    try:
        tx = {
            "to": pair_address,
            "value": w3.to_wei(0.001, "ether"),
            "gas": 300000,
            "gasPrice": w3.to_wei("5", "gwei"),
            "nonce": w3.eth.get_transaction_count(account.address)
        }
        signed_tx = w3.eth.account.sign_transaction(tx, private_key=private_key)
        tx_hash = w3.eth.send_raw_transaction(signed_tx.rawTransaction)
        log_action(f"[Hunter] 🚀 Sent live trade to pair: {tx_hash.hex()}")
    except Exception as e:
        log_action(f"[Hunter] ⚠️ Trade failed on pair: {e}")

def main():
    print("[LiveHunter] 👻 Starting live liquidity hunter with getReserves + new pair chasing.")
    while True:
        try:
            with open(DNA_FILE, "r") as f:
                dna = json.load(f)
        except FileNotFoundError:
            dna = {}

        total_delta = 0.0
        for chain in WEB3_PROVIDERS.keys():
            w3 = providers[chain]
            factory = FACTORIES[chain]
            prev = previous_balances[chain] or check_balance(w3, chain)

            best_pool, best_liquidity = find_new_pairs_and_liquidity(w3, factory)
            if best_pool:
                log_action(f"[Hunter] Best pool on {chain} has liquidity: {best_liquidity}")
                execute_optimal_swap(w3, best_pool[0])

            time.sleep(5)
            new_bal = check_balance(w3, chain)
            delta = new_bal - prev
            total_delta += delta
            previous_balances[chain] = new_bal

        # Update DNA
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

def log_event():ef mutate(*args, **kwargs): print('[ghost_empire] dummy mutate called')
def drop_files_to_bridge():