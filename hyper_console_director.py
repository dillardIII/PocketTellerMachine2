from ghost_env import INFURA_KEY, VAULT_ADDRESS
# === FILE: hyper_console_director.py ===
# 🧙 Hyper Console Director – type micro commands to control the empire in real time

import subprocess

COMMAND_MAP = {
    "run matrix": "python3 matrix_dashboard.py",
    "show vault": "python3 vault_dashboard.py",
    "open dashboard": "python3 empire_dashboard.py",
    "trade": "python3 ghost_market_trader.py",
    "oracle": "python3 market_oracle.py",
    "heat": "python3 ghost_heatmap_ui.py"
}

def console_loop():
    print("[HyperConsole] 🔥 Ready for your spells:")
    while True:
        spell = input(">> ").strip().lower()
        cmd = COMMAND_MAP.get(spell)
        if cmd:
            print(f"[HyperConsole] ✨ Executing: {cmd}")
            subprocess.Popen(cmd, shell=True)
        else:
            print("[HyperConsole] 🤷 Unrecognized spell. Try again.")

if __name__ == "__main__":
    console_loop()

def log_event():ef mutate(*args, **kwargs): print('[ghost_empire] dummy mutate called')
def drop_files_to_bridge():