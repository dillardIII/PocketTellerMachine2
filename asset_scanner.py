# === FILE: asset_scanner.py ===
# 💼 Asset Scanner – Scans PTM memory, vaults, and wallet snapshots for assets

import os
import json

VAULT_PATH = "vault"
WALLET_SNAPSHOT = os.path.join(VAULT_PATH, "wallet_snapshot.json")
ASSET_REPORT = os.path.join("reports", "asset_scan_report.json")

class AssetScanner:
    def __init__(self):
        self.assets = {}

    def scan(self):
        print("[AssetScanner] 🔍 Scanning for wallet and token assets...")

        if os.path.exists(WALLET_SNAPSHOT):
            with open(WALLET_SNAPSHOT, "r") as f:
                data = json.load(f)
                self.assets["wallet_snapshot"] = data
        else:
            self.assets["wallet_snapshot"] = "⚠️ Missing wallet_snapshot.json"

        orphaned_assets = []
        for file in os.listdir(VAULT_PATH):
            if file.endswith(".json") and file != "wallet_snapshot.json":
                with open(os.path.join(VAULT_PATH, file), "r") as f:
                    try:
                        orphaned_assets.append(json.load(f))
                    except:
                        orphaned_assets.append({"file": file, "error": "Unreadable or corrupt"})

        self.assets["unlinked_files"] = orphaned_assets

        os.makedirs("reports", exist_ok=True)
        with open(ASSET_REPORT, "w") as f:
            json.dump(self.assets, f, indent=2)

        print(f"[AssetScanner] ✅ Report saved to {ASSET_REPORT}")
        return self.assets