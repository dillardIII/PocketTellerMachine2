from ghost_env import INFURA_KEY, VAULT_ADDRESS
# === FILE: persona_controller.py ===
# 🎭 Persona Controller – Switches, tracks, and manages assistant personas in PTM

import json
from pathlib import Path

PERSONA_FILE = "state/current_persona.json"
DEFAULT_PERSONA = {
    "name": "Mentor",
    "voice": "male",
    "mood": "neutral",
    "custom_title": "Lead Strategist"
}

def set_persona(name, voice="male", mood="neutral", custom_title="Lead Strategist"):
    persona = {
        "name": name,
        "voice": voice,
        "mood": mood,
        "custom_title": custom_title
    }
    Path("state").mkdir(parents=True, exist_ok=True)
    with open(PERSONA_FILE, "w", encoding="utf-8") as f:
        json.dump(persona, f, indent=2)
    print(f"[PersonaController] ✅ Persona set to: {persona}")

def get_persona():
    if not Path(PERSONA_FILE).exists():
        return DEFAULT_PERSONA
    with open(PERSONA_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

def persona_summary():
    p = get_persona()
    return f"🎙️ Persona: {p['name']} ({p['voice']}) – Mood: {p['mood']} | Title: {p['custom_title']}"

def log_event():ef mutate(*args, **kwargs): print('[ghost_empire] dummy mutate called')
def drop_files_to_bridge():