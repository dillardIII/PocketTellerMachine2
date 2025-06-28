# === FILE: vault_file_dispatcher.py ===
# 🔐 Vault File Dispatcher – Tags, secures, and logs files into the vault system

import os
import hashlib
import shutil
import datetime

class VaultFileDispatcher:
    def __init__(self, watch_dir="ptm_inbox", vault_dir="vault"):
        self.watch_dir = watch_dir
        self.vault_dir = vault_dir
        self.logged_hashes = set()
        if not os.path.exists(self.vault_dir):
            os.makedirs(self.vault_dir)

    def _file_hash(self, filepath):
        with open(filepath, "rb") as f:
            return hashlib.sha256(f.read()).hexdigest()

    def monitor_and_tag(self):
        print("[VaultDispatcher] 🧭 Monitoring for file vaulting...")
        while True:
            for file in os.listdir(self.watch_dir):
                if file.endswith(".py") or file.endswith(".txt"):
                    path = os.path.join(self.watch_dir, file)
                    file_hash = self._file_hash(path)
                    if file_hash not in self.logged_hashes:
                        self._vault_file(path, file_hash)

    def _vault_file(self, filepath, file_hash):
        filename = os.path.basename(filepath)
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        new_name = f"{timestamp}__{filename}"
        dest = os.path.join(self.vault_dir, new_name)

        shutil.copy2(filepath, dest)
        self.logged_hashes.add(file_hash)

        print(f"[VaultDispatcher] 💾 Vaulted {filename} as {new_name}")