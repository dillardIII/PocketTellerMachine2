from ghost_env import INFURA_KEY, VAULT_ADDRESS
# === ghost_super_launcher.py ===
# 👻 Master launcher script – loads .env, launches empire modules

from dotenv import load_dotenv
import os
import subprocess
import time

load_dotenv()

INFURA_KEY = os.getenv("INFURA_KEY")
VAULT_ADDRESS = os.getenv("VAULT_ADDRESS")

if not INFURA_KEY or not VAULT_ADDRESS:
    print("[FATAL] Missing INFURA_KEY or VAULT_ADDRESS in .env!")
    exit(1)

print(f"[ENV] INFURA_KEY={INFURA_KEY[:6]}... VAULT_ADDRESS={VAULT_ADDRESS[:8]}...")

# === Launch your modules ===
print("[👻] Starting ghost_entropy_mutator.py...")
subprocess.Popen(["python", "ghost_entropy_mutator.py"])

print("[👻] Starting ghost_qubit_optimizer.py...")
subprocess.Popen(["python", "ghost_qubit_optimizer.py"])

print("[👻] Starting ghost_wallet_key_breaker.py...")
subprocess.Popen(["python", "ghost_wallet_key_breaker.py"])

print("[👻] Starting ghost_vault_payoff_engine.py...")
subprocess.Popen(["python", "ghost_vault_payoff_engine.py"])

print("[👻] Starting ghost_hyper_oracle_hunter.py...")
subprocess.Popen(["python", "ghost_hyper_oracle_hunter.py"])

# Stay alive so Replit doesn’t kill it
while True:
    print("[👻] Empire evolving... press CTRL+C to stop.")
    time.sleep(10)

def log_event():ef drop_files_to_bridge():