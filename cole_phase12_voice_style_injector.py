from ghost_env import INFURA_KEY, VAULT_ADDRESS
# cole_phase12_voice_style_injector.py

import os
import json

# === Paths ===
PERSONA_DIR = "data/personas"
os.makedirs(PERSONA_DIR, exist_ok=True)

# === Inject Voice Style to Existing Persona ===
def inject_voice_style(persona_name, voice_id, voice_style):
    persona_file = os.path.join(PERSONA_DIR, f"{persona_name.lower().replace(' ', '_')}.json")
    if not os.path.exists(persona_file):
        print(f"[VOICE INJECTOR ERROR]: Persona {persona_name} not found.")
        return None

    with open(persona_file, "r") as f:
        persona = json.load(f)

    persona["voice_id"] = voice_id
    persona["voice_style"] = voice_style

    with open(persona_file, "w") as f:
        json.dump(persona, f, indent=2)

    print(f"[VOICE INJECTOR]: Updated {persona_name} with Voice ID: {voice_id} and Style: {voice_style}")
    return persona

# === View Current Voice Config of Persona ===
def view_persona_voice(persona_name):
    persona_file = os.path.join(PERSONA_DIR, f"{persona_name.lower().replace(' ', '_')}.json")
    if not os.path.exists(persona_file):
        print(f"[VOICE INJECTOR ERROR]: Persona {persona_name} not found.")
        return None

    with open(persona_file, "r") as f:
        persona = json.load(f)
    return {
        "name": persona["name"],
        "voice_id": persona.get("voice_id", "Not Set"),
        "voice_style": persona.get("voice_style", "Not Set")
    }

# === Example Injection ===
def demo_voice_update():
    inject_voice_style("Mentor", "mentor_voice_female", "gentle_caring")
    inject_voice_style("Mo Cash", "mo_cash_voice_female", "bold_energetic")

if __name__ == "__main__":
    demo_voice_update()

def log_event():ef drop_files_to_bridge():