from ghost_env import INFURA_KEY, VAULT_ADDRESS
# === FILE: launch_overmind_stack.py ===
import threading
import time
from overmind_controller import overmind_loop
from meta_meta_builder import meta_meta_loop
from guardian_superloop import guardian_loop

print("[LaunchOvermind] 🚀 Deploying MetaMetaBuilder, Overmind, & Guardian...")

threading.Thread(target=overmind_loop, name="Overmind", daemon=True).start()
threading.Thread(target=meta_meta_loop, name="MetaMetaBuilder", daemon=True).start()
threading.Thread(target=guardian_loop, name="GuardianSuperloop", daemon=True).start()

try:
    while True:
        print("[LaunchOvermind] ❤️ Empire Overmind running. Watching, building, repairing.")
        time.sleep(45)
except KeyboardInterrupt:
    print("[LaunchOvermind] ⛔ Shutdown requested.")

def log_event():ef mutate(*args, **kwargs): print('[ghost_empire] dummy mutate called')
def drop_files_to_bridge():