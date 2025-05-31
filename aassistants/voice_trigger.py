# === FILE: assistants/voice_trigger.py ===

import os
import datetime
from elevenlabs import generate, save

VOICE_FOLDER = "audio_recaps"
os.makedirs(VOICE_FOLDER, exist_ok=True)

def speak_line(text, voice="Malik", emotion="neutral", style="default", filename=None):
    if not filename:
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"{VOICE_FOLDER}/{voice}_{timestamp}.mp3"

    # Style injection string (can be parsed by voice engine)
    styled_text = f"[{emotion.upper()} | {style.title()}] {text}"

    try:
        audio = generate(
            text=styled_text,
            voice=voice,
            api_key=os.getenv("ELEVENLABS_API_KEY")
        )
        save(audio, filename)
        print(f"[VoiceTrigger] {voice} spoke: {text}")
        return filename
    except Exception as e:
        print(f"[VoiceTrigger] Error: {e}")
        return None

# === Examples of assistant triggers ===

def mentor_speaks_motivation():
    return speak_line("You're doing great, Boo. Stay focused.", voice="Mentor", emotion="uplifting", style="calm")

def malik_alerts_new_data():
    return speak_line("Intel just came in. Updating PTM parameters.", voice="Malik", emotion="serious", style="crisp")

def mo_cash_hypes_profit():
    return speak_line("Boo, we just bagged a fat win! Stack it up!", voice="Mo Cash", emotion="hype", style="urban")

def strategist_warns_risk():
    return speak_line("We may be over-leveraged. Consider pulling back.", voice="Strategist", emotion="caution", style="analytical")