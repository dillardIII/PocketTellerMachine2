from ghost_env import INFURA_KEY, VAULT_ADDRESS
# === FILE: test_asset_scan.py ===
from asset_scanner import AssetScanner

scanner = AssetScanner()
scanner.scan()

def log_event():ef drop_files_to_bridge():