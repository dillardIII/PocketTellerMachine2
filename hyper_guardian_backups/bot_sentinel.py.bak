# === FILE: bot_sentinel.py ===
# 🛡️ Bot Sentinel – Monitors bot health, status, and self-recovery

import os
import time
import threading
import traceback

from file_patcher import patch_file
from ai_code_generator import generate_code_fix_from_trace

class BotSentinel:
    def __init__(self, bot_name, file_path, check_interval=10):
        self.bot_name = bot_name
        self.file_path = file_path
        self.check_interval = check_interval
        self.running = False
        self.last_error = ""

    def start_monitoring(self):
        print(f"[Sentinel] 🧠 Monitoring bot: {self.bot_name}")
        self.running = True
        thread = threading.Thread(target=self._monitor_loop)
        thread.daemon = True
        thread.start()

    def stop_monitoring(self):
        print(f"[Sentinel] 🛑 Stopped monitoring {self.bot_name}")
        self.running = False

    def _monitor_loop(self):
        while self.running:
            try:
                self._run_bot()
            except Exception as e:
                self.last_error = str(e)
                trace = traceback.format_exc()
                print(f"[Sentinel] ⚠️ Error detected in {self.bot_name}:\n{trace}")

                print(f"[Sentinel] 🤖 Attempting AI repair...")
                fixed_code = generate_code_fix_from_trace(trace)

                if fixed_code:
                    result = patch_file(self.file_path, fixed_code)
                    if result["status"] == "success":
                        print(f"[Sentinel] 🔄 Bot repaired and relaunched.")
                    else:
                        print(f"[Sentinel] ❌ Patch failed: {result.get('message')}")
                else:
                    print("[Sentinel] 🚫 No fix generated.")
            time.sleep(self.check_interval)

    def _run_bot(self):
        # This is a placeholder for executing the bot.
        # You should replace this with actual dynamic import or subprocess run logic.
        print(f"[Sentinel] ⏳ Checking {self.bot_name}...")
        exec(open(self.file_path).read(), {})