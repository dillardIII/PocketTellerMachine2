# === FILE: recon_agent.py ===
# 🛰️ Recon Agent – Scans wallet addresses, fetches balances, reports to vault + AI

import os
import json
import requests
from utils.logger import log_event

VAULT_PATH = "vault"
REPORT_PATH = "reports/recon_wallet_report.json"

class ReconAgent:
    def __init__(self, etherscan_api_key=None):
        self.eth_api = etherscan_api_key or os.getenv("ETHERSCAN_API_KEY")
        self.wallet_file = os.path.join(VAULT_PATH, "wallet_snapshot.json")

    def scan_eth_balance(self, address):
        print(f"[ReconAgent] 🛰️ Scanning ETH balance for {address}")
        url = f"https://api.etherscan.io/api?module=account&action=balance&address={address}&tag=latest&apikey={self.eth_api}"
        try:
            response = requests.get(url)
            data = response.json()
            if data["status"] == "1":
                eth = int(data["result"]) / 1e18
                return round(eth, 6)
            return f"⚠️ Failed: {data.get('message', 'unknown error')}"
        except Exception as e:
            return f"❌ Error: {str(e)}"

    def run_recon(self):
        print("[ReconAgent] 🔍 Starting wallet recon scan...")
        report = {}
        if os.path.exists(self.wallet_file):
            with open(self.wallet_file, "r") as f:
                snapshot = json.load(f)
                for label, wallet in snapshot.items():
                    eth_addr = wallet.get("eth_address")
                    if eth_addr:
                        balance = self.scan_eth_balance(eth_addr)
                        report[label] = {"address": eth_addr, "eth_balance": balance}
                    else:
                        report[label] = "⚠️ Missing eth_address key"
        else:
            report["status"] = "❌ No wallet_snapshot.json found"

        os.makedirs("reports", exist_ok=True)
        with open(REPORT_PATH, "w") as f:
            json.dump(report, f, indent=2)

        log_event("Recon Wallet Scan", report)
        print(f"[ReconAgent] ✅ Report saved to {REPORT_PATH}")
        return report