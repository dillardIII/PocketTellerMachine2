# === FILE: core/voice_to_directive.py ===
"""
Voice to Directive Engine
Converts voice-transcribed input into PTM-compatible commands, strategy triggers, or assistant prompts.
"""

import json
from datetime import datetime

COMMAND_LOG = "memory/voice_directive_log.json"

TRIGGERS = {
    "start trade": "initiate_trade()",
    "show dashboard": "launch_dashboard_ui()",
    "mentor lesson": "start_lesson_mode('Mentor')",
    "run strategy": "activate_strategy_module()",
    "ghost drop": "deploy_next_tier_bundle()",
    "sync devices": "trigger_ghostbridge_sync()",
    "go autonomous": "enable_recursive_loop()"
}

def interpret_voice(phrase: str):
    for trigger, command in TRIGGERS.items():
        if trigger in phrase.lower():
            log_directive(trigger, command)
            print(f"[Voice2Directive] 🎯 Interpreted: '{phrase}' → {command}")
            return command
    log_directive("unrecognized", phrase)
    print(f"[Voice2Directive] ❓ No match for: '{phrase}'")
    return None

def log_directive(trigger, result):
    record = {
        "timestamp": datetime.utcnow().isoformat(),
        "trigger": trigger,
        "result": result
    }

    try:
        with open(COMMAND_LOG, "r") as f:
            history = json.load(f)
    except:
        history = []

    history.append(record)
    with open(COMMAND_LOG, "w") as f:
        json.dump(history[-300:], f, indent=2)

if __name__ == "__main__":
    sample = "Mentor lesson on options"
    interpret_voice(sample)