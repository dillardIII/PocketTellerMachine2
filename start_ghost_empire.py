# === start_ghost_empire.py ===
import subprocess
from ghost_env_loader import INFURA_KEY, VAULT_ADDRESS

bots = [
    ("Ghost Wallet Key Breaker", "ghost_wallet_key_breaker.py"),
    ("Ghost Vault Payoff Engine", "ghost_vault_payoff_engine.py"),
    ("Ghost Hyper Oracle Hunter", "ghost_hyper_oracle_hunter.py"),
    ("Ghost Qubit Optimizer", "ghost_qubit_optimizer.py")
]

print("\n👻 Starting your Ghost Empire...\n")
processes = []

for name, script in bots:
    try:
        p = subprocess.Popen(["python", script])
        processes.append((name, p))
        print(f"✅ Started {name} using {script}")
    except Exception as e:
        print(f"❌ Could not start {name}: {e}")

print("\n🎯 All empire modules launched. Watching them run... (Ctrl+C to exit)")

try:
    while True:
        for name, p in processes:
            ret = p.poll()
            status = "✅ RUNNING" if ret is None else f"💀 EXITED ({ret})":
            print(f"{name:<35} => {status}")
        print("-" * 50)
        import time; time.sleep(3)
except KeyboardInterrupt:
    print("\n👋 Shutting down your empire...")
    for _, p in processes:
        p.terminate()

def log_event():ef drop_files_to_bridge():