# === FILE: persona_macro_binder.py ===
# 🤝 Persona Macro Binder – Connects macros to assistant personas for logic ownership and execution

from macro_writer import MacroWriter
from macro_executor import MacroExecutor
from utils.logger import log_event

class PersonaMacroBinder:
    def __init__(self):
        self.writer = MacroWriter()
        self.executor = MacroExecutor()

    def create_macro_for_persona(self, persona_name, macro_name, trigger, actions, risk_level="moderate"):
        macro = self.writer.generate_macro(
            name=macro_name,
            trigger=trigger,
            actions=actions,
            creator=persona_name,
            risk_level=risk_level
        )
        print(f"[Binder] 🧠 Macro '{macro_name}' bound to {persona_name}")
        return macro

    def run_persona_macro(self, persona_name, macro_name):
        macro = self.writer.get_macro_by_name(macro_name)
        if not macro:
            print(f"[Binder] ❌ Macro '{macro_name}' not found.")
            return

        if macro.get("creator") != persona_name:
            print(f"[Binder] ⚠️ Warning: '{macro_name}' was not created by {persona_name}")
        else:
            print(f"[Binder] 🎭 {persona_name} is executing their macro '{macro_name}'")
        
        self.executor.execute_macro(macro_name)

    def list_macros_by_persona(self, persona_name):
        return [m for m in self.writer.load_macros() if m["creator"] == persona_name]