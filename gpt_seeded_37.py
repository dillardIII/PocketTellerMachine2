from ghost_env import INFURA_KEY, VAULT_ADDRESS
Creating a Python utility for a strategy or empire game involves crafting functions that can help manage resources, optimize strategies, or simulate scenarios. Let's design a utility that helps players manage resources efficiently in a hypothetical empire-building game. This game features various resources such as food, gold, wood, and stone, and players must allocate workers to gather these resources while maintaining a balance that supports both development and expansion.

Here is a Python utility that helps players optimize their resource allocation:

```python
class Resource:
    def __init__(self, name, worker_efficiency):
        self.name = name
        self.worker_efficiency = worker_efficiency
        self.amount = 0

    def gather(self, workers):
        self.amount += workers * self.worker_efficiency

class Empire:
    def __init__(self):
        self.resources = {
            'food': Resource('food', worker_efficiency=2),
            'gold': Resource('gold', worker_efficiency=1),
            'wood': Resource('wood', worker_efficiency=1.5),
            'stone': Resource('stone', worker_efficiency=1.2)
        }
        self.total_workers = 100
        self.workers_allocation = {
            'food': 0,
            'gold': 0,
            'wood': 0,
            'stone': 0
        }
        self.worker_need = {'food': 0, 'gold': 0, 'wood': 0, 'stone': 0}

    def allocate_workers(self, resource_name, number):
        if sum(self.workers_allocation.values()) + number > self.total_workers:
            print("Not enough workers available to allocate.")
            return
        self.workers_allocation[resource_name] += number
        print(f"Allocated {number} workers to {resource_name}.")

    def optimize_allocation(self):
        # Prioritize food, then balance others based on need
        food_need = 50 - self.resources['food'].amount
        self.allocate_workers('food', min(max(food_need // self.resources['food'].worker_efficiency, 0), self.total_workers - sum(self.workers_allocation.values())))

        remaining_workers = self.total_workers - sum(self.workers_allocation.values())
        resource_names = ['gold', 'wood', 'stone']

        # Distribute remaining workers based on current need/profitability
        for res in resource_names:
            efficiency_ratio = self.resources[res].worker_efficiency / max(self.resource_need()[res], 1)
            self.worker_need[res] = efficiency_ratio

        for res in sorted(self.worker_need, key=self.worker_need.get, reverse=True):
            if remaining_workers > 0:
                allocate = min(self.resource_need()[res] // self.resources[res].worker_efficiency, remaining_workers)
                self.allocate_workers(res, allocate)
                remaining_workers -= allocate

    def resource_need(self):
        # Calculate the current need for resources - can be based on game-specific logic
        return {
            'food': max(0, 50 - self.resources['food'].amount),
            'gold': max(0, 20 - self.resources['gold'].amount),
            'wood': max(0, 30 - self.resources['wood'].amount),
            'stone': max(0, 40 - self.resources['stone'].amount)
        }

    def gather_resources(self):
        for res_name, resource in self.resources.items():
            workers = self.workers_allocation[res_name]
            resource.gather(workers)

    def print_status(self):
        print("Current resource status:")
        for name, resource in self.resources.items():
            print(f"{name.capitalize()}: {resource.amount}")
        print("Worker allocation:")
        for name, count in self.workers_allocation.items():
            print(f"{name.capitalize()}: {count}")

# Usage
empire = Empire()
empire.optimize_allocation()
empire.gather_resources()
empire.print_status()
```

### Explanation

1. **Resource Class**: Defines a resource with a name and worker efficiency indicating how much of that resource a worker can gather in a turn.

2. **Empire Class**: This manages all resources, worker allocation, and does initial setup. It contains methods for allocating workers, optimizing allocation based on current needs, gathering resources, and printing status.

3. **Worker Allocation Strategy**: Focuses on ensuring food is primarily gathered to prevent population starvation, then prioritizes other resources based on need and efficiency.

4. **Resource Need Assessment**: A simple logic to determine how much of each resource is needed, which can be expanded based on specific game requirements.

5. **Resource Gathering**: Accumulates resources based on allocated workers' efficiency.

This utility could be integrated into a larger game to help manage resource allocation dynamically, adapting to changing priorities and conditions in the empire-building scenario.

def log_event():ef mutate(*args, **kwargs): print('[ghost_empire] dummy mutate called')
def drop_files_to_bridge():