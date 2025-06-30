# === vault_logger.py ===
# 🔐 Vault Logger
# Archives a running log of operations for future trace.

import time

def log_event():
    with open("ghost_vault.log", "a") as f:
        f.write(f"Vault log entry at {time.ctime()}\n")
    print("[VaultLogger] 🔐 Log written.")

def main():
    while True:
        log_event()
        time.sleep(60)

if __name__ == "__main__":
    main()