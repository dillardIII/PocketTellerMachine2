# === FILE: persona_recap_speaker.py ===
"""
Persona Recap Speaker:
Speaks the latest trade using ElevenLabs voice API.
Maps each persona to a voice style or voice ID.
"""

import json
import os
from datetime import datetime
from elevenlabs import generate, play, save, set_api_key
from dotenv import load_dotenv

# === 🔐 Load ElevenLabs API Key from .env ===
load_dotenv()
set_api_key(os.getenv("ELEVENLABS_API_KEY"))

# === File paths ===
TRADE_LOG_FILE = "data/trade_log.json"
RECAP_AUDIO_FOLDER = "audio/recaps"

# === ElevenLabs Voice IDs (replace placeholders with real voice IDs)
VOICE_IDS = {
    "MoCash": "EXAVITQu4vr4xnSDxMaL",           # replace with real
    "Mentor": "ErXwobaYiN019PkySvjV",            # replace with real
    "DrillInstructor": "DomiID123456789",        # replace with real
    "Strategist": "ElliID123456789",             # replace with real
    "ChillTrader": "AntoniID123456789",          # replace with real
    "Default": "EXAVITQu4vr4xnSDxMaL"
}

def load_latest_trade():
    """
    Load the most recent trade from the trade log.
    """
    if not os.path.exists(TRADE_LOG_FILE):
        print("[Recap Speaker] ❌ No trade log file found.")
        return None

    with open(TRADE_LOG_FILE, "r") as f:
        try:
            trades = json.load(f)
            return trades[-1] if trades else None
        except json.JSONDecodeError:
            print("[Recap Speaker] ⚠️ Failed to decode trade log.")
            return None

def build_recap_message(trade):
    """
    Format the spoken message based on trade data.
    """
    base = (
        f"On {trade['datetime']}, {trade['persona']} executed a {trade['action']} on "
        f"{trade['symbol']} at ${trade['price']} using the {trade['strategy']} strategy."
    )
    result = trade.get("result", "pending")
    if result == "win":
        return base + " This trade was a success! Total value was positive."
    elif result == "loss":
        return base + " Unfortunately, this trade ended in a loss."
    return base + " The trade result is still pending."

def get_voice_id(persona):
    """
    Get the ElevenLabs voice ID for a persona.
    """
    return VOICE_IDS.get(persona, VOICE_IDS["Default"])

def speak_recap(trade=None):
    """
    Speak the recap of the provided trade (or load latest).
    """
    trade = trade or load_latest_trade()
    if not trade:
        print("[Recap Speaker] ❌ No trade data available.")
        return

    message = build_recap_message(trade)
    persona = trade.get("persona", "Default")
    voice_id = get_voice_id(persona)

    print(f"[Recap Speaker] 🎤 {persona} is speaking using voice ID {voice_id}")
    print(f"[Recap Message] {message}")

    try:
        audio = generate(
            text=message,
            voice=voice_id,
            model="eleven_multilingual_v2"
        )
        os.makedirs(RECAP_AUDIO_FOLDER, exist_ok=True)
        filename = os.path.join(
            RECAP_AUDIO_FOLDER,
            f"{persona}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.mp3"
        )
        save(audio, filename)
        play(audio)
        print(f"[Recap Speaker] ✅ Audio saved to {filename}")
    except Exception as e:
        print(f"[Recap Speaker] ❌ Error generating audio: {e}")

if __name__ == "__main__":
    latest_trade = load_latest_trade()
    if latest_trade:
        speak_recap(latest_trade)
    else:
        print("[Recap Speaker] No trade found to recap.")