# === FILE: autonomy_engine.py ===

# 🧠 Autonomy Engine – Watches queues, triggers GhostForge rebuilds, logs results

import os
import time
from ghostforge_core import rebuild_file
from file_exec_engine import execute_file

# === Define folders for queue and log processing ===
AUTOFIX_QUEUE = "autofix_queue"
AUTOBUILD_QUEUE = "autobuild_queue"
AUTOFIX_LOG = "autofix_logs"
AUTOBUILD_LOG = "autobuild_logs"

# === Ensure required directories exist ===
def ensure_dirs():
    for d in [AUTOFIX_QUEUE, AUTOBUILD_QUEUE, AUTOFIX_LOG, AUTOBUILD_LOG]:
        os.makedirs(d, exist_ok=True)

# === Main autonomy loop ===
def run_autonomy_engine():
    print("[AutonomyEngine] 🤖 Watching autofix and autobuild queues...")
    ensure_dirs()

    while True:
        # === Handle Fixes ===
        for file in os.listdir(AUTOFIX_QUEUE):
            path = os.path.join(AUTOFIX_QUEUE, file)
            print(f"[AutonomyEngine] 🔧 Rebuilding: {file}")
            try:
                output = rebuild_file(file)
                with open(os.path.join(AUTOFIX_LOG, file + ".log"), "w") as f:
                    f.write(output or "Rebuild attempted")
                os.remove(path)
            except Exception as e:
                print(f"[AutonomyEngine] ❌ Error fixing {file}: {e}")

        # === Handle Builds ===
        for file in os.listdir(AUTOBUILD_QUEUE):
            path = os.path.join(AUTOBUILD_QUEUE, file)
            print(f"[AutonomyEngine] 🛠️ Building: {file}")
            try:
                output = rebuild_file(file, fresh=True)
                with open(os.path.join(AUTOBUILD_LOG, file + ".log"), "w") as f:
                    f.write(output or "Build attempted")
                os.remove(path)
            except Exception as e:
                print(f"[AutonomyEngine] ❌ Build error {file}: {e}")

        time.sleep(3)

# === Optional standalone runner ===
if __name__ == "__main__":
    run_autonomy_engine()