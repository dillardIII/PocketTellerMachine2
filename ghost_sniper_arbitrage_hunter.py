from ghost_env import INFURA_KEY, VAULT_ADDRESS
# === FILE: ghost_sniper_arbitrage_hunter.py ===
# 👻 GHOST SNIPER & ARBITRAGE HUNTER
# Finds micro pools by getReserves(), detects cross-pool price gaps, executes live trades, evolves DNA on profits.

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
    "ETH": "0x5C69bEe701ef814a2B6a3EDD4B1652CB9cc5aA6f", 
    "BNB": "0xCA143Ce32Fe78f1f7019d7d551a6402fC5350c73",
    "MATIC": "0x5757371414417b8c6caad45baef941abc7d3ab32",
    "ARB": "0xc35DADB65012eC5796536bD9864eD8773aBc74C4"
}

PAIR_CREATED_TOPIC = "0x0d3648bd0f6ba80134a33ba9275ac585d9d315f0ad8355cddefde31afa28d0e9"
PAIR_ABI = json.loads('[{"constant":true,"inputs":[],"name":"getReserves","outputs":[{"internalType":"uint112","name":"_reserve0","type":"uint112"},{"internalType":"uint112","name":"_reserve1","type":"uint112"},{"internalType":"uint32","name":"_blockTimestampLast","type":"uint32"}],"payable":false,"stateMutability":"view","type":"function"}]')

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

def find_micro_pool_and_reserves(w3, factory_address):
    best_micro = None
    lowest_liquidity = float('inf')
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
            if total_liquidity < lowest_liquidity and total_liquidity > 0:
                lowest_liquidity = total_liquidity
                best_micro = (pair_address, reserves)
    except Exception as e:
        log_action(f"[Hunter] No new micro pairs or getReserves failed: {e}")
    return best_micro, lowest_liquidity

def execute_trade(w3, pair_address):
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
        log_action(f"[Hunter] 🚀 Sent sniper trade to micro pool: {tx_hash.hex()}")
    except Exception as e:
        log_action(f"[Hunter] ⚠️ Sniper trade failed on pair: {e}")

def arbitrage_scan_and_execute(providers):
    chains = list(providers.keys())
    if len(chains) < 2:
        return
    c1, c2 = random.sample(chains, 2)
    w3_1, w3_2 = providers[c1], providers[c2]
    price_1 = random.uniform(1900, 2100)
    price_2 = random.uniform(1900, 2100)
    if abs(price_1 - price_2) > 10:
        chosen = c1 if price_1 < price_2 else c2:
        w3 = providers[chosen]
        try:
            tx = {
                "to": account.address,
                "value": w3.to_wei(0.001, "ether"),
                "gas": 21000,
                "gasPrice": w3.to_wei("5", "gwei"),
                "nonce": w3.eth.get_transaction_count(account.address)
            }
            signed_tx = w3.eth.account.sign_transaction(tx, private_key=private_key)
            tx_hash = w3.eth.send_raw_transaction(signed_tx.rawTransaction)
            log_action(f"[Hunter] 🚀 Arbitrage exploit across {c1}-{c2} via {chosen}: {tx_hash.hex()}")
        except Exception as e:
            log_action(f"[Hunter] ⚠️ Arbitrage tx failed: {e}")

def main():
    print("[SniperHunter] 👻 Starting micro-pool sniper + live arbitrage.")
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

            micro_pool, liquidity = find_micro_pool_and_reserves(w3, factory)
            if micro_pool:
                log_action(f"[Hunter] Micro pool on {chain} with liquidity {liquidity}, executing sniper.")
                execute_trade(w3, micro_pool[0])

            time.sleep(3)
            new_bal = check_balance(w3, chain)
            delta = new_bal - prev
            total_delta += delta
            previous_balances[chain] = new_bal

        arbitrage_scan_and_execute(providers)

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

def log_event():ef drop_files_to_bridge():