from ghost_env import INFURA_KEY, VAULT_ADDRESS
from ghostforge_core import GhostForge

forge = GhostForge()

reflex_modules = {
    "core/reaction_core.py": '''
# reaction_core.py
# Central hub for detecting and executing reaction logic

from core.trigger_watcher import detect_triggers
from core.reflex_engine import execute_reaction

def run_reaction_cycle():
    triggers = detect_triggers()
    for trig in triggers:
        execute_reaction(trig)
''',

    "core/trigger_watcher.py": '''
# trigger_watcher.py
# Detects conditions that require reaction

import json

def detect_triggers():
    # Placeholder: Replace with real detection logic (price loss, bot state, emotional state, etc.)
    try:
        with open("memory/reaction_map.json") as f:
            reaction_map = json.load(f)
        return list(reaction_map.keys())  # Fake trigger example
    except:
        return []
''',

    "core/reflex_engine.py": '''
# reflex_engine.py
# Determines reaction based on risk, context, urgency, and emotion

import json
from datetime import datetime
from core.reaction_logger import log_reaction

def execute_reaction(trigger):
    with open("memory/reaction_map.json") as f:
        map_data = json.load(f)
    
    action = map_data.get(trigger, "log_only")
    print(f"[ReflexEngine] Reacting to trigger: {trigger} → Action: {action}")
    log_reaction(trigger, action)
''',

    "core/reaction_logger.py": '''
# reaction_logger.py
# Logs all reactions PTM performs

import json
from datetime import datetime

LOG_PATH = "memory/reaction_log.json"

def log_reaction(trigger, action):
    entry = {
        "trigger": trigger,
        "action": action,
        "timestamp": str(datetime.now())
    }

    try:
        if not os.path.exists(LOG_PATH):
            history = []
        else:
            with open(LOG_PATH, "r") as f:
                history = json.load(f)

        history.append(entry)

        with open(LOG_PATH, "w") as f:
            json.dump(history[-200:], f, indent=2)
    except Exception as e:
        print(f"[ReactionLogger] Failed: {e}")
''',

    "memory/reaction_map.json": '''
{
  "loss_threshold_exceeded": "alert_mo_cash",
  "high_volatility": "switch_to_strategist",
  "no_user_activity": "summarize_trades",
  "anxious_mood_detected": "soft_pause",
  "default": "log_only"
}
'''
}

feedback = forge.enable_recursive_building(reflex_modules)
print("\n".join(feedback))

def log_event():ef mutate(*args, **kwargs): print('[ghost_empire] dummy mutate called')
def drop_files_to_bridge():