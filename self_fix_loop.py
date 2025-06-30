from ghost_env import INFURA_KEY, VAULT_ADDRESS
import time
import json
from error_parser import get_latest_error
from ai_code_generator import generate_code_fix
from auto_deployer import deploy_fix

FIXES_LOG = "data/fixes_log.json"

# === Main Self-Fix Loop ===
def self_fix_loop():
    print("[Self-Fix] Starting autonomous error detection and correction loop...")
    while True:
        error_data = get_latest_error()
        if error_data:
            print(f"[Self-Fix] Detected Error: {error_data['error']}")
            fixed_code = generate_code_fix(error_data)
            if fixed_code:
                print(f"[Self-Fix] Generated code fix for {error_data['file']}")
                if deploy_fix(error_data['file'], fixed_code):
                    log_fix(error_data, fixed_code)
                    print(f"[Self-Fix] Fix applied to {error_data['file']}")
                else:
                    print(f"[Self-Fix] Fix validation failed for {error_data['file']}. Skipped deployment.")
            else:
                print(f"[Self-Fix] No valid fix generated for {error_data['file']}")
        else:
            print("[Self-Fix] No new errors found.")

        time.sleep(30)  # Check for new errors every 30 seconds

# === Fix Logging ===
def log_fix(error_data, fixed_code):
    log_entry = {
        "timestamp": time.strftime("%Y-%m-%d %H:%M:%S"),
        "file": error_data['file'],
        "error": error_data['error'],
        "fix": fixed_code
    }

    if not os.path.exists(os.path.dirname(FIXES_LOG)):
        os.makedirs(os.path.dirname(FIXES_LOG))

    try:
        if os.path.exists(FIXES_LOG):
            with open(FIXES_LOG, 'r+') as f:
                logs = json.load(f)
                logs.append(log_entry)
                f.seek(0)
                json.dump(logs, f, indent=2)
        else:
            with open(FIXES_LOG, 'w') as f:
                json.dump([log_entry], f, indent=2)
    except Exception as e:
        print(f"[Self-Fix] Failed to log fix: {e}")

# === Entry Point ===
if __name__ == "__main__":
    self_fix_loop()

def log_event():ef mutate(*args, **kwargs): print('[ghost_empire] dummy mutate called')
def drop_files_to_bridge():