import os
import requests

ELEVENLABS_API_KEY = os.getenv("ELEVENLABS_API_KEY")

# Default voice ID from ElevenLabs (you can replace with persona-specific IDs)
DEFAULT_VOICE_ID = "EXAVITQu4vr4xnSDxMaL"

# List of personas and their one-liners
personas = {
    "strategist": "Strategizing success, one move at a time.",
    "optimist": "Every day is a win waiting to happen!",
    "shadow": "Plans hidden, results seen.",
    "comedian": "Why trade serious when you can trade hilarious?",
    "mentor": "Guiding you from novice to natural.",
    "chill_trader": "Relax... the market’s just another wave to ride.",
    "og": "Old school smarts. New world profits.",
    "malik": "Eyes sharp. Mind sharper.",
    "drill_instructor": "Discipline wins markets! Move it, trader!",
    "analyst": "I decode markets like blueprints—precise, sharp, and always on point.",
    "strategist_female": "Calculating every step to success.",
    "optimist_female": "The sun always rises on opportunity!",
    "shadow_female": "Silent strategies, loud wins.",
    "comedian_female": "Laugh now, profit later!",
    "mentor_female": "Wisdom whispered in every trade.",
    "chill_trader_female": "Stay cool. Trade cooler.",
    "og_female": "Classic skill, modern moves.",
    "malik_female": "Steady vision. Bold decisions.",
    "drill_instructor_female": "Stand tall, trade smart, stay winning!"
}

def generate_voice(persona, line):
    url = f"https://api.elevenlabs.io/v1/text-to-speech/{DEFAULT_VOICE_ID}"
    headers = {
        "Accept": "audio/mpeg",
        "Content-Type": "application/json",
        "xi-api-key": ELEVENLABS_API_KEY
    }
    payload = {
        "text": line,
        "voice_settings": {
            "stability": 0.5,
            "similarity_boost": 0.75
        }
    }

    response = requests.post(url, headers=headers, json=payload)

    if response.status_code == 200:
        output_path = f"voices/{persona}.mp3"
        with open(output_path, "wb") as f:
            f.write(response.content)
        print(f"✅ Voice generated for {persona}: saved to {output_path}")
    else:
        print(f"❌ Failed for {persona}: {response.text}")

def main():
    if not ELEVENLABS_API_KEY:
        print("❌ ElevenLabs API key not found. Please check your environment variable!")
        return

    os.makedirs("voices", exist_ok=True)

    for persona, line in personas.items():
        generate_voice(persona, line)

if __name__ == "__main__":
    main()