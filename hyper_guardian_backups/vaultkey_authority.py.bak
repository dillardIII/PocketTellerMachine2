# === FILE: vaultkey_authority.py ===
# 🔐 VaultKey Authority – Secure access handler for vault, bots, and external AI collaborators

import os
import json
from datetime import datetime
from utils.logger import log_event

KEY_DB_FILE = "vault/vault_keys.json"
AUTHORIZED_USERS_FILE = "vault/authorized_users.json"

class VaultKeyAuthority:
    def __init__(self):
        self.keys = {}
        self.authorized = {}
        self._load_keys()
        self._load_authorized()

    def _load_keys(self):
        if os.path.exists(KEY_DB_FILE):
            with open(KEY_DB_FILE, "r") as f:
                self.keys = json.load(f)
        else:
            self._save_keys()
        print("[VaultKeyAuthority] 🔑 Loaded vault keys.")

    def _save_keys(self):
        os.makedirs("vault", exist_ok=True)
        with open(KEY_DB_FILE, "w") as f:
            json.dump(self.keys, f, indent=4)

    def _load_authorized(self):
        if os.path.exists(AUTHORIZED_USERS_FILE):
            with open(AUTHORIZED_USERS_FILE, "r") as f:
                self.authorized = json.load(f)
        else:
            self._save_authorized()

    def _save_authorized(self):
        with open(AUTHORIZED_USERS_FILE, "w") as f:
            json.dump(self.authorized, f, indent=4)

    def register_key(self, key_id, access_level="basic"):
        self.keys[key_id] = {
            "access_level": access_level,
            "created": str(datetime.now()),
            "active": True
        }
        self._save_keys()
        log_event("Key Registered", {"key_id": key_id, "access": access_level})

    def authorize_user(self, user_id, key_id):
        if key_id not in self.keys or not self.keys[key_id]["active"]:
            return False
        self.authorized[user_id] = {
            "key_id": key_id,
            "access_level": self.keys[key_id]["access_level"],
            "authorized_on": str(datetime.now())
        }
        self._save_authorized()
        log_event("User Authorized", {"user": user_id, "key": key_id})
        return True

    def check_access(self, user_id, level="basic"):
        user = self.authorized.get(user_id)
        if not user:
            return False
        levels = ["basic", "privileged", "admin", "godcore"]
        return levels.index(user["access_level"]) >= levels.index(level)

    def revoke_key(self, key_id):
        if key_id in self.keys:
            self.keys[key_id]["active"] = False
            self._save_keys()
            log_event("Key Revoked", {"key_id": key_id})

# === Test Hook ===
if __name__ == "__main__":
    auth = VaultKeyAuthority()
    auth.register_key("omega-007", "godcore")
    auth.authorize_user("Dillard", "omega-007")
    print(auth.check_access("Dillard", "godcore"))