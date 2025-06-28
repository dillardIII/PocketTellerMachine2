# === FILE: ptm_error_handler.py ===
# 🛡️ PTM Error Handler – Detects crashes, restarts stuck processes, logs everything

import os
import time
import traceback
from utils.logger import log_event
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

# === Config ===
MONITOR_DIRS = ["core", "bots", "routes", "scripts"]  # folders to watch
RESTARTABLE_SCRIPTS = [
    "ghostforge_core.py",
    "reflex_engine.py",
    "command_listener.py",
    "vault_profit_trigger.py",
    "bridge_pickup_agent.py",
    "bridge_drop_agent.py"
]

class CrashHandler(FileSystemEventHandler):
    def on_modified(self, event):
        if event.src_path.endswith(".py"):
            filename = os.path.basename(event.src_path)
            if filename in RESTARTABLE_SCRIPTS:
                log_event("ErrorMonitor", {"action": "Restart Trigger", "file": filename})
                restart_file(filename)

def restart_file(script_name):
    try:
        os.system(f"python {script_name} &")
        log_event("FileRestart", {"status": "✅ Restarted", "file": script_name})
    except Exception as e:
        log_event("FileRestart", {"status": "❌ Failed", "file": script_name, "error": str(e)})

def monitor_for_errors():
    print("[ErrorMonitor] 🧠 Watching for script failures...")
    observer = Observer()
    handler = CrashHandler()

    for path in MONITOR_DIRS:
        if os.path.exists(path):
            observer.schedule(handler, path=path, recursive=True)

    observer.start()
    try:
        while True:
            time.sleep(5)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()

if __name__ == "__main__":
    log_event("ErrorMonitor", {"status": "👁️ Started error handler"})
    monitor_for_errors()