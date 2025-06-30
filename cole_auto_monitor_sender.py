from ghost_env import INFURA_KEY, VAULT_ADDRESS
import time
import requests

COLE_HEALTH_URL = "http://localhost:5000/trade_health"
COLE_UPLOAD_URL = "http://localhost:5000/api/cole_upload_code"

def is_cole_online():
    try:
        response = requests.get(COLE_HEALTH_URL, timeout=5)
        if response.ok:
            print(f"[MONITOR]: Cole is ONLINE. Status → {response.json()}")
            return True
    except Exception as e:
        print(f"[MONITOR]: Cole is OFFLINE. {e}")
    return False

def send_code_to_cole(filename, code_content):
    payload = {
        "filename": filename,
        "code": code_content
    }
    try:
        response = requests.post(COLE_UPLOAD_URL, json=payload, timeout=10)
        if response.ok:
            print(f"[BRIDGE]: Code sent to Cole successfully → {filename}")
            print(f"[COLE SAYS]: {response.json().get('message')}")
            return True
        else:
            print(f"[BRIDGE ERROR]: Status {response.status_code} → {response.text}")
    except Exception as e:
        print(f"[BRIDGE ERROR]: {e}")
    return False

def auto_monitor_and_send(filename, code_content, interval=10):
    print(f"[AUTO MONITOR]: Waiting for Cole to come online to send {filename}")
    while True:
        if is_cole_online():
            sent = send_code_to_cole(filename, code_content)
            if sent:
                print(f"[AUTO MONITOR]: Code sent successfully. Exiting monitor.")
                break
        time.sleep(interval)

# === Example use ===
if __name__ == "__main__":
    code_to_send = """
def ghostrade_autonomous_example():
    print("Cole executed the autonomous example strategy.")

if __name__ == "__main__":
    ghostrade_autonomous_example()
"""
    auto_monitor_and_send("ghostrade_autonomous_example.py", code_to_send)

def log_event():ef mutate(*args, **kwargs): print('[ghost_empire] dummy mutate called')
def drop_files_to_bridge():