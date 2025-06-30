from ghost_env import INFURA_KEY, VAULT_ADDRESS
Certainly! Let's create an empire utility in Python. This utility will simulate the management of a fictional medieval kingdom. It will help the user manage resources, expand territories, and keep the population satisfied.

### Kingdom Management Utility

The utility will handle several aspects of kingdom management:

- **Resources**: Gold, Food, and Lumber.
- **Population**: Total population and happiness levels.
- **Territories**: Management and expansion of territories.

```python
class Kingdom:
    def __init__(self, name):
        self.name = name
        self.gold = 1000
        self.food = 500
        self.lumber = 300
        self.population = 100
        self.happiness = 75
        self.territories = ["Capital"]

    def show_status(self):
        print(f"\nKingdom: {self.name}")
        print(f"Gold: {self.gold}")
        print(f"Food: {self.food}")
        print(f"Lumber: {self.lumber}")
        print(f"Population: {self.population}")
        print(f"Happiness: {self.happiness}")
        print(f"Territories: {', '.join(self.territories)}\n")

    def manage_resources(self):
        choice = input("Do you want to harvest resources (gold, food, lumber)? ").lower()
        amount = int(input("Enter amount: "))
        if choice == "gold":
            self.gold += amount
        elif choice == "food":
            self.food += amount
        elif choice == "lumber":
            self.lumber += amount
        else:
            print("Invalid resource type.")

    def expand_territory(self):
        cost = 200
        if self.gold >= cost:
            new_territory = input("Enter new territory name: ")
            self.territories.append(new_territory)
            self.gold -= cost
            self.happiness += 5
            print(f"Territory '{new_territory}' has been added.")
        else:
            print("Not enough gold to expand territory.")

    def feed_population(self):
        needed_food = self.population * 2
        if self.food >= needed_food:
            self.food -= needed_food
            self.happiness += 10
            print("The population is well fed.")
        else:
            self.happiness -= 20
            print("Not enough food! People are unhappy.")

    def main_menu(self):
        actions = {
            "1": self.show_status,
            "2": self.manage_resources,
            "3": self.expand_territory,
            "4": self.feed_population
        }
        while True:
            print("\nMain Menu:")
            print("1. Show Status")
            print("2. Manage Resources")
            print("3. Expand Territory")
            print("4. Feed Population")
            print("5. Quit")

            action = input("Choose an action: ")
            if action == "5":
                print("Exiting the program.")
                break
            elif action in actions:
                actions[action]()
            else:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    kingdom_name = input("Enter your kingdom's name: ")
    kingdom = Kingdom(kingdom_name)
    kingdom.main_menu()
```

### Explanation

1. **Resources Management**: Users can harvest gold, food, or lumber.
2. **Territory Expansion**: Users can expand their kingdom by adding new territories at the cost of 200 gold, which increases happiness.
3. **Feeding the Population**: Feeding requires food equal to twice the population; failing to feed them decreases happiness.
4. **Menu System**: Users interact with the utility through a menu-driven interface.

This utility can serve as a simple starting point for more complex simulation games, allowing for expansion with more features such as trade, wars, and alliances.

def log_event():ef drop_files_to_bridge():