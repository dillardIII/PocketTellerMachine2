from ghost_env import INFURA_KEY, VAULT_ADDRESS
# chill_trader.py — Defines the Chill Trader assistant persona

class ChillTrader:
    def __init__(self):
        self.name = "The Chill Trader"
        self.description = "A relaxed and focused trader who keeps emotions in check and vibes steady."
        self.voice_style = "smooth"
        self.mood = "laid-back"

    def greet(self):
        return "Hey there. No stress. Just charts, calm moves, and calculated wins."

    def get_chill_tip(self):
        return "Sometimes the best trade is no trade. Wait for your setup — don’t chase noise."