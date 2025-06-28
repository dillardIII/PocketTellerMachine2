import os
import time
from command_memory import log_command_event

WATCH_DIR = "ptm_inbox"
seen = set()

def execute_file(filepath):
    try:
        with open(filepath, "r") as f:
            code = f.read()
            exec(code, {})
        print(f"[FileExecEngine] ✅ Manually executed: {filepath}")
        log_command_event("FileExecuted", filepath)
    except Exception as e:
        print(f"[FileExecEngine] ❌ Error in execute_file: {e}")

def start_exec_engine():
    print("[FileExecEngine] 🧠 Watching ptm_inbox for .py files...")
    while True:
        try:
            files = os.listdir(WATCH_DIR)
            print(f"[FileExecEngine] 🧾 Inbox contents: {files}")
            for filename in files:
                if filename.endswith(".py") and filename not in seen:
                    filepath = os.path.join(WATCH_DIR, filename)
                    if not os.path.exists(filepath):
                        continue
                    print(f"[FileExecEngine] ▶️ Executing: {filename}")
                    execute_file(filepath)
                    with open(filepath + ".executed.locked", "w") as f:
                        f.write("executed:locked")
                    seen.add(filename)
        except Exception as e:
            print(f"[FileExecEngine] ❌ Loop error: {e}")
        time.sleep(5)