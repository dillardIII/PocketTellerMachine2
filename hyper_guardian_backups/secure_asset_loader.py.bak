# === FILE: secure_asset_loader.py ===
# 🔐 Secure Asset Loader – loads & decrypts protected AI modules into memory only.

from cryptography.fernet import Fernet
import json
import os

KEY_FILE = "secrets/aes_key.bin"
ASSET_FILE = "secure_assets/ai_core.enc"

def load_key():
    with open(KEY_FILE, "rb") as f:
        return f.read()

def decrypt_asset():
    key = load_key()
    fernet = Fernet(key)
    with open(ASSET_FILE, "rb") as f:
        encrypted_data = f.read()
    decrypted_data = fernet.decrypt(encrypted_data)
    print("[SecureLoader] 🔓 Asset decrypted in memory.")
    return json.loads(decrypted_data)

if __name__ == "__main__":
    data = decrypt_asset()
    print("[SecureLoader] ✅ Data ready:", data)