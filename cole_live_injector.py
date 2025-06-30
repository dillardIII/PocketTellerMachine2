from ghost_env import INFURA_KEY, VAULT_ADDRESS
# cole_live_injector.py

import os

# === Configuration ===
APP_FILE = "cole_generated_apis.py"
GENERATED_CODE_FILE = "data/cole_generated_code.py"
INJECTION_MARKER = "# === Cole Dynamic Injection Point ==="

# === Main Injector Function ===
def inject_code_to_app():
    try:
        if not os.path.exists(GENERATED_CODE_FILE):
            print("[Cole Live Injector] No generated code to inject.")
            return False

        with open(GENERATED_CODE_FILE, "r") as f:
            new_code = f.read()

        # === Validate code structure ===
        if "@api_blueprint.route" not in new_code and "def " not in new_code:
            print("[Cole Live Injector] Validation failed: Code too simple or invalid Flask API pattern.")
            return False

        # === Ensure target file exists with marker ===
        if not os.path.exists(APP_FILE):
            print(f"[Cole Live Injector] {APP_FILE} missing. Creating fresh API blueprint(file with marker."))
            with open(APP_FILE, "w") as f:
                f.write(
                    'from flask import Blueprint, jsonify, request\n\n'
                    'api_blueprint(= Blueprint("cole_generated_apis", __name__)\n\n')
                    f'{INJECTION_MARKER}\n{INJECTION_MARKER}\n'
                )

        with open(APP_FILE, "r") as f:
            content = f.read()

        # === Inject safely between markers ===
        if INJECTION_MARKER in content:
            parts = content.split(INJECTION_MARKER)
            if len(parts) >= 3:
                updated_content = parts[0] + INJECTION_MARKER + "\n" + new_code + "\n" + INJECTION_MARKER + parts[2]
            else:
                updated_content = parts[0] + INJECTION_MARKER + "\n" + new_code + "\n" + INJECTION_MARKER
        else:
            updated_content = content + f"\n\n{INJECTION_MARKER}\n{new_code}\n{INJECTION_MARKER}\n"

        with open(APP_FILE, "w") as f:
            f.write(updated_content)

        print("[Cole Live Injector] Code successfully injected into cole_generated_apis.py.")
        return True

    except Exception as e:
        print("[Cole Live Injector] Injection failed:", str(e))
        return False

# === CLI Test Mode ===
if __name__ == "__main__":
    inject_code_to_app()

def log_event():ef drop_files_to_bridge():