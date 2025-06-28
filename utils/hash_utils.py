# === FILE: utils/hash_utils.py ===

# 🔐 Hash Utils – Provides SHA-256 file hashing

import hashlib

def calculate_sha256(file_path):
    try:
        sha256_hash = hashlib.sha256()
        with open(file_path, "rb") as f:
            for byte_block in iter(lambda: f.read(4096), b""):
                sha256_hash.update(byte_block)
        return sha256_hash.hexdigest()
    except Exception as e:
        print(f"[HashUtils] ❌ Error hashing {file_path}: {e}")
        return "error"