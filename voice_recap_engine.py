import os
import datetime
from elevenlabs import generate, save
from assistants.malik import malik_report  # or switch to Mo Cash, Mentor, etc.

VOICE_FOLDER = "audio_recaps"
os.makedirs(VOICE_FOLDER, exist_ok=True)

# === Core Voice Recap Creation ===
def create_voice_recap(text, filename=None, voice="Mo Cash"):
    if not filename:
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"{VOICE_FOLDER}/recap_{timestamp}.mp3"

    try:
        audio = generate(
            text=text,
            voice=voice,
            api_key=os.getenv("ELEVENLABS_API_KEY")
        )
        save(audio, filename)
        print(f"[VoiceRecap] Recap saved to {filename}")
        return filename
    except Exception as e:
        print(f"[VoiceRecap] Error generating audio: {e}")
        return None

# === Trade Recap Summary ===
def recap_trade(trade):
    summary = f"""
    Trade completed using strategy {trade['strategy']}.
    Result: {trade['result']}.
    Grade: {trade['grade']}.
    Good work, boss.
    """
    create_voice_recap(summary.strip(), voice="Mo Cash")

# === Feature Build Summary ===
def recap_build(feature_name):
    summary = f"Feature {feature_name} was successfully built and added to the platform."
    create_voice_recap(summary, voice="Mo Cash")

# === General Text-to-Speech Trigger ===
def speak(text, voice="Mo Cash"):
    create_voice_recap(text, voice=voice)

# === Test Line: One-time confirmation voice ===
def voice_test_message():
    try:
        audio = generate(
            text="The first voice test is successful.",
            voice="Rachel",
            api_key=os.getenv("ELEVENLABS_API_KEY")
        )
        save(audio, "output.mp3")
        print("[VoiceTest] Test message saved as output.mp3")
    except Exception as e:
        print(f"[VoiceTest] Error during test generation: {e}")

# === Styled Voice Recap with Traits ===
def create_voice_recap_with_traits(text, voice_name="Mo Cash", mood="neutral", gender="male", accent="default", filename=None):
    if not filename:
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"{VOICE_FOLDER}/recap_{timestamp}.mp3"

    styled_text = f"[{mood.upper()} | {gender.title()} | {accent.title()}] {text}"

    try:
        audio = generate(
            text=styled_text,
            voice=voice_name,
            api_key=os.getenv("ELEVENLABS_API_KEY")
        )
        save(audio, filename)
        print(f"[VoiceRecap] Voice with traits saved to {filename}")
        return filename
    except Exception as e:
        print(f"[VoiceRecap] Error generating styled voice: {e}")
        return None