Creating a utility function for managing resources in a strategy or empire game can enhance gameplay by helping players optimize their strategies. Below, I'll outline a simple Python utility that manages resources like wood, stone, and food, updating based on production rates and consumption, and provides feedback to the player.

```python
class ResourceManager:
    def __init__(self, initial_wood, initial_stone, initial_food):
        self.resources = {
            "wood": initial_wood,
            "stone": initial_stone,
            "food": initial_food
        }
        self.production_rates = {
            "wood": 0,
            "stone": 0,
            "food": 0
        }
        self.consumption_rates = {
            "wood": 0,
            "stone": 0,
            "food": 0
        }
    
    def set_production_rate(self, resource, rate):
        if resource in self.production_rates:
            self.production_rates[resource] = rate
        else:
            print(f"Resource '{resource}' is not recognized.")

    def set_consumption_rate(self, resource, rate):
        if resource in self.consumption_rates:
            self.consumption_rates[resource] = rate
        else:
            print(f"Resource '{resource}' is not recognized.")

    def update_resources(self, turns=1):
        for resource in self.resources:
            net_change = (self.production_rates[resource] - self.consumption_rates[resource]) * turns
            self.resources[resource] = max(0, self.resources[resource] + net_change)
            print(f"After {turns} turns, the {resource} is now: {self.resources[resource]}")

    def display_status(self):
        print("Current Resource Status:")
        for resource, quantity in self.resources.items():
            print(f"{resource.capitalize()}: {quantity}")

    def is_resource_sufficient(self, resource, amount):
        if resource not in self.resources:
            print(f"Resource '{resource}' is not recognized.")
            return False
        
        return self.resources[resource] >= amount

    def allocate_resource(self, resource, amount):
        if self.is_resource_sufficient(resource, amount):
            self.resources[resource] -= amount
            print(f"Allocated {amount} units of {resource}.")
        else:
            print(f"Insufficient {resource} to allocate {amount} units.")

# Example use case:
if __name__ == "__main__":
    empire = ResourceManager(initial_wood=100, initial_stone=100, initial_food=100)
    
    # Setting production and consumption rates
    empire.set_production_rate("wood", 10)
    empire.set_consumption_rate("food", 5)
    
    # Simulate 5 turns
    empire.update_resources(turns=5)
    
    # Display current status
    empire.display_status()
    
    # Attempt to allocate resources
    empire.allocate_resource("stone", 20)
    empire.allocate_resource("food", 60)
```

### Features:
- **Resource Tracking:** The utility tracks the quantities of various resources.
- **Production & Consumption Rates:** Players can set production and consumption rates for each resource, impacting the resource availability.
- **Turn-Based Updates:** The function simulates resource changes over a number of turns.
- **Resource Allocation:** Allows for resource allocation checks and updates, useful for construction or upgrades.
- **Status Display:** An easy-to-read summary of current resource statuses.

This utility can be expanded with additional features, such as trading between resources, advanced strategy rules, or player notifications when resources run low.