Creating a new strategy or utility for a game like Civilization or an empire-building game involves implementing a feature that can enhance gameplay, optimize decision-making, or streamline management tasks. Below is a Python script for a simple AI utility that helps players make strategic decisions based on resource management and expansion strategies. This utility can be used to suggest optimal city placement based on available resources and strategic importance.

Here’s a mock-up of such a utility:

```python
import random

# Define types of resources
RESOURCES = [
    "food",
    "gold",
    "wood",
    "iron",
    "stone"
]

# Define terrain types with resource bonuses
TERRAINS = {
    "plains": {"food": 1, "wood": 1, "gold": 0, "iron": 0, "stone": 0},
    "forest": {"food": 0, "wood": 3, "gold": 0, "iron": 0, "stone": 0},
    "hills": {"food": 0, "wood": 0, "gold": 1, "iron": 1, "stone": 2},
    "mountains": {"food": 0, "wood": 0, "gold": 0, "iron": 3, "stone": 3},
    "river": {"food": 3, "wood": 0, "gold": 2, "iron": 0, "stone": 0}
}

# Define a simple map with terrains
MAP_SIZE = 10
game_map = [[random.choice(list(TERRAINS.keys())) for _ in range(MAP_SIZE)] for _ in range(MAP_SIZE)]

class City:
    def __init__(self, name, x, y):
        self.name = name
        self.x = x
        self.y = y
        self.resources = {resource: 0 for resource in RESOURCES}

    def gather_resources(self, terrain):
        bonus = TERRAINS[terrain]
        for resource, value in bonus.items():
            self.resources[resource] += value

    def report(self):
        return f"City: {self.name}, Location: ({self.x}, {self.y}) - Resources: {self.resources}"

def suggest_city_location(game_map):
    """ Suggest new city placement location based on resource yield """
    best_score = 0
    best_location = (0, 0)

    for y in range(MAP_SIZE):
        for x in range(MAP_SIZE):
            terrain = game_map[y][x]
            score = sum(TERRAINS[terrain].values())

            # prefer areas with a mix of resources, not just one.
            variety_score = len([value for value in TERRAINS[terrain].values() if value > 0])
            total_score = score + variety_score

            if total_score > best_score:
                best_score = total_score
                best_location = (x, y)

    return best_location

# Example usage of the utility
if __name__ == "__main__":
    city_name = "New Haven"
    x, y = suggest_city_location(game_map)
    new_city = City(city_name, x, y)

    # Simulate gathering resources for the new city
    new_city.gather_resources(game_map[y][x])
    
    # Print the game map
    for row in game_map:
        print(" ".join(row))

    print("\n" + new_city.report())
```

### Explanation:

1. **Resource and Terrain Definition**: Various resource types and terrain types are defined, each with their potential bonuses for resource gathering.

2. **Game Map Generation**: A random game map is created, which simulates different types of terrain across the map's grid.

3. **City Class**: Represents a city, holding its name, position, and current resources. The city can gather resources based on its surrounding terrain.

4. **suggest_city_location Function**: This function analyzes the map to find the best location for a new city, considering both the total resources available and the diversity of those resources (which can be a strategic advantage).

5. **Simulation and Reporting**: The main script creates a city at the suggested location, gathers resources based on the terrain, and prints a report of the city’s status and resources.

This utility can help players strategically place cities to maximize resource gain and foster a strong economy in their empire-building game. Adjustments and expansion of the script can be made to include more complex gameplay dynamics and strategic considerations.