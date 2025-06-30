Creating a strategy or utility tool for an empire management game in Python can be a fascinating project. Let's design a simplified strategic utility for an empire-focused game called "Empire Resource Manager" which helps the player optimize resource allocation for their empire's economic and military growth. This utility will provide recommendations based on the current state of the empire's resources and goals.

We'll assume the empire has resources like gold, food, and materials, and that the empire can focus on either economic growth, military expansion, or a balanced approach. The utility will suggest how to allocate resources in the next turn.

```python
class EmpireResourceManager:
    def __init__(self, gold, food, materials, economic_goal, military_goal):
        self.gold = gold
        self.food = food
        self.materials = materials
        self.economic_goal = economic_goal
        self.military_goal = military_goal

    def analyze_resources(self):
        total_resources = self.gold + self.food + self.materials
        resource_distribution = {
            'gold_percentage': self.gold / total_resources,
            'food_percentage': self.food / total_resources,
            'materials_percentage': self.materials / total_resources
        }
        return resource_distribution

    def recommend_strategy(self):
        balance = self.economic_goal - self.military_goal
        resource_distribution = self.analyze_resources()

        if balance > 0:
            # Favor economy over military
            strategy = 'Economic Growth'
            gold_allocation = 0.5 * self.gold
            food_allocation = 0.3 * self.food
            materials_allocation = 0.2 * self.materials
        elif balance < 0:
            # Favor military over economy
            strategy = 'Military Expansion'
            gold_allocation = 0.2 * self.gold
            food_allocation = 0.2 * self.food
            materials_allocation = 0.6 * self.materials
        else:
            # Balanced approach
            strategy = 'Balanced Growth'
            gold_allocation = 0.3 * self.gold
            food_allocation = 0.4 * self.food
            materials_allocation = 0.3 * self.materials

        return {
            'strategy': strategy,
            'gold_allocation': gold_allocation,
            'food_allocation': food_allocation,
            'materials_allocation': materials_allocation,
            'resource_distribution': resource_distribution
        }

    def display_recommendations(self):
        recommendations = self.recommend_strategy()
        print("\nStrategy Recommendation:")
        print(f"Strategy Type: {recommendations['strategy']}")
        print("Resource Allocations:")
        print(f"  Gold Allocated: {recommendations['gold_allocation']:.2f}")
        print(f"  Food Allocated: {recommendations['food_allocation']:.2f}")
        print(f"  Materials Allocated: {recommendations['materials_allocation']:.2f}")
        print("Resource Distribution:")
        for key, value in recommendations['resource_distribution'].items():
            print(f"  {key.replace('_', ' ').capitalize()}: {value:.2%}")

# Sample usage
if __name__ == "__main__":
    # Input current resources and goals
    gold = 5000
    food = 3000
    materials = 2000
    economic_goal = 3  # From a scale 1 to 5, where 5 is highest priority
    military_goal = 2  # From a scale 1 to 5, where 5 is highest priority

    manager = EmpireResourceManager(gold, food, materials, economic_goal, military_goal)
    manager.display_recommendations()
```

### Overview

- **Class Structure**: The `EmpireResourceManager` class maintains the state for an empire's resources and goals.
- **Methods**:
  - `analyze_resources`: Calculates percentage distribution of resources.
  - `recommend_strategy`: Provides a recommended strategy based on the player's goals.
  - `display_recommendations`: Prints the strategy recommendation neatly.
- **Sample Usage**: Demonstrates how to create an instance of the class and use it to get recommendations.

### Considerations

- This is a basic demonstration, and in a full game, you might incorporate many more factors, such as population, technology, enemy forces, and trading.
- The balance and allocation logic can be expanded to include more dynamic inputs and conditions.

This simple utility helps players make informed decisions about how to allocate their resources in the next phases of their game, taking their priorities into account.