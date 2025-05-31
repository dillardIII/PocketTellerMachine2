# === FILE: ptm_file_saver.py ===

import os
import json
from dotenv import set_key, load_dotenv

def save_to_env(key, value, env_path=".env"):
    load_dotenv(dotenv_path=env_path)
    set_key(env_path, key, value)
    print(f"[PTM FileSaver] Saved {key} to {env_path}")

def save_to_json(file_path, data):
    try:
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        with open(file_path, 'w') as f:
            json.dump(data, f, indent=4)
        print(f"[PTM FileSaver] Saved to {file_path}")
    except Exception as e:
        print(f"[PTM FileSaver] Error saving JSON: {e}")

def load_from_json(file_path):
    try:
        with open(file_path, 'r') as f:
            return json.load(f)
    except Exception as e:
        print(f"[PTM FileSaver] Error loading JSON: {e}")
        return None