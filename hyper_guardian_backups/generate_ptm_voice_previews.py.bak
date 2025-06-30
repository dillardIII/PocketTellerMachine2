# === FILE: generate_ptm_voice_previews.py ===
# 🎤 Generates voice previews for PTM assistant personas using ElevenLabs

import os
from elevenlabs import generate, save, set_api_key

# 🔐 STEP 1: Set your API key
set_api_key("your_elevenlabs_api_key_here")  # Replace this with your real API key

# 🔊 STEP 2: Define persona previews
personas = [
    {
        "name": "Mentor",
        "text": "This is Mentor. Calm, collected, and always watching the market with focus and reason.",
        "voice_id": "EXAVITQu4vr4xnSDxMaL",  # Default deep male
    },
    {
        "name": "Mo Cash",
        "text": "Yo! Mo Cash here. Let’s make these trades stack paper like legends.",
        "voice_id": "ErXwobaYiN019PkySvjV",  # Confident male
    },
    {
        "name": "Strategist",
        "text": "Strategist online. Logic, data, and calculated moves. That’s how we win.",
        "voice_id": "pNInz6obpgDQGcFmaJgB",  # Clean analytical voice
    },
    {
        "name": "Drill Instructor",
        "text": "Stand by, Devil Dog. I’m Drill. I don’t make trades. I execute missions.",
        "voice_id": "TxGEqnHWrfWFTfGW9XjX",  # Sharp commanding male
    },
    {
        "name": "Shadow",
        "text": "Shadow speaking. I only surface when the data whispers. Watch the quiet trends.",
        "voice_id": "VR6AewLTigWG4xSOukaG",  # Deep eerie voice
    },
    {
        "name": "Chill Trader",
        "text": "Hey, I’m Chill. Keep it easy, ride the waves, and always breathe before clicking.",
        "voice_id": "MF3mGyEYCl7XYWbV9V6O",  # Mellow vibe
    },
    {
        "name": "Optimist",
        "text": "The future’s bright. I’m Optimist. Let’s learn, grow, and win — together.",
        "voice_id": "D38z5RcWu1voky8WS1ja",  # Energetic, clean male
    },
]

# 🎯 STEP 3: Generate & Save MP3s
output_folder = "ptm_voice_previews"
os.makedirs(output_folder, exist_ok=True)

for persona in personas:
    print(f"Generating: {persona['name']}")
    audio = generate(
        text=persona["text"],
        voice=persona["voice_id"],
        model="eleven_monolingual_v1"
    )
    save(audio, os.path.join(output_folder, f"{persona['name'].lower()}.mp3"))

print("✅ All voice previews generated.") 