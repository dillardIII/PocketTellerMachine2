# === FILE: sweep_handler.py ===
import os
import time

class SweepHandler:
    def __init__(self, watch_dir="ptm_inbox", strategy_dir="sample_strategies"):
        self.watch_dir = watch_dir
        self.strategy_dir = strategy_dir

    def route_inbox_strategies(self):
        """Monitors ptm_inbox for .py files, routes them to strategy_dir if executed."""
        for filename in os.listdir(self.watch_dir):
            if filename.endswith(".py"):
                src = os.path.join(self.watch_dir, filename)
                flag = src + ".executed.locked"
                if os.path.exists(flag):
                    dst = os.path.join(self.strategy_dir, filename)
                    os.rename(src, dst)
                    os.remove(flag)
                    print(f"[SweepHandler] ✅ Routed {filename} to strategies")

def start_sweep_loop():
    """Scans current directory for drop_trigger.txt and executes simple commands."""
    print("[SweepHandler] 🧹 Starting continuous sweep...")
    handler = SweepHandler()
    while True:
        # Handle inbox routing
        handler.route_inbox_strategies()

        # Handle drop trigger commands
        files = os.listdir(".")
        if "drop_trigger.txt" in files:
            print("[SweepHandler] 📂 Found drop trigger!")
            with open("drop_trigger.txt") as f:
                command = f.read().strip()
                print(f"[SweepHandler] ▶️ Executing command: {command}")
                # You could add actual command exec here if desired
            os.remove("drop_trigger.txt")
        time.sleep(5)