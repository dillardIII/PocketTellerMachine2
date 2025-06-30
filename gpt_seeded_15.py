from ghost_env import INFURA_KEY, VAULT_ADDRESS
Sure! Let's build a simple Python-based supply chain optimization utility for an empire simulation game. This utility will help manage resources efficiently across different cities within the empire, considering variable production rates, demands, and transportation costs.

Here's a basic implementation:

```python
# Import necessary libraries
import random

# Define city class
class City:
    def __init__(self, name, production_rate, demand, stock):
        self.name = name
        self.production_rate = production_rate
        self.demand = demand
        self.stock = stock

    def produce(self):
        produced = random.randint(0, self.production_rate)
        self.stock += produced
        print(f"{self.name} produced {produced} units. Stock: {self.stock}")

    def consume(self):
        consumed = min(self.demand, self.stock)
        self.stock -= consumed
        print(f"{self.name} consumed {consumed} units. Stock: {self.stock}")

# Define empire class with supply chain optimization
class Empire:
    def __init__(self):
        self.cities = []
        self.transport_costs = {}

    def add_city(self, city):
        self.cities.append(city)

    def set_transport_costs(self, city1, city2, cost):
        self.transport_costs[(city1.name, city2.name)] = cost

    def optimize_supply_chain(self):
        print("Optimizing supply chain...")
        # Basic supply optimization: balance stock based on demand
        total_demand = sum(city.demand for city in self.cities)
        total_stock = sum(city.stock for city in self.cities)
        
        if total_stock >= total_demand:
            print("Total stock is sufficient for the demand.")
        else:
            print(f"Total stock of {total_stock} is insufficient. Need to produce more!")
        
        for city in self.cities:
            city.produce()
        
        for city in self.cities:
            city.consume()
        
        for city1 in self.cities:
            for city2 in self.cities:
                if city1 != city2:
                    stock_diff = city2.demand - city2.stock
                    if stock_diff > 0 and city1.stock > 0:
                        transfer_amount = min(city1.stock, stock_diff)
                        transport_cost = self.transport_costs.get((city1.name, city2.name), 10)
                        print(f"Transferring {transfer_amount} units from {city1.name} to {city2.name} at a cost of {transport_cost} per unit.")
                        city1.stock -= transfer_amount
                        city2.stock += transfer_amount

# Create instances of cities
city1 = City("Capital", production_rate=20, demand=15, stock=10)
city2 = City("BorderVillage", production_rate=10, demand=12, stock=5)
city3 = City("TradingPost", production_rate=15, demand=10, stock=10)

# Create an empire and add cities
empire = Empire()
empire.add_city(city1)
empire.add_city(city2)
empire.add_city(city3)

# Set transport costs between cities
empire.set_transport_costs(city1, city2, 3)
empire.set_transport_costs(city2, city3, 2)
empire.set_transport_costs(city3, city1, 4)

# Optimize supply chain
empire.optimize_supply_chain()
```

**Explanation:**
- The `City` class represents a city's production rate, demand, and current stock level. 
- Each city can produce resources up to its production rate and consumes resources based on demand.
- The `Empire` class manages multiple cities and optimizes the supply chain.
- It transfers resources between cities based on demand, production, stock levels, and transportation costs.
- The utility prints out the actions taken, such as production, consumption, and resource transfers. 

This setup provides a basic framework you can expand upon, adding features like dynamic production adjustment, resource types, or more complex transportation networks for a more sophisticated empire management simulation.

def log_event():ef drop_files_to_bridge():