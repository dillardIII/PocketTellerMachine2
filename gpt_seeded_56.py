from ghost_env import INFURA_KEY, VAULT_ADDRESS
Certainly! Let's create a simple utility for a fictional strategy game where you manage an empire. This utility will help simulate trading resources between different cities within your empire to optimize resource distribution.

```python
from collections import defaultdict

class City:
    def __init__(self, name, resources):
        self.name = name
        self.resources = resources  # dictionary of resources, e.g., {"food": 100, "wood": 50}
    
    def __str__(self):
        return f"{self.name} Resources: {self.resources}"

    def add_resource(self, resource, quantity):
        self.resources[resource] += quantity

    def remove_resource(self, resource, quantity):
        if self.resources[resource] >= quantity:
            self.resources[resource] -= quantity
        else:
            raise ValueError(f"Not enough {resource} in {self.name} to remove.")

class Empire:
    def __init__(self):
        self.cities = {}
    
    def add_city(self, city):
        self.cities[city.name] = city

    def trade_resources(self, sender, receiver, resource, quantity):
        if sender in self.cities and receiver in self.cities:
            try:
                self.cities[sender].remove_resource(resource, quantity)
                self.cities[receiver].add_resource(resource, quantity)
                print(f"Traded {quantity} of {resource} from {sender} to {receiver}.")
            except ValueError as e:
                print(e)
        else:
            print("One of the cities does not exist in the empire.")

    def balance_resources(self):
        # For simplicity, balance only considers overabundance and deficiencies in a simple manner
        resource_demand = defaultdict(int)
        resource_supply = defaultdict(int)
        
        # Calculate total demand and supply across all cities
        for city in self.cities.values():
            for resource, amount in city.resources.items():
                if amount < 50:
                    resource_demand[resource] += (50 - amount)
                else:
                    resource_supply[resource] += (amount - 50)
        
        # Trade resources between cities
        for resource in resource_demand:
            if resource_supply[resource] > 0:
                self._distribute_resource(resource, resource_supply[resource], resource_demand[resource])

    def _distribute_resource(self, resource, supply, demand):
        for city in self.cities.values():
            if city.resources[resource] < 50:
                needed = 50 - city.resources[resource]
                transfer_amount = min(needed, supply)
                if transfer_amount > 0:
                    supply -= transfer_amount
                    city.resources[resource] += transfer_amount
                    print(f"{city.name} received {transfer_amount} of {resource}")

# Example usage
rome = City("Rome", {"food": 30, "wood": 100})
athens = City("Athens", {"food": 80, "wood": 20})
sparta = City("Sparta", {"food": 70, "wood": 30})

empire = Empire()
empire.add_city(rome)
empire.add_city(athens)
empire.add_city(sparta)

empire.balance_resources()

for city_name, city in empire.cities.items():
    print(city)
```

### Explanation:

- **City Class**: Represents a city with a name and a dictionary of resources. Methods are provided to add or remove resources.
- **Empire Class**: Manages a collection of cities and provides methods to handle resource trading and balancing.
- **balance_resources Method**: Checks resource levels in each city. If a resource is below a certain threshold (in this case, 50 units), it will redistribute available resources from cities with an excess.
- **Trade Simulation**: The `trade_resources` method manually trades resources between two cities, and `balance_resources` attempts to automate balancing according to defined rules.

You can extend this utility by adding complexities, such as transport costs, trade agreements, or even dynamic resource production and consumption rates.

def log_event():ef drop_files_to_bridge():