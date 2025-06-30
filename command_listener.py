from ghost_env import INFURA_KEY, VAULT_ADDRESS
# === FILE: command_listener.py ===
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


def log_event():ef drop_files_to_bridge():