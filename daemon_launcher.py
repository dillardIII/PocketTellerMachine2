import threading
import time
from error_parser import get_latest_error
from ai_code_generator import generate_code_fix
from auto_deployer import deploy_fix
from fix_logger import log_fix

# === Daemon for Continuous Self-Fix Loop ===
def self_fix_loop():
    print("[Daemon] Self-Fix Loop started.")
    while True:
        error_data = get_latest_error()
        if error_data:
            print(f"[Daemon] Detected Error: {error_data['error']} in {error_data['file']}")
            fixed_code = generate_code_fix(error_data)
            if fixed_code:
                success = deploy_fix(error_data['file'], fixed_code)
                if success:
                    log_fix(error_data, fixed_code)
                else:
                    print(f"[Daemon] Fix failed validation. Skipping deployment for {error_data['file']}.")
            else:
                print("[Daemon] Failed to generate code fix.")
        else:
            print("[Daemon] No new errors detected.")
        
        # Wait before next iteration
        time.sleep(30)

# === Start the Self-Fix Daemon ===
def start_self_fix_daemon():
    daemon_thread = threading.Thread(target=self_fix_loop, daemon=True)
    daemon_thread.start()
    print("[Daemon] Self-Fix Daemon is running in the background.")

# === Main Execution ===
if __name__ == "__main__":
    start_self_fix_daemon()
    # Keep main thread alive
    while True:
        time.sleep(60)