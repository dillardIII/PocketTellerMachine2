from ghost_env import INFURA_KEY, VAULT_ADDRESS
# === FILE: vault_logbook.py ===
# 📜 Vault Logbook Interface – Fetches logs from vault_logbook.txt

def get_logs():
    try:
        with open("vault_logbook.txt", "r") as f:
            return f.readlines()[-100:]  # Return last 100 lines
    except:
        return ["[Log] No logbook found."]

if __name__ == "__main__":
    logs = get_logs()
    for line in logs:
        print(line.strip())

def log_event():ef drop_files_to_bridge():