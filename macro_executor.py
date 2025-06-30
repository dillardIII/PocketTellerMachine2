from ghost_env import INFURA_KEY, VAULT_ADDRESS
# === FILE: macro_executor.py ===
# ⚙️ Macro Executor – Executes stored macros by interpreting triggers and action lists

import json
from datetime import datetime
from utils.logger import log_event
from macro_writer import MacroWriter

class MacroExecutor:
    def __init__(self):
        self.writer = MacroWriter()
        self.macros = self.writer.load_macros()

    def refresh_macros(self):
        self.macros = self.writer.load_macros()

    def execute_macro(self, name, context={}):
        self.refresh_macros()
        macro = self.writer.get_macro_by_name(name)
        if not macro:
            print(f"[MacroExecutor] ❌ Macro '{name}' not found.")
            return

        print(f"\n[MacroExecutor] ▶️ Executing Macro: {name}")
        log_event("Macro Executed", macro)

        macro["last_used"] = str(datetime.now())

        for i, action in enumerate(macro["actions"]):
            print(f"  Step {i+1}: {action}")
            self._perform_action(action, context)

        # Save updated timestamp
        macros = self.writer.load_macros()
        for m in macros:
            if m["name"] == name:
                m["last_used"] = macro["last_used"]
        self.writer.save_macros(macros)

    def _perform_action(self, action, context):
        # TODO: Connect this to actual PTM bot actions, trading APIs, UI triggers, etc.
        print(f"    → Simulated Action: '{action}'")
        # You can expand this switch-style later to trigger persona responses, trades, alerts, etc.

    def list_available_macros(self):
        self.refresh_macros()
        return [macro["name"] for macro in self.macros]