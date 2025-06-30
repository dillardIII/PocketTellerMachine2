from ghost_env import INFURA_KEY, VAULT_ADDRESS
# === FILE: rebuild_file_exec_engine.py ===
# 🔧 Rebuilds file_exec_engine.py – Code runner

with open("file_exec_engine.py", "w") as f:
    f.write('''# === FILE: file_exec_engine.py ===
import os
import time

WATCH_DIR = "ptm_inbox"

def execute_file(filepath):
    try:
        with open(filepath, "r") as f:
            exec(f.read(), {})
        print(f"[FileExecEngine] ✅ Manually executed: {filepath}")
    except Exception as e:
        print(f"[FileExecEngine] ❌ Error in execute_file: {e}")

def start_exec_engine():
    seen = set()
    print("[FileExecEngine] 🧠 Watching for drops...")
    while True:
        for filename in os.listdir(WATCH_DIR):
            if filename.endswith(".py") and filename not in seen:
                filepath = os.path.join(WATCH_DIR, filename)
                exec(open(filepath).read(), {})
                with open(filepath + ".executed.locked", "w") as f:
                    f.write("executed")
                seen.add(filename)
        time.sleep(1)
''')
print("[rebuild_file_exec_engine] ✅ file_exec_engine.py rebuilt.")

def log_event():ef mutate(*args, **kwargs): print('[ghost_empire] dummy mutate called')
def drop_files_to_bridge():