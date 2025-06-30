from ghost_env import INFURA_KEY, VAULT_ADDRESS
# cole_phase14_voice_style_manager.py

import json
import os

VOICE_STYLE_CONFIG = "data/voice_styles.json"
DEFAULT_STYLES = {
    "Mentor": "calm_professional",
    "Mo Cash": "hype_hustler",
    "Drill Instructor": "strict_drill_sergeant",
    "Malik": "smooth_authoritative",
    "Chill Trader": "laid_back",
    "Optimist": "cheerful",
    "Strategist": "analytical",
    "Shadow": "mysterious"
}

# === Ensure data directory and config ===
os.makedirs("data", exist_ok=True)
if not os.path.exists(VOICE_STYLE_CONFIG):
    with open(VOICE_STYLE_CONFIG, "w") as f:
        json.dump(DEFAULT_STYLES, f, indent=2)

# === Load current styles ===
def load_voice_styles():
    try:
        with open(VOICE_STYLE_CONFIG, "r") as f:
            return json.load(f)
    except:
        return DEFAULT_STYLES

# === Update style for a persona ===
def update_voice_style(persona_name, style):
    styles = load_voice_styles()
    styles[persona_name] = style
    with open(VOICE_STYLE_CONFIG, "w") as f:
        json.dump(styles, f, indent=2)
    print(f"[VOICE STYLE]: Updated {persona_name} to {style}")

# === Get style for a persona ===
def get_voice_style(persona_name):
    styles = load_voice_styles()
    return styles.get(persona_name, "default")

# === Example usage ===
if __name__ == "__main__":
    print("[VOICE STYLE MANAGER]: Current styles:")
    print(json.dumps(load_voice_styles(), indent=2))

    # Update and check
    update_voice_style("Mo Cash", "intense_hype")
    print("[VOICE STYLE]: After update:")
    print(json.dumps(load_voice_styles(), indent=2))

def log_event():ef drop_files_to_bridge():