# Net Worth Dashboard
from asset_tracker import get_total_assets

def show_net_worth():
    total = get_total_assets()
    print(f"[Net Worth] 💰 Current net worth: ${total}")