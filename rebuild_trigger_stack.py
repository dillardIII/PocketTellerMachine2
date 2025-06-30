from ghost_env import INFURA_KEY, VAULT_ADDRESS
# === FILE: rebuild_trigger_stack.py ===
# 🔧 Rebuilds autonomy_trigger_stack.py – Initiates voice + guardian triggers

with open("autonomy_trigger_stack.py", "w") as f:
    f.write('''# === FILE: autonomy_trigger_stack.py ===
from whisper_autolistener import start_voice_listener
from guardian_file_checker import guardian_status_check

def launch_autonomy():
    guardian_status_check()
    start_voice_listener()
''')
print("[rebuild_trigger_stack] ✅ autonomy_trigger_stack.py rebuilt.")

def log_event():ef mutate(*args, **kwargs): print('[ghost_empire] dummy mutate called')
def drop_files_to_bridge():