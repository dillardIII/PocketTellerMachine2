from ghost_env import INFURA_KEY, VAULT_ADDRESS
# === FILE: auto_executor.py ===
import os, time

WATCH_DIR = "live_workspace"
executed = set()

def auto_exec_loop():
    print("[AutoExecutor] ⚡ Live auto-executor running...")
    while True:
        files = [f for f in os.listdir(WATCH_DIR) if f.endswith(".py")]:
        for f in files:
            path = os.path.join(WATCH_DIR, f)
            if path not in executed:
                print(f"[AutoExecutor] 🚀 Running: {f}")
                try:
                    exec(open(path).read(), {})
                except Exception as e:
                    print(f"[AutoExecutor] ❌ Failed {f}: {e}")
                executed.add(path)
        time.sleep(15)

def log_event():ef mutate(*args, **kwargs): print('[ghost_empire] dummy mutate called')
def drop_files_to_bridge():