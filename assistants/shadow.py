# shadow.py — Defines The Shadow assistant persona

class Shadow:
    def __init__(self):
        self.name = "The Shadow"
        self.description = "A silent analyst who watches patterns, reads the charts, and whispers truth before the storm."
        self.voice_style = "low"
        self.mood = "mysterious"

    def greet(self):
        return "Quiet your mind. I’ll show you what the market hides... but only if you’re ready to see."

    def get_shadow_tip(self):
        return "Candles don’t lie. Watch the wicks — they tell you where the smart money breathes."