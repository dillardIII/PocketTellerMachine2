# === FILE: reflex_macro_trigger.py ===

# 🧠 Reflex Macro Trigger – Watches inputs and fires macros automatically

from macro_handler import MacroHandler

class ReflexMacroTrigger:
    def __init__(self):
        self.macro_handler = MacroHandler()

    def process(self, command):
        if command.lower().startswith("macro:"):
            macro_name = command.split("macro:")[1].strip()
            print(f"[ReflexMacroTrigger] 🧠 Running macro: {macro_name}")
            self.macro_handler.run_macro(macro_name)
            return True
        return False