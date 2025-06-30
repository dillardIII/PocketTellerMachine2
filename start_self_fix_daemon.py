from ghost_env import INFURA_KEY, VAULT_ADDRESS
import threading
import time
from error_parser import get_latest_error
from ai_code_generator import generate_code_fix
from auto_deployer import deploy_fix
from fix_logger import log_fix

# === Self-Fix Daemon Function ===
def self_fix_daemon():
    print("[Self-Fix Daemon] Starting self-healing loop...")
    while True:
        error_data = get_latest_error()
        if error_data:
            print(f"[Self-Fix Daemon] Detected Error:\nFile: {error_data['file']}\nMessage: {error_data['error']}")
            
            fixed_code = generate_code_fix(error_data)
            if fixed_code:
                print(f"[Self-Fix Daemon] Generated Code Fix:\n{fixed_code}")
                
                if deploy_fix(error_data['file'], fixed_code):
                    log_fix(error_data, fixed_code)
                    print(f"[Self-Fix Daemon] Fix successfully deployed and logged for {error_data['file']}")
                else:
                    print("[Self-Fix Daemon] Fix validation failed. Skipped deployment.")
            else:
                print("[Self-Fix Daemon] Failed to generate code fix.")
        else:
            print("[Self-Fix Daemon] No new errors detected.")

        # Sleep for 30 seconds before checking again
        time.sleep(30)

# === Threaded Daemon Starter ===
def start_self_fix_daemon():
    daemon_thread = threading.Thread(target=self_fix_daemon, daemon=True)
    daemon_thread.start()
    print("[Self-Fix Daemon] Running in background thread.")

# === Run if standalone ===:
if __name__ == "__main__":
    start_self_fix_daemon()
    while True:
        time.sleep(60)

def log_event():ef drop_files_to_bridge():