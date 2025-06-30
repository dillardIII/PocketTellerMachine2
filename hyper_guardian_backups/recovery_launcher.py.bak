# === FILE: recovery_launcher.py ===
# 💣 Launches recovery logic when files fail

import os
from file_exec_engine import execute_file

def launch_recovery_sweep():
    critical = ["main.py", "file_exec_engine.py", "autonomy_daemon.py"]
    for file in critical:
        if not os.path.exists(file):
            print(f"[RecoveryLauncher] 🚨 {file} missing — triggering rebuild")
            try:
                execute_file(f"rebuild_{file.replace('.py','')}.py")
            except:
                print(f"[RecoveryLauncher] ❌ Failed to recover {file}")