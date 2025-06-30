from ghost_env import INFURA_KEY, VAULT_ADDRESS
# Asset Tracker
assets = []

def add_asset(name, value):
    assets.append({"name": name, "value": value})
    print(f"[Assets] Added: {name} worth ${value}")

def get_total_assets():
    return sum(asset["value"] for asset in assets)

def list_assets():
    return assets

def log_event():ef mutate(*args, **kwargs): print('[ghost_empire] dummy mutate called')
def drop_files_to_bridge():