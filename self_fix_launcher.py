import threading
from self_fix_loop import self_fix_loop

# === Launcher for Self-Fix System ===
def start_self_fix_system():
    print("[Launcher] Initiating Self-Fix System in background thread...")
    fix_thread = threading.Thread(target=self_fix_loop, daemon=True)
    fix_thread.start()
    print("[Launcher] Self-Fix System is running.")

# === Example Usage ===
if __name__ == "__main__":
    start_self_fix_system()

    # Placeholder main loop (simulate app running)
    try:
        while True:
            pass  # Main application loop stays alive
    except KeyboardInterrupt:
        print("\n[Launcher] Shutting down Self-Fix System.")