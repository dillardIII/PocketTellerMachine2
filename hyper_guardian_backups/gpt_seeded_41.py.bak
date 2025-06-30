Certainly! Below is a Python script for a simple empire-building simulation game utility. This game involves managing resources, expanding territories, and maintaining citizen happiness. The utility provides functions to manage these aspects and can be integrated into a larger game system or used as a standalone module for empire management.

```python
import random

class Empire:
    def __init__(self, name):
        self.name = name
        self.resources = {
            'gold': 1000,
            'food': 5000,
            'wood': 3000
        }
        self.citizens = 100
        self.happiness = 50  # Scale of 0 to 100
        self.territories = 1

    def gather_resources(self):
        # Simulate gathering of resources each turn
        self.resources['gold'] += random.randint(10, 50) * self.territories
        self.resources['food'] += random.randint(100, 200) * self.territories
        self.resources['wood'] += random.randint(50, 150) * self.territories
        print(f"[INFO] Resources gathered. Current resources: {self.resources}")

    def expand_territory(self):
        # Costs and effects of expanding territory
        if self.resources['gold'] >= 500 and self.resources['food'] >= 1000:
            self.resources['gold'] -= 500
            self.resources['food'] -= 1000
            self.territories += 1
            self.happiness += 5
            print(f"[SUCCESS] Territory expanded. Total territories: {self.territories}")
        else:
            print("[FAILURE] Not enough resources to expand territory.")

    def manage_happiness(self):
        # Effects of happiness and methods to influence it
        if self.happiness < 20:
            print("[WARNING] Citizens are unhappy. Consider addressing their needs!")
            self.resources['food'] += random.randint(0, 50)  # Less food due to unrest

        # Party to boost happiness at a cost
        decision = input("Do you want to hold a celebration party to boost happiness at the cost of resources? (yes/no): ")
        if decision.lower() == "yes" and self.resources['gold'] >= 200 and self.resources['food'] >= 500:
            self.resources['gold'] -= 200
            self.resources['food'] -= 500
            self.happiness = min(self.happiness + 20, 100)
            print(f"[SUCCESS] Happiness increased. Current happiness: {self.happiness}")
        else:
            print("[INFO] No party held or insufficient resources.")

    def status_report(self):
        # Print the current status of the empire
        print("\nEmpire Status Report")
        print(f"Name: {self.name}")
        print(f"Resources: {self.resources}")
        print(f"Citizens: {self.citizens}")
        print(f"Happiness: {self.happiness}")
        print(f"Territories: {self.territories}")
        print("-" * 30)

def main():
    empire_name = input("Enter the name of your empire: ")
    empire = Empire(empire_name)

    # Game loop
    while True:
        print("\n1. Gather Resources")
        print("2. Expand Territory")
        print("3. Manage Happiness")
        print("4. View Status Report")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            empire.gather_resources()
        elif choice == "2":
            empire.expand_territory()
        elif choice == "3":
            empire.manage_happiness()
        elif choice == "4":
            empire.status_report()
        elif choice == "5":
            print("Exiting empire management utility.")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
```

### Key Features:

- **Resource Management**: Players gather resources every turn, which are essential for expansion and keeping citizens happy.
- **Territory Expansion**: Expanding requires strategy, as it consumes resources but increases potential for greater resource gathering.
- **Citizen Happiness**: Players must monitor and manage citizen happiness, which affects productivity.
- **Interactive Gameplay**: Simplistic input-driven gameplay for testing and prototyping larger empire management concepts. 

This utility is easy to expand by adding more resource types, events, random occurrences, or advanced economic systems.