from ghost_env import INFURA_KEY, VAULT_ADDRESS
# === FILE: boot_init.py ===
# 🚀 Initializes everything on system start – God Mode Bootloader

from autonomy_daemon import run_autonomy

if __name__ == "__main__":
    print("[BootInit] 🚀 Triggering full PTM auto-boot...")
    run_autonomy()

def log_event():ef drop_files_to_bridge():