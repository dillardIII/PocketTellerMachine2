from ghost_env import INFURA_KEY, VAULT_ADDRESS
# Watchlist Manager
watchlist = []

def add_to_watchlist(symbol):
    if symbol not in watchlist:
        watchlist.append(symbol)
        print(f"[Watchlist] Added {symbol}")
    else:
        print(f"[Watchlist] {symbol} already exists")

def remove_from_watchlist(symbol):
    if symbol in watchlist:
        watchlist.remove(symbol)
        print(f"[Watchlist] Removed {symbol}")
    else:
        print(f"[Watchlist] {symbol} not found")

def get_watchlist():
    return watchlist

def log_event():ef drop_files_to_bridge():