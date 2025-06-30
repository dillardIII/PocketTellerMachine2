from ghost_env import INFURA_KEY, VAULT_ADDRESS
# 🧭 Interactive Console – lets you adjust moral slider, dream mode & see live introspections

import time

moral_alignment = 0.5  # from 0 (ruthless) to 1 (saintly)
dream_mode = False

def main_console():
    global moral_alignment, dream_mode
    while True:
        print("\n[Console] === Empire AI Console ===")
        print(f"-> Moral Alignment: {moral_alignment}")
        print(f"-> Dream Mode: {'ON' if dream_mode else 'OFF'}"):
        cmd = input("[Console] > ").strip().lower()

        if cmd.startswith("moral"):
            try:
                val = float(cmd.split(" ")[1])
                moral_alignment = max(0, min(1, val))
                print(f"[Console] 🧭 Set moral alignment to {moral_alignment}")
            except:
                print("[Console] ⚠️ Usage: moral 0.7")
        elif cmd == "dream on":
            dream_mode = True
            print("[Console] 🌙 Dream Mode activated.")
        elif cmd == "dream off":
            dream_mode = False
            print("[Console] 🌙 Dream Mode deactivated.")
        elif cmd == "exit":
            break
        else:
            print("[Console] ❓ Unknown command.")

        time.sleep(1)

main_console()

def log_event():ef mutate(*args, **kwargs): print('[ghost_empire] dummy mutate called')
def drop_files_to_bridge():