Creating a Python utility for managing a strategy or empire-style game involves handling several components such as resources, military units, and expansion. Below is an example of a simplified strategy utility for managing resources and territories within a fictional empire-style game. This script will allow players to allocate resources, grow their empire, and handle basic interactions between territories.

```python
import random

# Define a Territory class to manage resources and interactions
class Territory:
    def __init__(self, name):
        self.name = name
        self.resources = {'gold': random.randint(100, 500), 'food': random.randint(100, 500)}
        self.units = random.randint(50, 150)

    def allocate_resources(self, gold=None, food=None):
        if gold:
            self.resources['gold'] += gold
        if food:
            self.resources['food'] += food
        self.show_status()

    def expand(self):
        self.units += random.randint(10, 30)
        self.resources['gold'] += random.randint(10, 50)
        self.resources['food'] += random.randint(10, 50)
        print(f"{self.name} has expanded its influence!")
        self.show_status()

    def show_status(self):
        print(f"----- {self.name} Status -----")
        print(f"Resources: Gold - {self.resources['gold']}, Food - {self.resources['food']}")
        print(f"Units: {self.units}")
        print("-------------------------------")

# Define an Empire class to manage multiple territories
class Empire:
    def __init__(self):
        self.territories = []

    def add_territory(self, territory_name):
        new_territory = Territory(territory_name)
        self.territories.append(new_territory)
        print(f"Territory {territory_name} added to the empire!")
        new_territory.show_status()

    def allocate_resources_to_territory(self, territory_name, gold=None, food=None):
        for territory in self.territories:
            if territory.name == territory_name:
                territory.allocate_resources(gold, food)
                break
        else:
            print(f"Territory {territory_name} not found in the empire!")

    def expand_territory(self, territory_name):
        for territory in self.territories:
            if territory.name == territory_name:
                territory.expand()
                break
        else:
            print(f"Territory {territory_name} not found in the empire!")

    def empire_status(self):
        print("== Empire Overview ==")
        for territory in self.territories:
            territory.show_status()

# Example Usage
def main():
    print("Welcome to the Empire Manager Utility!")
    my_empire = Empire()
    
    my_empire.add_territory("Eastern Lands")
    my_empire.add_territory("Northern Realm")

    my_empire.allocate_resources_to_territory("Eastern Lands", gold=50, food=30)
    my_empire.expand_territory("Northern Realm")

    my_empire.empire_status()

if __name__ == "__main__":
    main()
```

### Key Features:
1. **Territory Management**: Each territory has its resources and units. You can allocate additional resources or expand the territory to gain more units and resources.
2. **Expansion Mechanism**: The `expand()` method increases the units and resources, simulating a minor growth of influence.
3. **Empire Overview**: The `empire_status()` method provides a summary of all territories under your empire's control.

### Usage:
You can run the code as-is and modify or expand it to add more complexity, such as battles between territories, resource trading, or events affecting resource yield and territory status. This foundational script provides a framework on which to build more intricate mechanics.