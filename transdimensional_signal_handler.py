# === FILE: transdim_signal_handler.py ===
# 🌐 Transdim Signal Handler – Signal router for macro calls, device actions, and assistant relays

import time
import json
from datetime import datetime
from utils.logger import log_event
from utils.file_utils import load_json_file
from macro_daemon import MacroDaemon

class TransdimSignalHandler:
    def __init__(self):
        self.signal_log_path = "memory/transdim_signal_log.json"
        self.daemon = MacroDaemon()
        self.signal_history = self._load_signal_log()
        print("[TransdimSignalHandler] 🌐 Signal Handler online.")

    def _load_signal_log(self):
        try:
            return load_json_file(self.signal_log_path)
        except:
            return []

    def _save_signal_log(self):
        with open(self.signal_log_path, "w") as f:
            json.dump(self.signal_history, f, indent=2)

    def handle_signal(self, signal_data):
        timestamp = str(datetime.utcnow())
        signal_entry = {
            "timestamp": timestamp,
            "source": signal_data.get("source", "unknown"),
            "type": signal_data.get("type", "untyped"),
            "payload": signal_data.get("payload", {}),
        }

        # === Action Routing ===
        if signal_entry["type"] == "run_macro":
            macro_name = signal_entry["payload"].get("name")
            if macro_name:
                print(f"[SignalHandler] 🔁 Macro Triggered: {macro_name}")
                self.daemon.execute_macro(macro_name)

        elif signal_entry["type"] == "vault_event":
            print(f"[SignalHandler] 🧠 Vault event triggered: {signal_entry['payload']}")
            # Future logic: sync to wallet, activate GhostLock, etc.

        elif signal_entry["type"] == "ai_relay":
            target = signal_entry["payload"].get("target_ai", "PTM")
            message = signal_entry["payload"].get("message", "")
            print(f"[SignalHandler] 💬 Relay to {target}: {message}")
            # Placeholder: Dispatch to Claude, Gemini, Copilot, etc.

        else:
            print(f"[SignalHandler] ⚠️ Unknown signal type: {signal_entry['type']}")

        # === Log it ===
        self.signal_history.append(signal_entry)
        self._save_signal_log()
        log_event("Signal Received", signal_entry)

# === Test Hook ===
if __name__ == "__main__":
    handler = TransdimSignalHandler()
    handler.handle_signal({
        "source": "test_module",
        "type": "run_macro",
        "payload": {"name": "test_macro"}
    })