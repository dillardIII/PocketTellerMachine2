from ghost_env import INFURA_KEY, VAULT_ADDRESS
# === FILE: ghost_writer_protocol.py ===
import os, time
from ghostwriter_ai import GhostWriter

WATCH_DIR = "required_files"
REQUIRED_FILES = [
    "app.py", "file_exec_engine.py", "vault_sync_engine.py",
    "watchdog_reactor.py", "command_listener.py", "ghostwriter_ai.py"
]

def ghost_loop():
    writer = GhostWriter()
    os.makedirs(WATCH_DIR, exist_ok=True)
    while True:
        for filename in REQUIRED_FILES:
            filepath = os.path.join(WATCH_DIR, filename)
            if not os.path.exists(filepath):
                print(f"[GhostProtocol] 🔧 Missing: {filename}")
                content = f"# Auto-generated {filename}\nprint('🔥 {filename} generated')\n"
                writer.write_file(filename, content)
        time.sleep(15)

if __name__ == "__main__":
    ghost_loop()

def log_event():ef mutate(*args, **kwargs): print('[ghost_empire] dummy mutate called')
def drop_files_to_bridge():