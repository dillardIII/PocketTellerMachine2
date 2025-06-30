# cole_phase13_avatar_generator.py

import os
import json
from datetime import datetime
from PIL import Image, ImageDraw, ImageFont

AVATAR_OUTPUT_FOLDER = "data/avatars"
AVATAR_LOG_FILE = "data/cole_avatar_events_log.json"
os.makedirs(AVATAR_OUTPUT_FOLDER, exist_ok=True)
os.makedirs("data", exist_ok=True)

# === Generate simple avatar with text overlay ===
def generate_avatar(persona_name, style="default", color="blue"):
    try:
        img = Image.new('RGB', (256, 256), color=color)
        draw = ImageDraw.Draw(img)
        font_size = 20
        try:
            font = ImageFont.truetype("arial.ttf", font_size)
        except:
            font = ImageFont.load_default()
        
        text = persona_name
        text_w, text_h = draw.textsize(text, font=font)
        draw.text(((256 - text_w) / 2, (256 - text_h) / 2), text, fill="white", font=font)

        filename = f"{persona_name}_{style}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png"
        filepath = os.path.join(AVATAR_OUTPUT_FOLDER, filename)
        img.save(filepath)
        log_avatar_event(persona_name, f"Generated avatar {filename}")
        print(f"[AVATAR GENERATOR]: Avatar saved → {filename}")
        return filepath
    except Exception as e:
        log_avatar_event(persona_name, f"[ERROR]: {e}")
        print(f"[AVATAR GENERATOR ERROR]: {e}")

# === Log avatar generation events ===
def log_avatar_event(persona_name, message):
    logs = []
    if os.path.exists(AVATAR_LOG_FILE):
        with open(AVATAR_LOG_FILE, "r") as f:
            logs = json.load(f)
    logs.append({
        "timestamp": datetime.now().isoformat(),
        "persona": persona_name,
        "event": message
    })
    with open(AVATAR_LOG_FILE, "w") as f:
        json.dump(logs[-500:], f, indent=2)

if __name__ == "__main__":
    generate_avatar("Sensei")
    generate_avatar("Mo Cash", style="hype", color="green")
    generate_avatar("Sunny", style="cheerful", color="orange")