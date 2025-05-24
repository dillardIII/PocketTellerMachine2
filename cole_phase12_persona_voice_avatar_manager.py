# cole_phase12_persona_voice_avatar_manager.py

import os
import json
from datetime import datetime

# === Paths ===
PERSONA_DIR = "data/personas"
AVATAR_VOICE_LOG = "data/persona_avatar_voice_log.json"
os.makedirs(PERSONA_DIR, exist_ok=True)
os.makedirs("data", exist_ok=True)

# === Log Updates ===
def log_update(persona_name, avatar_url, voice_id, note=""):
    logs = []
    if os.path.exists(AVATAR_VOICE_LOG):
        try:
            with open(AVATAR_VOICE_LOG, "r") as f:
                logs = json.load(f)
        except:
            logs = []
    logs.append({
        "timestamp": datetime.now().isoformat(),
        "persona_name": persona_name,
        "avatar_url": avatar_url,
        "voice_id": voice_id,
        "note": note
    })
    with open(AVATAR_VOICE_LOG, "w") as f:
        json.dump(logs[-500:], f, indent=2)

# === Update Avatar + Voice ===
def update_persona_avatar_voice(persona_name, avatar_url, avatar_style, voice_id):
    persona_file = os.path.join(PERSONA_DIR, f"{persona_name.lower().replace(' ', '_')}.json")
    if not os.path.exists(persona_file):
        print(f"[PERSONA MANAGER ERROR]: Persona {persona_name} not found.")
        return None

    with open(persona_file, "r") as f:
        persona = json.load(f)

    persona["avatar_url"] = avatar_url
    persona["avatar_style"] = avatar_style
    persona["voice_id"] = voice_id

    with open(persona_file, "w") as f:
        json.dump(persona, f, indent=2)

    log_update(persona_name, avatar_url, voice_id, "Avatar and Voice Updated")
    print(f"[PERSONA MANAGER]: Updated {persona_name} with Avatar and Voice.")
    return persona

# === View Persona Info ===
def view_persona_info(persona_name):
    persona_file = os.path.join(PERSONA_DIR, f"{persona_name.lower().replace(' ', '_')}.json")
    if not os.path.exists(persona_file):
        print(f"[PERSONA MANAGER ERROR]: Persona {persona_name} not found.")
        return None

    with open(persona_file, "r") as f:
        persona = json.load(f)
    return {
        "name": persona["name"],
        "avatar_url": persona.get("avatar_url", "Not Set"),
        "avatar_style": persona.get("avatar_style", "Not Set"),
        "voice_id": persona.get("voice_id", "Not Set")
    }

# === Example Combined Update ===
def demo_persona_full_update():
    update_persona_avatar_voice("Mentor", "https://example.com/mentor_female_avatar.png", "soft_professional", "elevenlabs_mentor_female")
    update_persona_avatar_voice("Mo Cash", "https://example.com/mo_cash_female_avatar.png", "bold_flashy", "elevenlabs_mo_cash_female")

if __name__ == "__main__":
    demo_persona_full_update()