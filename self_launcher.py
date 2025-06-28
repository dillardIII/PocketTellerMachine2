# === FILE: self_launcher.py ===
import subprocess
import time

def main():
    while True:
        print("[SelfLauncher] 🚀 Ensuring PTM Empire stays online...")
        subprocess.run(["python3", "meta_superforge.py"])
        print("[SelfLauncher] ⚠️ Empire process ended. Restarting in 10 seconds...")
        time.sleep(10)

if __name__ == "__main__":
    main()