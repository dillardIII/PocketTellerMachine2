# === FILE: screeps_login_test.py ===

import requests
import json
import os
from datetime import datetime

# === Config ===
SCREEPS_API_BASE = "https://screeps.com/api"
SCREEPS_EMAIL = os.getenv("SCREEPS_EMAIL")
SCREEPS_PASSWORD = os.getenv("SCREEPS_PASSWORD")

LOG_FILE = "logs/screeps_login_log.json"
os.makedirs("logs", exist_ok=True)

# === Login Function ===
def screeps_login():
    print("[Screeps Login] Attempting login...")

    payload = {
        "email": SCREEPS_EMAIL,
        "password": SCREEPS_PASSWORD
    }

    try:
        response = requests.post(f"{SCREEPS_API_BASE}/auth/signin", data=payload)
        result = response.json()

        if "token" in result:
            print("[Screeps Login] Login successful.")
            log_login_result(True, result)
            return result["token"]
        else:
            print(f"[Screeps Login] Login failed: {result}")
            log_login_result(False, result)
            return None

    except Exception as e:
        print(f"[Screeps Login] Error: {str(e)}")
        log_login_result(False, {"error": str(e)})
        return None

# === Log Writer ===
def log_login_result(success, data):
    entry = {
        "timestamp": datetime.now().isoformat(),
        "success": success,
        "data": data
    }

    logs = []
    if os.path.exists(LOG_FILE):
        with open(LOG_FILE, "r") as f:
            logs = json.load(f)

    logs.append(entry)

    with open(LOG_FILE, "w") as f:
        json.dump(logs[-50:], f, indent=2)

    print(f"[Screeps Login] Logged result at {LOG_FILE}")

# === Execute Test ===
if __name__ == "__main__":
    token = screeps_login()
    if token:
        print(f"[Screeps Login] Received Token: {token[:10]}... [Truncated]")
    else:
        print("[Screeps Login] No token received.")