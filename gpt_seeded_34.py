Sure, I'll create a Python utility that could be useful for a strategy or empire-building game. This utility will simulate basic economic management by handling resources and trading between different cities within an empire. The utility will allow defining cities, managing resources like food, gold, wood, and stone, and simulating trade between cities. This can help players optimize their empire's resource management and strategic planning.

```python
class City:
    def __init__(self, name, resources):
        """
        Initialize a city with a name and a dictionary of resources.
        resources: a dictionary with resource types as keys (str) and amounts as values (int).
        Example: {'food': 100, 'gold': 50, 'wood': 200, 'stone': 150}
        """
        self.name = name
        self.resources = resources

    def add_resources(self, resource_type, amount):
        """Add resources of a specific type to the city."""
        if resource_type in self.resources:
            self.resources[resource_type] += amount
        else:
            self.resources[resource_type] = amount
        print(f"Added {amount} {resource_type} to {self.name}.")

    def deduct_resources(self, resource_type, amount):
        """Deduct resources of a specific type from the city."""
        if resource_type in self.resources and self.resources[resource_type] >= amount:
            self.resources[resource_type] -= amount
            print(f"Deducted {amount} {resource_type} from {self.name}.")
            return True
        else:
            print(f"Insufficient {resource_type} in {self.name}.")
            return False

    def __str__(self):
        return f"City: {self.name}, Resources: {self.resources}"


class Empire:
    def __init__(self):
        """Initialize the empire with an empty dictionary to hold cities."""
        self.cities = {}

    def add_city(self, city):
        """Add a new city to the empire."""
        if city.name in self.cities:
            print(f"City {city.name} already exists in the empire.")
        else:
            self.cities[city.name] = city
            print(f"City {city.name} added to the empire.")

    def trade(self, from_city_name, to_city_name, resource_type, amount):
        """Simulate trading resources between two cities in the empire."""
        if from_city_name in self.cities and to_city_name in self.cities:
            from_city = self.cities[from_city_name]
            to_city = self.cities[to_city_name]
            if from_city.deduct_resources(resource_type, amount):
                to_city.add_resources(resource_type, amount)
                print(f"Traded {amount} {resource_type} from {from_city_name} to {to_city_name}.")
            else:
                print(f"Failed to trade {resource_type}.")
        else:
            print("One or both cities do not exist in the empire.")

    def report(self):
        """Print a report of all cities and their resources."""
        for city in self.cities.values():
            print(city)


# Example Usage
if __name__ == "__main__":
    rome = City("Rome", {'food': 200, 'gold': 300, 'wood': 150, 'stone': 100})
    carthage = City("Carthage", {'food': 150, 'gold': 200, 'wood': 250, 'stone': 300})

    empire = Empire()
    empire.add_city(rome)
    empire.add_city(carthage)
    empire.report()

    # Simulate a trade
    empire.trade("Rome", "Carthage", "wood", 50)
    empire.trade("Carthage", "Rome", "gold", 75)

    # Final report
    empire.report()
```

This utility is flexible and extensible. You can add more resource types, refine the trade logic, or introduce additional mechanics like resource decay over time, city growth, or even adversities like plagues or pillages to add complexity to the simulation.