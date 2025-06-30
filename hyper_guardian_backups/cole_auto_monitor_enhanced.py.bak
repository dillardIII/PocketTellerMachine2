import time
import requests

def check_heartbeat():
    try:
        response = requests.get("http://localhost:5000/api/get_heartbeat")
        data = response.json()
        print(f"[COLE MONITOR]: Status {data['status']} at {data['timestamp']}")
    except Exception as e:
        print(f"[COLE MONITOR ERROR]: {e}")

def monitor_loop():
    print("[COLE MONITOR]: Enhanced monitor started...")
    while True:
        check_heartbeat()
        time.sleep(30)

if __name__ == "__main__":
    monitor_loop()