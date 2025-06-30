from ghost_env import INFURA_KEY, VAULT_ADDRESS
import time
import os
import json
from datetime import datetime
from cole_code_writer import cole_write_code

CODE_LOG_FILE = "data/code_writer_log.json"
LOOP_SECONDS = 900  # Every 15 minutes (adjust as needed)

def log_code_creation(filename, reason):
    logs = []
    if os.path.exists(CODE_LOG_FILE):
        try:
            with open(CODE_LOG_FILE, "r") as f:
                logs = json.load(f)
        except json.JSONDecodeError:
            logs = []
    logs.append({
        "filename": filename,
        "reason": reason,
        "timestamp": datetime.now().isoformat()
    })
    with open(CODE_LOG_FILE, "w") as f:
        json.dump(logs[-500:], f, indent=2)

def auto_code_writer_cycle():
    print("[AUTO CODE WRITER DAEMON]: Running...")
    # === Simulate smart reasons (Phase 9 will be expanded with AI-based triggers) ===
    reasons = [
        "Periodic strategy refresh",
        "Detected trade losses needing adaptation",
        "Market conditions change",
        "Random experimental strategy"
    ]

    while True:
        try:
            # Pick a reason
            reason = reasons[int(datetime.now().timestamp()) % len(reasons)]
            # Generate new code
            filename = cole_write_code(f"Auto_Strategy_{datetime.now().strftime('%Y%m%d%H%M%S')}", f"Auto-generated because: {reason}")
            # Log the action
            log_code_creation(filename, reason)
            print(f"[AUTO CODE WRITER DAEMON]: Generated {filename} | Reason: {reason}")
        except Exception as e:
            print(f"[AUTO CODE WRITER DAEMON ERROR]: {e}")
        
        time.sleep(LOOP_SECONDS)

if __name__ == "__main__":
    auto_code_writer_cycle()