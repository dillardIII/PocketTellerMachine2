Creating a new Python utility for strategy or empire management can be both a fun and educational project. Let's develop a simplified resource management utility for a fictional empire-building turn-based game. This utility will help manage resources, track population, and expand territories.

We'll name this utility "EmpireManager". It will allow the player to collect resources, expand their empire by claiming new territories, and maintain their population. Here’s a basic outline of how it might look:

```python
class EmpireManager:
    def __init__(self, name):
        self.name = name
        self.resources = {
            'gold': 100,
            'food': 100,
            'wood': 100
        }
        self.population = 10
        self.territories = 1

    def display_status(self):
        print(f"Empire: {self.name}")
        print(f"Resources: {self.resources}")
        print(f"Population: {self.population}")
        print(f"Territories: {self.territories}")
        print("-" * 20)

    def collect_resources(self):
        # Basic resource collection logic
        self.resources['gold'] += self.territories * 10
        self.resources['food'] += self.population * 2
        self.resources['wood'] += self.territories * 5
        print("Resources collected successfully.")

    def expand_territory(self):
        if self.resources['gold'] >= 50 and self.resources['wood'] >= 30:
            self.resources['gold'] -= 50
            self.resources['wood'] -= 30
            self.territories += 1
            print("Territory expanded successfully.")
        else:
            print("Not enough resources to expand territory.")

    def grow_population(self):
        # Assumes food is required to sustain population growth
        if self.resources['food'] >= self.population:
            self.resources['food'] -= self.population
            self.population += 1
            print("Population grew successfully.")
        else:
            print("Not enough food to sustain population growth.")

if __name__ == "__main__":
    empire = EmpireManager("Astral Kingdom")
    empire.display_status()
    
    # Perform some actions
    empire.collect_resources()
    empire.display_status()
    
    empire.grow_population()
    empire.display_status()
    
    empire.expand_territory()
    empire.display_status()
```

### Explanation:

- **EmpireManager**: A class that manages the state of the empire, including resources, population, and territories.
- **collect_resources**: Increases resources based on current population and territories.
- **expand_territory**: Expands territories if enough gold and wood are available.
- **grow_population**: Increases the population if there is enough food available.
- **display_status**: Prints the current status of the empire for easy monitoring.

This utility can serve as the basis for a more complex empire-building simulator. Players could eventually face random events, trade opportunities, and further strategic decisions to enhance the depth of gameplay.