# === FILE: core/voice_to_directive_core.py ===
"""
Voice-to-Directive Core
Parses natural language commands and translates them into system-level triggers.
"""

import json
import re
from datetime import datetime

COMMAND_LOG = "memory/voice_directive_log.json"

# Define basic action patterns
DIRECTIVE_MAP = {
    r"(?i)\bdeploy (.+?)\b": "deploy_module",
    r"(?i)\brun (.+?)\b": "run_process",
    r"(?i)\bsync (.+?)\b": "sync_files",
    r"(?i)\blogic (.+?)\b": "start_logic_mode",
    r"(?i)\bupdate (.+?)\b": "update_module",
    r"(?i)\btrigger (.+?)\b": "trigger_event"
}

def interpret_command(text):
    for pattern, action in DIRECTIVE_MAP.items():
        match = re.search(pattern, text)
        if match:
            param = match.group(1)
            log_command(text, action, param)
            return {"action": action, "target": param}
    log_command(text, "unknown", "")
    return {"action": "unknown", "target": ""}

def log_command(original, action, target):
    try:
        with open(COMMAND_LOG, "r") as f:
            log = json.load(f)
    except:
        log = []

    log.append({
        "timestamp": datetime.utcnow().isoformat(),
        "original_text": original,
        "action": action,
        "target": target
    })

    with open(COMMAND_LOG, "w") as f:
        json.dump(log[-300:], f, indent=2)

# Optional CLI test
if __name__ == "__main__":
    test = input("Say something: ")
    result = interpret_command(test)
    print(f"🗣️ Command interpreted: {result}")