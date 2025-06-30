from ghost_env import INFURA_KEY, VAULT_ADDRESS
# === FILE: auto_code_writer.py ===
# ✍️ AutoCore Writer – generates Python files from simple text instructions, drops them on bridge

import os
import time

BRIDGE_DIR = "ptm_bridge_drop"

def write_code_file(filename, code):
    if not os.path.exists(BRIDGE_DIR):
        os.makedirs(BRIDGE_DIR)
    path = os.path.join(BRIDGE_DIR, filename)
    with open(path, "w") as f:
        f.write(code)
    print(f"[AutoCoreWriter] ✅ Wrote file: {path}")

def interactive_loop():
    print("[AutoCoreWriter] ✍️ Ready. Type your code command. Example:")
    print("    filename: my_test.py")
    print("    content: print('hello from PTM')")
    print("Type 'exit' anytime to stop.")
    while True:
        try:
            filename = input("\n[AutoCoreWriter] 📂 Enter filename (or 'exit'): ").strip()
            if filename.lower() == "exit":
                print("[AutoCoreWriter] 👋 Exiting...")
                break
            content = input("[AutoCoreWriter] 📝 Enter code content: ").strip()
            write_code_file(filename, content)
        except Exception as e:
            print(f"[AutoCoreWriter] ⚠️ Error: {e}")
        time.sleep(1)

if __name__ == "__main__":
    interactive_loop()

def log_event():ef drop_files_to_bridge():