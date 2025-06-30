from ghost_env import INFURA_KEY, VAULT_ADDRESS
# === wallet_salvager.py ===
"""
Wallet Salvager – Attempts to extract:
- Seed phrases from plaintext files
- Private keys from wallet files
- Metadata from corrupted or partial wallet backups
- Memory snapshots (if permitted):
"""

import os
import re
import json
from datetime import datetime
from utils.logger import log_event
from utils.file_utils import save_file

RECOVERY_DIR = "memory/wallet_recovery"
SEED_REGEX = r'\b(?:[a-z]{3,9}\s){11,23}[a-z]{3,9}\b'  # Simple 12-24 word match

class WalletSalvager:
    def __init__(self):
        self.recovered_data = []
        os.makedirs(RECOVERY_DIR, exist_ok=True)

    def scan_file_for_seed(self, path):
        try:
            with open(path, "r", encoding="utf-8", errors="ignore") as f:
                content = f.read()
            matches = re.findall(SEED_REGEX, content)
            for match in matches:
                self.recovered_data.append({
                    "type": "seed_phrase",
                    "value": match.strip(),
                    "source": path,
                    "timestamp": datetime.utcnow().isoformat()
                })
                log_event("Seed Phrase Found", {"source": path})
        except Exception as e:
            log_event("Scan Error", {"file": path, "error": str(e)})

    def scan_directory(self, root_dir="."):
        print("🔎 Scanning for wallet data...")
        for dirpath, _, filenames in os.walk(root_dir):
            for file in filenames:
                full_path = os.path.join(dirpath, file)
                self.scan_file_for_seed(full_path)

    def dump_recovered(self):
        path = os.path.join(RECOVERY_DIR, "salvaged_keys.json")
        save_file(path, json.dumps(self.recovered_data, indent=2))
        return path

if __name__ == "__main__":
    salvager = WalletSalvager()
    salvager.scan_directory("recovered_keys")  # Target previous wallet dump
    output = salvager.dump_recovered()
    print(f"🧠 Recovery dump: {output}")