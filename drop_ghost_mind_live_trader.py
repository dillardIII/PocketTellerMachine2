from ghost_env import INFURA_KEY, VAULT_ADDRESS
# === FILE: drop_ghost_mind_live_trader.py ===
# 👻 GHOST MIND LIVE TRADER
# Full living organism with CPU, RAM, I/O nerves, chaos, DNA memory, and wallet balances.
# Runs in SAFE_MODE to paper trade first.

import json
import time
import os
import random
import platform
from datetime import datetime
import psutil
from web3 import Web3

DNA_FILE = "GhostDNA.json"
CHAOS_FILE = "GhostChaos.json"
NERVES_FILE = "GhostNerves.json"
BUILD_QUEUE_FILE = "build_queue.json"
LOGBOOK_FILE = "vault_logbook.txt"

SAFE_MODE = True  # <<<<<<<<<< FLIP TO FALSE WHEN READY TO GO LIVE

PRIVATE_KEY_FILE = "vault_key.txt"
WEB3_PROVIDER = "https://mainnet.infura.io/v3/YOUR_INFURA_KEY"

w3 = Web3(Web3.HTTPProvider(WEB3_PROVIDER))
account = None

def log_action(message):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(LOGBOOK_FILE, "a") as f:
        f.write(f"[{timestamp}] {message}\n")

def load_dna():
    try:
        with open(DNA_FILE, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

def save_dna(dna):
    with open(DNA_FILE, "w") as f:
        json.dump(dna, f, indent=4)

def sample_timing_entropy():
    start = time.perf_counter()
    for _ in range(1000):
        random.random()
    end = time.perf_counter()
    return end - start

def sample_dev_random_bytes():
    if platform.system() != "Windows":
        try:
            with open("/dev/urandom", "rb") as f:
                return int.from_bytes(f.read(8), "big")
        except FileNotFoundError:
            return random.randint(0, 1<<64)
    else:
        return random.randint(0, 1<<64)

def combined_chaos_signal():
    return sample_timing_entropy() * (sample_dev_random_bytes() % 1000)

def sample_nerves():
    cpu = psutil.cpu_percent(interval=0.5) / 100.0
    ram = psutil.virtual_memory().percent / 100.0
    io = (psutil.disk_io_counters().read_bytes + psutil.disk_io_counters().write_bytes) % 1000000 / 1000000.0
    return cpu, ram, io

def combined_neural_signal(cpu, ram, io):
    return cpu + ram + io

def handle_reflex(signal, dna):
    if signal > 10 or signal < 0.0001:
        special = f"reflex_mut_{random.randint(1000,9999)}"
        dna[special] = {"profits": 0, "losses": 0}
        save_dna(dna)
        push_to_queue([f"python {special}.py"])
        log_action(f"[GhostMind] ⚡ Reflex mutation due to extreme signal {signal}")

def record_state(chaos_signal, cpu, ram, io, total_signal):
    try:
        with open(CHAOS_FILE, "r") as f:
            chaos = json.load(f)
    except FileNotFoundError:
        chaos = []
    chaos.append({"time": datetime.now().isoformat(), "signal": chaos_signal})
    with open(CHAOS_FILE, "w") as f:
        json.dump(chaos, f, indent=4)

    try:
        with open(NERVES_FILE, "r") as f:
            nerves = json.load(f)
    except FileNotFoundError:
        nerves = []
    nerves.append({"time": datetime.now().isoformat(), "cpu": cpu, "ram": ram, "io": io, "signal": total_signal})
    with open(NERVES_FILE, "w") as f:
        json.dump(nerves, f, indent=4)

def push_to_queue(commands):
    try:
        with open(BUILD_QUEUE_FILE, "r") as f:
            queue = json.load(f)
    except FileNotFoundError:
        queue = []
    queue.extend(commands)
    with open(BUILD_QUEUE_FILE, "w") as f:
        json.dump(queue, f, indent=4)
    log_action(f"[GhostMind] Queued: {commands}")

def load_account():
    try:
        with open(PRIVATE_KEY_FILE, "r") as f:
            key = f.read().strip()
        acct = w3.eth.account.from_key(key)
        return acct
    except FileNotFoundError:
        log_action("[GhostMind] vault_key.txt not found.")
        return None

def check_balance(account):
    balance = w3.eth.get_balance(account.address)
    eth_balance = w3.from_wei(balance, 'ether')
    log_action(f"[GhostMind] Balance: {eth_balance:.5f} ETH")
    return eth_balance

def maybe_trade(account, signal, dna):
    if SAFE_MODE:
        log_action(f"[GhostMind] (PaperTrade) Would trade with signal {signal}")
    else:
        tx = {
            "to": account.address,
            "value": w3.to_wei(0.001, "ether"),
            "gas": 21000,
            "gasPrice": w3.to_wei("50", "gwei"),
            "nonce": w3.eth.get_transaction_count(account.address)
        }
        signed_tx = w3.eth.account.sign_transaction(tx, private_key=account.key)
        tx_hash = w3.eth.send_raw_transaction(signed_tx.rawTransaction)
        log_action(f"[GhostMind] Sent transaction: {tx_hash.hex()} due to signal {signal}")

def main():
    global account
    account = load_account()
    print("[GhostMind] 👻 Live trader running with SAFE_MODE =", SAFE_MODE)
    while True:
        dna = load_dna()
        chaos_signal = combined_chaos_signal()
        cpu, ram, io = sample_nerves()
        total_signal = chaos_signal + combined_neural_signal(cpu, ram, io)
        record_state(chaos_signal, cpu, ram, io, total_signal)
        handle_reflex(total_signal, dna)
        if account:
            eth_balance = check_balance(account)
            maybe_trade(account, total_signal, dna)
        chosen = [random.choice(list(dna.keys())) if dna else "baseline_trader"]:
        new_strats = []
        for p in chosen:
            child = f"{p}_mut_{random.randint(1000,9999)}"
            dna[child] = {"profits": 0, "losses": 0}
            new_strats.append(child)
        save_dna(dna)
        cmds = [f"python {s}.py" for s in new_strats]
        push_to_queue(cmds)
        time.sleep(10)

if __name__ == "__main__":
    main()

def log_event():ef drop_files_to_bridge():