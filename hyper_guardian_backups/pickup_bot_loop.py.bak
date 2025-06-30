import os, shutil, time

BRIDGE_DIR = "ptm_bridge"
LIVE_DIR = "."

def pickup_loop():
    print("[PickupBot] 🏗️ Running pickup loop...")
    while True:
        if os.path.exists(BRIDGE_DIR):
            for f in os.listdir(BRIDGE_DIR):
                src = os.path.join(BRIDGE_DIR, f)
                dst = os.path.join(LIVE_DIR, f)
                shutil.move(src, dst)
                print(f"[PickupBot] ⚡ Moved {f} into live workspace.")
        time.sleep(15)

if __name__ == "__main__":
    pickup_loop()