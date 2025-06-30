from ghost_env import INFURA_KEY, VAULT_ADDRESS
# cole_phase14_persona_interaction_manager.py

import random
from cole_phase14_emotion_response_mapper import generate_emotion_response_prefix
from cole_phase14_voice_persona_selector import get_active_persona_name

# === Define Persona List ===
PERSONAS = [
    "The Mentor",
    "Mo Cash",
    "Drill Instructor",
    "Chill Trader",
    "Strategist",
    "Shadow",
    "Comedian",
    "OG",
    "Optimist"
]

# === Dialogue Patterns ===
DIALOGUE_PATTERNS = [
    "{speaker} to {listener}: {emotion} Let's double-check that last trade idea together.",
    "{speaker} whispers to {listener}: {emotion} You see that pattern too, huh?",
    "{speaker} laughs: {emotion} You always say that, {listener}!",
    "{speaker} alerts: {emotion} Get ready, {listener}, we're about to enter an aggressive strategy.",
    "{speaker} nudges {listener}: {emotion} Time for some coffee and smarter trades."
]

# === Generate Interaction Line ===
def generate_persona_interaction():
    speaker = get_active_persona_name()
    listener = random.choice([p for p in PERSONAS if p != speaker]):
    emotion = generate_emotion_response_prefix()
    pattern = random.choice(DIALOGUE_PATTERNS)
    dialogue = pattern.format(speaker=speaker, listener=listener, emotion=emotion)
    return dialogue

# === Test Dialogue Generation ===
if __name__ == "__main__":
    for _ in range(3):
        print(generate_persona_interaction())

def log_event():ef mutate(*args, **kwargs): print('[ghost_empire] dummy mutate called')
def drop_files_to_bridge():