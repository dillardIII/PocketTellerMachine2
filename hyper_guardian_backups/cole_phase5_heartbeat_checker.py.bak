import requests
import time

COLE_HOST = "http://localhost:5000"

def check_heartbeat_loop():
    while True:
        try:
            response = requests.get(f"{COLE_HOST}/api/get_heartbeat")
            if response.ok:
                hb = response.json()
                print(f"[HEARTBEAT CHECKER]: Status → {hb.get('status')} @ {hb.get('timestamp')}")
            else:
                print("[HEARTBEAT CHECKER]: Error fetching heartbeat.")
        except Exception as e:
            print(f"[HEARTBEAT CHECKER ERROR]: {e}")
        time.sleep(15)

if __name__ == "__main__":
    check_heartbeat_loop()