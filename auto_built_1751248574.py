```python
# ghost_ai.py

import random
import uuid

class GhostPersonality:
    def __init__(self, name, traits):
        self.id = uuid.uuid4()
        self.name = name
        self.traits = traits

    def describe(self):
        return f"Ghost {self.name}[{self.id}]: Traits - {', '.join(self.traits)}"

class GhostAISpawner:
    def __init__(self):
        self.personality_names = [
            "Eerie Earl", "Spooky Susan", "Whispering White", "Haunting Harold", "Phantom Fiona"
        ]
        self.possible_traits = [
            "Friendly", "Mischievous", "Mysterious", "Terrifying", "Benevolent", "Curious"
        ]

    def spawn_personality(self):
        name = random.choice(self.personality_names)
        traits = random.sample(self.possible_traits, random.randint(2, 4))
        return GhostPersonality(name, traits)

# Demonstration of module usage
if __name__ == "__main__":
    ghost_ai = GhostAISpawner()
    ghost = ghost_ai.spawn_personality()
    print(ghost.describe())
```
