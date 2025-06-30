# === FILE: ghost_autonomous_builder.py ===
# 👻 GHOST AUTO BUILDER V5 – MULTI-CHAIN PREDATOR
# Tracks live multi-chain profits across ETH, BNB, MATIC, ARB, evolves DNA, prunes losers, crossbreeds strongest.

import os
import json
import time
import hashlib
import subprocess
import random
from datetime import datetime
from web3 import Web3

DNA_FILE = "GhostDNA.json"
LOGBOOK_FILE = "vault_logbook.txt"
PRIVATE_KEY_FILE = "vault_key.txt"

# === Multi-chain RPC endpoints ===
WEB3_PROVIDERS = {
    "ETH": "https://mainnet.infura.io/v3/YOUR_INFURA_KEY",
    "BNB": "https://bsc-dataseed1.binance.org",
    "MATIC": "https://polygon-rpc.com",
    "ARB": "https://arb1.arbitrum.io/rpc"
}

CORE_BLUEPRINTS = {
    "DropGhostMindLiveTrader.py": """
# Minimal ghost mind bootstrap
print("[GhostMind] 🚀 Rebuilt minimal live trader.")
""",
    "master_watcher.py": """
# Minimal master watcher
print("[MasterWatcher] 🚀 Rebuilt minimal master watcher.")
""",
    "DropAutoEvolverBuilder.py": """
# Minimal auto evolver builder
print("[AutoEvolver] 🚀 Rebuilt minimal evolver.")
""",
    "GhostDNA.json": "{}",
    "GhostChaos.json": "[]",
    "GhostNerves.json": "[]"
}

EXPECTED_HASHES = {
    "DropGhostMindLiveTrader.py": "",
    "master_watcher.py": "",
    "DropAutoEvolverBuilder.py": ""
}

# === Setup multi-chain connections ===
def load_account_and_providers():
    try:
        with open(PRIVATE_KEY_FILE, "r") as f:
            key = f.read().strip()
    except FileNotFoundError:
        log_action("[AutoBuilder] ⚠️ vault_key.txt not found.")
        return None, {}

    providers = {}
    for chain, url in WEB3_PROVIDERS.items():
        providers[chain] = Web3(Web3.HTTPProvider(url))

    account = providers["ETH"].eth.account.from_key(key)
    return account, providers

account, providers = load_account_and_providers()
previous_balances = {chain: None for chain in WEB3_PROVIDERS.keys()}

# === Logging ===
def log_action(message):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(LOGBOOK_FILE, "a") as f:
        f.write(f"[{timestamp}] {message}\n")

# === File hashing ===
def file_hash(filename):
    if not os.path.exists(filename):
        return None
    h = hashlib.sha256()
    with open(filename, "rb") as f:
        while chunk := f.read(8192):
            h.update(chunk)
    return h.hexdigest()

# === Rebuild from DNA or blueprint ===
def rebuild_file_from_dna(filename, dna):
    with open(filename, "w") as f:
        if dna:
            baseline = random.choice(list(dna.keys()))
            f.write(f"# Auto-rebuilt from GhostDNA baseline {baseline}\n")
            f.write("print('[Rebuilt] Ghost DNA base module running.')\n")
        else:
            f.write("# Auto-rebuilt from empty DNA\nprint('[Rebuilt] Empty GhostDNA')\n")
    log_action(f"[AutoBuilder] ⚡ Rebuilt {filename} from GhostDNA")

def rebuild_from_blueprint(filename):
    blueprint = CORE_BLUEPRINTS.get(filename)
    if blueprint:
        with open(filename, "w") as f:
            f.write(blueprint.strip() + "\n")
        log_action(f"[AutoBuilder] 🛠️ Rebuilt {filename} from blueprint")

def launch_file(filename):
    try:
        subprocess.Popen(["python", filename])
        log_action(f"[AutoBuilder] 🚀 Launched {filename}")
    except Exception as e:
        log_action(f"[AutoBuilder] 🚨 Failed to launch {filename}: {e}")

# === Multi-chain balance check & adjust DNA ===
def check_multichain_balances(dna):
    global previous_balances
    total_delta = 0.0

    for chain, w3 in providers.items():
        try:
            balance = w3.eth.get_balance(account.address)
            eth_balance = w3.from_wei(balance, 'ether')
            log_action(f"[AutoBuilder] {chain} balance: {eth_balance:.5f}")

            if previous_balances[chain] is not None:
                delta = eth_balance - previous_balances[chain]
                total_delta += delta
                log_action(f"[AutoBuilder] Δ {chain}: {delta:.5f}")
            previous_balances[chain] = eth_balance

        except Exception as e:
            log_action(f"[AutoBuilder] ⚠️ Failed to check {chain} balance: {e}")

    # Update DNA with total cross-chain delta
    if total_delta != 0:
        for key in dna.keys():
            if total_delta > 0:
                dna[key]["profits"] = dna[key].get("profits", 0) + 1
            else:
                dna[key]["losses"] = dna[key].get("losses", 0) + 1
        log_action(f"[AutoBuilder] 🔥 Updated DNA with {'profit' if total_delta > 0 else 'loss'} from total cross-chain Δ {total_delta:.5f}")
    return dna

# === DNA prune & crossbreed ===
def evolve_dna(dna):
    if not dna:
        return dna
    to_delete = []
    for key, info in dna.items():
        profit = info.get("profits", 0) - info.get("losses", 0)
        if profit < -3:
            to_delete.append(key)
    for key in to_delete:
        del dna[key]
        log_action(f"[AutoBuilder] 🩸 Pruned weak DNA: {key}")

    sorted_lines = sorted(dna.items(), key=lambda x: x[1].get("profits",0) - x[1].get("losses",0), reverse=True)
    if len(sorted_lines) >= 2:
        p1, p2 = sorted_lines[0][0], sorted_lines[1][0]
        child = f"{p1[:6]}_{p2[:6]}_x_{random.randint(1000,9999)}"
        dna[child] = {"profits": 0, "losses": 0}
        log_action(f"[AutoBuilder] 🧬 Crossbred {p1} + {p2} -> {child}")
    return dna

# === Main loop ===
def main():
    print("[GhostAutoBuilder] 👻 Watching empire across ETH, BNB, MATIC, ARB – evolving DNA by total profits.")
    while True:
        try:
            with open(DNA_FILE, "r") as f:
                dna = json.load(f)
        except FileNotFoundError:
            dna = {}

        dna = check_multichain_balances(dna)
        dna = evolve_dna(dna)

        with open(DNA_FILE, "w") as f:
            json.dump(dna, f, indent=4)

        for filename in CORE_BLUEPRINTS.keys():
            current_hash = file_hash(filename)
            expected_hash = EXPECTED_HASHES.get(filename, "")
            needs_rebuild = not current_hash or (expected_hash and current_hash != expected_hash)
            if needs_rebuild:
                if filename in EXPECTED_HASHES:
                    rebuild_file_from_dna(filename, dna)
                else:
                    rebuild_from_blueprint(filename)
                launch_file(filename)

        time.sleep(10)

if __name__ == "__main__":
    main()