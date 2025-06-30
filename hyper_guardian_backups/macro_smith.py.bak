# === FILE: macro_smith.py ===
# 🔨 MacroSmith – Learns user behavior and generates macros for future execution

import json
from datetime import datetime
from utils.logger import log_event

MACRO_FILE = "memory/forged_macros.json"

class MacroSmith:
    def __init__(self):
        self.macros = []
        self.log_file = MACRO_FILE

    def observe_action(self, source, action, context=""):
        macro = {
            "timestamp": str(datetime.now()),
            "source": source,
            "action": action,
            "context": context
        }

        self.macros.append(macro)
        log_event(f"🛠️ MacroSmith logged: {macro}")
        self.save()

    def save(self):
        with open(self.log_file, "w") as f:
            json.dump(self.macros, f, indent=4)

# Example usage
if __name__ == "__main__":
    smith = MacroSmith()
    smith.observe_action("User", "Buy AAPL", "Voice Command > Confidence 0.92")