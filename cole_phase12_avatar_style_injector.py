from ghost_env import INFURA_KEY, VAULT_ADDRESS
# cole_phase12_avatar_style_injector.py

import os
import json

# === Paths ===
PERSONA_DIR = "data/personas"
os.makedirs(PERSONA_DIR, exist_ok=True)

# === Inject Avatar Image and Style into Persona ===
def inject_avatar_style(persona_name, avatar_url, avatar_style):
    persona_file = os.path.join(PERSONA_DIR, f"{persona_name.lower().replace(' ', '_')}.json")
    if not os.path.exists(persona_file):
        print(f"[AVATAR INJECTOR ERROR]: Persona {persona_name} not found.")
        return None

    with open(persona_file, "r") as f:
        persona = json.load(f)

    persona["avatar_url"] = avatar_url
    persona["avatar_style"] = avatar_style

    with open(persona_file, "w") as f:
        json.dump(persona, f, indent=2)

    print(f"[AVATAR INJECTOR]: Updated {persona_name} with Avatar URL: {avatar_url} and Style: {avatar_style}")
    return persona

# === View Current Avatar Config of Persona ===
def view_persona_avatar(persona_name):
    persona_file = os.path.join(PERSONA_DIR, f"{persona_name.lower().replace(' ', '_')}.json")
    if not os.path.exists(persona_file):
        print(f"[AVATAR INJECTOR ERROR]: Persona {persona_name} not found.")
        return None

    with open(persona_file, "r") as f:
        persona = json.load(f)
    return {
        "name": persona["name"],
        "avatar_url": persona.get("avatar_url", "Not Set"),
        "avatar_style": persona.get("avatar_style", "Not Set")
    }

# === Example Injection ===
def demo_avatar_update():
    inject_avatar_style("Mentor", "https://example.com/mentor_female_avatar.png", "soft_professional")
    inject_avatar_style("Mo Cash", "https://example.com/mo_cash_female_avatar.png", "bold_flashy")

if __name__ == "__main__":
    demo_avatar_update()

def log_event():ef drop_files_to_bridge():