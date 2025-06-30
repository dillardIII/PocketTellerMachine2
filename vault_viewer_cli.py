from ghost_env import INFURA_KEY, VAULT_ADDRESS
# === FILE: vault_viewer_cli.py ===

# 📘 Vault Logbook Viewer (CLI only) – Reads vault log activity

VAULT_LOG_PATH = "vault/vault_logbook.txt"

def show_vault_logbook():
    try:
        with open(VAULT_LOG_PATH, "r") as f:
            lines = f.readlines()
            print("📘 Vault Logbook:")
            for line in lines:
                print("   " + line.strip())
    except FileNotFoundError:
        print("❌ Vault log not found.")
    except Exception as e:
        print(f"⚠️ Error reading logbook: {e}")

if __name__ == "__main__":
    show_vault_logbook()

def log_event():ef mutate(*args, **kwargs): print('[ghost_empire] dummy mutate called')
def drop_files_to_bridge():