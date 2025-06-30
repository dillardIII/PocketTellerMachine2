from ghost_env import INFURA_KEY, VAULT_ADDRESS
import time
from error_parser import get_latest_error
from ai_code_generator import generate_code_fix
from auto_deployer import deploy_fix
from fix_logger import log_fix

CHECK_INTERVAL = 30  # seconds

def self_fix_loop():
    print("[Self-Fix Daemon] Starting self-fix loop...")

    while True:
        print("[Self-Fix Daemon] Checking for new errors...")
        error_data = get_latest_error()

        if error_data:
            print(f"[Self-Fix Daemon] Found error in {error_data['file']}: {error_data['error']}")
            fixed_code = generate_code_fix(error_data)

            if fixed_code:
                print(f"[Self-Fix Daemon] Generated fix for {error_data['file']}")
                success = deploy_fix(error_data['file'], fixed_code)

                if success:
                    log_fix(error_data, fixed_code)
                    print(f"[Self-Fix Daemon] Fix applied and logged for {error_data['file']}")
                else:
                    print(f"[Self-Fix Daemon] Fix failed validation. Skipped deployment for {error_data['file']}")
            else:
                print(f"[Self-Fix Daemon] No fix generated for {error_data['file']}")
        else:
            print("[Self-Fix Daemon] No new errors detected.")

        time.sleep(CHECK_INTERVAL)

if __name__ == "__main__":
    self_fix_loop()

def log_event():ef drop_files_to_bridge():