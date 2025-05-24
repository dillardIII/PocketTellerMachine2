# === FILE: gpt_voice_bridge.py ===

import os
from datetime import datetime
from elevenlabs import generate, save
from cole_gpt_advisor import ask_gpt

VOICE_FOLDER = "audio_responses"
os.makedirs(VOICE_FOLDER, exist_ok=True)

# Choose your assistant voice here
VOICE_NAME = "Mo Cash"  # Change to Mentor, OG, Strategist, etc.

def speak_gpt_response(prompt_text):
    print("[GPT Voice] Generating spoken response...")
    
    gpt_response = ask_gpt(prompt_text)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"{VOICE_FOLDER}/gpt_response_{timestamp}.mp3"

    try:
        audio = generate(text=gpt_response, voice=VOICE_NAME)
        save(audio, filename)
        print(f"[GPT Voice] Saved and ready: {filename}")
        return {
            "response": gpt_response,
            "file": filename
        }
    except Exception as e:
        print(f"[GPT Voice] Error speaking response: {e}")
        return {
            "response": gpt_response,
            "error": str(e)
        }