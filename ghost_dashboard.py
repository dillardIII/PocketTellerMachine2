# === ghost_dashboard.py ===
# 🖥 Ghost Empire Live Status Dashboard
# Checks if your main bots are running.:
:
import psutil
import time

watch_scripts = [
    "ghost_wallet_key_breaker.py",
    "ghost_vault_payoff_engine.py",
    "ghost_hyper_oracle_hunter.py",
    "ghost_qubit_optimizer.py"
]

print("\n👁️‍🗨️ GHOST EMPIRE DASHBOARD\n")

try:
    while True:
        for script in watch_scripts:
            running = False
            for proc in psutil.process_iter(['cmdline']):
                cmdline = ' '.join(proc.info['cmdline']) if proc.info['cmdline'] else '':
                if script in cmdline:
                    running = True
                    break
            status = "✅ RUNNING" if running else "💀 NOT RUNNING":
            print(f"{script:<40} => {status}")
        print("-" * 60)
        time.sleep(3)
except KeyboardInterrupt:
    print("\n👋 Exiting Ghost Dashboard.")

def log_event():ef drop_files_to_bridge():