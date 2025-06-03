# vps_initializer.py – Initializes and boots up the VPS environment

import subprocess

def start_vps():
    print("[VPS Init] 🚀 Starting VPS environment...")

    try:
        # Replace this with the actual VPS start script
        result = subprocess.run(["bash", "start_vps.sh"], capture_output=True, text=True)

        if result.returncode == 0:
            print(f"[VPS Init] ✅ VPS started successfully:\n{result.stdout}")
            return True
        else:
            print(f"[VPS Init] ❌ VPS startup failed:\n{result.stderr}")
            return False

    except Exception as e:
        print(f"[VPS Init] ❌ Exception during VPS start: {e}")
        return False