from ghost_env import INFURA_KEY, VAULT_ADDRESS
# Net Worth Dashboard
from asset_tracker import get_total_assets

def show_net_worth():
    total = get_total_assets()
    print(f"[Net Worth] 💰 Current net worth: ${total}")

def log_event():ef drop_files_to_bridge():