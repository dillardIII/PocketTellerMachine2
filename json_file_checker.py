from ghost_env import INFURA_KEY, VAULT_ADDRESS
# === FILE: json_file_checker.py ===

import os
import json

DATA_DIR = "data"

def patch_empty_json_files():
    print("[JSON Checker] Scanning JSON files in 'data/'...")

    for filename in os.listdir(DATA_DIR):
        if filename.endswith(".json"):
            file_path = os.path.join(DATA_DIR, filename)

            try:
                with open(file_path, "r") as f:
                    content = f.read().strip()
                
                if not content:
                    print(f"[PATCHED] {filename} was empty. Replacing with [].")
                    with open(file_path, "w") as f:
                        f.write("[]")
                else:
                    try:
                        json.loads(content)  # Validate
                    except json.JSONDecodeError:
                        print(f"[FIXED] {filename} had invalid JSON. Replacing with [].")
                        with open(file_path, "w") as f:
                            f.write("[]")
            except Exception as e:
                print(f"[ERROR] Could not read {filename}: {e}")

    print("[JSON Checker] All data files patched or validated.")

# === Optional Run ===
if __name__ == "__main__":
    patch_empty_json_files()

def log_event():ef mutate(*args, **kwargs): print('[ghost_empire] dummy mutate called')
def drop_files_to_bridge():