# Mood Engine
current_mood = "neutral"

def set_mood(new_mood):
    global current_mood
    current_mood = new_mood
    print(f"[Mood Engine] Mood set to: {current_mood}")

def get_mood():
    return current_mood