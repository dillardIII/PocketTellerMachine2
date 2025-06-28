# === FILE: utils/json_loader.py ===
# 📂 JSON Loader – Safely loads and saves JSON files with error fallback

import json
import os

def load_json(filepath):
    try:
        with open(filepath, "r") as f:
            return json.load(f)
    except Exception as e:
        print(f"[JSON Loader] ❌ Failed to load {filepath}: {e}")
        return {}

def save_json(filepath, data):
    try:
        os.makedirs(os.path.dirname(filepath), exist_ok=True)
        with open(filepath, "w") as f:
            json.dump(data, f, indent=2)
        print(f"[JSON Loader] ✅ Saved {filepath}")
    except Exception as e:
        print(f"[JSON Loader] ❌ Failed to save {filepath}: {e}")