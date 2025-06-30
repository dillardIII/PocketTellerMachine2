from ghost_env import INFURA_KEY, VAULT_ADDRESS
# mood_engine.py

def update_mood(confidence):
    """
    Returns an emotional mood and reaction string based on the trade confidence score.
    """

    if confidence >= 0.9:
        return {
            "mood": "Pumped",
            "reaction": "I'm hyped! This setup looks 🔥."
        }
    elif confidence >= 0.75:
        return {
            "mood": "Confident",
            "reaction": "Feeling good about this one."
        }
    elif confidence >= 0.6:
        return {
            "mood": "Cautious",
            "reaction": "Could go either way. Stay sharp."
        }
    else:
        return {
            "mood": "Worried",
            "reaction": "Mmm… not loving this. Might wanna pass."
        }