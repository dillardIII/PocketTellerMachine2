from ghost_env import INFURA_KEY, VAULT_ADDRESS
# === FILE: utils/notifications.py ===
def notify(message):
    print(f"[Notify] 🔔 {message}")
    # Optional: Add OS notifications or Discord webhook