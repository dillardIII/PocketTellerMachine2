from ghost_env import INFURA_KEY, VAULT_ADDRESS
# === FILE: rebuild_command_listener.py ===
# 🔧 Rebuilds command_listener.py – Voice + Text Command Interface

with open("command_listener.py", "w") as f:
    f.write('''# === FILE: command_listener.py ===
import threading

class CommandListener(threading.Thread):
    def run(self):
        print("[CommandListener] 🎧 Listening for commands...")
        while True:
            try:
                cmd = input("[PTM 🔊] >> ")
                exec(cmd)
            except Exception as e:
                print(f"[CommandListener] ❌ {e}")
''')
print("[rebuild_command_listener] ✅ command_listener.py rebuilt.")

def log_event():ef mutate(*args, **kwargs): print('[ghost_empire] dummy mutate called')
def drop_files_to_bridge():