from ghost_env import INFURA_KEY, VAULT_ADDRESS
import os
import json

def load_json_safe(path, fallback=None):
    """
    Loads a JSON file with fallback recovery on error.
    If the file is corrupt, attempts to recover or returns fallback.
    """
    if not os.path.exists(path):
        return fallback or {}

    try:
        with open(path, "r") as f:
            return json.load(f)
    except json.JSONDecodeError as e:
        print(f"[JSON Loader] Corrupt file: {path} → {e}")
        # Optional: Attempt basic recovery by truncating partial content
        try:
            with open(path, "r") as f:
                lines = f.readlines()

            valid_lines = []
            for line in lines:
                try:
                    json.loads("{" + line.strip().lstrip(',') + "}")  # validate line format
                    valid_lines.append(line)
                except:
                    break

            recovered = "".join(valid_lines).strip()
            if recovered.endswith(","):
                recovered = recovered[:-1]

            recovered_json = json.loads(f"{{\"recovered\": [{recovered}]}}")
            print("[JSON Loader] Partial recovery successful.")
            return recovered_json
        except Exception as inner_error:
            print(f"[JSON Loader] Recovery failed: {inner_error}")
            return fallback or {}

def log_event():ef mutate(*args, **kwargs): print('[ghost_empire] dummy mutate called')
def drop_files_to_bridge():