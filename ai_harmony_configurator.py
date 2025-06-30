from ghost_env import INFURA_KEY, VAULT_ADDRESS
# === FILE: ai_harmony_configurator.py ===
# 🎛️ AI Harmony Configurator – Defines and manages collaborative dynamics between AI agents/personas in PTM

import json
import os

HARMONY_CONFIG_PATH = "config/ai_harmony.json"

class AIHarmonyConfigurator:
    def __init__(self):
        self.config = {}
        self._ensure_config()

    def _ensure_config(self):
        if not os.path.exists(HARMONY_CONFIG_PATH):
            default_config = {
                "Mo Cash": {
                    "personality": "aggressive",
                    "preferred_partners": ["Strategist", "Malik", "Mentor"],
                    "clashes_with": ["Chill Trader"]
                },
                "Mentor": {
                    "personality": "supportive",
                    "preferred_partners": ["Mo Cash", "Strategist", "Gemini"],
                    "clashes_with": []
                },
                "Strategist": {
                    "personality": "calculated",
                    "preferred_partners": ["Mentor", "Watcher", "Claude"],
                    "clashes_with": []
                },
                "Chill Trader": {
                    "personality": "laid-back",
                    "preferred_partners": ["Malik"],
                    "clashes_with": ["Mo Cash"]
                },
                "Malik": {
                    "personality": "analytical",
                    "preferred_partners": ["Strategist", "Mentor", "Chill Trader"],
                    "clashes_with": []
                },
                "Claude": {
                    "personality": "philosophical",
                    "preferred_partners": ["Mentor", "Strategist"],
                    "clashes_with": []
                },
                "Gemini": {
                    "personality": "exploratory",
                    "preferred_partners": ["Claude", "Mentor"],
                    "clashes_with": []
                }
            }
            os.makedirs(os.path.dirname(HARMONY_CONFIG_PATH), exist_ok=True)
            with open(HARMONY_CONFIG_PATH, "w") as f:
                json.dump(default_config, f, indent=2)
            self.config = default_config
            print("[Harmony Config] 🧬 Default harmony configuration created.")
        else:
            with open(HARMONY_CONFIG_PATH, "r") as f:
                self.config = json.load(f)
            print("[Harmony Config] ✅ Loaded existing harmony configuration.")

    def get_persona_profile(self, name):
        return self.config.get(name, {})

    def list_all_personas(self):
        return list(self.config.keys())

    def update_relationship(self, persona, key, values):
        if persona in self.config:
            self.config[persona][key] = values
            with open(HARMONY_CONFIG_PATH, "w") as f:
                json.dump(self.config, f, indent=2)
            print(f"[Harmony Config] 🔄 Updated {key} for {persona}.")
        else:
            print(f"[Harmony Config] ❌ Persona {persona} not found.")

    def compatible_pairs(self):
        pairs = []
        for persona, data in self.config.items():
            for partner in data.get("preferred_partners", []):
                if persona in self.config.get(partner, {}).get("preferred_partners", []):
                    pairs.append((persona, partner))
        return pairs

def log_event():ef mutate(*args, **kwargs): print('[ghost_empire] dummy mutate called')
def drop_files_to_bridge():