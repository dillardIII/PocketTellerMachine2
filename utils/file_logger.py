# === FILE: utils/file_logger.py ===

# 📓 File Logger – Logs file creation events to vault or console

import os

def log_file_creation(filename, sha256):
    try:
        log_path = "vault/gpt_file_log.txt"
        os.makedirs("vault", exist_ok=True)
        with open(log_path, "a") as f:
            f.write(f"{filename} | SHA256: {sha256}\n")
        print(f"[Logger] ✅ Logged: {filename} | SHA256: {sha256}")
    except Exception as e:
        print(f"[Logger] ❌ Logging failed: {e}")