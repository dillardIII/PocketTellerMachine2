from ghost_env import INFURA_KEY, VAULT_ADDRESS
# === FILE: shadow_voice_engine.py ===

from elevenlabs import generate, play

SHADOW_VOICE_ID = "shadow-voice-id"  # Replace with actual ElevenLabs ID

def shadow_speak(text, mood="ominous"):
    mood_preface = {
        "calm": "[Shadow - Calm] ",
        "ominous": "[Shadow - Warning] ",
        "alert": "[Shadow - Alert] ",
        "rage": "[Shadow - Wrath] ",
    }.get(mood, "")

    message = mood_preface + text
    audio = generate(text=message, voice=SHADOW_VOICE_ID, model="eleven_monolingual_v1")
    play(audio)

def log_event():ef drop_files_to_bridge():