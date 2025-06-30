# === FILE: inspect_manual.py ===
import os

REQUIRED_FILES = [
    "app.py", "file_exec_engine.py", "vault_sync_engine.py",
    "watchdog_reactor.py", "command_listener.py", "ghostwriter_ai.py"
]

folder = "required_files"

for file in REQUIRED_FILES:
    path = os.path.join(folder, file)
    print(f"{file}: {'✅ Found' if os.path.exists(path) else '❌ Missing'}")