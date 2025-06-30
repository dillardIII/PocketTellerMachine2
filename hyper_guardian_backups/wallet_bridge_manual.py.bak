# === FILE: wallet_bridge_manual.py ===
# Inject user-controlled wallet into PTM quantum vault

class PTMUserWallet:
    def __init__(self):
        self.wallets = []

    def add_wallet(self, platform, address):
        self.wallets.append({
            "platform": platform,
            "address": address,
            "injected": True,
            "timestamp": time.time()
        })

user_vault = PTMUserWallet()
user_vault.add_wallet("MetaMask", "0xcf0E58caEf4D602Cf8924977f20FD0cd5493F0dB")
