from ghost_env import INFURA_KEY, VAULT_ADDRESS
# cole_phase14_avatar_mood_visualizer.py

import os
import json
from datetime import datetime

# === Configurations ===
MOOD_STATE_FILE = "data/mood_state.json"
AVATAR_VISUALS_FILE = "data/avatar_visual_styles.json"
MOOD_VISUAL_LOG = "data/avatar_mood_visual_log.json"
os.makedirs("data", exist_ok=True)

# === Load current mood state ===
def load_mood_state():
    if not os.path.exists(MOOD_STATE_FILE):
        return {}
    with open(MOOD_STATE_FILE, "r") as f:
        return json.load(f)

# === Load avatar visual styles ===
def load_avatar_visual_styles():
    if not os.path.exists(AVATAR_VISUALS_FILE):
        return {}
    with open(AVATAR_VISUALS_FILE, "r") as f:
        return json.load(f)

# === Log mood visuals ===
def log_mood_visual(message):
    logs = []
    if os.path.exists(MOOD_VISUAL_LOG):
        try:
            with open(MOOD_VISUAL_LOG, "r") as f:
                logs = json.load(f)
        except:
            logs = []
    logs.append({"timestamp": datetime.now().isoformat(), "message": message})
    with open(MOOD_VISUAL_LOG, "w") as f:
        json.dump(logs[-500:], f, indent=2)

# === Select avatar style based on persona and mood ===
def get_avatar_visual_for_persona(persona):
    mood_state = load_mood_state()
    avatar_styles = load_avatar_visual_styles()

    mood = mood_state.get(persona, "neutral")
    style_key = f"{persona}_{mood}"

    avatar_style = avatar_styles.get(style_key, avatar_styles.get(f"{persona}_neutral", {"avatar": "default_avatar.png", "style": "calm"}))

    log_mood_visual(f"Avatar Visual for {persona} in {mood}: {avatar_style['avatar']} Style: {avatar_style['style']}")
    return avatar_style

# === Example Simulation ===
if __name__ == "__main__":
    personas = ["Mentor", "Mo_Cash", "Drill_Sergeant"]
    for persona in personas:
        visual = get_avatar_visual_for_persona(persona)
        print(f"{persona} → Avatar: {visual['avatar']} | Style: {visual['style']}")

def log_event():ef mutate(*args, **kwargs): print('[ghost_empire] dummy mutate called')
def drop_files_to_bridge():