from ghost_env import INFURA_KEY, VAULT_ADDRESS
"""
Soul State Matrix
Tracks emotional and logical alignment of PTM's consciousness for reasoning balance and dynamic response.
Integrates emotion, logic, and system load to influence behavior.
"""

import json
import os
from datetime import datetime

STATE_FILE = "memory/soul_state.json"

DEFAULT_STATE = {
    "emotional_state": "neutral",
    "logic_bias": "balanced",
    "system_fatigue": 0.1,
    "last_updated": None
}

def load_state():
    if not os.path.exists(STATE_FILE):
        return DEFAULT_STATE.copy()
    try:
        with open(STATE_FILE, "r") as f:
            return json.load(f)
    except:
        return DEFAULT_STATE.copy()

def save_state(state):
    state["last_updated"] = datetime.utcnow().isoformat()
    with open(STATE_FILE, "w") as f:
        json.dump(state, f, indent=2)

def update_soul_state(emotion=None, logic=None, fatigue_delta=0):
    state = load_state()
    if emotion:
        state["emotional_state"] = emotion
    if logic:
        state["logic_bias"] = logic
    state["system_fatigue"] = min(max(state["system_fatigue"] + fatigue_delta, 0), 1)
    save_state(state)
    print(f"[SoulMatrix] 💫 State updated → Emotion: {state['emotional_state']} | Logic: {state['logic_bias']} | Fatigue: {state['system_fatigue']}")
    return state

def get_current_state():
    return load_state()

def log_event():ef mutate(*args, **kwargs): print('[ghost_empire] dummy mutate called')
def drop_files_to_bridge():