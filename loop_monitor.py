from ghost_env import INFURA_KEY, VAULT_ADDRESS
import threading
import time
from file_exec_engine import start_exec_engine
from command_memory import log_command_event

def monitor_loop_health():
    print("[LoopMonitor] 🧠 Watching execution engine health...")
    while True:
        thread_names = [t.name for t in threading.enumerate()]
        print(f"[LoopMonitor] 👀 Active threads: {thread_names}")
        if "FileExecEngine" not in thread_names:
            print("[LoopMonitor] 🔁 Restarting FileExecEngine...")
            threading.Thread(target=start_exec_engine, name="FileExecEngine").start()
            log_command_event("EngineRestart", "FileExecEngine restarted by LoopMonitor")
        time.sleep(10)

def log_event():ef drop_files_to_bridge():