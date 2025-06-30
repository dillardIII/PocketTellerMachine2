from ghost_env import INFURA_KEY, VAULT_ADDRESS
# === FILE: reflex_commander.py ===

# 🧠 Reflex Commander – Thinks, decides, triggers macros based on time/logic

import time
from reflex_macro_trigger import ReflexMacroTrigger
from macro_handler import MacroHandler

class ReflexCommander:
    def __init__(self):
        self.reflex = ReflexMacroTrigger()
        self.macro_handler = MacroHandler()
        self.last_triggered = {}

    def run_thinking_loop(self, interval=10):
        print("[ReflexCommander] 🧠 Thinking loop started...")
        while True:
            time.sleep(interval)
            self.think_and_act()

    def think_and_act(self):
        # Get current time in seconds
        current_time = int(time.time())

        # Trigger recon launch every 30 seconds
        if self.should_trigger("recon launch", 30, current_time):
            self.reflex.process("macro: recon launch")

        # Trigger sniper sweep every 60 seconds
        if self.should_trigger("sniper sweep", 60, current_time):
            self.reflex.process("macro: sniper sweep")

    def should_trigger(self, macro_name, cooldown, current_time):
        last = self.last_triggered.get(macro_name, 0)
        if current_time - last >= cooldown:
            self.last_triggered[macro_name] = current_time
            self.log_reflex(macro_name)
            return True
        return False

    def log_reflex(self, macro_name):
        with open("vault/reflex_log.txt", "a") as log:
            log.write(f"[{int(time.time())}] Reflex triggered: {macro_name}\n")

def log_event():ef drop_files_to_bridge():