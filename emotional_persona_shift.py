"""
Emotional Persona Shift:
Adjusts persona responses and tone dynamically based on emotional state.
Used to evolve assistant behavior, sarcasm, tone, and decision-making.
"""

from emotion_engine import get_mood

PERSONA_TONE_MODIFIERS = {
    "MoCash": {
        "win": "🔥 Hyped up and hungry.",
        "loss": "😤 Frustrated, but not giving up.",
        "neutral": "😎 Calm and watching the charts."
    },
    "Mentor": {
        "win": "😊 Proud and affirming.",
        "loss": "🤔 Reflective and analytical.",
        "neutral": "🧘 Steady and grounded."
    },
    "Strategist": {
        "win": "📈 Confident in pattern detection.",
        "loss": "🔍 Reevaluating algorithms.",
        "neutral": "📊 Focused on data gathering."
    },
    "DrillInstructor": {
        "win": "🏋️ Fired up — results or death.",
        "loss": "💢 Furious — demanding review.",
        "neutral": "🪖 Locked in, awaiting next brief."
    }
}

def describe_mood(persona):
    """
    Returns a string description of the current mood modifier.
    """
    mood = get_mood(persona)
    modifier = PERSONA_TONE_MODIFIERS.get(persona, {}).get(mood, "")
    return f"{persona} [{mood.upper()}]: {modifier}" if modifier else f"{persona} is {mood}"

# === Optional test run
if __name__ == "__main__":
    for persona in ["MoCash", "Mentor", "Strategist", "DrillInstructor"]:
        print(describe_mood(persona))