Certainly! Below is a Python utility for a simple turn-based strategy game where the player manages an empire. The utility is called `EmpireManager`, and it helps players manage resources, population, and military units. The players can allocate resources to different areas and respond to random events.

```python
import random

class Empire:
    def __init__(self, name):
        self.name = name
        self.resources = 1000
        self.population = 100
        self.military = 50
        self.happiness = 70
        self.event_history = []

    def allocate_resources(self, for_population: int, for_military: int):
        if for_population + for_military > self.resources:
            print(f"Not enough resources to allocate!")
            return

        self.resources -= (for_population + for_military)
        self.population += for_population // 10
        self.military += for_military // 20
        self.update_happiness(for_population, for_military)

    def update_happiness(self, for_population: int, for_military: int):
        self.happiness += (for_population // 50) - (for_military // 50)
        self.happiness = max(min(self.happiness, 100), 0)  # Clamp between 0 and 100

    def random_event(self):
        event_type = random.choice(['bountiful_harvest', 'disease_outbreak', 'barbarian_attack', 'festival', 'resource_boom'])
        if event_type == 'bountiful_harvest':
            self.resources += 200
            print("A bountiful harvest! Resources increased by 200.")
        elif event_type == 'disease_outbreak':
            lost_population = random.randint(5, 15)
            self.population -= lost_population
            self.happiness -= 10
            print(f"A disease outbreak! Lost {lost_population} population.")
        elif event_type == 'barbarian_attack':
            lost_military = random.randint(5, 15)
            self.military -= lost_military
            self.resources -= 100
            print(f"A barbarian attack! Lost {lost_military} military units.")
        elif event_type == 'festival':
            self.happiness += 20
            print("A successful festival! Happiness increased.")
        elif event_type == 'resource_boom':
            gained_resources = random.randint(100, 300)
            self.resources += gained_resources
            print(f"A resource boom! Resources increased by {gained_resources}.")
        self.event_history.append(event_type)

    def display_status(self):
        print(f"Empire: {self.name}")
        print(f"Resources: {self.resources}")
        print(f"Population: {self.population}")
        print(f"Military: {self.military}")
        print(f"Happiness: {self.happiness}")

class EmpireManager:
    def __init__(self):
        self.empires = []

    def add_empire(self, name):
        self.empires.append(Empire(name))

    def manage_turns(self):
        for _ in range(10):  # Simulate 10 turns
            for empire in self.empires:
                self.take_turn(empire)
                self.end_turn_status(empire)

    def take_turn(self, empire):
        print("\nTaking turn for empire:", empire.name)
        # Random resource allocation
        for_population = random.randint(50, 200)
        for_military = random.randint(50, 200)
        empire.allocate_resources(for_population, for_military)
        empire.random_event()

    def end_turn_status(self, empire):
        print("\nStatus after turn:")
        empire.display_status()
        print('-' * 30)

if __name__ == "__main__":
    manager = EmpireManager()
    manager.add_empire("Asgard")
    manager.add_empire("Olympus")
    manager.manage_turns()
```

### Description:

- **Empire Class**: Represents each empire with resources, population, military, and happiness attributes. It includes methods to allocate resources and handle random events.
  
- **EmpireManager Class**: Manages multiple empires, facilitating the game's turn structure and processing actions for each empire during a turn.

- **Gameplay Mechanics**:
  - **Resource Allocation**: Resources can be allocated to either increase population or strengthen the military, affecting happiness.
  - **Random Events**: Emulate unforeseen events that can benefit or harm empires.
  - **Status Display**: After each turn, the status of empires is displayed.

With `EmpireManager`, you can manage the growth and challenges faced by your empire, testing strategic resource allocation and response to events.