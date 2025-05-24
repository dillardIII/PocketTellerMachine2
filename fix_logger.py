import json
import os
import time

FIXES_LOG_FILE = "data/fixes_log.json"

# === Log Successful Code Fix ===
def log_fix(error_data, fixed_code):
    log_entry = {
        "timestamp": time.strftime("%Y-%m-%d %H:%M:%S"),
        "file": error_data['file'],
        "error": error_data['error'],
        "fix": fixed_code
    }

    # Ensure log directory exists
    os.makedirs(os.path.dirname(FIXES_LOG_FILE), exist_ok=True)

    # Append to existing log or create new log file
    if os.path.exists(FIXES_LOG_FILE):
        try:
            with open(FIXES_LOG_FILE, 'r+') as f:
                logs = json.load(f)
                logs.append(log_entry)
                f.seek(0)
                json.dump(logs, f, indent=2)
            print(f"[Fix Logger] Logged fix for {error_data['file']}")
        except json.JSONDecodeError:
            # Handle corrupted JSON file case
            with open(FIXES_LOG_FILE, 'w') as f:
                json.dump([log_entry], f, indent=2)
            print(f"[Fix Logger] Corrupted log detected. Reinitialized log file.")
    else:
        with open(FIXES_LOG_FILE, 'w') as f:
            json.dump([log_entry], f, indent=2)
        print(f"[Fix Logger] Created new log file and logged fix.")

# === Log Fix Entry (Alternative Form) ===
def log_fix_entry(file_path, error_message, fix_code):
    log_entry = {
        "timestamp": time.strftime("%Y-%m-%d %H:%M:%S"),
        "file": file_path,
        "error": error_message,
        "fix": fix_code
    }

    if not os.path.exists(os.path.dirname(FIXES_LOG_FILE)):
        os.makedirs(os.path.dirname(FIXES_LOG_FILE))

    try:
        if os.path.exists(FIXES_LOG_FILE):
            with open(FIXES_LOG_FILE, 'r') as f:
                log_data = json.load(f)
        else:
            log_data = []

        log_data.append(log_entry)

        with open(FIXES_LOG_FILE, 'w') as f:
            json.dump(log_data, f, indent=2)

        print(f"[Fix Logger] Logged fix for {file_path}")

    except Exception as e:
        print(f"[Fix Logger] Error logging fix: {e}")