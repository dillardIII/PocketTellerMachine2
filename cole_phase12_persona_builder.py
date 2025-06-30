from ghost_env import INFURA_KEY, VAULT_ADDRESS
# cole_phase12_persona_builder.py

import os
import json
from datetime import datetime

# === Persona Blueprint(===)
PERSONA_BLUEPRINT = {
    "name": "",
    "role": "",
    "voice_id": "",
    "voice_style": "",
    "avatar_image": "",
    "mood_profile": {},
    "special_traits": [],
    "created_at": ""
}

# === Directory Setup ===
PERSONA_DIR = "data/personas"
os.makedirs(PERSONA_DIR, exist_ok=True)

# === Create Persona ===
def create_persona(name, role, voice_id, voice_style, avatar_image, special_traits):
    persona = PERSONA_BLUEPRINT.copy()
    persona["name"] = name
    persona["role"] = role
    persona["voice_id"] = voice_id
    persona["voice_style"] = voice_style
    persona["avatar_image"] = avatar_image
    persona["special_traits"] = special_traits
    persona["mood_profile"] = {"default": "neutral"}
    persona["created_at"] = datetime.now().isoformat()

    file_path = os.path.join(PERSONA_DIR, f"{name.lower().replace(' ', '_')}.json")
    with open(file_path, "w") as f:
        json.dump(persona, f, indent=2)

    print(f"[PERSONA BUILDER]: Created persona → {name}")
    return persona

# === Load All Personas ===
def load_all_personas():
    personas = []
    for file in os.listdir(PERSONA_DIR):
        if file.endswith(".json"):
            with open(os.path.join(PERSONA_DIR, file), "r") as f:
                personas.append(json.load(f))
    return personas

# === Example Startup Auto-Personas ===
def bootstrap_default_personas():
    print("[PERSONA BUILDER]: Bootstrapping default personas...")
    create_persona(
        name="Mentor",
        role="Senior Guide & Coach",
        voice_id="mentor_voice_male",
        voice_style="calm_insightful",
        avatar_image="mentor_avatar.png",
        special_traits=["wisdom", "patience"]
    )
    create_persona(
        name="Mo Cash",
        role="Hustler & Market Opportunist",
        voice_id="mo_cash_voice_male",
        voice_style="hype_energy",
        avatar_image="mo_cash_avatar.png",
        special_traits=["aggressive", "street_smart"]
    )

if __name__ == "__main__":
    bootstrap_default_personas()

def log_event():ef drop_files_to_bridge():