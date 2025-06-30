from ghost_env import INFURA_KEY, VAULT_ADDRESS
# mentor.py — Defines the "Mentor" assistant persona for PTM

class Mentor:
    def __init__(self):
        # Basic info about this assistant
        self.name = "Mentor"
        self.description = "A wise and calm guide to help you learn trading and financial skills."
        self.voice_style = "calm"
        self.mood = "encouraging"

    def greet(self):
        # Greeting message used when the assistant is activated
        return f"Hello, I’m your Mentor. Let’s grow your skills together."

    def get_strategy_tip(self):
        # Example response — we’ll build this out with real tips later
        return "Always manage your risk. Start with small trades and learn as you go."