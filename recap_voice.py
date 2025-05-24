import random
import requests
import os
import json
from voice_mood_router import get_voice_mood_by_trade

ELEVENLABS_API_KEY = os.getenv("ELEVENLABS_API_KEY")
DEFAULT_VOICE_ID = os.getenv("ELEVENLABS_VOICE_ID", "EXAVITQu4vr4xnSDxMaL")
AUDIO_OUTPUT_FILE = "static/audio/recap.mp3"
VOICE_MAP_FILE = "data/persona_voice_map.json"

# === Load Active Persona Voice ===
def get_voice_id_for_persona(persona_name):
    try:
        with open(VOICE_MAP_FILE, "r") as f:
            voice_map = json.load(f)
        return voice_map.get(persona_name, DEFAULT_VOICE_ID)
    except:
        return DEFAULT_VOICE_ID

# === Speak Trade Recap with Persona-Based Voice ===
def speak_trade_recap(trade, speaker="Mo Cash"):
    ticker = trade.get("ticker", "UNKNOWN")
    strategy = trade.get("strategy", "N/A")
    result = trade.get("result", "pending")
    profit = trade.get("profit", 0)

    if result == "win":
        responses = [
            f"Victory! That {strategy} on {ticker} earned us ${profit}. Nice move.",
            f"We crushed it with a {strategy} on {ticker}. Up ${profit}!",
            f"That's a W — {strategy} on {ticker} brought in ${profit}."
        ]
    elif result == "loss":
        responses = [
            f"Tough loss on that {strategy} for {ticker}. Down ${abs(profit)}.",
            f"Oof. The {strategy} didn’t work out for {ticker}. Lost ${abs(profit)}.",
            f"That trade stung — {strategy} on {ticker} set us back ${abs(profit)}."
        ]
    else:
        responses = [
            f"Trade for {ticker} using {strategy} is still pending.",
            f"No final result yet on the {strategy} for {ticker}."
        ]

    message = random.choice(responses)
    mood = get_voice_mood_by_trade(trade)
    voice_id = get_voice_id_for_persona(speaker)

    print(f"[Recap Voice - {speaker} - Mood: {mood}] {message}")
    speak_with_elevenlabs(message, mood, voice_id)

# === ElevenLabs Voice API ===
def speak_with_elevenlabs(text, style="neutral", voice_id=DEFAULT_VOICE_ID):
    url = f"https://api.elevenlabs.io/v1/text-to-speech/{voice_id}/stream"

    headers = {
        "xi-api-key": ELEVENLABS_API_KEY,
        "Content-Type": "application/json"
    }

    payload = {
        "text": text,
        "model_id": "eleven_multilingual_v2",
        "voice_settings": {
            "stability": 0.5,
            "similarity_boost": 0.75,
            "style": style
        }
    }

    try:
        response = requests.post(url, headers=headers, json=payload)
        if response.status_code == 200:
            with open(AUDIO_OUTPUT_FILE, "wb") as f:
                f.write(response.content)
            print(f"[Voice] Playback saved to {AUDIO_OUTPUT_FILE}")
        else:
            print(f"[Voice Error] {response.status_code}: {response.text}")
    except Exception as e:
        print(f"[Voice Exception] {e}")

# === Basic Fallback Voice Print ===
def speak_text(text, speaker="Malik"):
    print(f"[Voice Recap - {speaker}] {text}")