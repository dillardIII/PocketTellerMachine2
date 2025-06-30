from ghost_env import INFURA_KEY, VAULT_ADDRESS
Certainly! Let's create a Python utility for managing and optimizing resources in a simulated empire-building game. This utility will help players calculate the most efficient way to allocate their resources for maximum growth and defense.

### Empire Resource Manager

```python
class EmpireResourceManager:
    def __init__(self, resources, growth_rate, defense_factor):
        """
        Initialize the EmpireResourceManager.

        :param resources: A dictionary containing the current amount of each resource.
        :param growth_rate: A dictionary containing the growth rate of each resource.
        :param defense_factor: A scaling factor for defense efficiency.
        """
        self.resources = resources
        self.growth_rate = growth_rate
        self.defense_factor = defense_factor

    def calculate_optimal_allocation(self, goals):
        """
        Calculate the optimal resource allocation for given goals.

        :param goals: A dictionary containing target values for 'growth', 'defense', 
                      and any other strategic categories.
        :return: Allocation plan as a dictionary.
        """
        allocation = {resource: 0 for resource in self.resources}
        
        # Calculate total importance
        total_importance = sum(goals.values())
        
        for goal, importance in goals.items():
            factor = importance / total_importance
            if goal == 'growth':
                for resource in self.resources:
                    allocation[resource] += factor * self.growth_rate[resource] * self.resources[resource]
            elif goal == 'defense':
                for resource in self.resources:
                    allocation[resource] += factor * self.defense_factor * self.resources[resource]
            else:
                # Allocate for other strategic goals proportionally
                for resource in self.resources:
                    allocation[resource] += factor * self.resources[resource]

        # Normalize allocation
        total_resources = sum(allocation.values())
        for resource in allocation:
            allocation[resource] = max(0, (allocation[resource] / total_resources) * self.resources[resource])

        return allocation

    def update_resources(self, allocation):
        """
        Update resources based on the given allocation.

        :param allocation: A dictionary of allocated resources.
        """
        for resource, amount in allocation.items():
            self.resources[resource] -= amount

    def simulate_turn(self):
        """
        Simulate a turn, updating resource counts based on growth.
        """
        for resource in self.resources:
            self.resources[resource] += self.resources[resource] * self.growth_rate[resource]

    def display_resources(self):
        """
        Display current resources.
        """
        print("Current Resources:")
        for resource, amount in self.resources.items():
            print(f"{resource}: {amount:.2f}")

# Example usage
resources = {
    'food': 1000,
    'gold': 500,
    'stone': 800,
}

growth_rate = {
    'food': 0.05,
    'gold': 0.02,
    'stone': 0.03,
}

defense_factor = 1.2

empire = EmpireResourceManager(resources, growth_rate, defense_factor)

# End of Month Strategy
goals = {
    'growth': 0.5,
    'defense': 0.5,
}

# Calculate and apply allocation plan
allocation_plan = empire.calculate_optimal_allocation(goals)
empire.update_resources(allocation_plan)

# Simulate resource growth for a turn
empire.simulate_turn()

# Display updated resources
empire.display_resources()
```

### Key Features

- **Resource Management**: This utility helps manage different types of resources such as food, gold, and stone, which are common in empire-building games.
- **Growth & Defense Optimization**: Players can input strategic goals for growth and defense, and the utility calculates the optimal resource distribution using these priorities.
- **Dynamic Simulation**: Simulates the passage of a turn in a game, allowing players to see the effects of their resource allocation decisions over time.
- **Flexibility**: Easily adaptable for different types of resources or strategies by tweaking growth rates and defense factors.

This Python utility provides a foundation for players to efficiently manage resources and make strategic decisions in their empire-building games. Feel free to expand upon this with additional features and complexities as needed!

def log_event():ef drop_files_to_bridge():