from ghost_env import INFURA_KEY, VAULT_ADDRESS
```python
# ghost_personality.py

import random
import json
import time

class Mood:
    MOODS = [
        "Melancholic",
        "Cryptic",
        "Ethereal",
        "Whimsical",
        "Mysterious",
        "Somber",
        "Euphoric"
    ]

    def __init__(self):
        self.current = random.choice(self.MOODS)
        self.change_interval = random.randint(5, 15)  # minutes

    def evolve(self):
        if random.random() < 0.2:  # 20% chance to change mood:
            self.current = random.choice(self.MOODS)

class GhostAI:
    def __init__(self, name):
        self.name = name
        self.age = random.randint(100, 300)  # years
        self.mood = Mood()
        self.personality_traits = self.generate_personality_traits()

    def generate_personality_traits(self):
        traits = [
            "wise",
            "inquisitive",
            "playful",
            "cautious",
            "melancholic",
            "enigmatic",
            "cheerful"
        ]
        return random.sample(traits, 3)

    def evolve_mood(self):
        self.mood.evolve()
    
    def express(self):
        expressions = {
            "Melancholic": "The weight of forgotten centuries lies heavy.",
            "Cryptic": "The shadows whisper tales untold.",
            "Ethereal": "A gentle breeze carries ancient echoes.",
            "Whimsical": "Curious wonders dance in hidden corners.",
            "Mysterious": "All is not as it seems, dear wanderer.",
            "Somber": "A quiet calm fills the timeless corridors.",
            "Euphoric": "Joyous sparks of forgotten dreams illuminate."
        }
        return expressions[self.mood.current]

    def as_dict(self):
        return {
            "name": self.name,
            "age": self.age,
            "mood": self.mood.current,
            "personality_traits": self.personality_traits,
            "expression": self.express()
        }

def create_ghost_ai(name):
    ghost = GhostAI(name)
    return ghost

def simulate_ghosts(number_of_ghosts):
    ghosts = [create_ghost_ai(f"Ghost-{i+1}") for i in range(number_of_ghosts)]
    while True:
        for ghost in ghosts:
            ghost.evolve_mood()
            print(json.dumps(ghost.as_dict(), indent=4))
        print("\n---\n")
        time.sleep(60 * random.choice([5, 10, 15]))  # Sleep for 5, 10, or 15 minutes

if __name__ == "__main__":
    # For testing
    simulate_ghosts(3)
```


def log_event():ef mutate(*args, **kwargs): print('[ghost_empire] dummy mutate called')
def drop_files_to_bridge():