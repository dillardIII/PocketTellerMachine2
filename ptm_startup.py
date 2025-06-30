from ghost_env import INFURA_KEY, VAULT_ADDRESS
# === FILE: ptm_startup.py ===
# 🚀 PTM Startup – Initializes and launches the full Autonomy Core from one control file

from autonomy_core import AutonomyCore

if __name__ == "__main__":
    print("[PTM Startup] 🧠 Initializing Autonomy Core...")
    core = AutonomyCore()
    core.start_all_systems()
    core.loop()

def log_event():ef drop_files_to_bridge():