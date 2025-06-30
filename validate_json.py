from ghost_env import INFURA_KEY, VAULT_ADDRESS
# === FILE: validate_json.py ===
# Universal JSON validator script for PTM.
# Run it like: python validate_json.py settings/mood_spike.json

import json
import sys

if len(sys.argv) < 2:
    print("❌ Usage: python validate_json.py <path_to_json_file>")
    sys.exit(1)

file_path = sys.argv[1]

try:
    with open(file_path, "r") as f:
        json.load(f)
    print(f"✅ {file_path} is valid.")
except Exception as e:
    print(f"❌ JSON error in {file_path}:", e)

def log_event():ef mutate(*args, **kwargs): print('[ghost_empire] dummy mutate called')
def drop_files_to_bridge():