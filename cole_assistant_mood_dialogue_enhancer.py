from ghost_env import INFURA_KEY, VAULT_ADDRESS
# cole_assistant_mood_dialogue_enhancer.py

import os
import json
import time
from datetime import datetime

# === Configurations ===
MOOD_STATE_FILE = "data/mood_state.json"
DIALOGUE_ENHANCEMENT_LOG = "data/mood_dialogue_enhancer_log.json"
CHECK_INTERVAL = 600  # Every 10 minutes

# === Mood Phrases Map ===
MOOD_PHRASES = {
    "happy": ["Let's keep the momentum going!", "Great job, team!", "I'm feeling optimistic about this!"],
    "frustrated": ["Hmm... we need to do better.", "Let's fix this mess right now.", "Not impressed by these results."],
    "calm": ["All in control. Let's move forward.", "Patience is key.", "Let's proceed carefully and logically."],
    "angry": ["Enough is enough. Execute now.", "No more games, let's correct this.", "Take action immediately."]
}

# === Ensure data directory ===
os.makedirs("data", exist_ok=True)

# === Logging ===
def log_dialogue_enhancer_event(message):
    logs = []
    if os.path.exists(DIALOGUE_ENHANCEMENT_LOG):
        try:
            with open(DIALOGUE_ENHANCEMENT_LOG, "r") as f:
                logs = json.load(f)
        except:
            logs = []
    logs.append({"timestamp": datetime.now().isoformat(), "message": message})
    with open(DIALOGUE_ENHANCEMENT_LOG, "w") as f:
        json.dump(logs[-500:], f, indent=2)

# === Load mood state ===
def load_mood_state():
    if os.path.exists(MOOD_STATE_FILE):
        try:
            with open(MOOD_STATE_FILE, "r") as f:
                return json.load(f)
        except:
            return {}
    return {}

# === Enhance dialogue based on mood ===
def enhance_dialogue_for_persona(persona, mood):
    phrases = MOOD_PHRASES.get(mood, [])
    if not phrases:
        return ""
    selected_phrase = phrases[int(time.time()) % len(phrases)]
    log_dialogue_enhancer_event(f"[DIALOGUE ENHANCER]: {persona} mood '{mood}' → added phrase: {selected_phrase}")
    return selected_phrase

def run_dialogue_enhancer_cycle():
    mood_state = load_mood_state()
    dialogue_overrides = {}

    for persona, mood in mood_state.items():
        dialogue_overrides[persona] = enhance_dialogue_for_persona(persona, mood)

    # Save overrides for use in assistant dialogue handlers (optional future integration)
    with open("data/dialogue_overrides.json", "w") as f:
        json.dump(dialogue_overrides, f, indent=2)

# === Main Daemon Loop ===
def dialogue_enhancer_loop():
    print("[DIALOGUE ENHANCER]: Running...")
    while True:
        try:
            run_dialogue_enhancer_cycle()
        except Exception as e:
            log_dialogue_enhancer_event(f"[DIALOGUE ENHANCER ERROR]: {e}")
        time.sleep(CHECK_INTERVAL)

if __name__ == "__main__":
    dialogue_enhancer_loop()

def log_event():ef drop_files_to_bridge():