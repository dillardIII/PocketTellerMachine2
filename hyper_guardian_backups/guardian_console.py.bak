# 🖥️ Guardian Console – matrix view of cams + alerts

import json
import time

def display_matrix():
    while True:
        try:
            with open("vault/guardian_log.json") as f:
                lines = f.readlines()
            print("\n=== Guardian Alert Console ===")
            for line in lines[-5:]:
                print(line.strip())
        except Exception as e:
            print(f"[GuardianConsole] ⚠️ {e}")
        time.sleep(20)

display_matrix()