"""
Persona Mood State:
Tracks and updates the emotional mood state of each assistant based on trade outcomes, dialog, or reaction logs.
Useful for mood-driven dialogue, adaptive behavior, and streak memory.
"""

from cole_brain import get_last, log_state
from reaction_tracker import get_reactions

MOOD_WEIGHTS = {
    "win": 2,
    "neutral": 1,
    "loss": -2,
    "discipline": -1
}

def calculate_mood_score(persona, recent=10):
    """
    Computes a mood score based on recent emotional reactions.
    Positive = confident/happy, negative = frustrated/focused.
    """
    reactions = get_reactions(persona)
    recent_reactions = reactions[-recent:]

    score = 0
    for entry in recent_reactions:
        mood = entry.get("emotion", "neutral")
        score += MOOD_WEIGHTS.get(mood, 0)

    return score

def update_persona_mood(persona):
    """
    Updates the assistant's mood in system state based on recent reaction data.
    """
    score = calculate_mood_score(persona)
    mood = "confident" if score > 3 else "neutral" if score >= 0 else "frustrated"
    log_state(f"{persona}_current_mood", mood)
    print(f"[🧠 Mood Update] {persona}: Score={score} ➤ Mood={mood}")
    return mood

# === Manual test
if __name__ == "__main__":
    for name in ["MoCash", "Mentor", "Strategist", "DrillInstructor"]:
        update_persona_mood(name)