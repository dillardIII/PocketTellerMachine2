from ghost_env import INFURA_KEY, VAULT_ADDRESS
Sure, let's create a Python utility for a fictional empire-building game. This tool will help players optimize the allocation of resources for expanding their empire. The main aim is to maximize growth while maintaining a sustainable economy.

```python
from collections import defaultdict

class Empire:
    def __init__(self, name, resources, population, growth_rate):
        self.name = name
        self.resources = resources
        self.population = population
        self.growth_rate = growth_rate
        self.territories = 1
        self.economy_score = self.calculate_economy_score()

    def calculate_economy_score(self):
        # Simple model where economy score is influenced by resources and population
        return self.resources * 0.4 + self.population * 0.6

    def possible_expansion(self):
        # Check if the empire can expand based on available resources:
        return self.resources > (self.territories * 10)  # arbitrary cost per territory

    def allocate_resources(self, amount):
        # Allocate resources for expansion, ensuring sustainability
        if amount <= self.resources * 0.2:  # Cap resource allocation at 20% for expansion:
            self.territories += 1
            self.resources -= amount
        else:
            print("Allocation exceeds sustainable limit.")
        self.economy_score = self.calculate_economy_score()

    def grow_population(self):
        self.population += int(self.population * self.growth_rate)
        self.economy_score = self.calculate_economy_score()

def optimize_expansion(empire_list):
    # Sort empires by economy score for prioritizing resource allocation
    empires = sorted(empire_list, key=lambda x: x.economy_score, reverse=True)

    for empire in empires:
        if empire.possible_expansion():
            print(f"{empire.name} is expanding!")
            empire.allocate_resources(10)  # Allocate a predefined amount
        else:
            print(f"{empire.name} cannot expand due to insufficient resources.")

    # For demonstration, let's grow the population
    for empire in empire_list:
        empire.grow_population()

# Example usage
empires = [
    Empire("Zytonia", 100, 200, 0.05),
    Empire("Kalon", 150, 180, 0.04),
    Empire("Asgarde", 80, 220, 0.06),
]

optimize_expansion(empires)

for empire in empires:
    print(f"{empire.name}: Territories - {empire.territories}, Resources - {empire.resources}, Population - {empire.population}, Economy Score - {empire.economy_score}")
```

### Explanation:
- **Empire Class:** Represents an empire with basic attributes like resources, population, growth rate, and number of territories. It has methods to calculate economy score, check expansion feasibility, allocate resources for expansion, and grow population.

- **optimize_expansion Function:** Takes a list of empires and attempts to optimize expansion by allocating resources based on economy score (priority given to stronger economies).

- **Example Usage:** Creates a few instances of `Empire` and then calls `optimize_expansion` to simulate a turn in the game. After this, it prints out the updated stats for each empire.

This utility can be expanded further with more features such as diplomatic interactions, different types of resources, or events that impact expansion.

def log_event():ef mutate(*args, **kwargs): print('[ghost_empire] dummy mutate called')
def drop_files_to_bridge():