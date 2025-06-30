# 🧠 Bridge File Exec Engine – Executes Python files dropped into the incoming folder

import os
import importlib.util
import traceback

INCOMING_FOLDER = "bridge/incoming"

def execute_incoming_files():
    print("[FileExecEngine] 🔧 Initialized. Ready to execute files.")
    os.makedirs(INCOMING_FOLDER, exist_ok=True)

    for filename in os.listdir(INCOMING_FOLDER):
        if filename.endswith(".py"):
            filepath = os.path.join(INCOMING_FOLDER, filename)
            print(f"[FileExecEngine] 🧪 Found file: {filepath}. Executing now...")

            try:
                spec = importlib.util.spec_from_file_location("module.name", filepath)
                foo = importlib.util.module_from_spec(spec)
                spec.loader.exec_module(foo)
                print(f"[FileExecEngine] ✅ Executed: {filename}")
            except Exception as e:
                print(f"[FileExecEngine] ❌ Failed to execute {filename}:\n{traceback.format_exc()}")