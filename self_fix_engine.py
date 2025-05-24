from error_parser import detect_latest_error
from ai_code_generator import generate_code_fix
from code_validator import validate_fix
from auto_deployer import deploy_fix
import json
import os

FIX_LOG_FILE = "data/fixes_log.json"

def log_fix_event(file_path, fix_code):
    if not os.path.exists(FIX_LOG_FILE):
        with open(FIX_LOG_FILE, "w") as f:
            json.dump([], f)

    with open(FIX_LOG_FILE, "r") as f:
        log_data = json.load(f)

    log_data.append({
        "file": file_path,
        "fix": fix_code,
        "status": "applied"
    })

    with open(FIX_LOG_FILE, "w") as f:
        json.dump(log_data, f, indent=2)

def main():
    print("[Self-Fix Engine] Scanning for errors...")
    error_data = detect_latest_error()

    if not error_data:
        print("No new errors detected.")
        return

    file_path, error_msg, broken_code = error_data

    print(f"[Detected] File: {file_path} | Error: {error_msg}")

    fix_code = generate_code_fix(file_path, broken_code, error_msg)
    if not fix_code:
        print("[Fix Generation] Failed.")
        return

    if validate_fix(file_path, fix_code):
        deploy_fix(file_path, fix_code)
        log_fix_event(file_path, fix_code)
        print("[Fix Applied] Successfully deployed fix.")
    else:
        print("[Validation Failed] Fix did not pass tests.")

if __name__ == "__main__":
    main()